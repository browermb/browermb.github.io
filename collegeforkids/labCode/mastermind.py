import random

def validateInput():
    inputGuess = input("Enter your guess as 4 letters e.g. XXXX:")

    while True:
        if len(inputGuess) != 4:
           inputGuess = input("Enter your guess as 4 letters e.g. XXXX:")
        else:
            wordList = list( inputGuess.upper() )

            invalidLetters = False
            for letter in wordList:
                if letter not in ['R','G','Y','B','W']:
                    invalidLetters = True 


            #Check if invalidLetters is True
                print("Possible colours are R G Y B W")
                inputGuess = input("Enter your guess as 4 letters e.g. XXXX:") 

            else:
                return wordList

guessesRemaining = 12
code = []
guess = []
correctPosition = 0
correctColour = 0

#Loop 4 times (use i)
    code.append(random.choice(['R','G','Y','B','W']))

print("Guess my sequence of four colours, in the correct order.")
print("\nPossible colours are R G Y B W")

while guessesRemaining > 0:

    correctPosition = 0
    correctColour = 0
    lettersChecked = []

    guess = validateInput()
    guessesRemaining -= 1 # Deduct one guess

    tempGuess = list(guess)
    tempCode = list(code)


    #Loop 4 times (use i)
        if guess[i] == code[i]:
            correctPosition += 1
            tempGuess[i] = "X"
            tempCode[i] = "X"

    #Loop 4 times (use j)

        if tempGuess[j] in tempCode and tempGuess[j] != "X" and tempGuess[j] not in lettersChecked:

            if tempCode.count(guess[j]) > tempGuess.count(tempGuess[j]):
                correctColour += tempGuess.count(tempGuess[j])

            else:
                correctColour += tempCode.count(tempGuess[j])

            lettersChecked.append(tempGuess[j])

    #if correct position is greater than 0
        print("You had",correctPosition,"correct colours in the correct place")
    
    #if correct color is greater than 0
        print ("You had",correctColour,"correct colours in the wrong place")

    #if correct position and correct color are equal to 0
        print("No correct colours")

    #if correct position is equal to 4
        print("You won in",12-guessesRemaining,"guesses, congratulations!")
        guessesRemaining = 0

print("Thanks for playing")