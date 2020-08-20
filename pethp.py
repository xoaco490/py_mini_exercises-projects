#ALGORITMO DE COMPORTAMIENTO DE CLASE
def classin(classe):
    global brut
    if classe == "Picaro":
        msa = int(input("Acciones traviesas:"))
        msa = msa*3
        brut += msa
        sts = int(input("Robo algo:"))
        sts = sts*4
        brut += sts
        ssy = int(input("Te soprendio:"))
        ssy = ssy*5
        brut += ssy
        return brut
    elif classe == "Clerigo":
        brut
        soa = int(input("Accion calmante:"))
        soa = soa*3
        brut += soa
        gth = int(input("Interactuo contigo gentilmente:"))
        gth = gth*4
        brut += gth
        ahn = int(input("Aparecio en tiempos de necesidad:"))
        ahn = ahn*5
        brut += ahn
        return brut
    elif classe == "Paladin":
        brut
        lya = int(input("Accion leal:"))
        lya = lya*3
        brut += lya
        dgd = int(input("Acciones buenas:"))
        dgd = dgd*4
        brut += dgd
        bsd = int(input("Trajo algo que no pediste:"))
        bsd = bsd*5
        brut += bsd
        return brut
    elif classe == "Arquero":
        brut
        cla = int(input("Accion astuta:"))
        cla = cla*3
        brut += cla
        gzc = int(input("Miro contemplando:"))
        gzc = gzc*4
        brut += gzc
        iyc = int(input("Te ignoro completamente"))
        iyc = iyc*5
        brut += iyc
        return brut
    elif classe == "Barbaro":
        brut
        ipa = int(input("Accion descortes"))
        ipa = ipa*3
        brut += ipa
        cof = int(input("Hazaña valiente:"))
        cof = cof*4
        brut += cof
        ngs = int(input("No dio importancia a cosa inteligente:"))
        ngs = ngs*5
        brut += ngs
        return brut
#Algoritmo baseHP
def basesb(tippo,classe):
    global basehp
    if classe == "Picaro":
        list_bhps = { "Perro" : 35, "Gato" : 40, "Pez": 20, "Reptil" : 30,"Pajaro": 40, "Equino" : 45, "Mamifero pequeño" : 10, "Insecto" : 1, "Anfibio" : 40, "Animal de granja": 50, "Exotico" : 35, "Planta" : 30}
        for i in range(12):
            if tippo in list_bhps:
                basehp += list_bhps[tippo]
                return basehp
    elif classe == "Clerigo":
        list_bhps = { "Perro" : 76, "Gato" : 75, "Pez": 73, "Reptil" : 78,"Pajaro": 79, "Equino" : 86, "Mamifero pequeño" : 51, "Insecto" : 40, "Anfibio" : 77, "Animal de granja": 88, "Exotico" : 83, "Planta" : 68}
        for i in range(12):
            if tippo in list_bhps:
                basehp += list_bhps[tippo]
                return basehp
    elif classe == "Paladin":
        list_bhps = { "Perro" : 116, "Gato" : 110, "Pez": 126, "Reptil" : 126,"Pajaro": 116, "Equino" : 126, "Mamifero pequeño" : 91, "Insecto" : 77, "Anfibio" : 114, "Animal de granja": 126, "Exotico" : 130, "Planta" : 106}
        for i in range(12):
            if tippo in list_bhps:
                basehp += list_bhps[tippo]
                return basehp
    elif classe == "Arquero":
        list_bhps = { "Perro" : 156, "Gato" : 144, "Pez": 178, "Reptil" : 173,"Pajaro": 154, "Equino" : 166, "Mamifero pequeño" : 131, "Insecto" : 115, "Anfibio" : 150, "Animal de granja": 163, "Exotico" : 177, "Planta" : 143}
        for i in range(12):
            if tippo in list_bhps:
                basehp += list_bhps[tippo]
                return basehp
    elif classe == "Barbaro":
        list_bhps = { "Perro" : 196, "Gato" : 179, "Pez": 231, "Reptil" : 221,"Pajaro": 191, "Equino" : 206, "Mamifero pequeño" : 171, "Insecto" : 152, "Anfibio" : 187, "Animal de granja": 201, "Exotico" : 224, "Planta" : 181}
        for i in range(12):
            if tippo in list_bhps:
                basehp += list_bhps[tippo]
                return basehp
