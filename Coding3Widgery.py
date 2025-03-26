#Coding Assignment 3
#MAT340 Spring 2024 Vermessi
#Jasmine Widgery

#IMPORTS
import random as rand
import math
import numpy as np
import pandas as pd
import statistics
#END IMPORTS

prompt = "Which test would you like to run? \n1. Gambler's Ruin \n2. Absorption Times \n3. Random Walk (distance) \n4. Random Walk (intersection)\n"

global testNumber
try:
    testNumber = int(input(prompt))
except ValueError:
       raise Exception("That\'s not a number!")
else:
    if testNumber not in [1, 2, 3, 4]:
        raise Exception("Please enter a value between 1 and 4.")


if testNumber == 1:
##############TEST 1 - GAMBLER'S RUIN##############
    print("You chose " + str(testNumber) + ", Gambler\'s Ruin.")
    a = 0
    try:
        a = int(input("Input the starting dollar amount: "))
    except ValueError:
        raise Exception("That\'s not a number!")
        
    b = 0
    try:
        b = int(input("Input the winning dollar amount you wish to stop at: "))
    except ValueError:
        raise Exception("That\'s not a number!")
    else:
        if b < a:
            raise Exception("Oops, the winning amount must be at least starting amount.")
        
    p = 0
    try:
        p = float(input("Input the probability of winning a match:"))
    except ValueError:
        raise Exception("That\'s not a number!")
    
    numMatches = 0
    try:
        numMatches = int(input("Input the number of matches you want to play: "))
    except ValueError:
        raise Exception("That\'s not a number!")


    #initialze transition matrix
    tMat = np.zeros((b+1,b+1))
    tMat[0][0] = 1
    tMat[b][b] = 1
    for i in range (1, b - 1):
        tMat[i][i - 1] = 1 - p
        tMat[i][i + 1] = p

    #print(tMat)
    tMatPowered = np.linalg.matrix_power(tMat, numMatches)
    steady_state = tMatPowered[a, :]
    print(steady_state)
##############END TEST 1 - GAMBLER\'S RUIN##############           
elif testNumber == 2:
##############TEST 2 - ABSORPTION##############
    print("You chose " + str(testNumber) + ", Absorption Times.") 
    numHeadsGoal = 0
    try:
        numHeadsGoal = int(input("Input the desired number of consecutive heads: "))
    except ValueError:
        raise Exception("That\'s not a number!")
    else:
        if numHeadsGoal < 1:
            raise Exception("Oops, the number must be more than 1.")
    totals = []
    for i in range(0, 2500):  
        numFlips = 0
        numHeads = 0
        while numHeads < numHeadsGoal:
            numFlips += 1
            flip = rand.randint(0, 1)
            if flip == 0:
                 numHeads += 1
            else:
                numHeads = 0
            #print(numHeads)
            
        totals.append(numFlips)
    avg = statistics.fmean(totals)
    print(totals)
    #avg = sum(totals) / float(len(totals))
    print("Average number of flips required: " + str(avg))
##############END TEST 2 - ABSORPTION##############  
elif testNumber == 3:
##############TEST 3 - RANDOM WALK (DISTANCE)##############
    print("You chose " + str(testNumber) + ", Random Walk (Distance).") 
    dim = 0
    try:
        dim = int(input("Input the dimension: "))
    except ValueError:
        raise Exception("That\'s not a number!")
        
    numSteps = 0
    try:
        numSteps = int(input("Input the number of steps: "))
    except ValueError:
        raise Exception("That\'s not a number!")
    else:
        if numSteps < 100:
            raise Exception("Oops, the number of steps must be 100 or higher.")

    distances = []
    for i in range(0, 2500):
        #init empty vector of size dim to keep track of movements
        dirs = []
        for j in range(0, dim):
            dirs.append(0)
        for step in range(0, numSteps):
            #randomly choose a direction
            randIndex = rand.choice(range(0, dim))
            
            #flip a coin - subtract or add 1 based on result
            randSign = rand.choice([-1, 1])
            dirs[randIndex] = dirs[randIndex] + randSign
        #after done looping through n, square each index, sum them, and store in distances
        currSum = 0
        for index in range(0, dim):
            currSum += (dirs[index]**2)
        distances.append(currSum)
    avg = statistics.fmean(distances) 
    print("Average distance is : " + str(avg))
            
##############END TEST 3 - RANDOM WALK (DISTANCE)##############
elif testNumber == 4:
##############TEST 4 - RANDOM WALK (INTERSECTION)##############
    print("You chose " + str(testNumber) + ", Random Walk (Intersection).") 
    dim = 1
    try:
        dim = int(input("Input the dimension: "))
    except ValueError:
        raise Exception("That\'s not a number!")
    else:
        if dim < 1:
            raise Exception("Please enter a value greater than 0.")

    numTrials = 0
    try:
        numTrials = int(input("Input the number of trials: "))
    except ValueError:
        raise Exception("That\'s not a number!")
        '''
    else:
        if numTrials < 1000000:
            raise Exception("Please enter a value greater than 1,000,000.")
        '''

    walkLen = 0
    try:
        walkLen = int(input("Input the walk length: "))
    except ValueError:
        raise Exception("That\'s not a number!")
        '''
    else:
        if walkLen < 400000:
            raise Exception("Please enter a value greater than 400,000.")
        '''
    rw1 = []
    rw2 = []
    numIntersect = 0
    rw1_history = []
    
    #start trials
    for i in range(0, numTrials):
        #init walk vectors
        rw1.clear()
        rw1_history.clear()
        rw2.clear()
        for init in range(0, dim):
            rw1.append(1)
            rw2.append(-1)
        #perform walk
        for rw1_iter in range(0, walkLen):
             #randomly choose a direction
            randIndex = rand.choice(range(0, dim))
            
            #flip a coin - subtract or add 1 based on result
            randSign = rand.choice([-1, 1])
            rw1[randIndex] = rw1[randIndex] + randSign
            if(rw1 not in rw1_history):
                rw1_history.append(rw1)
        #print(rw1_history)
        for rw2_iter in range(0, walkLen):
             #randomly choose a direction
            randIndex = rand.choice(range(0, dim))
            
            #flip a coin - subtract or add 1 based on result
            randSign = rand.choice([-1, 1])
            rw2[randIndex] = rw2[randIndex] + randSign
            if rw2 in rw1_history:
                numIntersect += 1
                #print("Intersection found!")
                break
    #end trials
    print(numIntersect)
    intersectionExponent = (math.log(numTrials) - math.log(numTrials - numIntersect)) / math.log(walkLen)
    print("With " + str(numTrials) + " trials of random walks of length " + str(walkLen) + " and " + str(numIntersect) + " total intersections" + ", the intersection exponent is " + str(intersectionExponent))
                
            
            
##############END TEST 4 - RANDOM WALK (INTERSECTION)##############
exit = input("If you'd like to play another game, you must exit and relaunch the program.\nPress 'Enter' to exit.") 
    