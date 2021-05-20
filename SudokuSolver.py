import numpy as numpy


# Lisää tähän sudoku, jonka haluat ratkaista
grid = [
    [1, 0, 0, 0, 2, 0, 3, 0, 5],
    [0, 0, 3, 0, 0, 0, 9, 6, 0],
    [5, 2, 0, 3, 9, 0, 0, 0, 0],
    [0, 8, 1, 5, 0, 0, 7, 0, 0],
    [0, 0, 0, 1, 8, 0, 6, 9, 0],
    [0, 3, 4, 0, 0, 0, 0, 5, 0],
    [0, 7, 0, 0, 0, 8, 0, 0, 9],
    [8, 0, 2, 0, 0, 3, 0, 0, 1],
    [4, 0, 0, 0, 0, 5, 0, 0, 6],
]


def possible(y, x, n):  # Testaa, voiko tiettyyn kohtaan tulla tiettyä numeroa
    global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0+i][x0+j] == n:
                return False
    return True


ratkaisuja = 0


def solve():  # Ratkaisee possible -funktion avulla koko sudokun kaikki kohdat backtracking -menetelmällä
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    # Lasketaan kuinka monta ratkaisua sudokulle on
    global ratkaisuja
    ratkaisuja += 1
    print(numpy.matrix(grid))


solve()

# Jos ratkaisuja ei ole
if ratkaisuja == 0:
    print("Sudokua ei voi ratkaista.")
# Jos ratkaisuja on monta
if ratkaisuja > 1:
    print("Sudokulle on", ratkaisuja,
          "ratkaisua, joten se ei ole kelvollinen.")
# Jos ratkaisuja on yksi
elif ratkaisuja == 1:
    print("Sudokulle on vain yksi ratkaisu. Hyvä!")
