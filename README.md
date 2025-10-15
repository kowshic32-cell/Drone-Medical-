# 🩺 Medi-Drone: AI-Powered Medical Drone System

Medi-Drone is a Flask-based web application that connects doctors and patients through an intelligent drone delivery and tele-consultation platform. 
It allows doctors to set delivery coordinates for medical supplies while patients can track the drone’s position live, upload medical files, and chat securely.

## 🚀 Features

- 🔐 Login System – Separate roles for doctors and patients.
- 🗺️ Real-Time Drone Map – Doctors can send drones to chosen coordinates; patients can view live positions.
- 📂 Secure File Uploads – Share patient reports safely.
- 💬 Real-Time Chat – Secure doctor-patient messaging system.
- ⚙️ Autonomous Drone Simulation – Background thread automatically moves the drone toward its destination.
- 📱 Mobile-First Design – Responsive UI for phones and tablets.

## 🧠 Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS (mobile-first Inter UI)
- **Hosting:** PythonAnywhere / Render / Local Server
- **Libraries:** Flask, threading, json, time

## 🧩 How to Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/medi-drone.git
cd medi-drone
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## 🌐 Deployment

Deploy easily on:
- [PythonAnywhere](https://www.pythonanywhere.com)
- [Render](https://render.com)

Both platforms provide a public URL for global access.

## 💡 Future Improvements

- Integrate ESP32 + Camera for real drone control
- Add AI for route optimization and live doctor video calls
- Push notifications for delivery status updates
