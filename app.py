import streamlit as st
import mysql.connector
from dotenv import load_dotenv
import os
import random
from datetime import datetime

# Loading .env file
load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Connecting to DB
def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

# Fetching random card
def get_random_card():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM flashcards ORDER BY RAND() LIMIT 1")
    card = cursor.fetchone()
    cursor.close()
    conn.close()
    return card

# Saving result
def log_answer(card_id, is_correct):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_stats (card_id, is_correct) VALUES (%s, %s)", (card_id, is_correct))
    conn.commit()
    cursor.close()
    conn.close()

# Streamlit UI
st.set_page_config(page_title="Data Science Flash Card Quiz App", page_icon="📘")
st.title("📘 Data Science Flash Card Quiz")
st.write("Improve your data science skills with flash cards!")

# Showing card
if 'card' not in st.session_state:
    st.session_state.card = get_random_card()
    st.session_state.show_answer = False
card = st.session_state.card
st.subheader(f"Topic: {card['topic']}")
st.write(f"Question: {card['question']}")

# Revealing answer
if st.button("Show Answer"):
    st.session_state.show_answer = True

if st.session_state.show_answer:
    st.markdown(f"Answer: {card['answer']}")

    # Asking if user got it right
    col1, col2 = st.columns(2)
    with col1:
        if st.button("I got it right"):
            log_answer(card['id'], True)
            st.session_state.card = get_random_card()
            st.session_state.show_answer = False
            st.rerun()
    with col2:
        if st.button("I got it wrong"):
            log_answer(card['id'], False)
            st.session_state.card = get_random_card()
            st.session_state.show_answer = False
            st.rerun()