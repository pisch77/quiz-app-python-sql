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
answers(a_id INTEGER PRIMARY KEY, q_number INTEGER, a_text TEXT NOT NULL,
is_correct INTEGER NOT NULL DEFAULT 0 CHECK (is_correct IN (0,1)),
FOREIGN KEY (q_number) REFERENCES questions(q_number))"""

cursor.execute(command2)

connection.commit()
cursor.close()
connection.close()