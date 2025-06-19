import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

# Loading variables from .env file
load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
# Connecting to MySQL database
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = conn.cursor()
# Reading flashcards from CSV
df = pd.read_csv("flashcards.csv")
# Inserting each row into the flashcards table
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO flashcards (question, answer, topic)
        VALUES (%s, %s, %s)
    """, (row['question'], row['answer'], row['topic']))
conn.commit()
cursor.close()
conn.close()
print("Flashcards uploaded successfully!")