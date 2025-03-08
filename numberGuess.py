import streamlit as st
import random

# Page Configurations
st.set_page_config(page_title="Number Guessing Game", page_icon="🎮", layout="centered")

# Custom CSS for Styling
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to right, #1e3c72, #2a5298);
            color: white;
            text-align: center;
        }
        .stButton>button {
            background-color: #ffcc00;
            color: black;
            padding: 10px 24px;
            font-size: 18px;
            border-radius: 10px;
            border: none;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #e6b800;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🎯 Number Guessing Game")
st.markdown("<h4 style='text-align: center; color: #ffcc00;'>🤖 I have chosen a number between 1 and 100. Can you guess it? 🔢</h4>", unsafe_allow_html=True)

# Initialize Game State
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 7

# User Input
guess = st.number_input("Enter your guess: ", min_value=1, max_value=100, step=1)

# Check Guess
if st.button("Submit Guess"):
    if st.session_state.attempts > 0:
        if guess < st.session_state.number:
            st.warning(f"📉 Too low! Try again. Attempts left: {st.session_state.attempts - 1}")
        elif guess > st.session_state.number:
            st.warning(f"📈 Too high! Try again. Attempts left: {st.session_state.attempts - 1}")
        else:
            st.success(f"🎊 Congratulations! You guessed the number {st.session_state.number} correctly! 🎉")
            st.balloons()
            st.session_state.number = random.randint(1, 100)
            st.session_state.attempts = 7
        
        st.session_state.attempts -= 1
    else:
        st.error(f"😢 Oops! You are out of guesses. The correct number was: {st.session_state.number}.")
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 7

# Footer
st.markdown("<div style='margin-top:50px; text-align:center; font-size:14px; color:#ffcc00; font-weight:bold;'>Developed by Zaryab Irfan 🚀</div>", unsafe_allow_html=True)
