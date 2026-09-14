import random
x=random.randint(1, 10) #picking a random number between 1 and 10
z = True
while z == True: 
  y = input("enter your guess (must be between 1 to 10): ") #accepting user input
  try:
    if float(y) in range(1,11): #type conversion and checking whether the input is valid
      if float(y) == x: #what happens if the guess is correct
        z = False
        print("correct!") 
      else:
        print("Wrong! Try again")
    else:
      print("Invalid input!")
  except:
      print("Invalid input!")
