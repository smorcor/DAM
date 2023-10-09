correo = input("Escribe tu correo: ")
c = correo.split("@")

if len(c) == 2:
    usuario, dominio = c 
    nuevo = usuario + "@ceu.es"
    print(nuevo)
else:
        print("ERROR")



