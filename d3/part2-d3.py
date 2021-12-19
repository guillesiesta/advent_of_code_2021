
def read_file():
    # abrir y leer archivo
    f = open ('input.txt','r')
    input_texto = f.read()
    f.close()
    list_numbers = input_texto.split('\n')

    matriz_inicial = []

    for linea in list_numbers:
        matriz_inicial.append([int(char) for char in linea])
    
    return matriz_inicial
    
def filterListByValueInIndex(list, index, value):
    return [item for item in list if item[index] == value]

def calculate_most_common(list):
    n_of_cero = list.count(0)
    n_of_uno = list.count(1)
    return 1 if n_of_uno >= n_of_cero else 0

def calculate_less_common(list):
    n_of_cero = list.count(0)
    n_of_uno = list.count(1)
    return 0 if n_of_cero <= n_of_uno else 1

def get_column(matriz, index):
    result_list = []
    for m_fila in matriz:
        result_list.append(m_fila[index])
    return result_list

def get_filter_list_by_most_common_value(matriz,i):
    if(len(matriz)==1):
        return matriz[0]
    lista_columna = get_column(matriz, i)
    most_common = calculate_most_common(lista_columna)
    filter_list = filterListByValueInIndex(matriz, i, most_common)
    return get_filter_list_by_most_common_value(filter_list, i+1)

def get_filter_list_by_less_common_value(matriz,i):
    if(len(matriz)==1):
        return matriz[0]
    lista_columna = get_column(matriz, i)
    most_common = calculate_less_common(lista_columna)
    filter_list = filterListByValueInIndex(matriz, i, most_common)
    return get_filter_list_by_less_common_value(filter_list, i+1)

def decimal_value_of_list(lista):
    variable = ''.join(map(str,lista))
    return int(variable,2)

def main():

    matriz_inicial = read_file()
    oxygen_generator = get_filter_list_by_most_common_value(matriz_inicial,0)
    co2_generator = get_filter_list_by_less_common_value(matriz_inicial,0)

    print(oxygen_generator)
    print(co2_generator)

    a = decimal_value_of_list(oxygen_generator)
    b = decimal_value_of_list(co2_generator)

    print(a*b)

main()