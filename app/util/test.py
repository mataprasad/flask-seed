from core.util.db_util import connection_pool
import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection
from mysql.connector import pooling

def test():
    try:
        print("Connection Pool Name - ", connection_pool.pool_name)
        connection_object = connection_pool.get_connection()
        print('connected',connection_object.is_connected())
        if connection_object.is_connected():
            db_Info = connection_object.get_server_info()
            cursor = connection_object.cursor()
            cursor.execute("select empno,ename,job from emp;")
            record = cursor.fetchall()
            #print("data", record)
            return record
    except Error as e:
        print ("Error while connecting to MySQL using Connection pool ", e)
    finally:
        if(connection_object.is_connected()):
            cursor.close()
            connection_object.close()
