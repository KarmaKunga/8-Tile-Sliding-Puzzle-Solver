# Author: Kunga
# Created: 09/10/2024

N = 3  # Tiles / Side

def printTile(tiles):
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
                return y, x                
    return None

def main():
    # validation_unit_testing()
    
    tiles = [["1","2","3"],["4","X","6"],["5","7","8"]]
    printTile(tiles)
    print(check_X(tiles))

if __name__ == '__main__':
    main()

