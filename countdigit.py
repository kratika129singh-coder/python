
num=int(input("Enter the Number"))
count=0
for i in range(1,num+1):
   digit = num % 10
   count=count+1
   num=num/10

print(count)

