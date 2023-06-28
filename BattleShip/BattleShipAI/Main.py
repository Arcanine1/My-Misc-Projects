from Board import Board
from Tile import Tile
import numpy as np
import neat
import os
import math

def showInput(input):
    for i in range(8):
        for j in range(8):
            index = i * 8 + j
            print(f"{input[index]:2}", end=" ")
        print()

#flattens board and normalizes it
def normalizeBoard(board):
    inputs = [item.state for sublist in board.gameState for item in sublist]
    for i in range(0,rows*columns):
        item = inputs[i]
        if(item>0):
            item =0
        if(item<-1):
            item= 1
        inputs[i]= item
    return inputs


def eval_genomes(genomes,config):
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        #Runs each network through 10 diffrent board to account for randomness through law of large numbers
        fitness = 0
        for i in range (0,10):
            board = Board(rows,columns,ships)
            while(not board.done):
                inputs= normalizeBoard(board)
                #gets outputs
                outputList = net.activate(inputs)
                movenumber =1
                #loops through best outputs until a valid one is found
                while(True):
                    output = int(np.argmax(outputList))
                    rowIndex,columnIndex = int(output/columns), output%columns
                    result = board.updateState(rowIndex+1,columnIndex+1)
                    movenumber =movenumber+1

                    #hits the same tile twice
                    if(result == False):
                        fitness=  fitness-1
                        outputList[output]= -1000
                    else:
                        break

                    # elif(result=="Hit"):
                    #     fitness = fitness+25/math.sqrt(movenumber)
                    #     break

                    # elif(result== "Miss"):
                    #     fitness=fitness-1
                    #     break

        genome.fitness= fitness

def runAI():
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'AIconfig.txt')

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                    neat.DefaultSpeciesSet, neat.DefaultStagnation,
                    config_path)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(time_interval_seconds= 1000))


    # Run for up to 300 generations.
    winner = p.run(eval_genomes, 300)

    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))


rows = int(input("How many rows: "))
columns =  int(input("How many columns: "))
ships = [0,3,3,1]

runAI()
