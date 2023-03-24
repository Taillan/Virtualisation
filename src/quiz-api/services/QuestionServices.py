from models.Question import Question
from dao.QuestionDAO import *
from services.PossibleAnswersServices import *
from utils.errors import NotFound

def NewQuestionService(payload):
    question = QuestionFromJson(payload)
    
    try:
        original = GetQuestionService(question.position)
        offsetPositionQuestion(question.position, 1)
    except NotFound:
        pass

    question_id = saveQuestion(question)
    NewPossibleAnswersService(payload, question_id)
    return id

def GetQuestionService(position):
    sql_result = getQuestion(position)

    if sql_result == None:
        raise NotFound

    question = QuestionFromSQL(sql_result)
    answers = GetPossibleAnswersService(question.id)
    question.possibleAnswers = answers
    return question

def GetAllQuestionService():
    questions = AllQuestionFromSQL(getAllQuestion())
    for question in questions:
        answers = GetPossibleAnswersService(question.id)
        question.possibleAnswers = answers
    return questions

def UpdateQuestionService(position, payload):
    question = QuestionFromJson(payload)

    original = GetQuestionService(position)

    if question.position != original.position:
        UpdateQuestionPositionsService(question.position, original.position)

    updateQuestion(question, original.id)

    UpdatePossibleAnswerService(original.id, payload)

    return position

def UpdateQuestionPositionsService(newpos, oldpos):
    if newpos > oldpos:
        offsetPositionRangeQuestion(oldpos,newpos,-1)
    else:
        offsetPositionRangeQuestion(newpos,oldpos,1)


def DeleteQuestionService(position):
    question = GetQuestionService(position)
    if question == None:
        raise NotFound

    deleteQuestion(position)
    DeletePossibleAnswerService(question.id)
    offsetPositionQuestion(position,-1)

def GetNumberQuestions():
    return getNumberQuestions()[0]
    
def QuestionFromJson(payload):    
    try:
        title = payload['title']
    except:
        return "Missing title field"
    try:
        text = payload['text']
    except:
        return "Missing text field"
    try:
        position = payload['position']
    except:
        return "Missing position field"
    try:
        image = payload['image']
    except:
        image = ""
    return Question(title, text, position, image)

def QuestionFromSQL(payload):
    try:
        id = payload[0]
    except:
        return "Missing id"
    try:
        title = payload[1]
    except:
        return "Missing title"
    try:
        text = payload[2]
    except:
        return "Missing text"
    try:
        position = payload[3]
    except:
        return "Missing title"
    try:
        image = payload[4]
    except:
        image = "falseb64imagecontent"
    return Question(title, text, position, image, id)

def AllQuestionFromSQL(payload):
    questions = []
    for question in payload:
        questions.append(QuestionFromSQL(question))
    return questions