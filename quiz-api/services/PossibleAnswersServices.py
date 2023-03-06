
from models.PossibleAnswers import PossibleAnswers
from dao.PossibleAnswersDAO import *

def NewPossibleAnswersService(payload, question_id):
    possibleAnswers = PossibleAnswersFromJson(payload)
    savePossibleAnswers(possibleAnswers, question_id)

def GetPossibleAnswersService(id):
    return PossibleAnswersFromSQL(getPossibleAnswers(id))

def DeletePossibleAnswerService(id):
    deletePossibleAnswers(id)

def SavePossibleAnswerService(payload, question_id):
    savePossibleAnswers(payload, question_id)

def UpdatePossibleAnswerService(question_id, payload):
    DeletePossibleAnswerService(question_id)
    answers = PossibleAnswersFromJson(payload)
    SavePossibleAnswerService(answers, question_id)

def PossibleAnswersFromJson(payload):
    answers = []
    try:
        possibleAnswers = payload['possibleAnswers']
    except:
        return "Missing possibleAnswers field"
    for element in possibleAnswers:
        try:
            text = element['text']
        except:
            return "Missing text field"
        try:
            isCorrect = element['isCorrect']
        except:
            return "Missing isCorrect field or not a bool"
        answers.append(PossibleAnswers(text, isCorrect))
    return answers

def PossibleAnswersFromSQL(payload):
    answers = []
    for element in payload:
        try:
            id = element[0]
        except:
            return "Missing id field"
        try:
            text = element[1]
        except:
            return "Missing text field"
        try:
            isCorrect = element[2] == "True"
        except:
            return "Missing isCorrect field"
        answers.append(PossibleAnswers(text, isCorrect, id))
    return answers
