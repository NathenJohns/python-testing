# guessing game

secret_word = "lion"
guess = ""
attempts = 0
attempt_limit = 2
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if attempts < attempt_limit:
        attempts += 1
        guess = input("Enter guess: ")
        if attempts < attempt_limit:
            print("You have one guess left")
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE! The answer was " + secret_word)
else:
    print("You Win!")