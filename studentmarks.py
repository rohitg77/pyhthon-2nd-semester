n=int(input('entre the number of student'))
for i in range(0,n):
    sum=0
    a=5
    while a>0:
        b=int(input('entre the marks of subjects'))
        sum=sum+b
        a=a-1
    per=sum/5
    if(per>90):
        grade='A+'
    elif(per>81 and per<=90):
        grade='A'
    else:
        grade='fail'
    print(grade)

