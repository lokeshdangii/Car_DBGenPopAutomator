import psycopg2

try:
    connection = psycopg2.connect(
        dbname="lokesh",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )
    print("Connected to database successfully!")

    cursor = connection.cursor()


    # Create the "customers" table
    create_table_query = '''
    CREATE TABLE customers (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(100)
    );
    '''
    cursor.execute(create_table_query)
    print("Table 'customers' created successfully!")



    # Insert sample data into the "customers" table
    insert_data_query = '''
    INSERT INTO customers (first_name, last_name, email)
    VALUES
        ('John', 'Doe', 'john@example.com'),
        ('Jane', 'Smith', 'jane@example.com'),
        ('Michael', 'Johnson', 'michael@example.com');
    '''
    cursor.execute(insert_data_query)
    connection.commit()
    print("Sample data inserted successfully!")

    cursor.close()
    connection.close()

    
except psycopg2.Error as e:
    print("Error connecting to database:", e)
