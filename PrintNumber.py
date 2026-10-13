def Print1toN(num):
    if(num<=0):
        print("Invalid Number")
    for i in range(1,num+1):
        print(i,end=" ")
    
    print()
def PrintNto1(num):
    if(num<=0):
        print("Invalid Number")
    for i in range(num,0,-1):
        print(i,end=" ")
        


num=int(input("Enter the Number"))
Print1toN(num)
num=int(input("Enter the Number"))
PrintNto1(num)

