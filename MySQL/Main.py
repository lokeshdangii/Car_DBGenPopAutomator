# modules to create and populate data in table
import mysql.connector
from CarColor import create_car_color
from CarCategory import create_car_category
from CarEngine import create_car_engine
from CarModel import create_car_model
from CarVariant import create_car_variant
from Car import create_car
from Customer import create_customer
from SalesPerson import create_salesperson
from Installment import create_installment
from Payment import create_payment
from Sale import create_sale
from Finance import create_finance

# Function to create and return a database connection
def create_database_connection(host, user, password, database_name):
    db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database_name
    )
    return db

# Function to create database and populate tables
def create_database():
    host = input("Enter the host name: ")
    user = input("Enter the user name: ")
    password = input("Enter the password: ")
    database_name = input("Enter the database name: ")

    db = create_database_connection(host, user, password, "")
    cursor = db.cursor()

     # Drop the database if it exists
    cursor.execute(f"DROP DATABASE IF EXISTS {database_name}")

    # Create a new database
    create_database_query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
    cursor.execute(create_database_query)

    print(f"\nDatabase '{database_name}' created successfully.\n")

    # Close the connection to create the new database
    cursor.close()
    db.close()

    # Establish connection to the created database
    db = create_database_connection(host, user, password, database_name)
    cursor = db.cursor()

    # Call other scripts to populate tables
    create_car_color(db)
    create_car_category(db)
    create_car_engine(db)
    create_car_model(db)
    create_car_variant(db)
    create_car(db)
    create_customer(db)
    create_salesperson(db)
    create_installment(db)
    create_payment(db)
    create_sale(db)
    create_finance(db)

    # close the connection
    cursor.close()
    db.close()

# Driver Code
if __name__ == "__main__":
    create_database()
