#Even/odd 
nums=[2,4,6,7,5,3,45,34,23,67,5,4,44,90]
result={"even: [] , odd: []"}

for i in nums:
    if(i%2==0):
        result["even"].append(nums)
    else:
        result["odd"].append(nums)

print("clasified Numbers:",result)
   