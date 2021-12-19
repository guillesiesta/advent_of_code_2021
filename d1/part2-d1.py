# abrir y leer archivo
f = open ('input.txt','r')
mensaje = f.read()
f.close()

# almacenar los números en una lista

list_numbers = mensaje.split('\n')
list_numbers = list(map(int,list_numbers))
#print(list_numbers)

increased = 0
for x in range(len(list_numbers)-3):
    previous = list_numbers[x] + list_numbers[x+1] + list_numbers[x+2]
    posterior = list_numbers[x+1] + list_numbers[x+2] + list_numbers[x+3]
    if(previous < posterior):
        increased = increased + 1

print(increased)