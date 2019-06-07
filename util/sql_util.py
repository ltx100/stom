import pymysql

def connect_db():
    conn = pymysql.connect()
    return conn, conn.cursor()

def intsert_sql(insert_str):
    conn, cursor = connect_db
    result = cursor.execute(insert_str)
    conn.comit()
    cursor.close()
    conn.close()
    return result