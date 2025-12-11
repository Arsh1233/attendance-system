# 🎓 AI-Powered Attendance System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-red)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8.1-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit%20Cloud-brightgreen)

An intelligent, automated attendance marking system using face recognition technology. Upload student photos and class photos to automatically detect faces and mark attendance with visual annotations.

## ✨ Features

- **Automated Face Detection**: Uses Haar Cascade classifiers to detect faces in images
- **Face Recognition**: Compares faces using cosine similarity for accurate matching
- **Visual Annotations**: Draws bounding boxes with names around recognized faces
- **Attendance Reports**: Generates detailed CSV reports of present/absent students
- **Multiple Export Options**: Download annotated images and attendance reports
- **User-Friendly Interface**: Clean Streamlit interface with step-by-step workflow
- **Cloud Ready**: Deploys easily on Streamlit Cloud, Hugging Face Spaces, and more

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Git (for version control)
- Modern web browser

### Local Installation

**Clone the repository**
   ```bash
   git clone https://github.com/Arsh1233/attendance-system.git
   cd attendance-system
```
### Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

**Open your browser** and navigate to `http://localhost:8501`

## 📖 How to Use

### Step 1: Upload Student Photos

1. **Navigate to the sidebar** in the web interface
2. **Upload individual photos** of each student
3. **Naming convention**: Use `firstname_lastname.jpg` (e.g., `john_doe.jpg`)
4. The system will automatically extract names from filenames

### Step 2: Upload Class Photo

1. Use the **main uploader** to upload a group/class photo
2. **Supported formats**: JPG, JPEG, PNG
3. **For best results**:
   - Ensure good lighting
   - Use frontal face photos
   - Avoid blurry images

### Step 3: Run Attendance Recognition

1. Click the **"Run Attendance Recognition"** button
2. The system will automatically:
   - Detect all faces in the class photo
   - Compare each face with the known student database
   - Mark attendance with:
     - **Green boxes**: Recognized students
     - **Red boxes**: Unknown faces
   - Generate a comprehensive attendance report

### Step 4: Download Results

- **📊 CSV Report**: Download attendance data as CSV file
- **🖼️ Annotated Image**: Download the class photo with face annotations
- **🔄 Reset System**: Clear all uploaded data and start fresh

## 🔧 Quick Commands Reference

| Action | Command |
|--------|---------|
| Create environment (Windows) | `python -m venv venv` |
| Activate (Windows) | `venv\Scripts\activate` |
| Create environment (Mac/Linux) | `python3 -m venv venv` |
| Activate (Mac/Linux) | `source venv/bin/activate` |
| Install dependencies | `pip install -r requirements.txt` |
| Run application | `streamlit run app.py` |
| Access application | Visit `http://localhost:8501` |

## 💡 Tips for Best Results

1. **Photo Quality**: Use clear, well-lit photos with plain backgrounds
2. **Face Position**: Ensure faces are looking directly at the camera
3. **File Names**: Stick to the naming convention for automatic name extraction
4. **Group Photos**: Try to get everyone's face clearly visible in class photos
5. **File Size**: Keep individual photos under 2MB for faster processing

## 🆘 Troubleshooting

**If you encounter issues:**

1. **Activation fails on Windows**: Run PowerShell as Administrator
2. **Dependencies won't install**: Update pip first: `python -m pip install --upgrade pip`
3. **Port already in use**: Use a different port: `streamlit run app.py --server.port 8502`
4. **Face detection not working**: Check OpenCV installation in requirements.txt

---

*For more detailed information, advanced configuration, or deployment instructions, please refer to the full README documentation.*
