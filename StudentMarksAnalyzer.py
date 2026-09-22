NameList = []
MarksList = []
total=0
for i in range(5):
    name=input("Enter the Name of the Student ")
    marks=input("Enter the Marks of the Student ")


    

    NameList.append(name)
    MarksList.append(marks)
    total=total+i
    average=total/len(MarksList)
    print(NameList)
    print(MarksList)
    print(average)
    