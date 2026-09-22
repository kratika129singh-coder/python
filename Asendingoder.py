a=int(input("Enter the first number "))
b=int(input("Enter the Second Number"))
c=int(input("Enter the Third Number"))

if(a<=b and a<=c):
    print(a)
    if(b<=c):
      print(b,c)
    else:
       print(c,b)

else:
    if(b<=c):
     print(b)
     if(c<=a):
       print(c,a)
     else:
       print(a,c)
    else:
     print(c)
     if(a<=b):
      print(a,b)
     else:
       print(b,a)




   
