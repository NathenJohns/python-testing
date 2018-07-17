print("Welcome to my quiz")

score = 0

question1 = input("Who is the current Prime Minister?: ")
answer1 = "Theresa May"

if question1 == answer1:
    score += 1
    print("Correct")
elif question1 != answer1:
    print("Incorrect. You have one attempt remaining.")
    
    
question2 = input("What is the capital of France?: ")
answer2 = "Paris"

if question2 == answer2:
    score += 1
    print("Correct")
elif question2 != answer2:
    print("Incorrect")

question3 = input("What is the closest planet to the Sun?: ")
answer3 = "Mercury"

if question3 == answer3:
    score += 1
    print("Correct")
elif question3 != answer3:
    print("Incorrect")

question4 = input("What currency does the US use?: ")
answer4 = "Dollar"

if question4 == answer4:
    score += 1
    print("Correct")
elif question4 != answer4:
    print("Incorrect")

question5 = input("What is the biggest ocean on planet Earth?: ")
answer5 = "Pacific"

if question5 == answer5:
    score += 1
    print("Correct")
elif question5 != answer5:
    print("Incorrect")
   
print("Thanks for playing. Your score was: " + str(score) + " out of 5") 