# import random

# cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
# user_cards=[]
# computer_cards=[]

# def deal_cards():
#     return random.choice(cards)

# def calculate_score(cards):
#     if sum(cards)==21 and len(cards)==2:
#         return 0
#     if 11 in cards and sum(cards)>21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)

# def compare(user_score, computer_score):
#     if computer_score==user_score:
#         print("Both have same cards, match DRAW")
#     elif user_score==0:
#         print("You have a black jack, YOU WIN !!")
#     elif computer_score==0:
#         print("Compter has a blackjack, You Lose !!")
#     elif user_score>21:
#         print("You went over, You Lose !!")
#     elif computer_score>21:
#         print("Computer went over, You WIN !!")
#     elif user_score>computer_score:
#         print("YOU WIN !!")
#     else:
#         print("You Lose !!")

# for n in range(2):
#     user_cards.append(deal_cards())
#     computer_cards.append(deal_cards())

# is_game_over=False
# while not is_game_over:
#     user_score=calculate_score(user_cards)
#     computer_score=calculate_score(computer_cards)
#     print(f"Users cards are {user_cards} and Score is {user_score}")      
#     print(f"Computer's first card is {computer_cards[0]}")
#     if user_score==0 or computer_score==0 or user_score>21:
#         is_game_over=True
#     else:
#         more_draw=input("want to draw more, type y for more or type n to pack: ").lower()
#         if more_draw=="y":
#             user_cards.append(deal_cards())
#         else:
#             is_game_over=True

# while computer_score!=0 and computer_score<17:
#     computer_cards.append(deal_cards())
#     computer_score=calculate_score(computer_cards)

# print(f"Your final hand is {user_cards}, Score: {user_score}")
# print(f"Computer final hand is {computer_cards}, Score: {computer_score}")
# print(compare(user_score,computer_score))

import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = []
comp_cards = []
game_is_on = True

def deal_cards():
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0

    if sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(comp_score, user_score):
    if comp_score==user_score:
        return "It's a draw"
    elif user_score==0:
        return "You got blackjack,  You Win!!"
    elif comp_score==0:
        return "Computer got blackjack, You Lose!!"
    elif user_score>21:
        return 

def game():
    print(logo)
    print("Welcome to the Blackjack game!!")
    for i in range(2):
        user_cards.append(deal_cards())
        comp_cards.append(deal_cards())
    
    while game_is_on:
        user_score= calculate_score(user_cards)
        comp_score= calculate_score(comp_cards)
        print(f"Your cards are {user_cards}, score = {user_score}.")
        print(f"Computer first card is {comp_cards[0]}")

        if user_score == 0 or comp_score==0 or user_score>21:
            game_is_on =False
        else:
            want_to_draw =input("Want to draw more? Type 'Y' or 'N': ").lower()
            if want_to_draw=='y':
                user_cards.append(deal_cards)
            else:
                game_is_on= False

    while comp_score<17:
        comp_cards.append(deal_cards)



        







    