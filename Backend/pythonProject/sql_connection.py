import mysql.connector
__cnx = None

def get_sql_connection():
    global __cnx

    __cnx = mysql.connector.connect(user='root', password='Rohan@1213',
                                  host='127.0.0.1',
                                  database='shop')
    return __cnx