def fibonacci(num):
    if(num<=0):
        return "Not Valid"

    a=0
    b=1
    for i in range(num):
        print(a ,  end = " ")
        next=a+b
        a=b
        b=next

# for the nth term number in the series
def nth_fibonacci(num):
    if(num<0):
        return "InValid Number"
    elif(num==0):
        return 0
    elif(num==1):
        return 1

    a=0
    b=1
    for i in range(3,num+1):
        next=a+b
        a=b
        b=next
        
    return b
num=int(input("Enter the Number"))
fibonacci(num)
num=int(input("Enter the term position :- "))
result=nth_fibonacci(num)
print(f"Fibonacci Series {num}th term : {result} ")