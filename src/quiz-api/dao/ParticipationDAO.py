
from utils.db_connect import db_connection,get_cur

def saveParticipation(participation):
    instruction = f'insert into Participation (playerName,answers,score) values ("{participation.playerName}","{participation.answers}","{participation.score}")'
    db_connection(instruction)
    return get_cur().lastrowid

# TODO Manque les possible answer #
def updateParticipation(participation, id):
    instruction =   f'update Participation set playerName="{participation.playerName}", answers="{participation.answers}", score="{participation.score}" where id={id}'
    return db_connection(instruction)
    
def getParticipation(id):    
    instruction = f'select * from Participation where id={id}'
    return db_connection(instruction).fetchone()

def getAllParticipation():
    instruction = f'select * from Participation order by -score'
    return db_connection(instruction).fetchall()

def deleteParticipation(id):
    instruction = f'delete from Participation where id={id}'
    return db_connection(instruction)

def deleteAllParticipation():
    instruction = f'delete from Participation'
    return db_connection(instruction)