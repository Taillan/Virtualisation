import sqlite3
from flask import g
import mariadb

database = "db/database.db"


def get_db():
    con = getattr(g, '_database', None)
    if con is None:
        con = mariadb.connect(
            host='127.0.0.1',
            port= 3306,
            user='root',
            password='rootroot',
            database='QuizzDB')
    return con

def get_cur():
    cur = getattr(g, '_cursor', None)
    if cur is None:
        cur = g._cursor = get_db().cursor()
    return cur

def db_connection(instruction):
    try:
        #création d'un objet connection
        sql_result = get_cur().execute(instruction)            
        get_db().commit()        
        return sql_result
    except sqlite3.Error as er:
        print("error : ", er)


        import mariadb
from flask import g, jsonify 
import sys
