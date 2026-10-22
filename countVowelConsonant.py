def countvowel(text):
    vowels="aeiouAEIOU"
    vowel_count=0
    consonant_count=0
    for char in text:
       if char.isalpha():
          if char in vowels:
           vowel_count=vowel_count+1
          else:
           consonant_count=consonant_count+1

    return vowel_count,consonant_count


text=input("Enter the Text")
vowel,consonant=countvowel(text)
print(text)
print(f"vowels : {vowel}")
print(f"consonant : {consonant}")
      