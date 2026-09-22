marks=[22,33,55,78,67,40]
total=0
highest=marks[0]
lowest=marks[0]
count=0
for i in marks :
   total=total+i


if i>highest:
   highest=i

if i<lowest:
   lowest=i

if i>=40:
 count=count+i



average=total/len(marks)


print("Tota\l",total)
print("Average",average)
print("Highest",highest)
print("Lowest",lowest)
print("passing student ",count)
   