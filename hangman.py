import random
import streamlit as st

# Set up the game state
if 'word' not in st.session_state:
    words = ["python", "developer", "software", "debugger", "variable", "function", "compiler", "algorithm", "database", "framework"]
    st.session_state.word = random.choice(words)
    st.session_state.word_letters = set(st.session_state.word)
    st.session_state.correct_guesses = set()
    st.session_state.attempts = 6

# UI Styling
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .stApp {
            max-width: 600px;
            margin: auto;
            text-align: center;
        }
        .title {
            color: #0078D7;
            font-size: 28px;
            font-weight: bold;
        }
        .word {
            font-size: 24px;
            letter-spacing: 5px;
        }
        .message {
            font-size: 20px;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Game UI
st.markdown("<div class='title'>💻 Tech Hangman Challenge 🚀</div>", unsafe_allow_html=True)

display_word = " ".join([letter if letter in st.session_state.correct_guesses else "_" for letter in st.session_state.word])
st.markdown(f"<div class='word'>{display_word}</div>", unsafe_allow_html=True)

st.write(f"Attempts Left: {st.session_state.attempts}")

guess = st.text_input("Enter a letter", max_chars=1).lower()

if st.button("Submit Guess") and guess:
    if guess in st.session_state.correct_guesses:
        st.warning("⚠️ You've already guessed that letter!")
    elif guess in st.session_state.word_letters:
        st.session_state.correct_guesses.add(guess)
        st.session_state.word_letters.remove(guess)
        st.success("✅ Correct Guess!")
    else:
        st.session_state.attempts -= 1
        st.error(f"❌ Wrong! Attempts left: {st.session_state.attempts}")

# Hangman Stages
hangman_stages = [
    "☠️💀", "😵|", "😨/|", "😰/|\\", "😢/|\\ ", "😱/|\\ /"
]
if st.session_state.attempts < 6:
    st.markdown(f"**{hangman_stages[5 - st.session_state.attempts]}**")

# Game Over Check
if not st.session_state.word_letters:
    st.success(f"🎉 Amazing! You figured out the word: {st.session_state.word.upper()} 🏆")
    if st.button("Play Again"):
        st.session_state.clear()
        st.experimental_rerun()
elif st.session_state.attempts == 0:
    st.error(f"💀 Game Over! The word was: {st.session_state.word.upper()}")
    if st.button("Try Again"):
        st.session_state.clear()
        st.experimental_rerun()
