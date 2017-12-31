#matrices input output using loops
import math

a = int(input("enter row size of matrice : "))
b = int(input("enter column size of matrice: "))
x = [a][b]

for i in range(0,a):
    for j in range(0,b):
        x[i][j].append(int(input()))

for i in range(a):
    for j in range(b):
        print(x[i][j])

