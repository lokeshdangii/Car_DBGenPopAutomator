import mysql.connector
from faker import Faker
import random

def create_car_model(db):

    cursor = db.cursor()

    # List of predefined vehicle models
    vehicle_models = [
        "Alto K10","Celerio","Ignis","Swift","Baleno","Dzire","Ciaz","Ertiga","XL6","Brezza","Grand Vitara","Fronx", "Jimny","Alto 800","Wagon R","S-Presso"]

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CarModel (
            ModelID INT AUTO_INCREMENT PRIMARY KEY,
            ModelName VARCHAR(100),
            CategoryID INT,
            EngineID INT,
            ModelSpecifications TEXT,
            FOREIGN KEY (CategoryID) REFERENCES CarCategory(CategoryID)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (EngineID) REFERENCES CarEngine(EngineID)
            ON UPDATE CASCADE
            ON DELETE CASCADE
        )
    """)

    car_models = []
    fake = Faker()
    for model_name in vehicle_models:
        car_models.append((None, model_name, random.randint(1, 5), random.randint(1, 4), fake.paragraph()))

    insert_query = "INSERT INTO CarModel (ModelID, ModelName, CategoryID, EngineID, ModelSpecifications) VALUES (%s, %s, %s, %s, %s)"
    cursor.executemany(insert_query, car_models)

    db.commit()
    cursor.close()
    

    print("CarModel table created and populated successfully.")
