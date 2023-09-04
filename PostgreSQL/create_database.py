import psycopg2

# Connect to the PostgreSQL server with autocommit mode
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
        exit(1)


# Database name to create
new_database_name = 'new_db'

try:
    with connection.cursor() as cursor:
        # Check if the database already exists
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{new_database_name}'")
        exists = cursor.fetchone()

        if exists:
            # Drop the existing database
            cursor.execute(f"DROP DATABASE {new_database_name}")
            print(f"Database '{new_database_name}' dropped successfully.")

        # Create a new database
        cursor.execute(f"CREATE DATABASE {new_database_name}")
        print(f"Database '{new_database_name}' created successfully.")

except psycopg2.Error as e:
    print(f"Error: Unable to create or drop the database '{new_database_name}'")
    print(e)
finally:
    connection.close()
