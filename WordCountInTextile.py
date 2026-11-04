#2 question # WAP to read text file and check how many word present in file
f=open("Table.txt","r")
count=0
content=f.read().split()
for char in content:
   count=count+1

print(count)
f.close()
