import json
from flask import Flask, request
from utils.jwt_utils import build_token
from services.ParticipationServices import *
from services.QuestionServices import *
from utils.errors import *
from flask_cors import CORS
from blueprints.ParticipationsController import participation_blueprint
from blueprints.QuestionController import question_blueprint
from utils.db_connect import get_db, get_cur

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.register_blueprint(question_blueprint)
app.register_blueprint(participation_blueprint)
CORS(app)

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": GetNumberQuestions(), "scores": [ p.toJSON() for p in GetAllParticipationService() ]}, 200

@app.route('/login', methods=['POST'])
def Login():
	payload = request.get_json()

	try:
		password = payload['password']
	except:
		return BAD_REQUEST_PASSWORD_MESSAGE, 400

	if password == "Vive l'ESIEE !":
		response = {"token": build_token()}
		return json.dumps(response), 200
	else:
		return WRONG_PASSWORD_MESSAGE, 401

if __name__ == "__main__":
	with app.app_context():
		get_db()
		get_cur()
	app.run()