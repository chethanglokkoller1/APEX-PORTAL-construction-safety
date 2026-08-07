# AI Construction Site Safety Intelligence Platform

🏗️ A real-time AI-powered construction safety monitoring platform that automatically detects workers and identifies PPE (Personal Protective Equipment) violations using Computer Vision, Deep Learning, YOLOv8, OpenCV, and Streamlit.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Latest-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Dashboard](#dashboard)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Project Overview

The AI Construction Site Safety Intelligence Platform is an industry-level capstone project designed to enhance construction site safety through automated monitoring. The system uses advanced computer vision and deep learning techniques to detect safety violations in real-time from CCTV feeds, video files, and live camera streams.

### Key Objectives

- **Detect PPE Violations**: Automatically identify workers without helmets or safety vests
- **Real-Time Monitoring**: Process live video feeds with GPU-accelerated inference
- **Analytics Dashboard**: Provide comprehensive safety compliance analytics
- **Alert System**: Generate instant alerts for safety violations
- **Report Generation**: Create automated daily, weekly, and compliance reports

## ✨ Features

### Core Features

- **Worker Detection**: Accurately detect and count workers in construction sites
- **Helmet Detection**: Identify workers wearing and not wearing helmets
- **PPE Violation Detection**: Real-time violation identification and alerting
- **Real-Time Video Processing**: Support for webcam, video files, and RTSP streams
- **Live Dashboard**: Professional Streamlit-based monitoring dashboard
- **Violation Counter**: Track and display violation statistics
- **Analytics Dashboard**: Comprehensive safety compliance analytics
- **Daily Safety Reports**: Automated report generation
- **GPU Accelerated Inference**: NVIDIA GPU support for faster processing
- **Construction Site Monitoring**: Scalable monitoring solution

### Advanced Features

- **Object Tracking**: Track workers across video frames using Deep SORT
- **Compliance Scoring**: Calculate safety compliance percentages
- **Risk Level Prediction**: Automatically classify site safety as LOW, MEDIUM, or HIGH risk
- **Safety Grade System**: Assign grades A-D based on safety score and PPE compliance
- **Safety Compliance Analytics**: Visualize compliance, violation, and risk trends using Plotly
- **Historical Analytics Storage**: Persist daily records in `reports/Compliance_History.csv`
- **Smart Recommendation Engine**: Generate safety recommendations based on violations and score
- **Email Alerts**: Automated email notifications for violations
- **Data Persistence**: SQLite database for analytics storage
- **Export Capabilities**: Export reports in PDF, Excel, and CSV formats
- **Customizable Thresholds**: Adjustable confidence and IOU thresholds
- **Multi-Model Support**: Support for different YOLOv8 model sizes

## 🛠 Technology Stack

### Programming Language
- **Python 3.8+**

### Deep Learning & Computer Vision
- **YOLOv8** (Ultralytics) - Object detection
- **OpenCV** - Image and video processing
- **PyTorch** - Deep learning framework

### Dashboard & Visualization
- **Streamlit** - Interactive web dashboard
- **Plotly** - Interactive charts and graphs
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical visualization

### Data Processing
- **NumPy** - Numerical computing
- **Pandas** - Data manipulation and analysis
- **Pillow** - Image processing

### Object Tracking
- **Deep SORT** - Object tracking algorithm
- **FilterPy** - Kalman filtering

### Hardware Acceleration
- **NVIDIA GPU** - CUDA acceleration
- **Tensor Cores** - Optimized deep learning operations

### Development Platform
- **Google Colab** - Model training and development
- **Jupyter Notebooks** - Interactive development

## 📁 Project Structure

```
AI_Construction_Site_Safety/
│
├── data/
│   ├── images/              # Dataset images
│   │   ├── train/          # Training images
│   │   ├── val/            # Validation images
│   │   └── test/           # Test images
│   ├── videos/             # Video files for testing
│   ├── sample_data/        # Sample data
│   └── data.yaml          # Dataset configuration
│
├── models/
│   ├── yolov8_training.ipynb  # Training notebook
│   ├── safety_detection/      # Training results
│   │   └── weights/
│   │       ├── best.pt      # Best trained model
│   │       └── last.pt      # Last epoch model
│
├── src/
│   ├── detection.py        # Real-time detection module
│   ├── tracking.py         # Object tracking module
│   ├── analytics.py         # Violation analytics module
│   ├── alerts.py           # Alert system module
│   └── utils.py            # Utility functions
│
├── dashboard/
│   ├── app.py              # Main Streamlit application
│   └── components.py       # Dashboard components
│
├── reports/
│   ├── screenshots/         # Detection screenshots
│   ├── generated_reports/   # Generated reports
│   └── safety_analytics.db  # Analytics database
│
├── docs/
│   ├── README.md           # This file
│   ├── INSTALLATION.md     # Installation guide
│   ├── USER_MANUAL.md      # User manual
│   ├── TECHNICAL_DOC.md    # Technical documentation
│   ├── ARCHITECTURE.md     # Architecture diagram
│   ├── FLOW_DIAGRAM.md     # Flow diagram
│   └── PROJECT_REPORT.md   # Complete project report
│
├── presentation/
│   └── PPT_CONTENT.md      # PowerPoint presentation content
│
├── requirements.txt        # Python dependencies
├── main.py               # Main application entry point
└── LICENSE               # Project license
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- NVIDIA GPU (recommended for optimal performance)
- CUDA Toolkit (if using GPU)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/AI_Construction_Site_Safety.git
cd AI_Construction_Site_Safety
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA Available: {torch.cuda.is_available()}')"
```

For detailed installation instructions, see [INSTALLATION.md](docs/INSTALLATION.md).

## 📖 Usage

### Running the Dashboard

```bash
# Launch the Streamlit dashboard
streamlit run dashboard/app.py
```

The dashboard will be available at `http://localhost:8501`

### New Safety Intelligence Dashboard

After launching the Streamlit app, select the `Safety Intelligence Dashboard` page in the sidebar to view:

- Worker count and PPE violation metrics
- Safety score and grade
- Risk level with color-coded status
- Compliance and violation percentage analytics
- Smart safety recommendations
- Weekly compliance and risk trend charts
- Historical records loaded from `reports/Compliance_History.csv`

### Running Real-Time Detection

```bash
# Detect from webcam
python main.py --mode detection --video-source 0

# Detect from video file
python main.py --mode detection --video-source path/to/video.mp4 --output-path output.mp4

# Detect from RTSP stream
python main.py --mode detection --video-source rtsp://username:password@ip:port/path
```

### Generating Reports

```bash
# Generate 30-day safety report
python main.py --mode report --report-days 30
```

### Using the Modules

```python
from src.detection import SafetyDetector
from src.analytics import SafetyAnalytics
from src.alerts import AlertSystem

# Initialize detector
detector = SafetyDetector(model_path='models/safety_detection/weights/best.pt')

# Run detection on video
detector.detect_video(video_source=0, show_display=True)

# Initialize analytics
analytics = SafetyAnalytics()
safety_score = analytics.get_safety_score(days=30)
print(f"Safety Score: {safety_score['safety_score']}")
```

For detailed usage instructions, see [USER_MANUAL.md](docs/USER_MANUAL.md).

## 🎓 Model Training

### Training in Google Colab

1. Open `models/yolov8_training.ipynb` in Google Colab
2. Mount Google Drive
3. Upload your dataset to the appropriate directories
4. Run all cells to train the model
5. The trained model will be saved as `best.pt`

### Training Locally

```bash
# Run the training notebook
jupyter notebook models/yolov8_training.ipynb
```

### Dataset Preparation

1. Collect images of construction sites with workers
2. Annotate images using LabelImg or Roboflow
3. Organize images and labels in the data/ directory
4. Update `data/data.yaml` with your dataset configuration

### Training Parameters

- **Epochs**: 100
- **Image Size**: 640x640
- **Batch Size**: 16
- **Learning Rate**: 0.01
- **Optimizer**: AdamW

## 📊 Dashboard

The Streamlit dashboard provides:

### Pages

1. **Home**: Overview of key safety metrics and statistics
2. **Live Monitoring**: Real-time video detection interface
3. **Analytics**: Detailed compliance analytics and trends
4. **Reports**: Generate and download safety reports
5. **Settings**: Configure detection and alert parameters

### Features

- **KPI Cards**: Real-time safety metrics display
- **Interactive Charts**: Violation trends and compliance graphs
- **Safety Score Gauge**: Visual compliance indicator
- **Violation Log**: Real-time violation tracking
- **Alert Configuration**: Customize alert settings
- **Report Generation**: Automated report creation

## 📚 Documentation

- [Installation Guide](docs/INSTALLATION.md) - Detailed installation instructions
- [User Manual](docs/USER_MANUAL.md) - Complete user guide
- [Technical Documentation](docs/TECHNICAL_DOC.md) - Technical specifications
- [Architecture Diagram](docs/ARCHITECTURE.md) - System architecture
- [Flow Diagram](docs/FLOW_DIAGRAM.md) - Data flow diagram
- [Project Report](docs/PROJECT_REPORT.md) - Complete project report
- [Presentation](presentation/PPT_CONTENT.md) - PowerPoint presentation content

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## 🙏 Acknowledgments

- Ultralytics for YOLOv8
- Streamlit team for the amazing framework
- NVIDIA for GPU acceleration support
- OpenCV community for computer vision tools

## 📞 Contact

For questions and support:
- Email:mkdivya054@gmail.com
- GitHub Issues: [Project Issues](https://github.com/yourusername/AI_Construction_Site_Safety/issues)

## 🎯 Project Status

- ✅ Core Detection Module
- ✅ Object Tracking
- ✅ Analytics Dashboard
- ✅ Alert System
- ✅ Report Generation
- ✅ Streamlit Dashboard
- ✅ Documentation

## 🔮 Future Enhancements

- Integration with IoT sensors
- Mobile app for on-site monitoring
- Advanced 3D safety monitoring
- Integration with construction management systems
- Multi-site monitoring support
- AI-powered predictive safety analytics

---

**Built with ❤️ for safer construction sites**
