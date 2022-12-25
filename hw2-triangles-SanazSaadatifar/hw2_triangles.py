"""
These are Function Headers
Complete the functions to ensure they return expected results
Replace these comments with documenation about the program
@author [add your name]
"""

#    this is the HW2 code
#    this code defines different types of triangles based on the three inputs by user
#    @author: Sanaz Saadatifar
a = float(input("Enter the length of the first side:"))
b = float(input("Enter the length of the second side:"))
c = float(input("Enter the length of the third side:"))
#    Read three (3) numbers from the keyboard. These numbers represent the side lengths of a triangle.

def isReal(a, b, c):
    return bool(a>0 and b>0 and c>0 and a+b>c and c+b>a and a+c>b)
#    This function Returns True with valid lengths and inequality sumation a + b > c (all arragements)

def isEquilateral(a,b,c):
    return bool( a>0 and b>0 and c>0 and a == b == c )
#    This function Returns True whenever all sides are equal

def isIsosceles(a,b,c):
    return bool( a>0 and b>0 and c>0 and (a == b != c or a == c != b or c == b != a ))
#    This function Returns True whenever two (and only two) sides match

def isScalene(a,b,c):
    return bool(a>0 and b>0 and c>0 and a != b != c and c != a)
#    This function Returns True whenever all three sides are different lengths

def isPythagorean(a,b,c):
    return bool((a>0 and b>0 and c>0) and a*a + b*b == c*c or c*c + b*b == a*a or a*a + c*c == b*b)
#    This function Returns True whenever a*a + b*b = c*c including re-order




#    the if process starts here based on the given variables for each side of the triangle.
if isReal(a, b, c) is True:
#    This function Returns True whenever all sides are equal
#    check to see if the tiangle is real, if yes, then the following if statems are defined within this first if statement.    
#    def isEquilateral(a,b,c):
#        return bool( a == b == c )

#    if not at then end the else statement will print appropriate result
    if isEquilateral(a,b,c) is True:
        print('This is an Equilateral triangle.')
    else:
        pass
#    check to see if the tiangle is Equilateral, if yes, then print. if not, then pass.
    
    
    
    if isIsosceles(a,b,c) is True:
        print('This is an Isosceles triangle.')
    else:
        pass
#    check to see if the tiangle is Isosceles, if yes, then print. if not, then pass.   
    
    
    if isScalene(a,b,c) is True:
        print('This is a Scalene triangle.')
    else:
        pass
#    check to see if the tiangle is Scalene, if yes, then print. if not, then pass.    
    
    
    if isPythagorean(a,b,c) is True:
        print('In addition, This is a Pythagorean triangle.')
    else:
        pass
#    check to see if the tiangle is Pythagorean, if yes, then print. if not, then pass.    
    
    
else:
    print("This is not a Real triangle.") 
#    here the result of if not for the first if statement is shown.

