import time

import cv2
from ultralytics import YOLO

from config import (CONFIDENCE, IMAGE_SIZE, MODEL_PATH, MODERATE_LIMIT,
                    ORANGE_ALERT_INTERVAL, RED_ALERT_INTERVAL, SAFE_LIMIT,
                    VIDEO_PATH)
from voice_alert import VoiceAlert


class CrowdDetector:

    def __init__(self):

        print("Loading YOLO model...")
        self.model = YOLO(MODEL_PATH)
        print("YOLO Model Loaded Successfully!")

        self.voice = VoiceAlert()

        self.people_count = 0
        self.status = "SAFE"

        self.last_orange = 0
        self.last_red = 0

    def process_frame(self, frame):

        results = self.model(
            frame,
            imgsz=IMAGE_SIZE,
            conf=CONFIDENCE,
            verbose=False,
        )

        count = 0

        for result in results:

            for box in result.boxes:

                cls = int(box.cls[0])

                if cls != 0:
                    continue

                count += 1

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                if count <= SAFE_LIMIT:
                    color = (0, 255, 0)

                elif count <= MODERATE_LIMIT:
                    color = (0, 165, 255)

                else:
                    color = (0, 0, 255)

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    color,
                    2,
                )

        self.people_count = count

        now = time.time()

        if count <= SAFE_LIMIT:

            self.status = "SAFE"

        elif count <= MODERATE_LIMIT:

            self.status = "MODERATE"

            if now - self.last_orange >= ORANGE_ALERT_INTERVAL:

                self.voice.speak(
                    "Moderate crowd detected. Please board carefully."
                )

                self.last_orange = now

        else:

            self.status = "OVERCROWDED"

            if now - self.last_red >= RED_ALERT_INTERVAL:

                self.voice.speak(
                    "Warning. The coach is overcrowded. Please wait for the next train."
                )

                self.last_red = now

        cv2.putText(
            frame,
            f"People : {count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2,
        )

        cv2.putText(
            frame,
            self.status,
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2,
        )

        return frame

    def run(self):

        cap = cv2.VideoCapture(VIDEO_PATH)

        if not cap.isOpened():

            print("ERROR : Unable to open video.")
            return

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            frame = cv2.resize(frame, (960, 540))

            frame = self.process_frame(frame)

            cv2.imshow("Train CrowdSense", frame)

            key = cv2.waitKey(1)

            if key == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
        