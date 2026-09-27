num=int(input("Enter the Number"))
sum=0
while(num>0):
    digit = num % 10
    rest=num/10
    sum=sum+digit
    
print(sum)
