a=int(input('amount of bread'))
b=int(input('amount of bread'))
c=int(input('amount of bread'))
d=int(input('total amount of cake'))
if(d/a==0):
    print('true')
elif(d%b==0):
    print('true')
elif(d%c==0):
    print('true')
elif(d%(a+b)==0):
    print('true')
elif(d%(c+b)==0):
    print('true')
elif(d%(c+a)==0):
    print('true')
elif(d%(a+b+c)==0):
    print('true')
else:
    print('falsse')
