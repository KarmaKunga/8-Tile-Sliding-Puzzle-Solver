# Author: Kunga
# Created: 09/10/2024

from copy import deepcopy

N = 3  # Tiles / Side

class location:
    def __init__(self, i, j):
        self.i = int(i)
        self.j = int(j)
    
    def __str__(self):
        return f"{self.i}, {self.j}"

class BFS_node:
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

    # for i in range(len(moves)):
    #     printTile(moves[i][0])
    #     print(moves[i][1])

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

def BFS_solver(target, start):
    closed_list = []
    open_list = []

    def retrace(last_node):

        print("Trace back moves")
        prev_tile = last_node.previous_tiles

        moves = [last_node.tiles]
        
        while (prev_tile != None):

            for i in closed_list:
                if tile_equal(prev_tile, i.tiles):
                    prev_tile = i.previous_tiles
                    moves.append(i.tiles)
                    break
        
        for i in range(len(moves)-1, -1, -1):
            printTile(moves[i])

    open_list.append(BFS_node(start, check_X(start), None))

    while 1:
        
        if open_list:

            current_node = open_list[0]

            print("current node")
            printTile(current_node.tiles)

            if tile_equal(current_node.tiles, target):
                retrace(current_node)
                break
            else:
                open_list = open_list[1:]

                # print("nodes in open list")
                # for i in open_list:
                #     printTile(i.tiles)

                print("Finding possible moves")
                for neighbour in possible_moves(current_node.tiles, current_node.location):
                    in_closed_list = False

                    for j in closed_list:
                        if (j.tiles == neighbour[0]):
                            in_closed_list = True
                            break

                    if (not in_closed_list):
                        in_open_list = False

                        for j in open_list:
                            if (j.tiles == neighbour[0]):
                                in_open_list = True
                                break

                        if (not in_open_list):
                            open_list.append(BFS_node(neighbour[0], neighbour[1], current_node.tiles))
                
                closed_list.append(current_node)

                print("nodes in open list")
                for i in open_list:
                    printTile(i.tiles)
                
                print("nodes in closed list")
                for i in closed_list:
                    printTile(i.tiles)

                # break
        else:
            print("Solution not found")
            break
        
    
    



def main():
    # validation_unit_testing()
    # check_X_unit_testing()
    # heuristic_unit_testing()
    # equal_unit_testing()
    
    ## 3x3
    print("Target:")
    tilesA = [["1","2","X"],["4","5","6"],["3","7","8"]]
    printTile(tilesA)

    # print("Start:")
    # tilesB = [["2","4","6"],["1","7","5"],["3","X","6"]]
    # printTile(tilesB)

    # print("Start:")
    # tilesB = [["X","1","2"],["4","5","6"],["3","7","8"]]
    # printTile(tilesB)

    print("Start:")
    tilesB = [["4","1","2"],["5","X","6"],["3","7","8"]]
    printTile(tilesB)

    # 2x2
    # tilesA = [["1","X"],["3","2"]]
    # printTile(tilesA)

    # tilesB = [["1","X"],["3","2"]]
    # printTile(tilesB)
    # tilesB = [["1","2"],["X","3"]]
    # printTile(tilesB)

    # possible_moves(tilesA, location(0,1))
    # for i in possible_moves(tilesA, location(0,1)):
    #     printTile(i[0])

    BFS_solver(tilesA, tilesB)

    # print(type(possible_moves(tilesA, check_X(tilesA))[0][1]))
    


if __name__ == '__main__':
    main()

