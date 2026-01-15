import random

words_list = ["utkirbek", "nice", "you","better"]

chosen_word = random.choice(words_list)
print(chosen_word)

placeholder = ""

len_word = len(chosen_word)





for position in range(len_word):
    placeholder += "_"
print(placeholder)

guess = input("Guess the letter: ").lower()
game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess the letter: ").lower()


    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You win!")

