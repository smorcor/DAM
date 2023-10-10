
#Inicio
#Escribe "Introduce tu nombre: "
#Escribe "Introduce tu edad: "

#Mientras (nombre esta vacio) hacer 
#   Lee "Desconocido"
#   nombre = 0

#Mientras (edad <= 125) y  (edad >= 0) hacer 
#   Escribe "Introduce tu edad: "


#Si (125 - edad >= 0) entonces
#años = 125 - edad

#Fin
nombre = input("Introduce tu nombre: ") 
edad = input("Introduce tu edad: ") 

while (edad <= 125) and  (edad >= 0) : 
    edad = input("Introduce tu edad: ") 


if 125 - edad >= 0 and nombre : 
    años = 125 - edad 
    print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {años} años por cumplir") 
else :
    print("Desconocido")