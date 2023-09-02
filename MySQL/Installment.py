import mysql.connector
from faker import Faker

def create_installment(db):
    
    cursor = db.cursor()

    fake = Faker()

    # Create Installment table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Installment (
            InstallmentID INT AUTO_INCREMENT PRIMARY KEY,
            InstallmentNumber INT,
            DueDate DATE,
            InstallmentAmount DECIMAL(10, 2),
            RemainingAmount DECIMAL(10, 2),
            TotalInstallment INT
        )
    """)

    # Populate Installment table
    installment_data = []
    for i in range(1, 101):
        installment_data.append((None, fake.random_int(min=1, max=12), fake.future_date(end_date='+1y'), 
                                fake.pydecimal(left_digits=5, right_digits=2), 
                                fake.pydecimal(left_digits=5, right_digits=2), 
                                fake.random_int(min=12, max=60)))
    insert_installment_query = "INSERT INTO Installment (InstallmentID, InstallmentNumber, DueDate, InstallmentAmount, RemainingAmount, TotalInstallment) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_installment_query, installment_data)

    db.commit()
    cursor.close()
   

    print("Installment table created and populated successfully.")
