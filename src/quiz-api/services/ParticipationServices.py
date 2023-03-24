from models.Participation import Participation
from dao.ParticipationDAO import *
from services.QuestionServices import GetNumberQuestions, GetQuestionService
from utils.errors import BadParticipation, NotFound
from utils.db_connect import get_cur

def NewParticipationService(payload):
    participation = ParticipationFromJson(payload)

    if len(participation.answers) != GetNumberQuestions():
        raise BadParticipation

    for index, answer in enumerate(participation.answers, start=1):
        if GetQuestionService(index).possibleAnswers[answer-1].isCorrect == True:
            participation.score+=1

    saveParticipation(participation)
    print(participation.score)
    return participation

def GetParticipationService(position):
    sql_result = getParticipation(position)

    if sql_result == None:
        raise NotFound

    participation = ParticipationFromSQL(sql_result)
    return participation

def GetAllParticipationService():
    return AllParticipationFromSQL(getAllParticipation())

def UpdateParticipationService(id, payload):
    participation = ParticipationFromJson(payload)
    return updateParticipation(participation, id)

def DeleteParticipationService(id):
    deleteParticipation(id)

    if get_cur.rowcount == 0:
        raise NotFound

def DeleteAllParticipations():
    deleteAllParticipation()
        
            
def ParticipationFromJson(payload):    
    try:
        playerName = payload['playerName']
    except:
        return "Missing playerName field"
    try:
        answers = payload['answers']
    except:
        return "Missing answers field"
    return Participation(playerName, answers)

def ParticipationFromSQL(payload):
    try:
        id = payload[0]
    except:
        return "Missing id"
    try:
        playerName = payload[1]
    except:
        return "Missing playerName"
    try:
        answers = payload[2]
    except:
        return "Missing answers"
    try:
        score = payload[3]
    except:
        return "Missing score"
    return Participation(playerName, answers, score, id)

def AllParticipationFromSQL(payload):
    participations = []
    for participation in payload:
        participations.append(ParticipationFromSQL(participation))
    return participations