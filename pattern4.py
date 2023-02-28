'''n=''
a=int(input())
for i in range(65,65+a):
    n=n+chr(i)
print((n+'\n')*a)'''
'''n=int(input())
for j in range(n):
    print(chr(65+j)*(j+1))'''
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end='')
    print()    

    
    