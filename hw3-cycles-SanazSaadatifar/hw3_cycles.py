"""
These are Function Headers
Complete the functions to ensure they return expected results
Replace these comments with documenation about the program
@author [add your name]
"""

#    this is the HW3 code
#    this code detects when a given sequence has a cycle has uses in cryptography and data science. 
#    @author: Sanaz Saadatifar
path = []

m = input("Enter an index (X or x to stop) ")
while m != "X" and m !="x": # 'X'or'x' cause to stop getting new inputs
	path.append(int(m)) 
	m = input("Enter an index (X or x to stop) ")
#    m are inputs that user defines    




def isUnitPath(path):
        return path == [0]
if isUnitPath(path) is True:
    print(path, ' is UnitPath.')
else:
    print(path, ' is not UnitPath.')
    
#    the isUnitPath(path) function checsk to see if the path has only one item values as zero
#    Returns True whenever the path list is only one element with a value of zero, otherwise False



def hasMatchingIndex(path):
    i = 0
    while i <= len(path)-1 :
        if path[i]==i:
            return True
        i +=1
        
    return False
    
    
if hasMatchingIndex(path) is True:
    print(path, ' hasMatchingIndex.')
else:
    print(path, ' does not  have MatchingIndex.')
    
#   the hasMatchingIndex(path) function checks to see if there is an item wihc has the same value as its item number
#   Returns True whenever any element corresponds to its index, otherwise False



def hasInvalidEntry(path):
    
    if len(path)==0 :
        return True
    else:
        for m in path:
            if m<0 or m>=len(path):
                return True
        return False


if hasInvalidEntry(path) is True:
    print (path, ' has Invalid Entry')
else:
    print (path, ' does not have Invalid Entry')
    
#    the hasInvalidEntry(path) function chechks for not having invalid entries
#    Invalid is defined when there is no item in the list or the items are less than zero or greater than length of list
#    Returns True whenever an element in path list is outside the valid range or the path is empty
#    Once all of the elements are checked as valid then it is safe to return False


def hasEveryNumber(path):
    if len(path)==0:
        return False
    i = 0
    while i <= len(path)-1 :
        if (not i in path):
            return False
        i +=1
        
    return True
    
    
if hasEveryNumber(path) is True :
    print (path, ' has every number')
else:
    print (path, ' does not have every number')
    

#    this hasEveryNumber(path) function checks to see if all items required in the range of len(path) is in the list or not
#    Returns True whenever the path list contains each unique value from 0 to len(path)-1 in any order, otherwise False




def cycleLength(path):
    path2 = []
    if hasInvalidEntry(path) is True:
        return 0
        
    else:
        i = 0
        j = 0
        while j<len(path) and (path[i] not in path2):
            path2.append(path[i])
            i = path[i]
            j = j + 1
        return len(path2) 
 
print ('the cycleLength for: ', path, ' is ', cycleLength(path))  


#    this def cycleLength(path) function defines a sycle based on a logic described below 
#    a new list called path2 would result at the end which the main task of this function is to count the length od path2
#    In the event that the path list contains invalid or no entries, return 0
#    Otherwise, to have the path2 the path starting from index zero and append to another list every index you have visited
#    When it is encounteres to an index that you've already visited you can stop iterating
#    Either use a counter to keep track of the path length or return the length of your visted list

