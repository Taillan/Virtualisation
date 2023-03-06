# define Python user-defined exceptions
NOT_FOUND_MESSAGE = "Question not found"
BAD_REQUEST_PASSWORD_MESSAGE = "Missing password field in JSON body"
WRONG_PASSWORD_MESSAGE = "Wrong password"
BAD_TOKEN_MESSAGE = "Error while parsing token, ensure it's in form : 'Bearer ...'"
WRONG_TOKEN_MESSAGE = "Wrong token, please reload it"
PARTICIPATION_CREATED_MESSAGE = "Participation successfully created"
BAD_PARTICIPATION_MESSAGE = "The player need to answer precisely the number of questions"
ALLPARTICIPANT_DELETED_MESSAGE = "All participation successfully deleted"
QUESTION_CREATED_MESSAGE = "Question successfully created"
QUESTION_DELETED_MESSAGE = "Question successfully deleted"
QUESTION_UPDATED_MESSAGE = "Question successfully updated"
POSITION_ERROR_MESSAGE = "This position is already attributed"
INTERNAL_ERROR_MESSAGE = "Internal error : "

class Error(Exception):
    pass

class NotFound(Error):
    pass

class AlreadyExisting(Error):
    pass

class BadToken(Error):
    pass

class WrongToken(Error):
    pass

class BadParticipation(Error):
    pass