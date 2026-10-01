lists=list(map(int,input("Enter the prize of item list").split()))
isMember=input("Do you have Gold Membership? (True/False)").strip().lower()=="true"

sum=0
for i in lists:
    sum=sum+i

print(f"Toal Bill :-{sum}")

if (sum<1000):
    print("There is no Discount")
elif(1000<=sum<=5000):
    discount=10
    print("10% Discount applied")
elif(sum>5000):
    discount=20
    print("20% Discount applied")


if(isMember):
    discount = discount + 5
    print("5% Gold Member Discount Applied")
    total_discount=(sum*discount)/100
    bill=sum-total_discount

    


print(f"total discount applied: {discount}%") 
print(f" Final Payable Amount with Discount :{bill}")



    