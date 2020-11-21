# Write your code here

import random
import string

lis = ['python', 'java', 'kotlin', 'javascript']
print('H A N G M A N')
input('Type "play" to play the game, "exit" to quit:')


random_choice = random.choice(lis)
alphabet = set(string.ascii_lowercase)
alphabet_upper = set(string.ascii_uppercase)
signs = set('();:+-=!@£$%^&*-\|~`?<''>.0123/456789,}{]["#¢∞§¶•ª_º€¡').union(set("'"))
word_letters = set(random_choice)
used_letters = set()
lives = 8

while len(word_letters) > 0 and lives > 0:
    word_list = [letter if letter in used_letters else '-' for letter in random_choice]
    final_word = ''.join(word_list)
    print()
    print(final_word)
    user_letter = input("Input a letter: ")

    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
        else:
            lives -= 1
            print("That letter doesn't appear in the word")

    elif user_letter in used_letters:
        print("You've already guessed this letter")
    elif user_letter in alphabet_upper or user_letter in signs:
        print("Please enter a lowercase English letter")
    elif user_letter not in alphabet:
        print("You should input a single letter")

if lives == 0:
    print("You lost!")
else:
    print(random_choice)
    print("""You guessed the word!
You survived!""")



