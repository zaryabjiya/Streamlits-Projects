import streamlit as st
import time

# Page Configurations
st.set_page_config(page_title="⏳ Countdown Timer", page_icon="⏰", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to right, #1e3c72, #2a5298);
            color: white;
            text-align: center;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #ff5733;
            color: white;
            padding: 12px 24px;
            font-size: 16px;
            border-radius: 8px;
            border: none;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s ease-in-out;
            width: 200px;
            display: block;
            margin: 10px auto;
            box-shadow: 0px 5px 15px rgba(255, 87, 51, 0.6);
        }
        .stButton>button:hover {
            background-color: #c70039;
            transform: scale(1.05);
        }
        .stButton.pause-btn>button {
            background-color: #f4c542 !important;
            color: black !important;
        }
        .stButton.pause-btn>button:hover {
            background-color: #d6a321 !important;
        }
        .stButton.resume-btn>button {
            background-color: #1ecb71 !important;
            color: white !important;
        }
        .stButton.resume-btn>button:hover {
            background-color: #16a85c !important;
        }
        .timer-box {
            background-color: #2a5298;
            color: white;
            font-size: 24px;
            font-weight: bold;
            padding: 15px;
            border-radius: 8px;
            margin-top: 15px;
            text-align: center;
        }
        div[data-testid="stRadio"] label {
            font-size: 20px !important;
            font-weight: bold !important;
            color: white !important;
        }
        div[data-baseweb="input"] label {
            font-size: 18px !important;
            font-weight: bold !important;
            color: white !important;
        }
        .footer {
            margin-top: 50px;
            text-align: center;
            font-size: 14px;
            color: #ffcc00;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("⏳ Countdown Timer with Pause & Resume")
st.subheader("🎯 Set your timer in minutes or seconds and start the countdown! ⏰")

# Initialize Session State for Timer Control
if "remaining_time" not in st.session_state:
    st.session_state.remaining_time = 0
    st.session_state.running = False

# User Input
st.markdown("<h3 style='color:white; text-align:center;'>⏳ Select Time Format:</h3>", unsafe_allow_html=True)
time_format = st.radio("Choose:", ["Minutes", "Seconds"], index=0)

if time_format == "Minutes":
    st.markdown("<h3 style='color:white; text-align:center;'>⏱️ Enter time in minutes:</h3>", unsafe_allow_html=True)
    user_time = st.number_input("", min_value=0, max_value=60, step=1, key="minutes_input")
    total_seconds = user_time * 60
else:
    st.markdown("<h3 style='color:white; text-align:center;'>⏳ Enter time in seconds:</h3>", unsafe_allow_html=True)
    user_time = st.number_input("", min_value=0, max_value=3600, step=1, key="seconds_input")
    total_seconds = user_time

# Start Button
if st.button("🚀 Start Countdown", key="start_button"):
    if total_seconds > 0:
        st.session_state.remaining_time = total_seconds
        st.session_state.running = True

# Pause Button
if st.button("⏸️ Pause Timer", key="pause_button", help="Pause the countdown timer", args=("pause-btn",)):
    st.session_state.running = False

# Resume Button
if st.button("▶️ Resume Timer", key="resume_button", help="Resume the countdown timer", args=("resume-btn",)):
    st.session_state.running = True

# Timer Logic
countdown_placeholder = st.empty()

while st.session_state.running and st.session_state.remaining_time > 0:
    mins, secs = divmod(st.session_state.remaining_time, 60)
    countdown_placeholder.markdown(
        f"<div class='timer-box'>🕒 {mins:02}:{secs:02} remaining...</div>", unsafe_allow_html=True
    )
    time.sleep(1)
    st.session_state.remaining_time -= 1

    # If timer is paused, break the loop
    if not st.session_state.running:
        break

# When Timer Finishes
if st.session_state.remaining_time == 0 and st.session_state.running:
    st.markdown("<div class='timer-box' style='background-color:#FF5733;'>⏰ Ding Ding! Time’s up! 🚨</div>", unsafe_allow_html=True)
    st.balloons()
    st.session_state.running = False

# Footer
st.markdown("<div class='footer'>🚀 Developed by Zaryab Irfan</div>", unsafe_allow_html=True)
