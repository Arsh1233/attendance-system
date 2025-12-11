import streamlit as st
import pandas as pd
import os
from PIL import Image
import io
import warnings
warnings.filterwarnings('ignore')

from face_recognizer import SimpleFaceRecognizer

# Initialize directories
os.makedirs("known_faces", exist_ok=True)
os.makedirs("class_photos", exist_ok=True)

# Page configuration
st.set_page_config(
    page_title="AI-Powered Attendance System",
    page_icon=":school:",
    layout="wide"
)

# Title and description
st.title(":school: AI-Powered Attendance System")
st.write("Upload student photos and a class photo to automatically mark attendance.")

# Initialize face recognizer
@st.cache_resource
def get_face_recognizer():
    return SimpleFaceRecognizer()

face_recognizer = get_face_recognizer()

# Sidebar for student uploads
st.sidebar.header("1. Upload Known Faces (Students)")
st.sidebar.write("Upload individual photos for each student. Name files like 'john_doe.jpg'.")

uploaded_student_files = st.sidebar.file_uploader(
    "Choose student photos (JPG, PNG)",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True,
    key="student_uploader"
)

if uploaded_student_files:
    for student_file in uploaded_student_files:
        file_path = os.path.join("known_faces", student_file.name)
        with open(file_path, "wb") as f:
            f.write(student_file.getbuffer())
    st.sidebar.success(f"Uploaded {len(uploaded_student_files)} student files.")

# Load known faces
known_faces_features, known_names = face_recognizer.load_known_faces()

if known_names:
    st.sidebar.write(f"Loaded {len(known_names)} students: {', '.join(known_names)}")
else:
    st.sidebar.info("Please upload student photos to build the database.")

# Main area for class photo upload
st.header("2. Upload Class Photo")
uploaded_class_photo = st.file_uploader(
    "Choose a class photo (JPG, PNG)",
    type=["jpg", "jpeg", "png"],
    key="class_uploader"
)

class_photo_display = None
if uploaded_class_photo is not None:
    class_photo_display = Image.open(uploaded_class_photo)
    st.image(class_photo_display, caption='Uploaded Class Photo', use_column_width=True)
    st.success("Class photo uploaded successfully!")
    
    # Save to class_photos directory
    class_photo_path = os.path.join("class_photos", uploaded_class_photo.name)
    with open(class_photo_path, "wb") as f:
        f.write(uploaded_class_photo.getbuffer())

# Attendance recognition
st.header("3. Run Attendance Recognition")

if st.button('Run Attendance Recognition', key="run_button"):
    if not known_names:
        st.error("Please upload student photos first (Step 1).")
    elif uploaded_class_photo is None:
        st.error("Please upload a class photo first (Step 2).")
    else:
        with st.spinner("Running face recognition..."):
            uploaded_class_photo.seek(0)
            present_students, unknown_faces, result_image, message = face_recognizer.recognize_faces(
                uploaded_class_photo
            )
            
            st.info(message)
            
            if result_image:
                st.subheader("Attendance Results")
                st.image(
                    result_image, 
                    caption=f'Recognized Faces (Total: {len(present_students)}, Unknown: {unknown_faces})', 
                    use_column_width=True
                )

                # Attendance Report
                st.subheader("Attendance Report")
                unique_present_students = list(set(present_students))

                attendance_status = []
                for student in known_names:
                    status = "Present" if student in unique_present_students else "Absent"
                    attendance_status.append(status)

                attendance_df = pd.DataFrame({
                    'Student Name': known_names,
                    'Status': attendance_status
                })
                
                # Display dataframe
                st.dataframe(attendance_df)

                # Summary statistics
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.success(f"✅ Present: {len(unique_present_students)}")
                with col2:
                    st.error(f"❌ Absent: {len(known_names) - len(unique_present_students)}")
                with col3:
                    if unknown_faces > 0:
                        st.warning(f"❓ Unknown: {unknown_faces}")

                # Download options
                st.subheader("Download Results")
                
                # CSV Download
                csv_buffer = io.StringIO()
                attendance_df.to_csv(csv_buffer, index=False)
                st.download_button(
                    label="Download Attendance Report (CSV)",
                    data=csv_buffer.getvalue(),
                    file_name="attendance_report.csv",
                    mime="text/csv",
                )

                # Image Download
                img_buffer = io.BytesIO()
                result_image.save(img_buffer, format="JPEG")
                st.download_button(
                    label="Download Annotated Image (JPG)",
                    data=img_buffer.getvalue(),
                    file_name="attendance_result.jpg",
                    mime="image/jpeg",
                )
            else:
                st.error("No faces were detected or an error occurred during recognition.")

# Reset System Button
st.sidebar.markdown("---")
if st.sidebar.button("Reset System", type="secondary"):
    import shutil
    if os.path.exists("known_faces"):
        shutil.rmtree("known_faces")
        os.makedirs("known_faces")
    if os.path.exists("class_photos"):
        shutil.rmtree("class_photos")
        os.makedirs("class_photos")
    st.sidebar.success("System reset complete!")
    st.rerun()

# Footer
st.markdown("---")
st.markdown("Built with Streamlit & OpenCV | Face Recognition Attendance System")