import math
import cmath

x = input("enter X")
y = input("enter Y")
z = x+y
z = math.ceil(z)
a = cmath.sqrt(z)

print z
print a
if z >=10 :
    print "greater than 10"
elif z <10:
    print "less than 10"
else:
    print "hello world"

    