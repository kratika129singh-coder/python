print("Mobile Rechare Billing System")
recharge_amount=float(input("Enter the Amount"))
fixed_charge=20
if(recharge_amount>2000):
    service_charge=0.08
elif(recharge_amount<500):
    service_charge=0.05
else:
    service_charge=0.0


service_charge=recharge_amount*service_charge
final = recharge_amount + fixed_charge + service_charge

print("Billing Summary")
print(f"Recharge Amount:{recharge_amount:2f}")
print(f"Fixed Charge:{fixed_charge:2f}")
print(f"service charge{service_charge:2f}")
print(f"Final_Amount:{final:2f}")


