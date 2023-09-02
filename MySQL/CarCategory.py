import mysql.connector

def create_car_category(db):

    cursor = db.cursor()

    car_categories = [
        (1, "SUV"),
        (2, "Sedan"),
        (3, "Hatchback"),
        (4, "Convertible"),
        (5, "Sport")
    ]

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CarCategory (
            CategoryID INT PRIMARY KEY,
            CategoryName VARCHAR(100)
        )
    """)

    insert_query = "INSERT INTO CarCategory (CategoryID, CategoryName) VALUES (%s, %s)"
    cursor.executemany(insert_query, car_categories)

    db.commit()
    cursor.close()
    
    print("CarCategory table created and populated successfully.")
