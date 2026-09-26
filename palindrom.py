string=input("Enter the String :")
text=string.upper()
left=0
right=len(text)-1

while left < right:
    if text[left] == text[right]:
         left=left+1
         right=right-1
    else:
        print(f'"{string}" is not palindrom')
        break

else:
    print(f'"{string}" is Palindrom')