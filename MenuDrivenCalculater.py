def calculator():
    while(True):
      print("=========================Caculator========================")
      print("=============Which Operation you want to perform===========")
      print("1. Addition")
      print("2. Subtration")
      print("3. Multiplication")
      print("4. Division")
      print("5. Module")
      print("6. Exit the Calculator")
      print("============================================================")

      
      choice=input("Select Operation(1 to 6) :-")

      if choice=='6':
         print("Thanku you for using\nGood Day!...")
         break
      
      try:
          num1=float(input("Enter the Number :-"))
          num2=float(input("Enter the Number :-"))

          match choice: 
                  case '1':
                      print(f"Result :- {num1} + {num2} = {num1+num2}")
                  case '2':
                      print(f"Result :- {num1} - {num2} = {num1-num2}")
                  case '3':
                      print(f"Result :- {num1} * {num2} = {num1*num2}")
                  case '4':
                   if(num2!=0):
                       print(f"Result :- {num1} / {num2} = {num1/num2}")
                   else:
                        print("Error:can not divide by zero")
              
                  case '5':print(f"Result :- {num1} % {num2} = {num1%num2}")
              
                  case _:print("Enter the Valid Number operation to Perform")
              
      except ValueError:
            print("Enter the valid Number")
            continue
            
    

calculator()    
