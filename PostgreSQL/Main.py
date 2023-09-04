# import all required modules
import psycopg2
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


# -----------------------------------------------Connection and Database Creation -----------------------------------------------------

def create_connection_and_newdb(database_name):

    # Connect to the PostgreSQL server (postgres DB) with autocommit mode
    # try except for connection

    try:
        connection = psycopg2.connect(
                host="localhost",
                user="postgres",
                password="root",
                dbname="postgres",
                port=5432)
        
        connection.autocommit = True  # Disable transactions
        
    except psycopg2.Error as e:
        print("Error: Unable to connect to the database")
        print(e)
        return None


    # -------------------------------------------------------- DROP & CREATE -------------------------------------------------------------
    # try except to drop and create database
    try:
        with connection.cursor() as cursor:
            # Check if the database already exists
            cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{database_name}'")
            exists = cursor.fetchone()

            if exists:
                # Drop the existing database
                cursor.execute(f"DROP DATABASE {database_name}")
                print(f"Database '{database_name}' dropped successfully.")

            # Create a new database
            cursor.execute(f"CREATE DATABASE {database_name}")
            print(f"Database '{database_name}' created successfully.")

    except psycopg2.Error as e:
        print(f"Error: Unable to create or drop the database '{database_name}'")
        print(e)
        return None




# ---------------------------- Create tables and Poulate data ----------------------------------------------------------------

# Function to create tables and populate data
def create_tables_and_populate_data(database_name):

    # Establish connection to the new created database
    db = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="root",
            dbname=database_name,
            port=5432)
    
    if db is None:
        return

    cursor = db.cursor()

    # Calling other scripts to populate tables
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

    # Commit changes and close the connection
    db.commit()
    cursor.close()
    db.close()


# Driver Code
if __name__ == "__main__":
    database_name = input("Enter the database name: ")
    create_connection_and_newdb(database_name)
    create_tables_and_populate_data(database_name)
