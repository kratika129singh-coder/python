a="kratika"
b=100
print("my name is %s and age is %d" %(a,b))
print("My name is {},and age is {}".format(a,b))
#1.write a program is take two string and check these strings are equal or not
a=input("Enter any word : ")
b=input("Enter any word : ")
if a==b:
  print("String are same")
else:
  print("String are not same")

#2.Take a string and check vowels and count.
c=input("Enter the the word : ")
count=0
for i in c:
   if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
    count=count+1
  
print("There are",count,"vowels")


#3. write a program to check to input username and password if both are correct then display the login successfull otherwise display incorrect password.
user = "Kratika"
passwd = "Password"
Username=input("Enter the Username")
Password=input("Enter the Password")
if Username==user and Password==passwd :
  print("Login is successfull")
else:
  print("Login is unseccessfull")

#4. WAP to the input username if the username is admin and ask for password and verify it .display login is successfull display password is correct and otherwise password is incorrect.
 users= "admin"
 Username = input("Enter the Username")
if(users==Username):
  Passwor=input("Enter the Password")
  print("Login is good")
else:
  print("Login is not good")


#5. WAP to input two string if string 1 is contained in string 2 then create a third string with first four character of string 2  added with word 'restore'.
 
 








#6. WAP to check a string is palindrome by using slicing.