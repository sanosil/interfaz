import sqlite3

database = sqlite3.connect("program_database.db")
print("database conectada correctamente")

continuar = 1

while continuar == 1:
    comando = input("Introduzca comando sql: ")
    try:
        datos = database.execute(comando)
        for row in datos:
            print(row)
    except:
        print("comando no aceptado")

    continuar = int(input("Seguir escribiendo escriba 1, de lo contrario escriba 0: "))

database.commit()
database.close()
print("Database cerrada correctamente")
