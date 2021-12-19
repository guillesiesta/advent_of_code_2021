# abrir y leer archivo
f = open ('input.txt','r')
mensaje = f.read()
f.close()

# almacenar los números en una lista

list_numbers = mensaje.split('\n')

result = {}

for line in list_numbers:
    key, value = line.split(" ")
    if key in result:
        result[key] += int(value)
    else:
        result[key] = int(value)

# print(result)
print(result["forward"] * (result["down"] - result["up"]))