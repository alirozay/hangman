import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
word_list = []
guess_list = []
display = []
correct = False
# Check if inputs for insert are valid or not
word_list.append(input("Add the first word: "))
insert = input("Would you like to add more words?Type Y or N: ")
while insert.upper() != 'N':
    word = input("Input the word to be added to the list: ")
    word_list.append(word.lower())
    insert = input("Would you like to add more words? ")

chosen = random.choice(word_list)
print(f"Chosen word is {chosen}")
for i in range(len(chosen)):
    display.append('-')
print(''.join(display))
while '-' in display and lives != 0:
    print(stages[lives - 1] + "\n")
    user_guess = input("Enter your guess: ").lower()
    if user_guess in guess_list:
        print(f"You already guessed letter {user_guess} \n")
    else:
        for i in range(len(chosen)):
            if user_guess == chosen[i]:
                display[i] = user_guess
                correct = True

        if not correct:
            print("You lost a life")
            lives -= 1
    correct = False
    print("\n" + ''.join(display))
if lives != 0:
    print("You have won!")
else:
    print(f"\n The word was {chosen} \n You lost :(")
