import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
directory = []
highest_bid = 0

def new_person(person_name, bid_amount):
    details = {}
    details['name'] = person_name
    details['amount'] = bid_amount
    directory.append(details) 

bid_continue = True
print(logo)
print("Welcome to the secret auction program!!")
while bid_continue:
    person_name = input("What is your name?: ").upper()
    bid_amount = int(input("What is your bid?: "))
    new_person(person_name,bid_amount)
    more_person = input("Is there any other person for bidding? Type Yes or No: ").lower()
    os.system('cls')
    if more_person == "no":
        bid_continue = False
for i in directory:
    if i['amount'] >= highest_bid:
        highest_bid = i['amount']
        highest_bidder = i['name']
print(f"The winner is {highest_bidder} with bid amount of ${highest_bid}.")
print(directory)

