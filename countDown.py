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
            font-family: Arial, sans-serif;
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
        }
        .stButton>button:hover {
            background-color: #c70039;
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
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("⏳ Countdown Timer")
st.subheader("🎯 Set your timer in minutes or seconds and start the countdown! ⏰")

# User Input
time_format = st.radio("Select Time Format:", ["Minutes", "Seconds"])

if time_format == "Minutes":
    user_time = st.number_input("Enter time in minutes:", min_value=0, max_value=60, step=1, key="minutes_input")
    total_seconds = user_time * 60
else:
    user_time = st.number_input("Enter time in seconds:", min_value=0, max_value=3600, step=1, key="seconds_input")
    total_seconds = user_time

# Start Countdown
if st.button("Start Countdown 🚀"):
    if total_seconds > 0:
        st.markdown("<div class='timer-box'>⏳ Timer Started! Stay Ready! 🚀</div>", unsafe_allow_html=True)
        
        countdown_placeholder = st.empty()
        
        for remaining in range(total_seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            countdown_placeholder.markdown(f"<div class='timer-box'>🕒 {mins:02}:{secs:02} remaining...</div>", unsafe_allow_html=True)
            time.sleep(1)
        
        st.markdown("<div class='timer-box' style='background-color:#FF5733;'>⏰ Ding Ding! Time’s up! 🚨</div>", unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("⚠️ Please enter a valid time before starting the timer.")

# Footer
st.markdown(
    """
    <div style='margin-top:50px; text-align:center; font-size:14px; color:#ffcc00; font-weight:bold;'>
        Developed by Zaryab Irfan 🚀
    </div>
    """,
    unsafe_allow_html=True
)
