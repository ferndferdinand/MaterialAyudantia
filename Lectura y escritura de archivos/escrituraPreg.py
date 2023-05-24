
import csv

#Primero intentar sin u
with open("preguntasU.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    for i in range(1,31):
        writer.writerow(["u",f"¿Pregunta número {i} de las 30 preguntas?", "Opción 1 (correcta)", "Opción 2 (incorrecta)", "Opción 3 (incorrecta)"])
    

with open("preguntasM.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    for i in range(1,31):
        writer.writerow(["m",f"Pregunta número {i} de formato 2", "Opción 1 (correcta)", "Opción 2 (correcta)", "Opción 3 (incorrecta)","Opción 4 (incorrecta)"])
    
