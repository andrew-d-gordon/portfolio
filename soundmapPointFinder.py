'''
Created on Jan 16, 2020, updated 1/20/20

@author: Andrew Gordon
For UCSC Soundmap Research Group
'''

from fractions import Fraction
from math import *
from json.encoder import INFINITY
    
if __name__ == '__main__':
    pass

'''This program serves to find points which are the farthest from an array of existing "recorded" points. 
The "weight" attributed to a given candidate point is the minimum distance from a candidate to a "recorded" point. 
The candidates are generated by selecting the bounds latitude and longitude, and a factor to the grid size (e.g. factor = 10 gives 100 evenly spread out points within bounds).
The amount of points is contingent on the factor, and the bounds is the size of frame you want to work with (longitude = x axis, latitude = y axis).
Eventually we will want to have the "recs" array be filled with the list of longitude/latitude values from the maps api'''

#need to work on recursing in order to add "best" finalist to recs array, and running for predetermined amount of times.

'''points function initializes storage and loads candidate points into array'''
def points(boundsLat, boundsLong, factor, recs):
    #boundsLat is size of region on y axis
    #boundsLong is size of region on x axis
    #factor = 20 #factor gives us how many points are represented on each axis
    #recs is array of current recordings latitude and longitude points
     
    candidates = [] #candidates is array of potential points to be addded as point to fill in gaps so to say
    
    #finalists = [] #finalists will contain the 10 most distant points in our space
    
    k=0 #variable to be index of candidates, incremented in loop second for loop
    for i in range(factor): #this loop will fill candidates array with potential points (lat., long.)
        for j in range(factor):
            #print(str(j))
            candidates.append([])
            candidates[k] = ((i+1)*(boundsLong/factor), (j+1)*(boundsLat/factor)) #set lat, long, and weight, use i+1 to not have 0,0 point
            k+=1 #makes sure we are on newest appended space
            
    #print(candidates.__len__())
    print("Candidates List:") #prints list of candidates
    print(candidates)
    
    furthestCandidate = [0.0, 0.0, 0.0] #furthestCandidate will be the farthest candidate from any recorded point, candidates x, y and minDist to rec point

    #now will find "best" candidates to fill in bounded space,  distances from rec. points added up
    for i in range(candidates.__len__()):
        
        minDist = inf #minDist acts to store min. distance from candidate to rec point
        candPtList = list(candidates[i]) #translate tuple to list as tuples are immutable
        
        for rec in recs:
            dist = distance(candPtList, rec) #dist acts to be current dist to recorded point from candidate, will replace current minDist if dist < minDist
            if dist < minDist:
                minDist = dist #set minDist to be dist if new minimum distance to rec. point found for candidate
            else:
                continue
            
        candPtList.append(minDist) #appends minDist to candidate
        #candidates[i] = candPtList #candidate with minDist "updates" current candidate in candidates
        
        if furthestCandidate[2] < minDist: #makes new furthestCandidate if current point is found to be the furthest candidate
            furthestCandidate = (candPtList[0], candPtList[1], minDist)
        
        #finalists.append([]) #finalists appended to add index of current candidate and it's minDist to recorded point
        #finalists[i] = [i+1, candPtList[2]] #i+1 to have indexing start at 1
    
    return candidates, furthestCandidate #returns updated candidates list, and furthestCandidate

'''distance function will provide us the distance between our candidate point and the current
point we are looking at in recs, then will attach weight to third index in triplet of candidate'''
def distance(candPtList, rec):
    #currentWeight = candPtList[2]
    latDiff = abs(candPtList[0]-rec[0])
    longDiff = abs(candPtList[1]-rec[1])
    subDist = sqrt(latDiff**2 + longDiff**2) 
    return subDist #+ currentWeight

##############
'''TEST RUN'''

iterations = 7 #the number of new recordings you would like to locate
boundsLat = 10 #the length of our boundaries y axis (how much latitude distance, 0 to boundsLat value)
boundsLong = 10 #the length of our boundaries x axis (how much longitude distance, 0 to boundsLong value)
factor = 10 #the factor to determine axis "point" frequencies. e.g. factor of 10 on bounds of 10 gives 100 points.

recs = [(1,1), (1,2), (1,3)] #initiate recs array (previously recorded points
newRecs = [] #initialize newRecs for points to be chosen to be recorded

for i in range(iterations):
    
    print("--------------------")
    print("ROUND #" + str(i+1))
    print("--------------------")
    
    test = points(boundsLat, boundsLong, factor, recs) #run algo
    
    #test[2].sort(key = lambda x: x[1], reverse=True) #sort "finalists" list, which was returned in second index of points triple-tuplet return
    
    #print("")
    #print("Candidates List (with dist):") #updated candidates list print, candidates updated list was in first index of points triple tuplet return
    #print(test[0])
    
    print("")
    print("Furthest Candidate:") #prints furthest candidate
    print("X: " + str(test[1][0]) + ", Y: " + str(test[1][1]) + ", Distance: " + str(test[1][2]))
    
    #print("")
    #print("finalists:") #prints furthest candidate
    #print(test[2])
    
    newRecs.append([])
    #newRecs[len(newRecs)-1] = (test[0][test[1][0]-1][0], test[0][test[1][0]-1][1]) #appends newly recorded point to new recordings to be made list
    newRecs[len(newRecs)-1] = (test[1][0], test[1][1])
    
    print("")
    print("Points to record:") #points to be recorded printed
    print(newRecs)
    
    recs.append([]) #would be cool to have points that are added to be recorded get colored in a different color than initial recordings on a final graph made up of points in recs array after run 
    #recs[len(recs)-1] = (test[0][test[1][0][0]-1][0], test[0][test[1][0][0]-1][1]) #appends newly recorded point to recs for next round
    #recs[len(recs)-1] = (test[0][test[1][0]-1][0], test[0][test[1][0]-1][1]) #appends newly recorded point to recs for next round
    recs[len(recs)-1] = (test[1][0], test[1][1])
    
    print("")
    print("Updated recording points:") #recs array updated for next run of algo, print
    print(recs)
    
    print("")
    
print("FINISH")
print("********************")