
CREATE TABLE IF NOT EXISTS "PossibleAnswers"(
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "question_id" INT NOT NULL,
    "text" TEXT NOT NULL,
    "isCorrect" INT NOT NULL,
    FOREIGN KEY(question_id) REFERENCES Question(position)
);

CREATE TABLE IF NOT EXISTS "Question" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "title" TEXT NOT NULL,
        "text"  TEXT NOT NULL,
        "position"  INTEGER NOT NULL,
        "image" TEXT
);

CREATE TABLE IF NOT EXISTS "Participation" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "playerName" TEXT NOT NULL,
        "answers"  TEXT NOT NULL,
        "score" INT NOT NULL
);