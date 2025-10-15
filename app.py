from flask import Flask, request, session, redirect, render_template_string, flash, jsonify
import os
import threading
import time

SECRET_KEY = os.environ.get("SECRET_KEY", "A_FALLBACK_SECRET_KEY_FOR_LOCAL_TESTING")
app = Flask(__name__)
app.secret_key = SECRET_KEY

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

users_db = {
    "doctor1": {"password": "doc123", "role": "doctor"},
    "patient_zero": {"password": "test", "role": "patient"}
}

drone_state = {"x": 0, "y": 0, "destination": None}
uploaded_files = {}
chat_history = []

@app.route("/")
def index():
    return "Medi-Drone Flask App Ready!"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
