import psycopg2
from faker import Faker

def create_finance(db):

    cursor = db.cursor()

    fake = Faker()

    # Create Finance table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Finance (
            FinanceID SERIAL PRIMARY KEY,
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
    for i in range(1, 101):
        finance_data.append((fake.random_int(min=1, max=100), fake.random_int(min=1, max=100), 
                            fake.random_int(min=1, max=100), fake.random_int(min=12, max=72), 
                            fake.pydecimal(left_digits=3, right_digits=2)))
    insert_finance_query = "INSERT INTO Finance (SaleID, PaymentID, InstallmentID, FinancingTerm, InterestRate) VALUES (%s, %s, %s, %s, %s)"
    cursor.executemany(insert_finance_query, finance_data)

    db.commit()
    cursor.close()
    

    print("Finance table created and populated successfully.")
