# 5 Take two list from the user and find the largest and smallest number after that add the minimum element of the first list and maximum 
# element of the second list 
List1=[int(x) for x in input("Enter the item in List").split()]
List2=[int(x) for x in input("Enter the item in List").split()]

max=List1[0]
for i in List1:
    if(i>max):
        max=i

min=List2[0]
for i in List2:
    if(i<min):
        min=i  

add=max+min 
print(f"Maximum Number in List 1: {max}")
print(f"Minimum Number in List 2: {min}")
print(f"Total of Maximum and Minimum: {add}")     


