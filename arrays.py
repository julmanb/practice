# you cannot add elements or remove them after it has been created
# elements must be of the same type
# arrays allows to create grids, unlike lists that are just one-dimensional
# need to use numpy package
from numpy import array
from numpy import zeros
a = zeros(4, float)
print(a)

print("\n")
print("two dimensional arrays")
# you can do so by stating b = zeros([m,n], float), where m is the number of rows and n the number of columns
b = zeros([4,5], float)
print(b)

print("\n")
print("you can also create an empty array")

from numpy import empty
c = empty(4, float)
print(c)

print("the way to create two dimensional arrays is by using lists")
r = [1, 2, 3]
s = [4, 5, 6]
c = array([r, s], float)
print(c)

print("\n")
d = zeros([2,2], float)
print(d)
print("\n")
# first row and first column = 1
d[0,0] = 1
print(d)
print("\n")
# first row and second column = 2
d[0,1] = 2
print(d)
print("\n")
# second row and first row =3
d[1,0] = 3
#print(d)
print("\n")
#second row and column = 4
d[1,1] = 4
print(d)
# here the first index from d[0,0] denotes the row element and the second denotes the column

print("reading arrays from files, like in HW3")
# here we have to use the function loadtxt from the numpy
from numpy import loadtxt
f = loadtxt("values.txt", float)
print(f)
print("doing the same as above but skipping the first two line of data")
i = loadtxt("values.txt", float, skiprows = 2)
# the number next to skiprows determine the numbers that will be removed from the data set
print(i)
