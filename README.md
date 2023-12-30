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

## Task 3: Web Scraping - Real Estate Data from Batdongsan.com

The solution for this task is in the `task3/` directory.

- `main.py`: The script that scrapes the data from the website.
- `scraper.py`: Scraper class for scraping the data from an URL of multiple products.
- `product_parser.py`: Parser class for parsing the data from the HTML of a product page.
- `cache_schema.sql`: The SQL script that creates the tables and relationships for the cache schema.

### Usage

To run the script:
- Setup a virtual environment with `python3 -m venv venv`.
- Activate the virtual environment with `source venv/bin/activate`.
- Install the dependencies with `pip3 install -r requirements.txt`.
- Install `sqlite3`.
- Copy the `.env.example` file to `.env` and modify the variables to the desired values.
- Modify the `URL` variable in `main.py` to the desired URL.
- Run the script with `python3 main.py`.

## Task 4: Nested Set Model Implementation

The solution for this task is in the `task4/` directory.

- `data_gen.py`: The script that generates the data for the nested set model.
- `hierarchical_to_nested_set.py`: The script that converts the data from hierarchical model to nested set model.
- `retrieve_parent_child_relationship.py`: The script that retrieves the parent-child relationship from the nested set model.
- `schema.sql`: The SQL script that creates the tables and relationships for the schema.
- `benchmark.txt`: The output after benchmarking the performance of the above scripts.

There are also 2 example data files in the `task4/` directory:
- `small_example.csv`: The data file with 14 nodes.
- `large_example.csv`: The data file with 5018 nodes.

### Usage

To run the script:
- Setup a virtual environment with `python3 -m venv venv`.
- Activate the virtual environment with `source venv/bin/activate`.
- Install the dependencies with `pip3 install -r requirements.txt`.
- Install `sqlite3`.
- Create tables with `sqlite3 data.sqlite < schema.sql`.
- Modify the `MAX_DEPTH` and `MAX_CHILDREN` variables in `data_gen.py` to the desired value.
- Populate the database with `python3 data_gen.py`.
- Convert the data to nested set model with `python3 hierarchical_to_nested_set.py`.
- Retrieve the data from nested set model with `python3 retrieve_parent_child_relationship.py`.

## Task 5: Database and SQL - Stored Procedure Creation

The solution for this task is in the `task5/` directory.

- `schema.sql`: The SQL script that creates the tables and relationships for the schema.
- `procedure.sql`: The SQL script that creates the stored procedure.

### Usage

To create the schema:
- Create a database in MariaDB.
- Run the script with `mysql -u <username> -p <database_name> < schema.sql` to create the tables.
- Run the script with `mysql -u <username> -p <database_name> < procedure.sql` to create the stored procedure.
- The schema should be created in the database.