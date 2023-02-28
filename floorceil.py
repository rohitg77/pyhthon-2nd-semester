l=int(input('entre length of floor'))
b=int(input('entre breadth of floor'))
l1=int(input('entre length of tile'))
b2=int(input('entre breadth of tile'))
area=l*b
area1=l1*b2
number=-(-area//area1)
#floor divide converted in to ceil by -ve sign and again -ve sign for making value +ve
print(number)


