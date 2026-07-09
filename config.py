import os

# Base Directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# YOLO Model
MODEL_PATH = os.path.join(BASE_DIR, "yolov8n.pt")

# Video Path
VIDEO_PATH = os.path.join(BASE_DIR, "videos", "Sample_crowd_2.mp4")

# Flask Settings
HOST = "0.0.0.0"
PORT = 5000
DEBUG = False

# Crowd Thresholds
SAFE_LIMIT = 10
MODERATE_LIMIT = 15

# Alert Timing (seconds)
ORANGE_ALERT_INTERVAL = 10
RED_ALERT_INTERVAL = 5

# Detection
CONFIDENCE = 0.40
IMAGE_SIZE = 640