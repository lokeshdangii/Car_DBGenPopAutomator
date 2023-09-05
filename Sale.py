import mysql.connector
from faker import Faker

def create_sale(db):
    
    cursor = db.cursor()

    fake = Faker()

    # Create Sale table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Sale (
            SaleID INT AUTO_INCREMENT PRIMARY KEY,
            CustomerID INT,
            CarID INT,
            SalespersonID INT,
            PaymentID INT,
            SaleDate DATE,
            SalePrice INT,
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
    for i in range(1, 100):
        sale_data.append((None, fake.random_int(min=1, max=50), fake.random_int(min=1, max=100), 
                        fake.random_int(min=1, max=20), fake.random_int(min=1, max=100), 
                        fake.future_date(end_date='+1y'), fake.random_int(min = 500000,max = 2000000)))
    insert_sale_query = "INSERT INTO Sale (SaleID, CustomerID, CarID, SalespersonID, PaymentID, SaleDate, SalePrice) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_sale_query, sale_data)

    db.commit()
    cursor.close()
    

    print("Sale table created and populated successfully.")
