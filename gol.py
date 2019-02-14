import random

def setup_game(size,max_alive):
    a_grid = get_empty_grid(size)
    fill_grid_random(a_grid,max_alive)

def get_empty_grid(size):
    new_grid = []
    for row in range(size):
        new_sublist = []
        for column in range(size):
            new_sublist.append('-')
        new_grid.append(new_sublist)
    return new_grid

def rand_alive():
    number = random.randint(1,2)
    if number == 1:
        return True
    else:
        return False

def fill_grid_random(a_grid, max_alive):
    size = len(a_grid)
    count = 0
    for r_i in range(size):
        for c_i in range(size):
            if rand_alive() == True:
                a_grid[r_i][c_i] = 'x'
                count = count + 1
            if count == max_alive:
                return a_grid
    return a_grid

grid = get_empty_grid(10)
grid = fill_grid_random(grid, 40)

def print_grid(a_grid):
    size = len(a_grid)
    for r_i in range(size):
        for c_i in range(size):
            print(a_grid[r_i][c_i] + " ", end = '')
        print('')
print_grid(grid)
def count_neighb(a_grid, row, col):
    size = len(a_grid)
    n_neighb = 0
    if a_grid:
        pass

def duplicates(list_a, list_b):
    size_a = len(list_a)
    size_b = len(list_b)
    duplicates = list()
    for i in range(size_a):
        for j in range(size_b):
            if list_a[i] == list_b[j] and list_a[i] not in duplicates:
                duplicates.append(list_a[i])
    return duplicates

def different_elements(list_a, list_b):
    size_a = len(list_a)
    size_b = len(list_b)
    different = list()
    for i in range(size_a):
        if list_a[i] not in duplicates(list_a, list_b) and list_a[i] not in different:
            different.append(list_a[i])
    for j in range(size_b):
        if list_b[j] not in duplicates(list_a, list_b) and list_b[j] not in different:
            different.append(list_b[j])
    return different
