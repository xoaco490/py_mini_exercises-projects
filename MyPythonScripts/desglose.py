#El siguiente programa mostrara los desgloses de un nuemero en moneda argentina

#Variables para cada desglose
Peso1 = 0
Mitre2 = 0
Martin5 = 0
Belgrano10 = 0
Rosas20 = 0
Sarmiento50 = 0
Roca100 = 0
Yaguarete500 = 0
Hornero1000 = 0
tot = 0
#Establecer un input del usuario preguntando por desglose
des = int(input("Bienvenido, ingrese el numero para el deslgose"))
while des >= 0:
    if des >= 1000:
        Hornero1000 = Hornero1000 + 1
        des = des - 1000
    elif des >= 500:
        Yaguarete500 = Yaguarete500 + 1
        des = des - 500
    elif des >= 100:
        Roca100 = Roca100 + 1
        des = des - 100
    elif des >= 50:
        Sarmiento50 = Sarmiento50 + 1
        des = des - 50
    elif des >= 20:
        Rosas20 = Rosas20 + 1
        des = des - 20
    elif des >= 10:
        Belgrano10 = Belgrano10 + 1
        des = des - 10
    elif des >= 5:
        Martin5 = Martin5 + 1
        des = des - 5
    elif des >= 2:
        Mitre2 = Mitre2 + 1
        des = des - 2
    elif des >= 1:
        Peso1 = Peso1 + 1
        des = des - 1
    else:
        break
#Uso del while y if para mostrar todos los contadores de cada billete desglosado
print("Los billetes necesarios para el desglose son: ")
while des == 0:
    if Hornero1000 >= 1:
        print(Hornero1000, "Billetes de $1000")
        Hornero1000 = 0
    elif Yaguarete500 >= 1:
        print(Yaguarete500, "Billetes de $500")
        Yaguarete500 = 0
    elif Roca100 >= 1:
        print(Roca100, "Billetes de $100")
        Roca100 = 0
    elif Sarmiento50 >= 1:
        print(Sarmiento50, "Billetes de $50")
        Sarmiento50 = 0
    elif Rosas20 >= 1:
        print(Rosas20, "Billetes de $20")
        Rosas20 = 0
    elif Belgrano10 >= 1:
        print(Belgrano10, "Billetes de $10")
        Belgrano10 = 0
    elif Martin5 >= 1:
        print(Martin5, "Billetes de $5")
        Martin5 = 0
    elif Mitre2 >= 1:
        print(Mitre2, "Billetes de $2")
        Mitre2 = 0
    elif Peso1 >= 1:
        print(Peso1, "Monedas de $1")
        Peso1 = 0
    else:
        break