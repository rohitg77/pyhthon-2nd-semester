n=int(input())
p=n
s=0
while p>0:
    r=p%10
    s=s*10+r
    p=p//10
if(n==s):
    print('parraleodeome')
else:
    print('not')