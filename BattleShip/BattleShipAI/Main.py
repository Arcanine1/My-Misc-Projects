from Board import Board
from Solver import Solver
import numpy as np

height= 8
width=8
ships = [0,3,3,1]

board = Board(height,width,ships)

Solver.getBestMove(board)