#porcentaje bruto de acciones
brut = 0
name = str(input("Bienvenido al calculador de HP de su mascota. \nPorfavor ingrese el nombre de su mascota: "))
n = int(input("\n1: Perro\n2: Gato\n3: Pez\n4: Reptil\n5: Pajaro\n6: Equino\n7: Mamifero pequeño\n8: Insecto\n9: Anfibio\n10: Animal de granja\n11: Exotico\n12: Planta\nQue el tipo de mascota es "+str(name)+"?"))
while(n < 1 or n > 12):
    n = int(input("Tipo de mascota incorrecto ingrese nuevamente: "))  
#Tipo de mascota
#Esta parte de aca abajo es re importante para evitar llenar el codigo con IF y ELSE IF y asi conseguir un resultado mas rapido
options = {1 : "Perro", 2: "Gato", 3: "Pez", 4 : "Reptil",5 : "Pajaro", 6 : "Equino", 7 : "Mamifero pequeño", 8 : "Insecto", 9 : "Anfibio", 10: "Animal de granja", 11 : "Exotico", 12 : "Planta"}
for i in range(12):
    if n in options:
        tippo = options[n]
print(tippo)
#Clase de mascota
n1 = int(input(" 1:PICARO:\n-Libre\n-Dañino\n-Agil\n 2:CLERIGO:\n-Amable\n-Reservado\n-Sanador\n 3:PALADIN:\n-Leal\n-Ingenioso\n-Intenta de demasiado\n 4:ARQUERO:\n-Autosuficiente\n-Distanciado\n-Estan en su mundo\n 5:BARBARO:\n-Grosero\n-Descarado\n-Valientes por una causa\nIngrese el numero de la clase de su mascota segun su comportamiento: "))
while(n1 < 1 or n1 > 5):
    n1 = int(input("Clase de mascota incorrecto ingrese nuevamente: "))

options1 = {1 : "Picaro", 2: "Clerigo", 3: "Paladin", 4 : "Arquero",5 : "Barbaro"}
for c in range(5):
    if n1 in options1:
        classe = options1[n1]
print(classe)
#HS de mascota
hs = int(input("¿Cuantas horas se observo a la mascota?:"))
#Si se quiere obtener la formula exacta para calcular estos datos esta en: https://www.youtube.com/watch?v=9Jcxc-ddWKI 
#COMPORTAMIENTOS GENERALES:
#Alimentacion
print("Responda las siguientes preguntas por veces.dia en numeros enteros")
enf = int(input("Comio comida normal:"))
enf = enf*1
brut += enf
hun = int(input("Cazo:"))
hun = hun*2
brut += hun
scv = int(input("Busco comida en otras partes:"))
scv = scv*2
brut += scv
#Vocalizacion
sng = int(input("Canto:"))
sng = sng*1
brut += sng
alc = int(input("Ruidos de alarma:"))
alc = alc*1
brut += alc
fnc = int(input("Ruidos graciosos:"))
fnc = fnc*2
brut += fnc
#Aseo
prg = int(input("Se acicalo:"))
prg = prg*1
brut += prg
bth = int(input("Se baño:"))
bth = bth*1
brut += bth
scg = int(input("Practico acicalado social(https://es.wikipedia.org/wiki/Acicalado_social):"))
scg = scg*2
brut += scg
#algoritmo tabla clase
classin(classe)
#Modificadores
list_mods = { "Perro" : 2.4, "Gato" : 2 , "Pez": 3.1, "Reptil" : 2.8 ,"Pajaro": 2.3, "Equino" : 2.4, "Mamifero pequeño" : 2.4, "Insecto" : 2.3, "Anfibio" : 2.2, "Animal de granja": 2.2, "Exotico" : 2.8, "Planta" : 2.2}
for i in range(12):
    if tippo in list_mods:
        mod = list_mods[tippo]
basehp = 0
#algoritmo hp base por tipo/clase
basesb(tippo,classe)
lvl = brut/hs
Hit_points = basehp+(lvl*mod)
print(str(name)+" es un "+str(tippo)+" "+str(classe)+" de nivel "+str(lvl)+" con "+str(Hit_points)+" Hit poins")