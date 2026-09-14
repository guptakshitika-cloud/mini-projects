import random
x=random.randint(1, 10)
z = True
while z == True: 
  y = input("enter your guess (must be between 1 to 10): ")
  try:
    if float(y) in range(1,11):
      if float(y) == x:
        z = False
        print("correct!")
      else:
        print("Wrong! Try again")
    else:
      print("Invalid input!")
  except:
      print("Invalid input!")
