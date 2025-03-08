import streamlit as st
import random
import time

def main():
    st.set_page_config(page_title="Number Guessing Game", page_icon="🎮", layout="centered")
    st.markdown(
        """
        <style>
            .stApp {
                background: linear-gradient(to right, #ff758c, #ff7eb3);
                color: white;
                text-align: center;
            }
            .stButton>button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 24px;
                font-size: 18px;
                border-radius: 10px;
                border: none;
            }
            .stButton>button:hover {
                background-color: #45a049;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("🎯 Number Guessing Game")
    st.subheader("🤖 I have chosen a number between 1 and 100. Can you guess it? 🔢")
    
    if 'number' not in st.session_state:
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 7

    guess = st.number_input("Enter your guess: ", min_value=1, max_value=100, step=1)
    
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
                return
            st.session_state.attempts -= 1
        else:
            st.error(f"😢 Oops! You are out of guesses. The correct number was: {st.session_state.number}.")
            st.session_state.number = random.randint(1, 100)
            st.session_state.attempts = 7

if __name__ == "__main__":
    main()

st.markdown("<div style='margin-top:50px; text-align:center; font-size:14px; color:#444; font-weight:bold;'>Developed by Zaryab Irfan 🚀</div>", unsafe_allow_html=True)
