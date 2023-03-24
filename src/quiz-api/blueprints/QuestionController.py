from flask import Blueprint
import json
from flask import request
from utils.jwt_utils import  verify_token
from services.ParticipationServices import *
from services.QuestionServices import *
from utils.errors import *

question_blueprint = Blueprint('question', __name__)

@question_blueprint.route('/questions', methods=['POST'])
def NewQuestion():
	try:
		verify_token(request.headers.get('Authorization'))
	except BadToken:
		return BAD_TOKEN_MESSAGE, 401
	except WrongToken:
		return WRONG_TOKEN_MESSAGE, 401

	payload = request.get_json()

	try:
		NewQuestionService(payload)
		return QUESTION_CREATED_MESSAGE, 200
	except AlreadyExisting:
		return POSITION_ERROR_MESSAGE, 400
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500


@question_blueprint.route('/questions', methods=['GET'])
def GetAllQuestion():
	try:
		questions = json.dumps([ q.toJSON() for q in GetAllQuestionService()])
		return questions, 200
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500 
	

@question_blueprint.route('/questions/<int:question_position>', methods=['DELETE'])
def DelQuestion(question_position):
	try:
		verify_token(request.headers.get('Authorization'))
	except BadToken:
		return BAD_TOKEN_MESSAGE, 401
	except WrongToken:
		return WRONG_TOKEN_MESSAGE, 401

	try:
		DeleteQuestionService(question_position)
		return QUESTION_DELETED_MESSAGE, 204
	except NotFound:
		return NOT_FOUND_MESSAGE , 404
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500 
	


@question_blueprint.route('/questions/<int:position>', methods=['GET'])
def GetQuestion(position):
	try:
		result = GetQuestionService(position)
		return result.toJSON(), 200
	except NotFound :
		return NOT_FOUND_MESSAGE , 404
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500

@question_blueprint.route('/questions/<int:position>', methods=['PUT'])
def UpdateQuestion(position):
	try:
		verify_token(request.headers.get('Authorization'))
	except BadToken:
		return BAD_TOKEN_MESSAGE, 401
	except WrongToken:
		return WRONG_TOKEN_MESSAGE, 401

	payload = request.get_json()

	try:
		UpdateQuestionService(position, payload)
	except NotFound:
		return NOT_FOUND_MESSAGE, 404
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500
	return QUESTION_UPDATED_MESSAGE, 200