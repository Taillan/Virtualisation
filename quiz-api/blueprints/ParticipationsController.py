from flask import Blueprint
from flask import request
from utils.jwt_utils import verify_token
from services.ParticipationServices import *
from services.QuestionServices import *
from utils.errors import *

participation_blueprint = Blueprint('participation', __name__)

@participation_blueprint.route('/participations', methods=['POST'])
def NewParticipations():

	payload = request.get_json()

	try:
		participation = NewParticipationService(payload)
		return participation.toJSON(), 200
	except BadParticipation:
		return BAD_PARTICIPATION_MESSAGE, 400
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500

@participation_blueprint.route('/participations', methods=['DELETE'])
def DelAllParticipation():
	try:
		verify_token(request.headers.get('Authorization'))
	except BadToken:
		return BAD_TOKEN_MESSAGE, 401
	except WrongToken:
		return WRONG_TOKEN_MESSAGE, 401

	try:
		DeleteAllParticipations()
		return ALLPARTICIPANT_DELETED_MESSAGE, 204
	except ValueError:
		return INTERNAL_ERROR_MESSAGE + ValueError, 500 
