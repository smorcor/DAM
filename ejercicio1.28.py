#Inicio
numero1 = int(input("Introduce un número entero: ")) #Escribe "Introduce un número entero: "
numero2 = int(input("Introduce otro número entero: ")) #Escribe "Introduce otro número entero: "

if numero1 < numero2 : #Si (numero1<numero2) entonces
    diferencia = numero2 - numero1 #diferencia = numero2 - numero1
    print(f"El número menor es el {numero1} y entre ellos existen {diferencia} números enteros") #Escribe "El número menor es el "+numero1+" y entre ellos existen "+diferencia+" números enteros"
elif numero1 > numero2 : #Sino (numero1 > numero2) entonces
    diferencia2 = numero1 - numero2 #diferencia2 = numero1 - numero2
    print(f"El número menor es el {numero2} y entre ellos existen {diferencia2} números enteros")#Escribe "El número menor es el "+numero2+" y entre ellos existen "+diferencia2+" números enteros"
else : #Sino 
    print("Los números no pueden ser iguales")#Escribe "Los números no pueden ser iguales"
#Fin