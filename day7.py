# def greet(name):
#     print(f"{name}, I am feeling light headache!")
#     print(f"{name}, No one gonna believe in you unless you do")
#     print(f"{name}, when people look at you, believe in you, stay confident")
#
# greet("Jack")

# def greer_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
#
# greer_with("Jack", "Warsaw")
#
#
# greer_with(location="Uzbeksitan", name="Utkirbek")


# PROJECT

alphabet = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s",
    "t", "u", "v", "w", "x", "y", "z"
]
# def encrpty(original_text, shift_amount):
#     cipher_text = ""
#
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#
#     print(f"Here is the encoded result: {cipher_text}")
#
# def decrpyt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#
#         shifted_position %= len(alphabet)
#
#         cipher_text += alphabet[shifted_position]
#
#     print(f"Here is the decrpted result: {cipher_text}")

def ceaser(original_text, shift_amount, encode_or_decode):
        cipher_text = ""
        if encode_or_decode == "decode":
            shift_amount *= -1

        for letter in original_text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                shifted_position = alphabet.index(letter) + shift_amount

                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]

        print(f"Here is the {encode_or_decode}d result: {cipher_text}")





continue_text = True

while continue_text:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n ").lower()
    text = input("Type your message \n").lower()
    shift = int(input("type the shift number: \n"))

    ceaser(text, shift, direction)

    restart = input("Type 'yes' if you want to continue type 'no' if you don't want to \n").lower
    if restart == "no":
        continue_text = False
        print("Goodbye")



