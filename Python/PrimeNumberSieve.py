#!/usr/bin/env pypy

import math
import time

start = time.time()

size=10**8 #search range
numbers  = [True] * size#defines array
numbers[0] , numbers[1]= False,False
factor=1  #current factor
root = math.sqrt(size)
num=3 #num evaluating currently

while(factor<root):

    #finds new factor
    factor=factor+1
    while(True):
        if(numbers[factor]):
            break
        factor=factor+1


    multiple =factor
    top = size/factor

    while(multiple<top):
        numbers[factor*multiple] = False
        multiple=multiple+1


        

print(numbers.count(True))
end = time.time()
print("Seconds:" + str(end - start))


    