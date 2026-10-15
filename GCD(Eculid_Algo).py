def gcd(num1,num2):
    while(num2>0):
      num1,num2 = num2 , num1 % num2
    
    return num1


num1=int(input("Enter the  First  Number"))
num2=int(input("Enter the  Second Number"))
result=gcd(num1,num2)
print(f"GCD of {num1},{num2} is {result}")