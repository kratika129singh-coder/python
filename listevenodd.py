evenlist =[]
oddlist=[]

for i in range(5):
    num=int(input("Enter the Number"))
    if num % 2 == 0:
       evenlist.append(num)

    else:
      oddlist.append(num)


print("Even List" ,evenlist)
print("Odd List" ,oddlist)