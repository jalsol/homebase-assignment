# Homebase Take-Home Assignment

Candidate: Quang-Truong Nguyen

This is my submission for the Homebase Take-Home Assignment. There are 5 tasks in total.

The version of Python used is 3.10.12. The version of MariaDB used is 10.6.12.

## Task 1: Python Programming

The solution for this task is in the `task1/` directory.
- `average_age.py`: The script that calculates the average age of all users in the `data.csv` file.
- `data*.csv`: The data files used for testing the script.

### Usage

To run the script:
- Change the variables `INPUT_CSV_FILE` and `DELIMITER` in `average_age.py` to the desired values.
- Run the script with `python3 average_age.py`.

## Task 2: Data Structures: E-commerce Inventory Schema 

The solution for this task is in the `task2/` directory.
- `schema.sql`: The SQL script that creates the tables and relationships for the schema.
- `diagram.png`: The ER diagram for the schema.

### Usage

To create the schema:
- Create a database in MariaDB.
- Run the script with `mysql -u <username> -p <database_name> < schema.sql`.
- The schema should be created in the database.
