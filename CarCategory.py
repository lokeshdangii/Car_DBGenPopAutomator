import mysql.connector

def create_car_category(db):
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CarCategory (
            CategoryID INT AUTO_INCREMENT PRIMARY KEY,
            CategoryName VARCHAR(100)
        )
    """)

    car_categories = [
        ("SUV"),
        ("Sedan"),
        ("Hatchback"),
        ("Convertible"),
        ("Sport")
    ]

    insert_query = "INSERT INTO CarCategory (CategoryName) VALUES (%s)"
    cursor.executemany(insert_query, car_categories)

    db.commit()
    cursor.close()
    
    print("CarCategory table created and populated successfully.")
