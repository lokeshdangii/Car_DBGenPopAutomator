# Database Generation and Population Automator
**DBGenPopAutomator:** A Python Module for automating the creation and population of car showroom database with realistic sample data.

## Overview

This project automates the process of creating a MySQL database and populating it with sample data using Python scripts. It leverages the `mysql.connector` library for database connectivity and the `Faker` library for generating sample data.

## Project Structure

The project consists of the following components:

### Main Script

- **Main.py:** This script is the entry point of the automation process. It imports and executes individual scripts for each table creation and data population.

### Individual Scripts

- **Car.py:** Create and populate the Car table.
- **CarCategory.py:** Create and populate the CarCategory table.
- **CarColor.py:** Create and populate the CarColor table.
- **CarEngine.py:** Create and populate the CarEngine table.
- **CarModel.py:** Create and populate the CarModel table.
- **CarVariant.py:** Create and populate the CarVariant table.
- **Customer.py:** Create and populate the Customer table.
- **Finance.py:** Create and populate the Finance table.
- **Installment.py:** Create and populate the Installment table.
- **Payment.py:** Create and populate the Payment table.
- **Sale.py:** Create and populate the Sale table.
- **SalesPerson.py:** Create and populate the SalesPerson table.

## Steps Taken

1. **Database Setup:** The Main.py script starts by checking for an existing database. If found, it drops the database to ensure a clean slate.

2. **Table Creation:** Each individual script corresponds to a specific table. These scripts create the necessary tables, defining primary keys, foreign keys, and attributes for each table.

3. **Data Population:** The same individual scripts handle data population for each table. The Faker library is used to generate random but realistic data for different attributes.

4. **Foreign Key Constraints:** The scripts ensure that foreign key references are maintained, ensuring data integrity across tables.

## Prerequisites

Before running the scripts, make sure you have the following:

- Python 3.5 or higher installed.
- MySQL server installed and running.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/lokeshdangii/DBGenPopAutomator
    cd DBGenPopAutomator
    ```

2. Install project dependencies from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

This ensures that the required Python packages (Faker and MySQL Connector) are installed.

## How to Run

1. Ensure your MySQL server is up and running.

2. Navigate to the repository directory and execute the main script:

    ```bash
    python Main.py
    ```

This script automatically creates database tables and populates them with data using individual scripts.

## DB Schema

Here is link to my database schema.You can view it from [here](https://docs.google.com/spreadsheets/d/142qSCSo7DvzJm0dkXzN0Z9ECH6Y3db7tqqDw3qo8G8s/edit#gid=0).

## Conclusion

This project showcases the power of automation in database setup and data population for a car dealership management system. By utilizing Python scripts, Faker library, and MySQL Connector, we have successfully streamlined the process, enabling consistent, efficient, and error-free database creation and population.

## Contributing

Feel free to contribute by submitting error and feature requests through the [GitHub repository](https://github.com/lokeshdangii/DBGenPopAutomator). Pull requests are also welcome!

## Acknowledgements

- [Faker Library](https://faker.readthedocs.io/en/master/): A Python library for generating fake data.
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/): Python driver for MySQL.

## Contact

You can reach me via email at [lokeshdangi1045@gmail.com](mailto:lokeshdangi1045@gmail.com) or connect with me on [LinkedIn](https://www.linkedin.com/in/lokeshdangi/)

## License

This project is licensed under the MIT License. [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


Thank you for visiting my repository!


