import psycopg2
import random

def create_car_variant(db):

    cursor = db.cursor()

    # List of predefined vehicle models and variants
    vehicle_models = [
        "Toyota Corolla", "Honda Civic", "Ford Mustang", "Chevrolet Camaro", "Volkswagen Golf",
        "BMW 3 Series", "Nissan Altima", "Mercedes-Benz C-Class", "Jeep Wrangler", "Subaru Outback",
        "Tesla Model S", "Kia Sportage", "Hyundai Elantra", "Mazda CX-5", "Audi A4"
    ]

    vehicle_variants = [
        "Standard", "Deluxe", "Premium", "Limited", "Sport", "Eco", "Touring", "Tech"
    ]

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CarVariant (
            VariantID SERIAL PRIMARY KEY,
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
        car_variants.append((random.randint(1, len(vehicle_models)), random.randint(1, 10), random.randint(1, 5),
                            variant_name, random.uniform(10, 50), random.choice(["Gasoline", "Diesel", "Electric", "Hybrid"]),
                            random.uniform(15000, 80000)))

    insert_query = "INSERT INTO CarVariant (ModelID, ColorID, CategoryID, VariantName, Mileage, EngineType, Price) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_query, car_variants)

    db.commit()
    cursor.close()

    print("CarVariant table created and populated successfully.")
