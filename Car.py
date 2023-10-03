import mysql.connector
from faker import Faker
import random

def create_car(db):

    cursor = db.cursor()

    fake = Faker()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Car (
            CarID INT AUTO_INCREMENT PRIMARY KEY,
            VariantID INT,
            CategoryID INT,
            EngineID INT,
            ColorID INT,
            ModelID INT,
            VIN VARCHAR(17) UNIQUE,
            Mileage FLOAT,
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
    for _ in range(100):
        car_data.append((None, random.randint(1, 8), random.randint(1, 5), random.randint(1, 4),
                        random.randint(1, 10), random.randint(1, 15), fake.unique.random_int(min=1000000000000000, max=9999999999999999),
                        round(random.uniform(12.0, 25.0), 2), random.randint(2014, 2023), "Maruti Suzuki"))

    insert_query = "INSERT INTO Car (CarID, VariantID, CategoryID, EngineID, ColorID, ModelID, VIN, Mileage, YearOfManufacture, BrandCompany) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_query, car_data)

    db.commit()
    cursor.close()
    

    print("Car table created and populated successfully.")
