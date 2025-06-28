# Data Science Flash Card Quiz App 
This is a both Data Science Capstone project and Flash card quiz app built using Python, Streamlit, and MySQL. This project helps you revise data science concepts and also demonstrates skills in GUI web app development, databases, and basic automation.
Try Project Live Here (App Link): http://172.20.10.3:8501

## Features
- View random flash cards with question-answer format
- Track if your answers are correct or incorrect
- Store flash card data in MySQL database
- Upload flash cards using a CSV upload script
- Built using Streamlit Web App (GUI frontend)

## Tools Used
- Python
- Streamlit
- MySQL
- Pandas
- dotenv
- mysql-connector-python|

## How to Run the Project
1. Download the files or Clone the Repository.
2. Rename .env.example file to .env
3. Install required libraries:
   pip install streamlit mysql-connector-python python-dotenv
4. Create the Database and Tables
   Run: flashcards.sql
5. Upload Flashcards to DB
   Run: upload_flashcards.py
6. Run the app using:
   streamlit run app.py
7. A new tab (web app) will open in your browser.
8. Click 'Show Answer' for viewing the answer and 'I got it right' or 'I got it wrong' for next question.

## Sample Output (App View)
- Topic: Python
- Question: What does the 'groupby' function do in pandas?
- Answer: Groups data by one or more columns and performs aggregate functions.

## App Screenshot
The above screenshot shows the Streamlit web app interface and an example predicted flash card with answer.
(FlashCardQuizApp-Screenshot.png)
