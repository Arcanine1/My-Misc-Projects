import numpy as np
import copy

#outputs the board with the correct amount of weight to define how likely a ship is to be there
def big_function(board):
    
    a=0
    b=0
    #does for ship lenght one
    for rows in board:
        for nums in rows:
            if(nums==0):
                 board[a][b]= ships[0]
            b=b+1
        a=a+1
        b=0
    

    #horizontal
    a=0
    b=0
    lenght=2
    while (lenght<=width):
        for rows in board:
            counter=lenght
            while(b<width):
                if(rows[b]!= -1 and rows[b]!= -2):
                    counter=counter-1

                else:
                    counter=lenght

                if(counter==0):
                    counter=lenght
                    while(counter>0):
                        board[a][b-counter+1] = board[a][b-counter+1] + ships[lenght-1]
                        counter=counter-1
                    counter=1
                b=b+1

            a=a+1
            b=0

        lenght=lenght +1
        a=0


    #vertical
    a=0
    b=0
    lenght=2
    while (lenght<=height):
        d=0
        while(d<width):
            col = [inner[d] for inner in board]
            counter=lenght
            while(a<height):
                if(col[a]!= -1 and col[a]!= -2):
                    counter=counter-1

                else:
                    counter=lenght

                if(counter==0):
                    counter=lenght
                    while(counter>0):
                        board[a-counter+1][b] = board[a-counter+1][b] + ships[lenght-1]
                        counter=counter-1
                    counter=1
                a=a+1

            b=b+1
            a=0
            d=d+1


        lenght=lenght +1
        b=0
        d=0

    return board





ships=[0,2,0,0,0,0,0,0] #number os ships of each size

#defines board
height=8 
width=8
board = [[0 for i in range(height)] for j in range(width)]

#0 is a open spot and -1 is a spot where a ship can't be. Modify this array as game goes on
board[0] = [ 0, 0,-1,-1,-1,-1,-1,-1]
board[1] = [-1,-1,-1,-1,-1,-1,-1,-1]
board[2] = [-1,-1,-1,-1,-1, 0,-1,-1]
board[3] = [-1,-1,-1,-1,-1, 0,-1,-1]
board[4] = [-1,-1,-1,-1,-1,-1,-1,-1]
board[5] = [-1,-1,-1,-1,-1,-1,-1, 0]
board[6] = [ 0,-1,-1,-1,-1,-1,-1,-1]
board[7] = [-1, 0,-1,-1,-1,-1,-1, 0]

#defines game state and probability
gameState= copy.deepcopy(board)
probabilityDensity = big_function(board)
outputProbabilityDensity =copy.deepcopy(probabilityDensity)

#output
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in probabilityDensity]))
    
#finds solutions    
solutions = np.argwhere(probabilityDensity == np.amax(probabilityDensity))


#to search between the solution and pick the best one iterate through the next move
min = 99999999999
real_solution=solutions[0]

c=0
#looks one move ahead
while (len(solutions)>c):
    probabilityDensityinUse=copy.deepcopy(gameState)
    probabilityDensityinUse=np.array(probabilityDensityinUse)

    #sets solution to -1 as if we did that move
    a=solutions[c][0]
    b=solutions[c][1]
    probabilityDensityinUse[a][b]=-1
    
    #checks effectivness of solution
    probabilityDensityinUse=big_function(probabilityDensityinUse)
    probabilityDensityinUse[probabilityDensityinUse<0] = 0
    j=np.sum(probabilityDensityinUse)

    print(j)
    #defines new best solution if neccessary
    if(min>j):
        real_solution=solutions[c]
        min=copy.deepcopy(np.sum(probabilityDensityinUse))

    c=c+1

#output
outputProbabilityDensity=np.array(outputProbabilityDensity)
print()
print()
print(np.amax(outputProbabilityDensity))
print(real_solution)
outputProbabilityDensity[outputProbabilityDensity<0] = 0 #all negative values become 0
print(np.sum(outputProbabilityDensity))
print(min)








  

