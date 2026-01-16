import random

words_list = ["utkirbek", "nice", "you","better"]
lives = 6
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
    print(f"{lives}lives left!")
    guess = input("Guess the letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed {guess}")


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


    if guess not in chosen_word:
        lives -= 1
        print(f"you already guessed {guess}")

        if lives == 0:
            game_over = True
            print(f"You lost! it was {chosen_word}")
    #         fjsd

    if "_" not in display:
        game_over = True
        print("You win!")

