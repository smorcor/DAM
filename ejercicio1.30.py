#Inicio
#Escribe "Introduce un número de inicio: "
#Escribe "Introduce un incremento: "
#Escribe "Introduce un total de la serie: "

#Si (incremento y total > 0) entonces
#   
#Fin

ini = int(input("Introduce un número de inicio: "))
inc = int(input("Introduce un incremento: "))
total = int(input("Introduce un total de la serie: "))

while (inc <= 0) or (total <= 0) :
    inc = input("Introduce un incremento mayor que 0: ")
    total = input("Introduce un total de la serie que sea mayor que 0: ")
serie= 0
serie = f"Serie => {ini}"
cont = 1
while cont <= total :
    ini = ini + inc
    cont = cont + 1
    if cont < (total - 1) :
        serie = str(serie + ini + "..")
    else :
        if cont == total :
            serie = serie + ini
        else : 
            serie = serie + ini + "-"




