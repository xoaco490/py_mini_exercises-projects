# Esto es un juego de adivina el numero.
import random
print("Hello, what is your name?")
nombre = input()
print ("Good, "+ nombre + ", im thinking of a number between 1 and 20")
print ("You have 7 tries")
numeroSecreto = random.randint(1, 20)
try:
    for adivinanzasTomadas in range (1, 7):
        print ("Guess it!")
        adivinanza = int(input ())
        if adivinanza < numeroSecreto:
            print ("Too low")
        elif adivinanza > numeroSecreto:
            print ("Too high")
        else:
            break # Esta condicion es cuando se acierta el numero
    if adivinanza == numeroSecreto:
        print ("Good job, " + nombre + ", you guessed my number in " + str(adivinanzasTomadas) + " tries")
    else:
        print ("No, el the number i was thinking of was: " + str(numeroSecreto))
except ValueError:
    print("That's not a number!")

    
    
        

    
  
