import re
filename = "input.txt"
variable = "c"

def parse_coordinates_and_create_grid():
    global grid
    coordinates_list = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
    max_x = 0
    max_y = 0
    for line in lines:
        x1, y1, x2, y2 = [int(entry) for entry in re.sub('[^0-9]', ' ', line).split()]
        if(x1==x2 or y1==y2):
            coordinates_list.append([x1, y1, x2, y2])
        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)
    print('max x', max_x, 'max y', max_y)
    grid = [[0 for x in range(max_x+1)] for y in range(max_y+1)]
    
    return grid, coordinates_list

def sumar_en_coordenada(x,y):
    for index in range(len(grid)):
        if(index == y):
            row = grid[y]
            for r in range(len(row)):
                if(r == x):
                    grid[y][x] += 1

def count_numbers_of_twos_in_grid():
    count = 0
    for row in grid:
        for entry in row:
            if(entry >= 2):
                count += 1
    return count

def main():
    grid, coordinates = parse_coordinates_and_create_grid()

    for c in coordinates:
        x1, y1 , x2, y2 = c
        if x1 != x2:
            max_x = max(x1, x2)
            min_x = min(x1, x2)
            contador = min_x

            while(contador < max_x+1): 
                sumar_en_coordenada(contador,y2)
                contador += 1
        elif y1 != y2:
            max_y = max(y1, y2)
            min_y = min(y1, y2)
            contador = min_y
            while(contador < max_y+1):
                sumar_en_coordenada(x1,contador)
                contador += 1

    #for g in grid:
    #    print(g)
    
    print('count', count_numbers_of_twos_in_grid())

main()