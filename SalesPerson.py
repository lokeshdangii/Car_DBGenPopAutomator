import mysql.connector
from faker import Faker
import random

def create_salesperson(db):
    
    cursor = db.cursor()

    fake = Faker()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS SalesPerson (
            SalesPersonID INT AUTO_INCREMENT PRIMARY KEY,
            SP_Name VARCHAR(50),
            Gender VARCHAR(10) NOT NULL,
            DateOfBirth DATE NOT NULL,
            MobileNo VARCHAR(15) NOT NULL,
            email VARCHAR(100) NOT NULL,
            Address1 VARCHAR(100) NOT NULL,
            Address2 VARCHAR(100) NOT NULL,
            City VARCHAR(50) NOT NULL,
            State VARCHAR(50) NOT NULL,
            PinCode VARCHAR(20) NOT NULL
        )
    """)

    salesperson_data = []
    for i in range(1, 21):
        salesperson_data.append((i, fake.name(), fake.random_element(["Male", "Female"]), fake.date_of_birth(minimum_age=25, maximum_age=65),
                                 fake.phone_number()[:11], fake.email(), fake.street_address(), fake.secondary_address(), fake.city(),
                                 fake.state(), fake.zipcode()))
    insert_salesperson_query = "INSERT INTO SalesPerson (SalesPersonID, SP_Name, Gender, DateOfBirth, MobileNo, email, Address1, Address2, City, State, PinCode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_salesperson_query, salesperson_data)

    db.commit()
    cursor.close()
    

    print("SalesPerson table created and populated successfully.")

if __name__ == "__main__":
    create_salesperson()
