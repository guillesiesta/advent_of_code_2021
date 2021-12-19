# abrir y leer archivo
f = open ('input.txt','r')
mensaje = f.read()
f.close()

# almacenar los números en una lista

list_numbers = mensaje.split('\n')

result = {}

aim = 0
depth = 0
horizontal = 0
for line in list_numbers:
    key, value = line.split(" ")
    if key=="forward":
        depth += aim * int(value)
        horizontal += int(value) 
    elif key=="up":
        aim -= int(value)
    elif key=="down":
        aim += int(value)

print(depth*horizontal)