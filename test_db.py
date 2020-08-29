import sqlite3

database = sqlite3.connect("program_database.db")
print("connection succsessfull")

database.execute("INSERT INTO spanish_phrases(ID, PHRASE) VALUES (1, 'BIENVENIDO');")
database.commit()
database.close()

print("Insertion successfull")

