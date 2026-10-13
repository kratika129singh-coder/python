def factorial(num):
    if(num<=0):
      return "Invalid Number"
    
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    
    return fact

num=int(input("Enter the Number :- "))
result=factorial(num)
print(f"factorial of {num} Number : {result}")