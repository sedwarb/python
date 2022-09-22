from datetime import datetime

def leave():
    date = datetime.now()
    print("Hora Actual:", date.hour)
    if date.hour > 19:
        print("Hora de Salida")
    else:
        print("Te quedan", 19-date.hour, "horas de Trabajo")

