
# SIMPLE DATABASE MIGRATION

A brief description of what this project does and what are the requirements.


## What is the use of this Repo
This Project simple database migration From One database to another using sql query.


## Requirements(windows)
- Firebird Server
- Python 3.10
- ODBC Driver for SQL Server

## Prerequisites
 ### 1. Download Firebird Server
 Download the firebird Server for windows.
[Firebird-Server](https://firebirdsql.org/en/firebird-3-0-7/#Win64)
 ### 2. Download Python
 Download 3.10 or latest version of Python
 ### 3. Download ODBC Driver for SQL Server
 Download ODBC From microsoft [ODBC DRIVER](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15)
 [Firebird-Server](https://firebirdsql.org/en/firebird-3-0-7/#Win64)
 ## Cloning and Running the Application in local

 Clone the Project into local

 Install the Python Requirements.

 ```
 pip install -r Requirements.txt

 ```
Edit the config.json

```
{
  "firebird":{
    "username":"sysdba",
    "password":"master",
    "host":"localhost",
    "db_path":"C:/user/firebird/firebird-db/examples.fdb" // put your firebird here
  },
  "mssql": {
    "DRIVER": "{ODBC Driver 17 for SQL Server}",
    "SERVER": "tcp:you-data-url.database.windows.net",
    "DATABASE": "database",
    "USERNAME": "username",
    "PASSWORD": "password"
  },
  "migration": {
    "table": "table-name",
    "type": "replace"
  }
}
```
Run run.bat file in your terminal.

### For Running continuously 
- User windows Schedule. [how](https://www.geeksforgeeks.org/schedule-a-python-script-to-run-daily/) 


