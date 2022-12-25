import numpy as np
import matplotlib.pyplot as plt 

#    this is the HW6 code
#    this code loads a text file with numpy for further processings.
#    @author: Sanaz Saadatifar

def average(parameter1, parameter2):
    return ((parameter1 + parameter2)/2)
# this function accepts two parameters, adds them together, divdes them by two, and returns that result



def cToF(Celcius):
    Fahrenheit = (1.8*Celcius) + 32
    return Fahrenheit
# this function accepts a Celcius parameter and returns its Fahrenheit conversion




def fToC(F):
    C = ((F-32)*5)/9
    return C
# this function accepts a Fahrenheit parameter and returns its Celcius conversion.





def main():
    TXT = np.loadtxt("heathrowdata.txt", skiprows=7, usecols=(0,2,3))
#print(TXT)    
# the text file is loading here with first seven rwos skipped and just three colomns used

    A = average(TXT[:,1], TXT[:,2])
#print(A)

    plt.plot(TXT[:,0], A, 'o')
# the base plot is created here
    m, b = np.polyfit(TXT[:,0], A, 1)

    plt.plot(TXT[:,0], m*TXT[:,0] + b)
#the line is created here
    plt.xlabel("YEARS")
    plt.ylabel("Average Temperature")
    plt.title('United Kingdom weather data')
#the labesl and titles are added here

    plt.savefig("United Kingdom weather.png", format = "png")
    plt.show()
#the png file is saved here   


###
# Do not delete the following lines of code. Add your code to the main() function.
###
if __name__ == "__main__":
    main()
