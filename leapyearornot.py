ar=['not leapyear','leapyear']
a=int(input('entre the year'))
output=ar[(a%4==0 and a%100!=0)or(a%400==0)]
print(output)