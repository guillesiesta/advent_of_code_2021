# abrir y leer archivo
f = open ('input.txt','r')
mensaje = f.read()
f.close()

# almacenar los números en una lista

list_numbers = mensaje.split('\n')

result = {}
lista_invertida = []

for x in range(len(list_numbers[0])):
    for i in list_numbers:
        lista_invertida.append(i[x]) 
        result[x] = lista_invertida
    lista_invertida=[]

gamma_rate = " "
epsilon_rate = " "
for r in result:
    #print(result[r].count('0'))
    #print(result[r].count('1'))
    if(result[r].count('0')>result[r].count('1')):
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'

print(gamma_rate)
print(epsilon_rate)

print(int(gamma_rate,2)*int(epsilon_rate,2))