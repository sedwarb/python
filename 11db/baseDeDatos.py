#sqlite
#esta base de datos solo funciona en un fichero en mi disco duro
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

insertar = False
individual = False
mostrar = False
mostrarUno = True

conn = sqlite3.connect('./miFichero.db')

cursor = conn.cursor()

if mostrarUno:
    rows = cursor.execute("SELECT * FROM alumnos WHERE nombre='elo'")
    for row in rows:
        print(row)

if mostrar:
    rows = cursor.execute("SELECT * FROM alumnos")
    for row in rows:
        print(row)

if individual:
    cursor.execute("insert into alumnos(id,nombre,apellido) values (1,'lucia','amapola')")
    conn.commit()
    
if insertar:
    for alumno in alumnos:
        cursor.execute(f"insert into alumnos(id,nombre,apellido) values ('{alumno['id']}','{alumno['nombre']}','{alumno['apellido']}')")    
    conn.commit()

cursor.close()
conn.close()