import psycopg2

def create_car_color(db):
    cursor = db.cursor()

    car_colors = [
        (1, "White"),
        (2, "Black"),
        (3, "Silver"),
        (4, "Gray"),
        (5, "Red"),
        (6, "Blue"),
        (7, "Green"),
        (8, "Brown"),
        (9, "Yellow"),
        (10, "Orange")
    ]

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CarColor (
            ColorID SERIAL PRIMARY KEY,
            ColorName VARCHAR(50)
        )
    """)

    insert_query = "INSERT INTO CarColor (ColorID, ColorName) VALUES (%s, %s)"
    cursor.executemany(insert_query, car_colors)

    db.commit()
    cursor.close()

    print("CarColor table created and populated successfully.")
