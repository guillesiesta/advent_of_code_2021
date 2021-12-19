# abrir y leer archivo
f = open ('input.txt','r')
mensaje = f.read()
f.close()

# almacenar los números en una lista

list_numbers = mensaje.split('\n')

result = {}
lista_invertida = []

# recorro por columnas el input que me han dado y creo una nueva lista con los números
# de las columnas. Digamos que invierto y me queda: que tengo un diccionario de 
# numero de keys=columnas (o longitud de los numeros)
for x in range(len(list_numbers[0])):
    for i in list_numbers:
        lista_invertida.append(i[x]) 
        result[x] = lista_invertida
    lista_invertida=[]

gamma_rate = " "
epsilon_rate = " "
for r in result:
    gamma_rate += max(result[r],key=result[r].count)
    epsilon_rate += min(result[r],key=result[r].count)

print(gamma_rate)
print(epsilon_rate)
print(int(gamma_rate,2)*int(epsilon_rate,2))