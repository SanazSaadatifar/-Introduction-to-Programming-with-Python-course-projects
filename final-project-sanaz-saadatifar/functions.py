#    this is the Final project functions code
#    this code loads a CSV file about sensor temperature data with pandas for further processings.
#    @author: Sanaz Saadatifar
 
import statistics


#The following function changes the data type of value to float 
def valueNUM(value):
  valueNUM = []
  for element in value:
    valueNUM.append(float(element))
  return valueNUM

#The following function give the maximum number of a list
def MAX(m):
  return max(m)

#The following function give the minimum number of a list
def MIN(m):
  return min(m)

#The following function give the range of the numbers in a given list
def RANGE(m):
  return (MAX(m)-MIN(m))

#The following function give the mean value of the numbers in a given list
def MEAN(m):
  return statistics.mean(m)

#The following function give the median value of the numbers in a given list
def MEDIAN(m):
  return statistics.median(m)

#The following function give the standard deviation value of the numbers in a given list
def StandardDeviation(m):
  return statistics.stdev(m)

#The following function give the mode value of the numbers in a given list
def MODE(m):
  return statistics.mode(m)

#The following function give the variance value of the numbers in a given list
def VARIANCE(m):
  return statistics.variance(m)

#The following function gives a dictionary from two given lists with the same number of rows
def dictionary(m,n):
  return dict(zip(m,n))

#The following function gives a value of a dictionary based on given key
def TimeOf(m,dictionary):
  return dictionary[m]

#The following function gives the index number of a key in a list
def rowindex(X,dictionary):
  for i in range(len(list(dictionary.keys()))):
    if str(X) == list(dictionary.keys())[i]:
      return i
#The following function asks for inputs from the user and returns a date
def UserInputTime():
  a = input("enter a month with the following format (e.g. April)=")
  b = input("enter a day number in the month between 1 and 31 (e.g. 28)=")
  c = input("enter a year (e.g. 2021)=")
  d = input("enter a day time with the following format(e.g. 06:52PM)=")
  return (a + ' ' + b + ', ' + c + ' at ' + d) 

#The following function calculates and returns the statistics based on a start and end date in a given list of sensor data  
def StatisticsOutput(MAX,TimeOfMax,MIN,TimeOfMin,RANGE,MEAN,MEDIAN,StandardDeviation,MODE,VARIANCE):
  l1 = 'The Highest temperature is ' +str(MAX)+'F occurred on '+TimeOfMax+' .\n'
  l2 = 'The lowest temperature is '+str(MIN)+'F occurred on '+TimeOfMin+' .\n'
  l3 = 'The Range of data gathered so far is ' +str(RANGE)+' .\n'
  l4 = 'The Mean of data gathered so far is ' +str(MEAN)+' .\n'
  l5 = 'The Median of data gathered so far is ' +str(MEDIAN)+' .\n'
  l6 = 'The Standard Deviation of data gathered so far is ' +str(StandardDeviation)+' .\n'
  l7 = 'The Mode of data gathered so far is ' +str(MODE)+' .\n'
  l8 = 'The Variance of data gathered so far is ' +str(VARIANCE)
  return (l1+l2+l3+l4+l5+l6+l7+l8)