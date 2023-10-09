frase = input("Escribe una frase: ")
vocal = input("Escribe una vocal: ")

if len(vocal) == 1 and vocal in "aeiouAEIOU":
    frasem = frase.replace(vocal.lower(), vocal.upper())
    print("Frase con la vocal en mayúscula:", frasem)
else:
    print("La entrada de la vocal no es válida. Debe ser una sola vocal.")
