def get_empty_grid(size):
    grid = list()
    row = list()
    for j in  range(0, size):
        row.append("-")
        for i in range(0, size):
            grid.append(row)
    return grid
print(get_empty_grid(5))

def get_empty_grid2(rows, columns):
    grid = list()
    row = list()
    for j in  range(0, columns):
        row.append("-")
    for i in range(0, rows):
        grid.append(row)
    return grid
print(get_empty_grid2(4,5))

def fill_grid_random(grid, n_alive):
    grid = my_flatten

def setup_game(size, max_alive):
    empty_grid = get_empty_grid(size)
    fill_grid_random(empty_grid, max_alive)

def my_flatten(list_of_lists):
    new_list = []
    for n in list_of_lists:
        if isinstance(n, list):
            for i in n:
                new_list.append(i)
        else:
            new_list.append(n)
    return new_list 

