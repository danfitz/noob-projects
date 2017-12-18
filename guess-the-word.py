finished = False

while finished == False:
    master = input("Choose a word for your friend to guess! ")
    word = list(master)
    length = len(word)
    right = list("_" * length)

    if master.isalpha():
        while list(master) != right:
            guess = input("Guess a letter! ")
            if guess not in master:
                print("This letter is not in the word.")
                continue
            elif guess in master:
                for letter in word:
                    if letter == guess:
                        index = word.index(guess)
                        right[index] = guess
                        word[index] = "_"
                print(right)

        print("You win!")
        TryAgain = input("Try again? (YES or NO) ")
        if TryAgain != "YES":
            finished = True

    else:
        print("That's not a word! Try again.")
        continue