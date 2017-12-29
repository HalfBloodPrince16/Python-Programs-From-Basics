import math

def getdata():
    x = input("enter x")
    y = input("enter y")
    return (x+y)

def process(z):
    sum = 0
    for i in range(z):
        sum = sum+i
        print(sum)
z = getdata()
process(z)
print(z)

#keywod args
def College(name='AIT',place='Pune'):
    print(name)
    print(place)
College();
College("VIT","Bangalore")
