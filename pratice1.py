print("""Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are
Twinkle, twinkle, little starpy
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are
Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are
Twinkle, twinkle, little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle, twinkle, little star
How I wonder what you are""")




import pyttsx3
engine = pyttsx3.init()
engine.say("Hello kratika  i am here what do you want i can help you    Mohit  Mohit Mohit Mohit ")
engine.runAndWait()



import os

# Specify the directory path (use '.' for current directory)
path = "/"  

try:
    contents = os.listdir(path)
    print(f"Contents of '{path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("Error: Directory not found.")
except PermissionError:
    print("Error: Permission denied.")

a="324"
t=type(a)
print(t)