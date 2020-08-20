import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new2_list = []
new3_list = []
for n in a:
    new2_list.append(random.randint(0,10))
for n2 in b:
    new3_list.append(random.randint(0,10))
print("The 1st random list is: ", new2_list)
print("The 2nd random list is: ", new3_list)
#aca set(a) funciona de forma que solo utiliza los numeros unicos que hay en a por ejemplo si agrega un 1 y despues hay otro 1 no lo registrara
result = [i for i in set(new3_list )]
print(result)