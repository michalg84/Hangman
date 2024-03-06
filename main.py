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



for _ in word:
    user_word.append("_")

while True:
    letter = input("Enter a letter: ")
    used_letters.append(letter)
    indexes = find_indexes(word, letter)
    if len(indexes) == 0:
        print("No such letter")
        no_of_tries -= 1
        print("No of tries left:", no_of_tries)
        if(no_of_tries == 0):
            print("Game Over")
            sys.exit(0)
    else:
        for index in indexes:
            user_word[index] = letter
        if("".join(user_word) == word):
            print("That's correct!: ", word)
            sys.exit(0)

    print("Used letters:", used_letters)
    print("".join(user_word))