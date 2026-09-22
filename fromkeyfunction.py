n=int(input("enter the element till that number you want"))
l= [i*5 for i in range(1,n+1) ]
d={}
d.fromkeys(l,0)
print(d)
