#Quadratic Equation Solver
import math
import cmath

def getdata():
    a = int(input("Enter a"))
    b = int(input("Enter b"))
    c = int(input("Enter c"))
    x = (-b + cmath.sqrt(b*b - 4*a*c))
    print x;

getdata();