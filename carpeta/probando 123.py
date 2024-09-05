import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
cantidad = int(input("Insertar longitud"))
password = ""
for i in range (cantidad):
    password = password + random.choice(caracteres)
print("su contraseña asignada es:", password)