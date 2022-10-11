import sqlite3

alumnos = [
    {"id":9,"nombre":'marcos',"apellido":'pantoja'},
    {"id":2,"nombre":'pedro',"apellido":'castillo'},
    {"id":3,"nombre":'rolando',"apellido":'rosales'},
    {"id":4,"nombre":'felipe',"apellido":'malsano'},
    {"id":5,"nombre":'luis',"apellido":'andreo'},
    {"id":6,"nombre":'pepe',"apellido":'pelotas'},
    {"id":7,"nombre":'nanda',"apellido":'milojas'},
    {"id":8,"nombre":'elo',"apellido":'bocagrande'}
]

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

rows = cursor.execute("SELECT * FROM alumnos")

if rows:
    for row in rows:
        print(row)
else:
    print("Sin Datos")

cursor.close()
conn.close()