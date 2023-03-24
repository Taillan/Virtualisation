from utils.db_connect import db_connection

def savePossibleAnswers(answers, question_id):
    instruction = f'insert into PossibleAnswers(question_id,text,isCorrect) values'
    for answer in answers:
        instruction += (
            f'("{question_id}",'
            f'"{answer.text}",'
            f'"{answer.isCorrect}"),'
        )
    return db_connection(instruction[:-1])

def getPossibleAnswers(id):
    instruction = f'select id,text,isCorrect from PossibleAnswers where question_id={id}'
    return db_connection(instruction)

def deletePossibleAnswers(id):
    instruction = f'delete from PossibleAnswers where question_id={id}'
    return db_connection(instruction)