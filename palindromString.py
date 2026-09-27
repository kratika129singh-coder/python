string=input("ENter the text")
rev = " "
for char in string:
    rev=char+rev
if(rev==string):
    print(f'"{string}" is Palindrom')
else:
    print(f'"{string}"is not palindrom')