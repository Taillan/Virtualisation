import sqlite3
from flask import g
import mysql.connector
import os

def get_db():
    con = getattr(g, '_database', None)
    if con is None:
        con = g._database = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DB")
            )
    return con

def get_cur():
    cur = getattr(g, '_cursor', None)
    if cur is None:
        cur = g._cursor = get_db().cursor(buffered=True)
    return cur

def db_connection(instruction):
    try:
        #création d'un objet connection
        get_cur().execute(instruction)
        get_db().commit()
        return get_cur()
    except ValueError as er:
        print("error : ", er)
