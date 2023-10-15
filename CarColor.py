import mysql.connector

# function to create CarColor table
def create_car_color(db):
    cursor = db.cursor()

    car_colors = [
        ("White",),
        ("Black",),
        ("Silver",),
        ("Gray",),
        ("Red",),
        ("Blue",),
        ("Green",),
        ("Brown",),
        ("Yellow",),
        ("Orange",)
    ]

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CarColor (
            ColorID INT AUTO_INCREMENT PRIMARY KEY,
            ColorName VARCHAR(50)
        )
    """)

    insert_query = "INSERT INTO CarColor (ColorName) VALUES (%s)"
    cursor.executemany(insert_query, car_colors)

    db.commit()
    cursor.close()
   
    print("CarColor table created and populated successfully.")
