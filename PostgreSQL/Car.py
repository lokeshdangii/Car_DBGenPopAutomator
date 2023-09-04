import psycopg2
from faker import Faker
import random

def create_car(db):

    cursor = db.cursor()

    fake = Faker()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Car (
            CarID SERIAL PRIMARY KEY,
            VariantID INT,
            CategoryID INT,
            EngineID INT,
            ColorID INT,
            ModelID INT,
            VIN VARCHAR(17) UNIQUE,
            Mileage INT,
            YearOfManufacture INT,
            BrandCompany VARCHAR(100),
            FOREIGN KEY (VariantID) REFERENCES CarVariant(VariantID)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (CategoryID) REFERENCES CarCategory(CategoryID)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (EngineID) REFERENCES CarEngine(EngineID)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (ColorID) REFERENCES CarColor(ColorID)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (ModelID) REFERENCES CarModel(ModelID)
            ON UPDATE CASCADE
            ON DELETE CASCADE
        )
    """)

    car_data = []
    for _ in range(151):
        car_data.append((random.randint(1, 8), random.randint(1, 5), random.randint(1, 4),
                        random.randint(1, 10), random.randint(1, 15), fake.unique.random_int(min=10000000000000000, max=99999999999999999),
                        random.randint(12, 30), random.randint(2000, 2023), fake.company()))

    insert_query = "INSERT INTO Car (VariantID, CategoryID, EngineID, ColorID, ModelID, VIN, Mileage, YearOfManufacture, BrandCompany) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_query, car_data)

    db.commit()
    cursor.close()

    print("Car table created and populated successfully.")
