f = open("probando 123.txt", "w", encoding= "utf=8") 
text = "cambio fe texto"
print(text)
f.write(text)
with open ("texto.txt", "r", encoding= "utf=8") as f:
    print(f.read())

i = open("images/reirei.png", "rb")