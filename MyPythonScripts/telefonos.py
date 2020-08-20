#Interroga el estado del telfono Nuevo/usado
est = int(input("Bienvenido al asistente de telefonos, es el telefono nuevo o usado \n ingrese 1)Usado 2)Nuevo "))
if est == 1:
    est = ("Usado")
else:
    est = ("Nuevo")
#Interroga el precio original del telefono y lo asigna
print("El telefono que desea comprar es,", est)
pro = int(input("Ingrese el precio original del telefono"))
#Si es usado se le descuenta un 20% y si es nuevo se suma un 20%
if est == ("Usado"):
    dest = pro * 0.20
    pro = (pro) - (dest)
    print("El telefono es usado por lo tanto tiene un descuento de 20%, su preico es: $", int(pro))
else:
    au = pro * 0.20
    pro = (pro) + (au)
    print("El telefono es nuevo por lo tanto tiene un aumento de 25% su precio es: $", int(pro))
#Se le suma el iva al producto y el precio fijo de 20K
iva = pro * 0.19
ivaf = (pro) + (iva)
pro = ivaf + 20000
print("El telefono con iva y precio agregado (20K) suma un total de: $", int(pro))
#Oferta de los audifonos gamer (950$) si supera los 250K
if pro > 250000:
    gam = int(input("Tiene la opcion de agregar unos audifonos gamer por el precio de $950 \n 1)Si 2)No"))
    if gam == 1:
        pro = pro + 950
        print("El precio final de el telefono con audifonos es de: $", int(pro), "\nGracias por su compra")
    else:
        print("El precio final de el telefono sin los audifonos es de: $", int(pro), "\nGracias por su compra")
else:
    print("""El precio total no supera los $250.000 asi que no aplica para la oferta de los audifonos gamer. \n 
Gracias por su compra""")




