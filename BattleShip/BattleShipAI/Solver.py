from Board import Board
import numpy as np
import copy
import matplotlib.pyplot as plt
import seaborn as sns




class Solver:
    
    @staticmethod
    def getBestMove(Board):
        #gets best ship move
        PDF = Solver._createPDF(Board)
        solutions = np.argwhere(PDF == np.amax(PDF))
        real_solution = solutions[0]

        Solver._showHeatMap
        return (real_solution[0]+1,real_solution[1]+1)

        
    @staticmethod
    def _showHeatMap(PDF):
        sns.set()
        ax = sns.heatmap(PDF)
        plt.show()


    @staticmethod
    #creates Probability distribution function
    def _createPDF(Board):
        PDF = np.zeros(shape= (Board.height,Board.width))
        for i in range(1,1000):
            #re rolls ships
            Current_Board =  copy.deepcopy(Board)
            Current_Board.eraseShips()
            Current_Board.randomizeBoard(Board.ships)

            #makes all ships worth 1 and creates array of just the states
            states = np.zeros(shape= (Board.height,Board.width))
            row_index = 0
            while row_index < Current_Board.height:
                row = Current_Board.gameState[row_index]
                tile_index = 0
                while tile_index < Current_Board.width:
                    tile = row[tile_index]
                    if tile.state > 0:
                        tile.state = 1
                    states[row_index][tile_index] = tile.state
                    tile_index += 1
                row_index += 1

                        
            
            #adds to PDF
            PDF = np.add(states,PDF)

        return PDF
