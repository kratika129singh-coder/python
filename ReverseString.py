def ReverseString(string):
    rev=""
    for char in string:
        rev=char+rev
     
    return rev


string=input("Enter the Text ")
result=ReverseString(string)
print(f"The Reverse of the {string}  is :{result}")