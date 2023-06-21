from Board import Board
from Tile import Tile


rows = int(input("How many rows: "))
columns =  int(input("How many columns: "))

ships = [0,50]

board = Board(rows,columns,ships)

for row in board.gameState:
    print('  '.join(str(tile.state) for tile in row))
