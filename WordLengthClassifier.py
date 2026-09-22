def classify_words(word_list):
    tuples_list = []


    for word in word_list:
     length=len(word)
     if len(word)>=5:
       tag="Long"
    else:
       tag="Short"

    word_tuple=(word,length,tag)
    tuples_list.append(word_tuple)

    return{"words_info": tuples_list}

word_list=[]

while True:
   word=input("Enter the Word or if you want to close it just type Done ")
   if word==Done:
      print
User_input=input("Enter the words : ")
words=User_input.split()

result=classify_words(words)
print(result)