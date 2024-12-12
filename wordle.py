# Edward Joshua M. Diesta
# 241571
# September 29, 2024

# I have not discussed the Python language code in my program 
# with anyone other than my instructor or the teaching assistants 
# assigned to this course.

# I have not used Python language code obtained from another student, 
# or any other unauthorized source, either modified or unmodified.

# If any Python language code or documentation used in my program 
# was obtained from another source, such as a textbook or website, 
# that has been clearly noted with a proper citation in the comments 
# of my program.



from random import random
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
WORD_BANK = ["DERBY", "HAPPY", "SWOON", "FLOUR", "ALTER", "ALTAR", "SLEEP", "SEVEN", "EIGHT", "PARTY", "DRILL", "FIBRE", "DROVE", "GLASS", "DYING", "LIGHT"]
SIZE = 5



# Generate a clue, which is a string with either "?" if the letter is wrong, "!" if the letter is in the wrong position, and the actual letter if it is correct.
def generate_clue(guess_word, random_word):
    clue_list = ["?" for _ in range(SIZE)]

    # Step 1: Display the correct letters.
    for i in range(SIZE):
        if guess_word[i] == random_word[i]:
            clue_list[i] = guess_word[i]

    # Step 2: Iterate through the wrong letters and display "!" if the letter is just in the wrong position.
    marked_positions = [False for _ in range(SIZE)]
    for i in range(SIZE):
        if clue_list[i] == "?" or clue_list[i] == "!": # Filter to avoid correct letters.

            for j in range(SIZE):
                if clue_list[j] == "?" or clue_list[j] == "!": # Also a filter to avoid correct letters.
                    if i != j and guess_word[i] == random_word[j] and not marked_positions[j]:
                        marked_positions[j] = True
                        clue_list[i] = "!"
                        break
    
    # Turn the list into a string.
    clue = ""
    for letter in clue_list:
        clue += letter

    return clue

# Function to convert all letters into UPPERCASE (for case-insensitive purposes).
def convert_uppercase(word):
    new_word = ""

    for letter in word:
        found = False
        for uppercase_letter in UPPERCASE:
            if letter == uppercase_letter:
                new_word += letter
                found = True
                break
        
        if not found:
            i = 0
            for lowercase_letter in LOWERCASE:
                if letter == lowercase_letter:
                    new_word += UPPERCASE[i]
                    break
                i += 1

    return new_word

# Function to update all letters present in the word to "0" in the remaining_letters list.
def update_remaining_letters(remaining_letters, word):
    for letter in word:
        index = 0
        for remaining in remaining_letters:
            if letter == remaining:
                remaining_letters = remaining_letters[:index] + remaining_letters[index + 1:]
            index += 1

    return remaining_letters

# Prints the letters that remain unused.
def display_remaining_letters(remaining_letters):
    display = ""
    if len(remaining_letters) > 0:
        i = 0

        for letter in remaining_letters:
            display += letter

            if i != len(remaining_letters) - 1:
                display += " "

            i += 1
    else:
        display += "There are no more remaining letters that have not yet been guessed!"
    print("")
    print(display)



# This wordle game has all 6 add-ons.
while True:
    # Initialize the values of the remaining letters list.
    remaining_letters = [letter for letter in UPPERCASE]
    
    # Keeps asking for a random word until it is a length of 5 or until they input special words.
    random_word = ""
    while len(random_word) != SIZE and random_word != "QUIT" and random_word != "RANDOM":
        print("Please enter a word for the player to guess:")
        random_word = convert_uppercase(input())
        print("")

    # Handles QUIT and RANDOM, 2 special words with certain functions.
    if random_word == "QUIT": # Breaks out of the game.
        break
    elif random_word == "RANDOM": # Chooses a random word in the word bank.
        random_word = WORD_BANK[int(random() * len(WORD_BANK))]

    # Asks for input on how many guesses they prefer.
    guesses = 0
    while guesses <= 0:
        print("Enter how many guesses you prefer:")
        guesses = int(input())
        print("")
    
    # Initializes the win boolean and the clue string.
    win = False
    broken_out = False
    clue = "-----"

    # Runs a for loop depending on the amount of guesses they inputted.
    for attempt in range(guesses, 0, -1):
        guess_word = ""

        while True:
            print("Guess the word, " + str(attempt) + " guess(es) left: " + clue)
            guess_word = convert_uppercase(input())

            # If the word they inputted was "ALPHABET", show remaining letters and repeat the prompt.
            if guess_word == "ALPHABET":
                display_remaining_letters(remaining_letters)

            if guess_word == "QUIT":
                broken_out = True
                break
            
            # Break out of the loop if the inputted word is the correct SIZE.
            elif len(guess_word) == SIZE:
                break
            print("")

        if broken_out == True:
            break
        
        # Break out of the loop if the word is correct.
        if guess_word == random_word:
            win = True
            print("")
            break
        
        # Update the clue to be printed for the next iteration, and the remaining unused letters.
        clue = generate_clue(guess_word, random_word)
        remaining_letters = update_remaining_letters(remaining_letters, guess_word)
        print("")

    if broken_out:
        break

    # States if you win or not.
    if win:
        print("Congratulations! You win!")
    else:
        print("SORRY, YOU LOSE!")
    print("")
    