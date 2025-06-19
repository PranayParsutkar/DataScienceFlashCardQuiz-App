CREATE DATABASE flashcards_db;
USE flashcards_db;
CREATE TABLE flashcards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    topic VARCHAR(100)
);
CREATE TABLE user_stats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    card_id INT,
    is_correct BOOLEAN,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);