import threading

from flask import Flask, jsonify, render_template

from config import DEBUG, HOST, PORT
from detector import CrowdDetector

app = Flask(__name__)

# Initialize detector
detector = CrowdDetector()


def run_detection():
    detector.run()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/status")
def status():
    return jsonify({
        "people_count": detector.people_count,
        "status": detector.status
    })


if __name__ == "__main__":

    detection_thread = threading.Thread(
        target=run_detection,
        daemon=True
    )

    detection_thread.start()

    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG
    )