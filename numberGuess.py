import streamlit as st
import random

# Page Configurations
st.set_page_config(page_title="Number Guessing Game", page_icon="🎮", layout="centered")

# Custom CSS for Improved Styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #121212;
            color: white;
            text-align: center;
            font-family: Arial, sans-serif;
        }
        .stButton>button {
            background-color: #00bfff;
            color: white;
            padding: 12px 24px;
            font-size: 16px;
            border-radius: 8px;
            border: none;
            font-weight: bold;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #009acd;
        }
        .guess-input {
            text-align: center;
            font-size: 18px;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🎯 Number Guessing Game")
st.subheader("🤖 I have chosen a number between 1 and 100. Can you guess it? 🔢")

# Initialize Game State
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 7

# User Input
st.write("**Enter your guess below:**")
guess = st.number_input("", min_value=1, max_value=100, step=1, key="guess_input")

# Check Guess
if st.button("Submit Guess"):
    if st.session_state.attempts > 0:
        if guess < st.session_state.number:
            st.warning(f"📉 Too low! Attempts left: {st.session_state.attempts - 1}")
        elif guess > st.session_state.number:
            st.warning(f"📈 Too high! Attempts left: {st.session_state.attempts - 1}")
        else:
            st.success(f"🎊 Congratulations! You guessed the number {st.session_state.number} correctly! 🎉")
            st.balloons()
            st.session_state.number = random.randint(1, 100)
            st.session_state.attempts = 7
            st.experimental_rerun()
        
        st.session_state.attempts -= 1
    else:
        st.error(f"😢 Out of guesses! The number was {st.session_state.number}.")
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 7
        st.experimental_rerun()

# Footer
st.markdown("""
    <div style='margin-top:50px; text-align:center; font-size:14px; color:white; font-weight:bold;'>
        Developed by Zaryab Irfan 🚀
    </div>
""", unsafe_allow_html=True)
