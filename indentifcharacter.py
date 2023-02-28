
a=input('entre the character')
if a>='0' and a<='9':
  print('digit')
elif a>='a' and a<='z' or a>='A' and a<='Z':
    print('alphabet')
else:
    print('special character')