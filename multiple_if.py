print("Thank you for choosing Python Pizza Deliveries!")
size = input() 
add_pepperoni = input() 
extra_cheese = input() 

bill=0
if size=="L":
  bill=25
  if add_pepperoni=="Y":
    bill=+3
elif size=="M":
  bill=20
  if add_pepperoni=="Y":
    bill=+3
else:
  bill=15
  if add_pepperoni=="Y":
    bill=+2
if extra_cheese=="Y":
  bill=+1
print(f"Your final bill is: ${bill}")