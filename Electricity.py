a=float(input("Enter Electricity units consumed : "))
if(a<=100):
    energy=a*5.0
elif(a>100 and a<=300):
    energy=a*5.5
else:
    energy=a*6.5

total_bill=energy+1000

if(total_bill>=3000):
    total_bill=total_bill*0.10

print(f"Total Electricity Bill: {total_bill:2f}")


