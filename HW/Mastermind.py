import streamlit as st
import random

st.title("Mastermind")
st.write("Guess the secret combination of 4 colors!")
st.write("You have 10 attempts to win.")

if "secret" not in st.session_state:
    st.session_state.secret = random.choices(
        ["Red", "Blue", "Green", "Yellow"], k=4
    )
    st.session_state.attempts = 0
    st.session_state.game_over = False

st.write("Choose your colors:")

colors = ["Red", "Blue", "Green", "Yellow"]

row1 = st.columns(4)

guess = []

for i in range(4):
    guess.append(
        row1[i].selectbox(
            "Piece " + str(i + 1),
            colors,
            key="color" + str(i)
        )
    )

row2 = st.columns(4)

for i in range(4):
    if guess[i] == "Red":
        row2[i].write("🔴")
    elif guess[i] == "Blue":
        row2[i].write("🔵")
    elif guess[i] == "Green":
        row2[i].write("🟢")
    else:
        row2[i].write("🟡")

if st.button("Check Guess"):

    if not st.session_state.game_over:

        st.session_state.attempts += 1

        correct = 0

        for i in range(4):
            if guess[i] == st.session_state.secret[i]:
                correct += 1

        st.write("Correct positions:", correct)

        if correct == 4:
            st.write("Congratulations! You cracked the code!")
            st.session_state.game_over = True

        elif st.session_state.attempts >= 10:
            st.write("Game over!")
            st.write("The secret code was:",
                     st.session_state.secret)
            st.session_state.game_over = True

        else:
            st.write("Try again!")

st.write("Attempts:", st.session_state.attempts, "/ 10")

if st.button("New Game"):

    st.session_state.secret = random.choices(
        ["Red", "Blue", "Green", "Yellow"], k=4
    )

    st.session_state.attempts = 0
    st.session_state.game_over = False

    st.rerun()
