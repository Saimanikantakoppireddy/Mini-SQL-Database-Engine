# Mini SQL Database Engine in Python

## Project Overview
This project is a simplified, in-memory SQL query engine built using Python.  
It loads data from CSV files into memory and allows users to run basic SQL queries
through a command-line interface.

The goal of this project is to demonstrate how SQL queries are parsed and executed
internally without using any database system.
## Features Supported
- Load CSV files into memory
- Interactive SQL command-line interface (REPL)
- Data stored as a list of dictionaries
- Query execution with filtering, projection, and aggregation
- Clear and graceful error handling

## Setup Instructions
### Requirements
- Python 3.x
- No external libraries required

### Run the Application
1. Open a terminal in the project folder
2. Run: python cli.py
3. Type SQL queries at the prompt
4. Type exit or quit to close the application

## Supported SQL Grammar
This engine supports the following SQL syntax only:

SELECT
SELECT * FROM table
SELECT column1, column2 FROM table
WHERE (Single Condition Only)

Supported operators:
=
!=
>
<
>=
<=

Examples:
SELECT * FROM users WHERE age > 30
SELECT name FROM users WHERE country = 'USA'

COUNT Aggregation
SELECT COUNT(*) FROM table
SELECT COUNT(column_name) FROM table

Examples:

SELECT COUNT(*) FROM users
SELECT COUNT(country) FROM users WHERE country = 'USA'

Example Queries
SELECT * FROM users
SELECT name, age FROM users WHERE age > 30
SELECT COUNT(*) FROM users
SELECT COUNT(country) FROM users WHERE country = 'USA'

# Sample CSV Files
The repository includes sample CSV files inside the data/ folder:
users.csv
products.csv

Each CSV file name is treated as a table name

## Project Structure

sql_engine/
│── parser.py      
│── engine.py     
│── cli.py        
│── README.md
│── data/
│   ├── users.csv
│   ├── products.csv

### Limitations

Only SELECT queries are supported
Only one WHERE condition allowed
No JOIN, ORDER BY, GROUP BY, or UPDATE queries
All data is processed in memory

# Conclusion

This project provides a clear demonstration of how a basic SQL engine works
internally by parsing queries, filtering rows, projecting columns, and performing
simple aggregations on CSV data.
