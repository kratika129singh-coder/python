num=int(input("Enter the Number"))
i=2
while(i<=num):
    if(num%i!=0):
        print("  prime")
        break
    else:
        i=i+1
else:
    print(" not prime ")
