import random
import string
str=input("Enter the Message")
words=str.split(" ")
coding=input("1 for Enter Coding or 0 for Decoding")
coding =True if (coding=='1') else False
if(coding):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            r1="".join(random.choices(string.ascii_lowercase,k=3)) 
            r2="".join(random.choices(string.ascii_lowercase,k=3))
            newstr=r1+word[1:]+word[0]+r2  
            nwords.append(newstr)
        else:
            nwords.append(word[::-1])

    print(" ".join(nwords))  

else:
    nwords=[]
    for word in words:
            if(len(word)>=3):
                newstr=word[3:-3]
                newstr=newstr[-1]+newstr[:-1] 
                nwords.append(newstr)
            else:
                nwords.append(word[::-1])
    
    print(" ".join(nwords))  
    
    


    