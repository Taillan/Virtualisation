class PossibleAnswers():
    def __init__(self, text: str, isCorrect: bool, id: int=None):
        self.id = id
        self.text = text
        self.isCorrect = isCorrect
    
    def toJSON(self):
        return {"text": self.text, "isCorrect": self.isCorrect}
