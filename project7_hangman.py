from hangman_art import stages,logo
from hangman_words import word_list
import random
import os 


def genrerate_word():
    return random.choice(word_list)

def check_answer(g_letter,chosen_word,lives,display):
    if g_letter in display:
        print("You have already entered the letter, try another!")
        return lives
    elif g_letter not in chosen_word:
        print("You have entered wrong word! You will lose a life!")
        return lives -1
    else:
        for i in range (len(chosen_word)):
            if chosen_word[i] == g_letter:
                display[i] = g_letter
        return lives
    

chosen_word = genrerate_word()
word_length = len(chosen_word)
display = []
for i in range(word_length):
    display +="_"
game_is_on = True
lives = 6
    

print(logo)
while game_is_on:
    guessed_letter = input("Guess a letter: ").lower()
    lives = check_answer(guessed_letter,chosen_word, lives, display)
    print(stages[lives])
    print(f"{' '.join(display)}")
    if "_" not in display:
        print(f"You won in the game\nFinal word is {chosen_word}")
        game_is_on = False
    elif lives == 0:
        print("You lose in the game!!")
        want_to_play_again = input("Want to play again! Yes or No: ").lower()
        if want_to_play_again =="yes":
            os.system('cls')
            print(logo)
        else:
            game_is_on = False

   
    

         
