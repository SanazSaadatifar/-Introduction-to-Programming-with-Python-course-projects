#    this is the HW3 code
#    this code converts a word file into lists in python further processings.
#    @author: Sanaz Saadatifar

def fileToList(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line.strip())
    return data

Names_str = fileToList("object_names.txt")   
Magnitudes_str = fileToList("object_magnitudes.txt")
Periods_str = fileToList("object_periods.txt")

#    fileToList function opens a given file with its name
#    return a list of strings without new line characters
#    an empty list is created at firts, iteration occurs over each line
#    strip() also is used to delete spaces    



def strListToFloatList(strings):
    strings_list = []
    for i in strings:
        strings_list.append(float(i))
    return strings_list
    
    

Magnitudes_flt = strListToFloatList(Magnitudes_str)
Periods_flt = strListToFloatList(Periods_str)

#     strListToFloatList function accepts a list of strings 
#     returns a new converted list of floats assuming that the list contains numbers
#     an empty list is created at firts, iteration occurs over each line for converting to float     


def minIndex(data):
    n = list(data)
    if n == []:
        return -1
    else:
        m = n.index(min(n))
        return m

i = minIndex(Magnitudes_flt)


print("The brightest small body object is ", Names_str[i], " with a magnitude of ", Magnitudes_flt[i], " H." )

#     minIndex  function returns the index of the minimum number from the list given as a parameter
#     -1 is set to be returned when the list is empty


def maxIndex(data):
    n = list(data)
    if n == []:
        return -1
    else:
        m = n.index(max(n))
        return m

ii = maxIndex(Periods_flt)

print("The small body object with the longest period is ", Names_str[ii], " with an orbit of ", Periods_flt[ii], " years." )
    
#     maxIndex  function returns the index of the maximum number from the list given as a parameter
#     -1 is set to be returned when the list is empty


