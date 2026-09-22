'''x=233
y=233
z='kratika'
print(type(x))
print(type(z))
print(id(x))
print(id(y))
#write a progrma that takes two integer inputs. swap their values without using a third variable ,print their values, data type('type()'),
#  and memory addresses ('id()') before and after the swap [span_19](end_span)[span_19](end_span).
n=int(input("Enter the Number :- "))
m=int(input("Enter the Number :- "))
print("Before Swaping")
print(f"n -> Value: {n} Type: {type(n)}, Memory id: {id(n)}")
print(f"m -> Value: {m} Type: {type(m)}, Memory id: {id(m)}")

n,m=m,n  #tuple unpacking

print("After Swaping")
print(f"n -> Value: {n} Type: {type(n)}, Memory id: {id(n)}")
print(f"m -> Value: {m} Type: {type(m)}, Memory id: {id(m)}")

#Create script that reads a tempreture in celsius,cnvert in farrenhit(f=c/times/frac{9}{5}+32)and kelvin (k=c+273.15)
# and fromat according the output adhering to PEP 8stanfards[span_20(start_span)[span_20](end_span).]
def convert_tempreture():                           

    c=float(input("Enter tempreture in celsius : "))
    f=(c * 9/5) + 32
    k=c+273.15

    print(f"Celsius : {c: 2f} ")
    print(f"Fahrenheit : {f: 2f}")
    print(f"Kelvin : {k: 2f}")

if __name__=="__main__":
    convert_tempreture()

#Leap year & Century Checker
year=int(input("Enter the Year :-"))
if(year % 400 == 0):
    print(f"{year} is  Century Leap year")
elif(year % 100 == 0 ):
    print(f"{year} is Century year but Not a leap year ")
elif(year % 4 == 0 ):
    print(f"{year} is Leap year")
else:
    print(f"{year} is a normal year.")'''

'''#Prime  Number Generator by using starting and ending range should be according to user
start_range=int(input("Enter the  Statring Number"))
end_range=int(input("Enter the ending Number"))
for i in range(start_range , end_range + 1):
    if(i > 1):
        for j in range(2, int(i**0.5) + 1): 
'''

'''#Armstrong Checker
number=int(input("Enter the Number"))
while(temp > 0):
    digit=number%10
    temp=digit
    temp=digit/10

if(total_sum==number)
   print("ArmStrong Number" )'''

'''#Number Guessing Game
import random
secret_number=random.randint(1,100)
attempt=0

while(True):
    number=int(input("Enter the Number :-"))
    if(number<=0):
        print("Positive value is requried only")
        continue #skip the below coe and goback to the loop again

    attempt=attempt+1
    if(number > secret_number):
        print("Too Big")
      
    elif(number < secret_number):
        print("Too low")
    
    else:
        print("Correct Gues !Congrats")
        break

print("Attempts : " ,attempt)'''

'''#Fibonacci Series with rules)
number=int(input("Enter the Maximum Nmber of Series"))
a,b=0,1

print("Fibnacci Series :-")
while (True):
    if(a>number):
        break
    if(a%2==0):
        a,b=b,a+b
        continue
    print("Fibonacci Series:" a,end=" ")
    a,b=b,a+b'''

'''#Menu Driven Calulate
while(True):
    print("==============Menu Driven Calculater============")
    print(" 1.Add Two Number")
    print(" 2.Subtract Two Number")
    print(" 3.Mutiply Two Number")
    print(" 4.Divide two Number")
    print(" 5.Exit")
    choice=input("Choose any Number (1 to 5) ")

    if(choice=='5'):
        print("Program successfully Executed")
        break
    if choice in ["1","2","3","4"]:
       num1=float(input("Enter the Number"))
       num2=float(input("Enter the Number"))

    if choice == "1":
        print(f"{ num1 } + { num2 } = { num1+num2 }")
    elif choice == "2":
        print(f"{ num1 } - { num2 } = { num1-num2 }")
    elif choice=="3":
        print(f"{ num1 } * { num2 } = { num1*num2 }")
    elif choice=="4":
        if(num2==0):
            print("Error: '0' can not be divide")
        else:
            print(f"{ num1 } / { num2 } = { num1/num2 }")

else:
    print("Invalid option ! choose between (1 to 5)")'''

#Digital Root Calculator
'''number=int(input("Enter the number"))
original_num=number

while(number>=10):
   digit_sum=0

   while(number>0):
       digit=number%10
       digit_sum = digit_sum + digit
       number=number//10


number=digit_sum
print(f"{original_num} of sum of digit {number}")'''







