"""
Inicio
    Escribe "Introduce un número de inicio: "
    lee ini
    Escribe "Introduce un incremento: "
    lee inc
    Escribe "Introduce un total de la serie: "
    lee total
    mientras (inc <= 0) o (total <= 0) hacer
        lee inc
        lee total
    serie = 0
    serie = "Serie => " + ini + "-"
    cont = 1
    mientras cont < total hacer
        ini = ini + inc
        cont = cont + 1
        si cont < (total - 1 ) entonces
            serie = serie + ini + ".."
        sino 
            si cont = total -1 entonces 
                serie = serie + ini
            sino
                serie = serie + "-" + ini
    lee serie
Fin
"""

ini = int(input("Introduce un número de inicio: "))
inc = int(input("Introduce un incremento: "))
total = int(input("Introduce un total de la serie: "))

while (inc <= 0) or (total <= 0) :
    inc = int(input("Introduce un incremento mayor que 0: "))
    total = int(input("Introduce un total de la serie que sea mayor que 0: "))
serie = 0
serie = "Serie => " + str(ini) + "-"
cont = 1
while cont < total :
    ini += inc
    cont += 1

    if cont < (total - 1 ) :
        serie = serie + str(ini) + ".."
    else :
        if cont == total -1:
            serie = serie + str(ini)
        else : 
            serie = serie + "-" + str(ini)

print(serie)


