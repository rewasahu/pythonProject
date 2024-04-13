rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lst = [rock,paper,scissors]

c_score=0
u_score=0

import random
import os
def computer_choice():
    comp=random.randint(0,2)
    return comp
def check_answer(comp,user):
    if user==comp:
        print("It's a tie")
        return 
    elif (user==0 and comp==2) or (user==1 and comp==0) or (user==2 and comp==1):
        print('You Win!')
        return True
    else:
        print('You Lose!')
        return False
    
   
game_end = False
while not game_end:   
    user = int(input("What do you choose?\nType 0 for 'Rock', 1 for 'Paper' or 3 for 'Scissors\n"))
    comp=computer_choice()
    print(f"{lst[comp]}\nComputer Choice:")
    print(f"{lst[user]} \nUser Choice:")        
    if check_answer(comp,user)==True:
        u_score+=1
    elif check_answer(comp, user)==False:
        c_score+=1
    else:
        u_score,c_score
    print(f"Computer Score: {c_score} vs User Score: {u_score}")

    want_to_contiue=input("Would you want to play more? type 'Y for yes or 'N' for exit").lower()
    if want_to_contiue=='y':
        os.system('cls')
        
    else:
        game_end=True
        if u_score>c_score:
            print("Finally You Win!")
        else:
            print("Finally You Lose!!")
        print("Thanks for playing!!")
        

        




