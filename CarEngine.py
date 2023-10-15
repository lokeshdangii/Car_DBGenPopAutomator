import mysql.connector

def create_car_engine(db):
    cursor = db.cursor()

    car_engines = [
        ("CNG",),
        ("Diesel",),
        ("Petrol",),
        ("Electric",)
    ]

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CarEngine (
            EngineID INT AUTO_INCREMENT PRIMARY KEY,
            EngineName VARCHAR(100)
        )
    """)

    insert_query = "INSERT INTO CarEngine (EngineName) VALUES (%s)"
    cursor.executemany(insert_query, car_engines)

    db.commit()
    cursor.close()

    print("CarEngine table created and populated successfully.")
