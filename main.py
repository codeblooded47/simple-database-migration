# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sqlalchemy
import pyodbc 
from sqlalchemy import create_engine
import json
import pandas as pd
import urllib
import time
from sqlalchemy.sql import text
if __name__ == '__main__':
    f = open('config.json', )
    config = json.load(f)
    f.close()

    print('Migrating..')
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+config["mssql"]["SERVER"]+';DATABASE='+config["mssql"]["DATABASE"]+';UID='+config["mssql"]["USERNAME"]+';PWD='+ config["mssql"]["PASSWORD"])
    cursor = cnxn.cursor()

    # query file for firebird
    file = open("query.sql")
    query = text(file.read())

    result = cursor.execute(query)
    row = result.fetchall()
    pdframe = pd.DataFrame(row)

    sql_engine = create_engine("mysql+mysqldb://%s:%s@%s/%s" % (config["mysql"]["USERNAME"], 
                                                    config["mysql"]["PASSWORD"], config["mysql"]["SERVER"],
                                                    config["mysql"]["DATABASE"]) )

    pdframe.to_sql(config["migration"]["table"], con=sql_engine, if_exists=config["migration"]["type"])
    print(pdframe)