# 🚆 TrainCrowdSense

An AI-powered crowd monitoring system that detects passengers inside train coaches using **YOLOv8**, performs **real-time crowd density analysis**, and provides **voice alerts** to improve passenger safety and station management.

---

## 📌 Project Overview

TrainCrowdSense is a Computer Vision based application designed to monitor crowd density inside train coaches. The system processes live video or recorded footage, detects passengers using the YOLOv8 object detection model, calculates crowd density, classifies congestion levels, and generates real-time voice alerts for overcrowding situations.

This project aims to assist railway authorities in improving passenger safety, reducing overcrowding, and enabling smarter crowd management.

---

## ✨ Features

- 👥 Real-time People Detection using YOLOv8
- 🚆 Train Coach Crowd Monitoring
- 📊 Live Passenger Count
- 🟢 Safe Crowd Detection
- 🟠 Moderate Crowd Detection
- 🔴 Overcrowded Detection
- 🔊 Automated Voice Alerts
- 🌐 Flask-based Web Dashboard
- 🎥 Video Processing using OpenCV
- ⚡ Fast and Lightweight YOLOv8 Nano Model
- 📈 Real-time Crowd Status Updates

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Framework
- Flask

### AI / Machine Learning
- YOLOv8 (Ultralytics)

### Computer Vision
- OpenCV

### Libraries
- NumPy
- PyTorch
- pyttsx3

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap 5

---

## 📂 Project Structure

```text
TrainCrowdSense/
│
├── app.py
├── detector.py
├── voice_alert.py
├── config.py
├── requirements.txt
├── README.md
│
├── templates/
│      └── index.html
│
├── static/
│      ├── css/
│      ├── js/
│      └── images/
│
├── videos/
│      └── Sample_crowd_2.mp4
│
├── models/
│      └── yolov8n.pt
│
└── screenshots/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/TrainCrowdSense.git
```

Navigate to the project folder

```bash
cd TrainCrowdSense
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 📊 Crowd Classification

| People Count | Status |
|--------------|--------|
| 0 - 10 | 🟢 Safe |
| 11 - 15 | 🟠 Moderate |
| Above 15 | 🔴 Overcrowded |

---

## 🚀 Future Enhancements

- Live CCTV Camera Integration
- Railway Station Dashboard
- Cloud Deployment
- Mobile Application
- Email & SMS Alerts
- Multi-Camera Support
- Passenger Analytics Dashboard
- AI-based Crowd Prediction
- Database Integration
- Occupancy Percentage Analysis

---

## 🎯 Applications

- Indian Railways
- Metro Rail Systems
- Smart Railway Stations
- Public Transport Monitoring
- Smart City Infrastructure
- Crowd Safety Management

---

## 📚 Learning Outcomes

- Object Detection using YOLOv8
- Computer Vision with OpenCV
- Flask Web Development
- Real-Time Video Processing
- AI-based Crowd Monitoring
- Voice Alert Automation

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork this repository and submit a Pull Request.



## 👨‍💻 Author

**Owais Batte**

B.Tech Computer Science & Engineering (Artificial Intelligence & Machine Learning)

