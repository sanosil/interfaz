import sqlite3

database = sqlite3.connect("program_database.db")
print("connection succsessfull")


a = 0

while a != 1:
    cmd = input("Introduzca comando sql\n")
    datos = database.execute(cmd)
    for dato in datos:
        print(dato)
    a = int(input("Si desea continuar escriba 0, de lo contrario 1\n"))
database.commit()
database.close()

print("Insertion successfull")
