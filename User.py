import mysql.connector
from faker import Faker

def create_user(db):
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS User (
            UserID INT AUTO_INCREMENT PRIMARY KEY,
            Username VARCHAR(255) NOT NULL,
            Password VARCHAR(200) NOT NULL
        )
    """)

    db.commit()
    cursor.close()

    print("User table created successfully.")
