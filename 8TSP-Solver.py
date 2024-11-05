# Author: Kunga
# Created: 09/10/2024

from copy import deepcopy

N = 2  # Tiles / Side

class location:
    def __init__(self, i, j):
        self.i = int(i)
        self.j = int(j)
    
    def __str__(self):
        return f"{self.i}, {self.j}"

class iter_DFS:
    def __init__(self, tiles, loc, prev_tiles):
        self.tiles = tiles
        self.location = loc
        self.previous_tiles = prev_tiles

def printTile(tiles):
    """Function to print tiles"""
    def printLine():
        print("+", end="")
        for i in range(N):
            print("---+", end="")
        print("")
    
    printLine()
    for i in range(N):
        print("|", end="")
        for j in range(N):
            print(" " + tiles[i][j] + " |", end="")    
        print("")
        printLine()

def tiles_not_valid(tiles):
    # Check if the array has exactly 3 rows
    if len(tiles) != N:
        return 1    # Dimensions not correct
    
    # Check if each row has exactly 3 columns
    for row in tiles:
        if len(row) != N:
            return 1    # Dimensions not correct
    
    # Flatten the array to a single list
    flattened = [item for sublist in tiles for item in sublist]
    
    validation = [str(i) for i in range(1,N*N)]
    validation.append("X")

    # Check if all numbers from 1 to 9 are present exactly once
    for i in validation:
        if flattened.count(i) != 1:
            return 2
    
    return 0

def validation_unit_testing():
    print("tiles_not_valid Test")
    
    tiles = [["1","2","3"],["4","5","6"],["X","7","8"]]
    print(tiles_not_valid(tiles))
    
    tiles = [[1,2,3],[4,5,6]]
    print(tiles_not_valid(tiles))

    tiles = [[1,2],[4,5],["X",7]]
    print(tiles_not_valid(tiles))

    tiles = [["1","2","3"],["4","5","1"],["X","7","8"]]
    print(tiles_not_valid(tiles))

def check_X(tiles):
    for y in range(0, N):
        for x in range(0, N):
            if tiles[y][x] == "X":
                return location(y, x)                
    return None

def check_X_unit_testing():
    print("chech_X Test")
    tiles = [["1","2","X"],["4","5","6"],["3","7","8"]]
    printTile(tiles)
    loc = check_X(tiles)
    print(loc)

def possible_moves(tiles, loc):
    moves = []

    if (loc.i > 0):
        new_loc = location(loc.i-1, loc.j)
        new_tiles = deepcopy(tiles)
        new_tiles[loc.i][loc.j], new_tiles[new_loc.i][new_loc.j] = new_tiles[new_loc.i][new_loc.j], new_tiles[loc.i][loc.j]
        moves.append([new_tiles, new_loc])
    
    if (loc.j > 0):
        new_loc = location(loc.i, loc.j-1)
        new_tiles = deepcopy(tiles)
        new_tiles[loc.i][loc.j], new_tiles[new_loc.i][new_loc.j] = new_tiles[new_loc.i][new_loc.j], new_tiles[loc.i][loc.j]
        moves.append([new_tiles, new_loc])

    if (loc.i < N-1):
        new_loc = location(loc.i+1, loc.j)
        new_tiles = deepcopy(tiles)
        new_tiles[loc.i][loc.j], new_tiles[new_loc.i][new_loc.j] = new_tiles[new_loc.i][new_loc.j], new_tiles[loc.i][loc.j]
        moves.append([new_tiles, new_loc])
    
    if (loc.j < N-1):
        new_loc = location(loc.i, loc.j+1)
        new_tiles = deepcopy(tiles)
        new_tiles[loc.i][loc.j], new_tiles[new_loc.i][new_loc.j] = new_tiles[new_loc.i][new_loc.j], new_tiles[loc.i][loc.j]
        moves.append([new_tiles, new_loc])

    for i in range(len(moves)):
        printTile(moves[i][0])
        # print(moves[i][1])

    return moves

def heuristic(target, current):
    h = 0

    for i in range(N):
        for j in range(N):
            if current[i][j] != target[i][j]:
                h += 1

    return h

def heuristic_unit_testing():
    print("heuristic Test")
    tilesA = [["1","2","X"],["4","5","6"],["3","7","8"]]
    printTile(tilesA)   

    tilesB = [["1","5","7"],["4","2","8"],["3","X","6"]]
    printTile(tilesB)

    print(heuristic(tilesA, tilesB))

def tile_equal(A, B):
    for i in range(N):
        for j in range(N):
            if A[i][j] != B[i][j]:
                return False
            
    return True

def equal_unit_testing():
    print("heuristic Test")

    tilesA = [["1","2","X"],["4","5","6"],["3","7","8"]]
    printTile(tilesA)
    tilesB = [["1","5","7"],["4","2","8"],["3","X","6"]]
    printTile(tilesB)

    print(tile_equal(tilesA, tilesB))

    printTile(tilesA)
    tilesB = [["1","2","X"],["4","5","6"],["3","7","8"]]
    printTile(tilesB)

    print(tile_equal(tilesA, tilesB))

def trace_back():
    print("Trace back moves")

def DFS_solver(target, start):
    closed_list = []
    open_list = []

    open_list.append([start, check_X(start)])

    while not open_list:
        current_tile = open_list[0][0]

        if tile_equal(current_tile, target):
            trace_back()
        else:
            current_loc = open_list[0][1]
            open_list = open_list[1:]

            for i in possible_moves(current_tile, current_loc):
                pass

        
    
    



def main():
    # validation_unit_testing()
    # check_X_unit_testing()
    # heuristic_unit_testing()
    # equal_unit_testing()
    
    ## 3x3
    # tilesA = [["1","2","X"],["4","5","6"],["3","7","8"]]
    # printTile(tilesA)

    # tilesB = [["1","5","7"],["4","2","8"],["3","X","6"]]
    # printTile(tilesB)

    # 2x2
    tilesA = [["1","X"],["3","2"]]
    printTile(tilesA)

    # tilesB = [["1","3"],["X","2"]]
    # printTile(tilesB)

    # print(type(possible_moves(tilesA, check_X(tilesA))[0][1]))
    


if __name__ == '__main__':
    main()

