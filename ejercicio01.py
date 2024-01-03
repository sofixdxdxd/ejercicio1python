import random 

x = random.randint(1, 10)

while True:

    Y = int(input("adivina el número:"))
    if Y == x:
        print("Felicidades, has acertado !")
        break

    else:
    
     print("has fallado ! intentalo de nuevo")
