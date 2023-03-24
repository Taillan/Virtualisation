from typing import List

class Participation():
    def __init__(self, playerName: str, answers: List[int], score: int=0, id: int=None):
        self.id = id
        self.playerName = playerName
        self.answers = answers
        self.score = score
    
    def toJSON(self):
        return {"playerName": self.playerName, "score": self.score}