#adivina el numero: programa que genere numero aleatorio y pida numero al usuario de manera repetida hasta que adivine.


import random 

x = random.randint(1, 10)

while True:

    Y = int(input("adivina el número:"))
    if Y == x:
        print("Felicidades, has acertado !")
        break

    else:
    
     print("has fallado ! intentalo de nuevo")
