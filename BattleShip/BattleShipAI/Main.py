from Board import Board
from Tile import Tile
import numpy as np
import neat
import os
import copy
import visualize


def eval_genomes(genomes,config):
    for genome_id, genome in genomes:
        moves=0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        #takes number of moves it takes for 50 random diffrent boards
        for i in range (0,10):
            board = Board(rows,columns,ships)
            #njmber of moves per board
            while(not board.done):
                #normalizes inputs
                inputs = [item.state for sublist in board.gameState for item in sublist]
                for i in range(0,rows*columns):
                    item = inputs[i]
                    if(item>0):
                        item =0
                    if(item<-1):
                        item= 1
                    inputs[i]= item

                #gets outputs
                outputList = net.activate(inputs)

                #loops through best outputs until a valid one is found
                while(True):
                    output = int(np.argmax(outputList))
                    outputList[output] = -1000

                    #Adjusts board
                    rowIndex,columnIndex = int(output/columns), output%columns
                    if(board.updateState(rowIndex+1,columnIndex+1)):
                        break
                    
                moves=moves+1 

        genome.fitness= -moves
        print(genome_id)

def runAI():
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'AIconfig.txt')

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                    neat.DefaultSpeciesSet, neat.DefaultStagnation,
                    config_path)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)
    p = neat.Checkpointer.restore_checkpoint("neat-checkpoint-296")


    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))


    # Run for up to 300 generations.
    winner = p.run(eval_genomes, 300)

    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))


rows = int(input("How many rows: "))
columns =  int(input("How many columns: "))
ships = [0,3,3,1]

runAI()
