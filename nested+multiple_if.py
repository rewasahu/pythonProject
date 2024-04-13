print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age=int(input("What is your age? "))
bill=0
if height > 120:
  print("you can ride the rollercoaster")
  if age<12:
    bill=5
    print(f"Your bill is ${bill}.")
  elif age<=18:
    bill=7
    print(f"Your bill is ${bill}.")
  else:
    bill=12
    print(f"Your bill is ${bill}.")
    
  wants_photo=input("Do you want a photo taken? Y or N ")
  if wants_photo=="Y":
    bill=bill+3
  print(f"Your bill is ${bill}.")
    
else:
  print("you are not allowed to ride the rollercoaster")