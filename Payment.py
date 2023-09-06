import mysql.connector
from faker import Faker

def create_payment(db):
    
    cursor = db.cursor()

    fake = Faker()

    # Create Payment table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Payment (
            PaymentID INT AUTO_INCREMENT PRIMARY KEY,
            InstallmentID INT,
            PaymentAmount INT,
            PaymentDate DATE,
            PaymentMethod VARCHAR(50),
            TransactionID VARCHAR(100),
            PaymentDue DATE,
            DownPayment INT,
            FOREIGN KEY (InstallmentID) REFERENCES Installment(InstallmentID)
            ON UPDATE CASCADE
            ON DELETE CASCADE
        )
    """)

    # Populate Payment table
    payment_data = []
    for i in range(1, 101):
        payment_data.append((None, fake.random_int(min=1, max=100), 
                            fake.random_int(min=500000,max=2100000), 
                            fake.future_date(end_date='+1y'), 
                            fake.random_element(["Credit Card", "Debit Card", "Cash"]), 
                            fake.uuid4(), 
                            fake.future_date(end_date='+1y'), 
                            fake.random_int(min=50000,max=500000)))
    insert_payment_query = "INSERT INTO Payment (PaymentID, InstallmentID, PaymentAmount, PaymentDate, PaymentMethod, TransactionID, PaymentDue, DownPayment) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_payment_query, payment_data)

    db.commit()
    cursor.close()
    
    print("Payment table created and populated successfully.")
