'''string=input("ENter the text")
rev = " "
for char in string:
    rev=char+rev
if(rev==string):
    print(f'"{string}" is Palindrom')
else:
    print(f'"{string}"is not palindrom')





m=int(input("Enter the Upper Number "))
n=int(input("Enter the Lower Number "))
for i in range(m,n+1):
    if(i%2==0):
        print(i)'''



'''
num=int(input("Enter the Number "))
sum=0
for i in range (1,num+1):
    sum=sum+i
   
   
print(sum)'''

num=int(input("Enter the NUmber "))
sum=0
while(num>0):
    digit=num%10
    sum=sum+digit
    num=num//10

print(sum)