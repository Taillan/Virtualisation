import sqlite3
from flask import g

database = "db/database.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database)
        db.isolation_level = None
    return db

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