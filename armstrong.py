n=int(input('entre the number'))
sum=0
s=n
b=str(n)
a=len(b)
while n>0:
     k=n%10
     sum=sum+(k**a)
     n=n//10
if(sum==s):
    print('arm strong') 
    

    
