import psycopg2

def create_car_engine(db):
    cursor = db.cursor()

    car_engines = [
        (1, "Gasoline"),
        (2, "Diesel"),
        (3, "Electric"),
        (4, "Hybrid")
    ]

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CarEngine (
            EngineID SERIAL PRIMARY KEY,
            EngineName VARCHAR(100)
        )
    """)

    insert_query = "INSERT INTO CarEngine (EngineID, EngineName) VALUES (%s, %s)"
    cursor.executemany(insert_query, car_engines)

    db.commit()
    cursor.close()

    print("CarEngine table created and populated successfully.")
