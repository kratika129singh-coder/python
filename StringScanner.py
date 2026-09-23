text=input("Enter the Text :")
count_vowel=0
count_consonant=0
count_space=0
count_digit=0

vowel="aeiouAEIOU"
 
for char in text:
    if char.isalpha():
           if char in vowel:
               count_vowel+=1
           else:
              count_consonant+=1

    elif char.isdigit():
         count_digit+=1
    else:
         count_space+=1

print("CHARACTER SCANNER")
print(f"1. Vowel : {count_vowel}")
print(f"2. Consonant : {count_consonant}")
print(f"3. Digit : {count_digit}")
print(f"4. Special Character :{count_space}")

         