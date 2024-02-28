
no_of_tries = 5
expected_word = "Guess me"

user_letters = []
used_letters = []


for _ in expected_word:
    user_letters.append("_")

while True:
    letter = input("Enter a letter: ")
    used_letters.append(letter)

    print(user_letters)
