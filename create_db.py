import sqlite3

# definiera länken och pekaren

connection = sqlite3.connect('quizdata.db')
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

# skapa frågetabell med frågenummer som PK och frågetext

command1 = """CREATE TABLE IF NOT EXISTS
questions(q_number INTEGER PRIMARY KEY, q_text TEXT NOT NULL)"""

cursor.execute(command1)

# skapa svarstabell med svars id, frågenummer (främmande nyckel), svarstext och rättning

command2 = """CREATE TABLE IF NOT EXISTS
answers(a_id INTEGER PRIMARY KEY, q_number INTEGER NOT NULL, a_text TEXT NOT NULL,
is_correct INTEGER NOT NULL DEFAULT 0 CHECK (is_correct IN (0,1)),
FOREIGN KEY (q_number) REFERENCES questions(q_number))"""

cursor.execute(command2)

questions_list = [
    ("När släpptes Star Wars: Revenge of the Sith?",),
    ("Vad blir 7 * 7?",),
    ("Vilket är världens största djur?",)
]

answers_list = [
    (1, "a) 2000", 0,),
    (1, "b) 1987", 0,),
    (1, "c) 2005", 1,),
    (1, "d) 2015", 0,),
    (2, "a) 49", 0,),
    (2, "b) 77", 1,),
    (2, "c) 63", 0,),
    (2, "d) 41", 0,),
    (3, "a) Myra", 0,),
    (3, "b) Blåval", 1,),
    (3, "c) Elefant", 0,),
    (3, "d) Giraff", 0,)
]

cursor.executemany("INSERT INTO questions(q_text) VALUES (?)", questions_list)
cursor.executemany("INSERT INTO answers(q_number, a_text, is_correct) VALUES (?, ?, ?)", answers_list)

connection.commit()
cursor.close()
connection.close()