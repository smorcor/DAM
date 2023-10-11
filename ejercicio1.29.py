"""
Inicio
    Escribe "Introduce tu nombre: "
    Lee nombre
    Escribe "Introduce tu edad: "
    Lee edad

    Si (nombre == "") hacer 
        Lee "Desconocido"
        nombre = "Desconocido"

    Mientras (edad >= 125) y (edad <= 0) hacer 
        Escribe "Introduce tu edad: "
        lee edad
diferencia = 125 - edad
Lee "Te llamas "+nombre+" y tienes "+edad+" años, te quedan aún "+diferencia+" años por cumplir")

Fin
"""
nombre = input("Introduce tu nombre: ") 
edad = int(input("Introduce tu edad: ")) 
if nombre == "" :
    nombre = "Desconocido"

while edad >= 125 and  edad <= 0 : 
    edad = input("Introduce tu edad: ") 
    edad = int(input("Introduce la edad: "))
diferencia = 125 - edad
print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {diferencia} años por cumplir")