import streamlit as st
import random
import time

# Page Configurations
st.set_page_config(page_title="Number Guessing Game", page_icon="🎮", layout="centered")

# Custom CSS for Enhanced Styling
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
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
        .guess-input {
            text-align: center;
            font-size: 18px;
            padding: 10px;
            background-color: #c70039;
            color: white;
            border-radius: 8px;
        }
        .stAlert {
            color: white !important;
            font-weight: bold;
        }
        .stMarkdown {
            color: #ffcc00;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🎯 Number Guessing Game")
st.subheader("🤖 I have chosen a number between 1 and 100. Can you guess it? 🔢")

# Initialize Game State
if 'number' not in st.session_state or 'attempts' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 7
    st.session_state.start_time = time.time()

# User Input
st.write("**Enter your guess below:**")
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="guess_input")

# Display Remaining Attempts
st.markdown(f"<h3 style='color: #ffcc00;'>🔥 Attempts Left: {st.session_state.attempts}/7</h3>", unsafe_allow_html=True)

# Check Guess
if st.button("Submit Guess"):
    if st.session_state.attempts > 1:
        st.session_state.attempts -= 1
        if guess < st.session_state.number:
            st.warning(f"📉 Too low! Attempts left: {st.session_state.attempts}", icon="⚠️")
        elif guess > st.session_state.number:
            st.warning(f"📈 Too high! Attempts left: {st.session_state.attempts}", icon="⚠️")
        else:
            elapsed_time = round(time.time() - st.session_state.start_time, 2)
            st.success(f"🎊 Congratulations! You guessed the number {st.session_state.number} correctly in {elapsed_time} seconds! 🎉", icon="🏆")
            st.balloons()
            st.session_state.number = random.randint(1, 100)
            st.session_state.attempts = 7
            st.session_state.start_time = time.time()
            st.rerun()
    else:
        st.error(f"😢 Out of guesses! The correct number was **{st.session_state.number}**. Try again!", icon="❌")
        time.sleep(2)  # Short delay to show the correct number
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 7
        st.session_state.start_time = time.time()
        st.rerun()

# Fun Fact Feature
if st.button("Get a Fun Fact 🎲"):
    facts = [
        "Did you know? The number 7 is considered lucky in many cultures! 🍀",
        "Fun Fact: The number 100 is a square number (10x10)! 🎲",
        "Interesting! The number 42 is known as the 'Answer to the Ultimate Question of Life' in The Hitchhiker's Guide to the Galaxy! 🚀",
        "Guess what? The number 13 is considered unlucky in some places, but lucky in others! 😲",
        "Did you know? The first prime number is 2, and it’s the only even prime! 🔢"
    ]
    st.info(random.choice(facts), icon="💡")

# Footer
st.markdown(
    """
    <div style='margin-top:50px; text-align:center; font-size:14px; color:#ffcc00; font-weight:bold;'>
        Developed by Zaryab Irfan 🚀
    </div>
    """,
    unsafe_allow_html=True
)
