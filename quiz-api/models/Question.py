class Question():
    def __init__(self, title: str, text: str, position: int, image: str,  question_id: int=None):
        self.id = question_id
        self.title = title
        self.text = text
        self.position = position
        self.image = image	
        self.possibleAnswers = []
    
    def toJSON(self):
        answers = [ a.toJSON() for a in self.possibleAnswers ]
        return {"title": self.title, "text": self.text, "position": self.position, "image": self.image, "possibleAnswers": answers}