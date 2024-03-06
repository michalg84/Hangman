import sys

no_of_tries = 5
word = "Guess me"

used_letters = []
user_word = []


###
def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word, in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes



#init
for _ in word:
    user_word.append("_")


def noHit(found_letter_indexes):
    return len(found_letter_indexes) == 0


def no_tries_left():
    return no_of_tries == 0


# Main app flow
while True:
    letter = input("Enter a letter: ")
    used_letters.append(letter)
    found_letter_indexes = find_indexes(word, letter)

    if noHit(found_letter_indexes):
        print("No such letter")
        no_of_tries -= 1
        print("Number of tries left:", no_of_tries)
        if no_tries_left():
            print("Game Over")
            sys.exit(0)
    else:
        for index in found_letter_indexes:
            user_word[index] = letter
        if("".join(user_word) == word):
            print("That's correct!: ", word)
            sys.exit(0)

    print("Used letters:", used_letters)
    print("".join(user_word))