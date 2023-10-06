import mysql.connector
from faker import Faker

def create_finance(db):

    cursor = db.cursor()

    fake = Faker()

    # Create Finance table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Finance (
            FinanceID INT AUTO_INCREMENT PRIMARY KEY,
            SaleID INT,
            PaymentID INT,
            InstallmentID INT,
            FinancingTerm INT,
            InterestRate DECIMAL(5, 2),
            FOREIGN KEY (SaleID) REFERENCES Sale(SaleID)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (PaymentID) REFERENCES Payment(PaymentID)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
            FOREIGN KEY (InstallmentID) REFERENCES Installment(InstallmentID)
            ON UPDATE CASCADE
            ON DELETE CASCADE
        )
    """)

    # Populate Finance table
    finance_data = []
    for i in range(1, 100):
        finance_data.append((None, fake.random_int(min=1, max=99), fake.random_int(min=1, max=100), 
                            fake.random_int(min=1, max=100), fake.random_int(min=12, max=72), 
                            fake.pydecimal(left_digits=1, right_digits=1, positive = True)))
        
    insert_finance_query = "INSERT INTO Finance (FinanceID, SaleID, PaymentID, InstallmentID, FinancingTerm, InterestRate) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_finance_query, finance_data)

    db.commit()
    cursor.close()
   

    print("Finance table created and populated successfully.")
