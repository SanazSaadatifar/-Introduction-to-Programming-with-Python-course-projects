#    this is the HW5 code
#    this code converts a CSV file into Dict in python also accepts user inputs for further processings.
#    @author: Sanaz Saadatifar


#the following function accepts a file name as a parameter and then returns a dictionary of lists
#The first line of the file (the headers) is not included in the returned dictionary
def csvToDictOfLists(filename):
    C = {}
    with open(filename, mode='r') as inp:
        lines = inp.readlines()[1:]
        for col in lines:
            Col = col.strip().split(",")
            key = Col[0]
            value = Col[1:]
            C[key]= value
    return C
   
        




# the following function accepts a dictionary as described in Step 1 and a string to filter against. 
#It returns a list of keys which coincide with the given string.    

def filterKeys( dictionary, search_key1):
    L = []
    for key in dictionary:
        if search_key1.lower() in key.lower():
            L.append(key)

    return L

        





# this following function accepts a dictionary as described in Step 1 and a column index 
# it returns a set which contains all of the values from that column index


def columnToSet(dictionary, column_index1):
    S = set()
    value = dictionary.values()
    for col in value:
        S.add(col[column_index1])
    return S






# the following function accepts a dictionary as described in Step 1, a column index , and a string value. 
# it return a list of keys which have a column element that matches against the given string.



def filterByColumn(dictionary, column_index2, search_key2):
    M = set()
    LL = []
    lw = []
    P = []
    key_list = list(dictionary.keys())
    val_list = list(dictionary.values())
    value = dictionary.values()
    for col in value:
        M.add(col[column_index2])
        MM = list(M)
    for i in range(len(MM)):
        if search_key2.lower() in MM[i]:
            LL.append(MM[i])

    for i in range(len(val_list)):
        lw.append((val_list[i])[column_index2])
    for i in range(len(lw)):
        if lw[i] in LL:
            P.append(key_list[i])
    return P
    

#################################################################################
#the following fuction is the main  body of code for pervious defined functions     

def main():
    mydict= csvToDictOfLists('pgh.csv')
    var = 1
    while var == 1:
        A = input("Enter 0 for Genus, 1 for Species, 2 for Subspecies, 3 for Types, or a name:")
        if A.isdigit():
            A1= int(A)
            print(columnToSet(mydict, A1))
            B = input("Enter a string =")
            BB = filterByColumn(mydict, A1, B) 
            print(BB)
            if len(BB) == 1:
                print(mydict[BB[0]])
            else:
                pass 
        else:
            N = filterKeys( mydict, A)
            print(N)
            if len(N) == 1:
                print(mydict[N[0]])
            else:
                pass
                

        U = input("Would you like to continue?(Y/N):").lower()
        if U == "n":
            print("bye, Have a good day")
            break
        

    var += 1

    
    


###
# Do not delete the following lines of code. Add the body of your code to the main() function.
###
if __name__ == "__main__":
    main()
