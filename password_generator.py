import random
import string

try:
    lenOfpass=int(input("enter the length to the password you want:"))
    
except ValueError:
    print("invalid input...please enter the length at least 8" )
    
uppercaselatter=string.ascii_uppercase
lowercaselatter=string.ascii_lowercase
digit=string.digits
symbol=string.punctuation
alLetters=uppercaselatter+lowercaselatter+digit+symbol
password=""

upper_case,lower_case,number,special_char=False,False,False,False

if lenOfpass<8:
        print("The Password length must be at least 8 ")
else:
  for i in range(lenOfpass):
     password+=random.choice(alLetters)

# to verify the password is strong or not

  for char in password:
      if char.isupper():
          upper_case=True
      elif char.islower():
          lower_case=True
      elif char.isdigit():
          number=True
      elif char in symbol:
          special_char=True

          
  if all([upper_case,lower_case,number,special_char]):
      print("The Password Is Strong")
  elif all([upper_case,lower_case,number,special_char]):
      print("The Password Is Medium")
  else:
      print("The Password Is Weak")
     
  print("The Password:",password)




