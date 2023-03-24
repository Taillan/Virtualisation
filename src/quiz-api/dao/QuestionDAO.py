from utils.db_connect import db_connection, get_cur

def saveQuestion(question):
    instruction = f'insert into Question (title,text,position,image) values ("{question.title}","{question.text}","{question.position}","{question.image}")'
    db_connection(instruction)
    print(get_cur().lastrowid)
    return get_cur().lastrowid

# TODO Manque les possible answer #
def updateQuestion(question, id):
    instruction =   f'update Question set title="{question.title}", text="{question.text}", \
                image="{question.image}", position={question.position} where id={id}'
    return db_connection(instruction)

def updatePositionQuestion(newpos, oldpos):
    instruction = f'update Question set position={newpos} where position={oldpos}'
    return db_connection(instruction)

def offsetPositionRangeQuestion(minrange, maxrange, offset):
    instruction = f'update Question set position=position+{offset} where position between {minrange} and {maxrange}'
    return db_connection(instruction)

def offsetPositionQuestion(position, offset):
    instruction = f'update Question set position=position+{offset} where position>={position}'
    return db_connection(instruction)
    
def getQuestion(position):    
    instruction = f'select * from Question where position={position}'
    return db_connection(instruction).fetchone()

def getAllQuestion():
    instruction = f'select * from Question'
    return db_connection(instruction).fetchall()

def deleteQuestion(position):
    instruction = f'delete from Question where position={position}'
    return db_connection(instruction)

def getNumberQuestions():
    instruction = f'select count(*) as count from Question;'
    return db_connection(instruction).fetchone()