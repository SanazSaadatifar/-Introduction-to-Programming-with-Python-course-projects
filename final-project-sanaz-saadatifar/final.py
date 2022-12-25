#    this is the Final project main code
#    this code loads a CSV file about sensor temperature data with pandas for further processings.
#    @author: Sanaz Saadatifar

import pandas as pd
import numpy as np
import functions as fn


def main():
    df = pd.read_csv('temperatureF.csv') #here the csv file is read with pandas
    A = df.to_numpy()     #here the pandas file is converted to numpy
    data = np.delete(A, [0,2], 1)    #the required columns are selected
        #the following data is needed for calculating statistics for temperature data considering the whole data in the csv file
    timeSoFar = data[:,1]
    value1 = data[:,0]
    valueSoFar = fn.valueNUM(value1)
    dictSoFar = fn.dictionary(value1,timeSoFar)
    MAXSoFar = fn.MAX(valueSoFar)
    MINSoFar = fn.MIN(valueSoFar)
    mydict = fn.dictionary(timeSoFar,value1)
        #the function is called within the print
    print('Welcome to Live temperature data monitoring program.')
    print('The following statistical information is for data collected since April 28, 2021 at 06:51PM.')
    print(fn.StatisticsOutput(MAXSoFar,fn.TimeOf(MAXSoFar,dictSoFar),MINSoFar,fn.TimeOf(MINSoFar,dictSoFar),fn.RANGE(valueSoFar),fn.MEAN(valueSoFar),fn.MEDIAN(valueSoFar),fn.StandardDeviation(valueSoFar),fn.MODE(valueSoFar),fn.VARIANCE(valueSoFar))) 
    var = 1 #the following questions will be asked continually until the user decides not to continue
    while var == 1:
        U = input("Would you like to continue?(Y/N):").lower()
        if U == "y":
            A = int(input('Please select 1 if you want to get statistical analysis for a slice of time based on your defined start and end date,\n and 2 if you want to get the sensor specific temperature data for your defined date.'))
           #if user answers 1, then he/she will get the static’s for a time slice within the csv file time frame            
            if A == 1:#the following data is needed for calculating statistics for temperature data considering a user-defined slice of the whole data in the csv file
                print('for START date:')
                UserInputTimeStartDate = fn.UserInputTime() 
                print('for END date:')
                aEndDate = input("enter a month with the following format (e.g. April)=")
                bEndDate = input("enter a day number in the month between 1 and 31 (e.g. 28)=")
                cEndDate = input("enter a year (e.g. 2021)=")
                dEndDate = input("enter a day time with the following format(e.g. 06:52PM)=")
                UserInputTimeEndDate = aEndDate + ' ' + bEndDate + ', ' + cEndDate + ' at ' + dEndDate
                value2 = data[fn.rowindex(UserInputTimeStartDate,mydict):fn.rowindex(UserInputTimeEndDate,mydict)+1,0]
                valueNUM2 = fn.valueNUM(value2)
                MAX2 = fn.MAX(valueNUM2)
                MIN2 = fn.MIN(valueNUM2)
                print('The following statistical information is for data collected since start Date and end date ')
                print(fn.StatisticsOutput(MAX2,fn.TimeOf(MAX2,dictSoFar),MIN2,fn.TimeOf(MIN2,dictSoFar),fn.RANGE(valueNUM2),fn.MEAN(valueNUM2),fn.MEDIAN(valueNUM2),fn.StandardDeviation(valueNUM2),fn.MODE(valueNUM2),fn.VARIANCE(valueNUM2)))
                #the function is called within the print
                #if the user answers 2, then he/she will get the exact temperature data in a specific time
            if A == 2:
                UserInputTime2 = str(fn.UserInputTime())
                if UserInputTime2 in mydict.keys():
                    print("your entered date is " +str(UserInputTime2)+ ", and the sensor data for that date is " + str(mydict[UserInputTime2]))
                else:
                    print("No data has found for the given time")  
        if U == "n": #here user has decides not to continue
            print("bye, Have a good day")
            break
            
    var += 1

    


###
# Do not delete the following lines of code. Add the body of your code to the main() function.
###
if __name__ == "__main__":
    main()
