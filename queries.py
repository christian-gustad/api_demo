import pyodbc
import os

def get_connection_string():
    SERVER = os.environ["SERVER"]
    USERNAME = os.environ["USERNAME"]
    PASSWORD = os.environ["PASSWORD"]
    DRIVER = '{ODBC Driver 17 for SQL Server}'
    DATABASE = "DwInsight"
    connection_string = f'DRIVER={DRIVER};SERVER=tcp:{SERVER};DATABASE={DATABASE};PORT=1433;UID={USERNAME};PWD={PASSWORD}'
    return connection_string


def my_query(parameter):
    connection_string = get_connection_string()
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    res = cursor.execute("Select * from DwStageNaviaq.CustomerLocations")
    rows = res.fetchall()
    data  = []
    for row in rows:
        data.append([x for x in row])
    return data
    


