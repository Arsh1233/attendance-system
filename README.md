# 🎓 AI-Powered Attendance System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-red)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8.1-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit%20Cloud-brightgreen)

An intelligent, automated attendance marking system using face recognition technology. Upload student photos and class photos to automatically detect faces and mark attendance with visual annotations.

**Live Demo**: [https://attendance-system-arsh1233.streamlit.app](https://attendance-system-arsh1233.streamlit.app)

![Attendance System Interface](https://via.placeholder.com/800x450.png?text=AI+Attendance+System+Interface)

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

1. **Clone the repository**
   ```bash
   git clone https://github.com/Arsh1233/attendance-system.git
   cd attendance-system
