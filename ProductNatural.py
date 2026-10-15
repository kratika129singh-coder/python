def product(num):
    if(num<0):
        return "Invalid Number"
    pro = 1
    for i in range(1, num + 1):
        pro = pro * i
    return pro

num = int(input("Enter the Number"))
result = product(num)
print(f"Product of {num} Natural Numbers : {result}")
