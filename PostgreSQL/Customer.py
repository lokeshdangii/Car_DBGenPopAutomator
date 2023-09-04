import psycopg2
from faker import Faker

def create_customer(db):
    
    cursor = db.cursor()

    fake = Faker()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customer (
            CustomerID SERIAL PRIMARY KEY,
            C_Name VARCHAR(50) NOT NULL,
            Gender VARCHAR(10) NOT NULL,
            DateOfBirth DATE NOT NULL,
            Phone VARCHAR(15) NOT NULL,
            Email VARCHAR(100) NOT NULL,
            Address1 VARCHAR(100) NOT NULL,
            Address2 VARCHAR(100) NOT NULL,
            City VARCHAR(50) NOT NULL,
            State VARCHAR(50) NOT NULL,
            PinCode VARCHAR(20) NOT NULL
        )
    """)

    customer_data = []
    for _ in range(101):
        customer_data.append((fake.name(), fake.random_element(["Male", "Female"]), fake.date_of_birth(minimum_age=18, maximum_age=65),
                              fake.phone_number()[:11], fake.email(), fake.street_address(), fake.secondary_address(), fake.city(),
                              fake.state(), fake.zipcode()))
    insert_customer_query = "INSERT INTO Customer (C_Name, Gender, DateOfBirth, Phone, Email, Address1, Address2, City, State, PinCode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_customer_query, customer_data)

    db.commit()
    cursor.close()
    

    print("Customer table created and populated successfully.")
