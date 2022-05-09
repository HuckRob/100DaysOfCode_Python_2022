#Step 5

import random
import hangman_art
import hangman_words

#Pick a random word from hangman_words.py 
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
previous_guessed_letters = []

#import and display the logo from hangman_art.py
print(hangman_art.logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #if the user enters the same guess as before let them know and let them try again
    if guess in previous_guessed_letters:
        
        print(f"You have already guessed{guess}")
        print(f"Previous Guesses: \n {previous_guessed_letters}")
        print("Try Again!")
        
    else:
        
        previous_guessed_letters.append(guess)
        
        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            #Debuging
            #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

        #Check if user is wrong.
        if guess not in chosen_word:
            print("Your guess is not in the chosen word.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #import art from hangman_art.py and display current stage
    print(hangman_art.stages[lives])