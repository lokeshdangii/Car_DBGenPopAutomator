import psycopg2
from faker import Faker

def create_sale(db):
    
    cursor = db.cursor()

    fake = Faker()

    # Create Sale table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Sale (
            SaleID SERIAL PRIMARY KEY,
            CustomerID INT,
            CarID INT,
            SalespersonID INT,
            PaymentID INT,
            SaleDate DATE,
            SalePrice DECIMAL(10, 2),
            FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (CarID) REFERENCES Car(CarID)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (SalespersonID) REFERENCES SalesPerson(SalesPersonID)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (PaymentID) REFERENCES Payment(PaymentID)
            ON UPDATE CASCADE
            ON DELETE CASCADE
        )
    """)

    # Populate Sale table
    sale_data = []
    for i in range(1, 101):
        sale_data.append((fake.random_int(min=1, max=50), fake.random_int(min=1, max=100), 
                        fake.random_int(min=1, max=20), fake.random_int(min=1, max=100), 
                        fake.future_date(end_date='+1y'), fake.pydecimal(left_digits=5, right_digits=2)))
    insert_sale_query = "INSERT INTO Sale (CustomerID, CarID, SalespersonID, PaymentID, SaleDate, SalePrice) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_sale_query, sale_data)

    db.commit()
    cursor.close()
    

    print("Sale table created and populated successfully.")
