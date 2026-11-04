import random
caracters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
loncon = int(input("longitud de la contraseña:"))
confin = ""
for i in range(loncon):
    pasfin = (random.choice(caracters))
    confin += pasfin
print(confin)
