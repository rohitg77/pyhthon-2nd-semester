amount=int(input("entre the amount you want to withdraws"))
amount=amount-100
a=amount//2000
amount=amount%2000
b=amount//500
amount=amount%500
c=amount//200
amount=amount%200
d=amount//100
print("number of 2000 rs note requireds",a)
print("number of 500 rs note required",b)
print("number of 200 rs note required",c)
print("number of 100 rs note required",d+1)

