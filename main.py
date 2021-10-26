# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sqlalchemy
import fdb
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
    fb_url = "firebird://%s:%s@%s/%s"%(config["firebird"]["username"],config["firebird"]["password"],config["firebird"]["host"],config["firebird"]["db_path"])
    firebird_engine = create_engine(fb_url)
    firebird_engine.connect()

    # query file for firebird
    file = open("query.sql")
    query = text(file.read())

    result = firebird_engine.execute(query)
    row = result.fetchall()
    pdframe = pd.DataFrame(row)

    params = urllib.parse.quote_plus("DRIVER=%s;"
                                        "SERVER=%s;"
                                        "DATABASE=%s;"
                                        "UID=%s;"
                                        "PWD=%s" % (config["mssql"]["DRIVER"], config["mssql"]["SERVER"],
                                                    config["mssql"]["DATABASE"], config["mssql"]["USERNAME"],
                                                    config["mssql"]["PASSWORD"]))

    sql_engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))

    pdframe.to_sql(config["migration"]["table"], con=sql_engine, if_exists=config["migration"]["type"])
    # dk = sql_engine.execute("SELECT * FROM NEWUSER").fetchall()
    print(pdframe)