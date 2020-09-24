# python3
import random

#Solucion mas lenta (multiplicar cada num)
def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

#Solucion mas rapida(solamente buscar los enteros mas grandes)
def max_pairwise_product_fast(numbers):
    n = len(numbers)
    #TODO porque carajos no funciona con == 0 REVISAR!!!!
    max_product1 = -1
    for i in range(n):
        if((max_product1 == -1) or (numbers[i]>numbers[max_product1])):
            max_product1 = i

    max_product2 = -1
    for j in range(n):
        if((j != max_product1) and ((max_product2==-1) or (numbers[j] > numbers[max_product2]))):
            max_product2 = j
 
    
    #print(str(max_product1)+" "+str(max_product2))

    return (numbers[max_product1]*numbers[max_product2])


if __name__ == '__main__':
    #TODO Stress test:
    """ while(True):
        n = random.randint(2,5)
        print(n)
        a = []
        for i in range(n):
            a.append(random.randint(0,10))
        for j in range(n):
            print(a[j])
        print("\n")

        res1 = max_pairwise_product(a)
        res2 = max_pairwise_product_fast(a)

        if(res1 != res2):
            print("Wrong answer max pair: "+str(res1)+ " max pair f: "+ str(res2))
            break;
        else:
            print("OK\n") """


    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
