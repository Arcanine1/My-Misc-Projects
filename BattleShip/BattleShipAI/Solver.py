from Board import Board
import numpy as np
import copy
import matplotlib.pyplot as plt
import seaborn as sns




class Solver:
    
    @staticmethod
    def getBestMove(Board):
        PDF = Solver._createPDF(Board)
        solutions = np.argwhere(PDF == np.amax(PDF))
        real_solution = solutions[0]

        return (real_solution[0]+1,real_solution[1]+1)

        
    @staticmethod
    def _showHeatMap(PDF):
        sns.set()
        ax = sns.heatmap(PDF)
        plt.show()


    @staticmethod
    def _createPDF(Board):
        PDF = np.zeros(size = (Board.height,Board.width))
        for i in range(1,1000):
            #re rolls ships
            Current_Board =  copy.deepcopy(Board)
            Current_Board.eraseShips()
            Current_Board.randomizeBoard()

            #makes all ships worth 1
            for row in Current_Board.gameState:
                for tile in row:
                    if(tile.state >0):
                        tile.state = 1

            PDF = np.add(Current_Board.gameState,PDF)

        return PDF
