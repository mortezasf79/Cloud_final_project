import datetime
import os
import time
from flask import jsonify
import pymysql
import mysql.connector
from dotenv import load_dotenv



host = os.environ.get('DB_HOST')
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
database = os.environ.get('DB_DATABASE')


load_dotenv()

def pprint():
    print("hello")



def cr_tb():
    timeout = 10
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE mytest (id INTEGER PRIMARY KEY)")
        cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
        cursor.execute("SELECT * FROM mytest")
        print(cursor.fetchall())
    finally:
        connection.close()





def count_of_server():
    timeout = 10
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT MAX(id) FROM server")
        max_id = cursor.fetchall()[0]['MAX(id)']
        # print(max_id)
        return max_id
        
    finally:
        connection.close()






def success_check(id):
    timeout = 10
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT success FROM server WHERE id = %s", (id))
        success = cursor.fetchone()['success']
        success += 1
        cursor.execute("UPDATE server SET success = %s WHERE id = %s", (success, id))
        connection.commit()

    finally:
        cursor.close()
        connection.close()






def failure_check(id):
    timeout = 10
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT failure FROM server WHERE id = %s", (id))
        failure = cursor.fetchone()['failure']
        failure += 1
        last_failure = time.time()
        cursor.execute("UPDATE server SET failure = %s, last_failure = %s WHERE id = %s", (failure, last_failure, id))
        connection.commit()

    finally:
        cursor.close()
        connection.close()








def ceate_table():
    timeout = 10 
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    


    try:
         cursor = connection.cursor() 
         query = '''CREATE TABLE IF NOT EXISTS server (id VARCHAR(256) PRIMARY KEY , address VARCHAR(256), success INT, 
                failure INT, last_failure VARCHAR(255), created_at VARCHAR(255)
            ) 
         '''
         cursor.execute(query) 
         connection.commit() 
         print() 
         print(cursor.fetchall()) 
    finally: 
        cursor.close()
        connection.close()






def insert_table(address):
    timeout = 10 
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    


    try:
         cursor = connection.cursor() 

         cursor.execute("SELECT MAX(id) FROM server")
         max_id = cursor.fetchall()[0]['MAX(id)']

        #  created_at = datetime.datetime.now()
         created_at = time.time()

         if max_id is not None:
            current_id = str(int(max_id) + 1)
         else:
            # در صورتی که مقدار max_id خالی باشد، مقدار اولیه برای current_id تعیین کنید
            current_id = "1"

         insert_query = "INSERT INTO server (id , address, success, failure, last_failure, created_at) VALUES (%s, %s, %s, %s, %s, %s)" 
         

         values = (current_id, address, 0, 0, "null", created_at) 
         cursor.execute(insert_query, values) 
         connection.commit() 
         print() 
         print(cursor.fetchall()) 
    finally: 
        connection.close()






def delete_table():
    timeout = 10 
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    


    try:
         cursor = connection.cursor() 
         query = "DELETE FROM server" 
         
         cursor.execute(query) 
         connection.commit() 
         print() 
    finally: 
        cursor.close()
        connection.close()







def getAllInfo():
    timeout = 10 
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    


    try:
        cursor = connection.cursor() 
        select_query = "SELECT id, address, success, failure, last_failure, created_at FROM server"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print()
        connection.commit() 
        return rows
        
    finally: 
        cursor.close()
        connection.close()
        




def show_info(server_id):
    timeout = 10 
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    try:
        cursor = connection.cursor() 
        select_query = "SELECT id, address, success, failure, last_failure, created_at FROM server where id = %s"
        cursor.execute(select_query, (server_id))
        data = cursor.fetchall()
        print(data)
        connection.commit() 
        return data
        
    finally: 
        cursor.close()
        connection.close()

    



def showInfo(ipAddress, email, lastName, nationalCode): 
    data = { "ip_address": ipAddress, "email": email, "last_name": lastName, "national_code": nationalCode, } 
    json_data = jsonify(data) 
    return json_data