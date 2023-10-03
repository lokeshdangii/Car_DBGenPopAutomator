import mysql.connector
import random

def create_car_variant(db):

    cursor = db.cursor()   #execute cursor

    # List of predefined vehicle models and variants
    vehicle_models = [
        "Alto K10","Celerio","Ignis","Swift","Baleno","Dzire","Ciaz","Ertiga","XL6","Brezza","Grand Vitara","Fronx", "Jimny","Alto 800","Wagon R","S-Presso"
    ]

    vehicle_variants = [
        "LXI","VXI","ZXI","Sigma","Delta","Zeta","Alpha","AMT","Hybrid","CNG","Tour"
        ]

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CarVariant (
            VariantID INT AUTO_INCREMENT PRIMARY KEY,
            ModelID INT,
            ColorID INT,
            CategoryID INT,
            VariantName VARCHAR(100),
            Mileage FLOAT,
            EngineType VARCHAR(50),
            Price DECIMAL(10, 2),
            FOREIGN KEY (ModelID) REFERENCES CarModel(ModelID)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (ColorID) REFERENCES CarColor(ColorID)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (CategoryID) REFERENCES CarCategory(CategoryID)
            ON UPDATE CASCADE
            ON DELETE CASCADE
        )
    """)

    car_variants = []
    for variant_name in vehicle_variants:
        car_variants.append((None, random.randint(1, len(vehicle_models)), random.randint(1, 10), random.randint(1, 5),
                            variant_name, random.uniform(10, 50), random.choice(["CNG", "Diesel", "Petrol", "Hybrid"]),
                            random.uniform(15000, 80000)))

    insert_query = "INSERT INTO CarVariant (VariantID, ModelID, ColorID, CategoryID, VariantName, Mileage, EngineType, Price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_query, car_variants)

    db.commit()
    cursor.close()
    

    print("CarVariant table created and populated successfully.")
