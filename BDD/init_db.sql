USE QuizzDB;

CREATE TABLE IF NOT EXISTS `Participation` (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        playerName TEXT NOT NULL,
        answers  TEXT NOT NULL,
        score INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `Question`(
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        position  INTEGER NOT NULL UNIQUE,
        title TEXT NOT NULL,
        `text`  TEXT NOT NULL,
        image TEXT
);

CREATE TABLE IF NOT EXISTS `PossibleAnswers`(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    `question_id` INTEGER NOT NULL UNIQUE,
    `text` TEXT NOT NULL,
    isCorrect INT NOT NULL,
    CONSTRAINT question_position
        FOREIGN KEY (question_id)
        REFERENCES Question(position)
);