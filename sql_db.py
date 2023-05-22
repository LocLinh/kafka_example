import pyodbc 

DRIVER = 'SQL SERVER'
# DRIVER = 'ODBC Driver 17 for SQL Server'
SERVER = '.\\SQLEXPRESS' 
DATABASE = 'HasakiDb' 
USERNAME = 'sa' 
PASSWORD = '123456' 

connection_string = f"""
    DRIVER={{{DRIVER}}};
    SERVER={SERVER};
    DATABASE={DATABASE};
    ENCRYPT=yes;
    UID={USERNAME};
    PWD={PASSWORD}
"""

# cnxn = pyodbc.connect(connection_string)
# cursor = cnxn.cursor()

def init_db():
    cnxn = pyodbc.connect(driver='{SQL Server}', host=SERVER, database=DATABASE, user=USERNAME, password=PASSWORD)
    return cnxn

