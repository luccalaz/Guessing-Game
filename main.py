import random
import time

def getInput(guessNum, guesses):
    validInput = False
    
    # get input and error check
    while (not validInput):
        guess = input(f"Enter guess #{guessNum} between 1 and 100: ")
        if (not guess.isnumeric()):
            print("*** Invalid Input : Please try again...")
        elif (not int(guess) in range(1, 101)):
            print("*** Incorrect Input : Must be in range from 1 to 100...")
        elif (int(guess) in guesses):
            print("*** Invalid Input : Cannot enter the same guess twice...")
        else:
            validInput = True
            guesses.append(int(guess)) # keep track of previous guesses
            return int(guess)
        
def checkGuess(guessNum, guess, number):
    won = False

    # provide hints if wrong answer or display win message if correct answer
    if (guess > number and guessNum < 10):
        print(f"Guess #{guessNum} : {guess} - Lower!")
        print(f"-----------------------------------")
        won = False
    elif (guess < number and guessNum < 10):
        print(f"Guess #{guessNum} : {guess} - Higher!")
        print(f"-----------------------------------")
        won = False
    elif (guess == number):
        print(f"Guess #{guessNum} : {guess} - CORRECT!")
        print("YOU WIN!")
        won = True
    
    return won

def main():
    number = random.randint(1, 100) # generates a random number
    won = False
    guessNum = 0
    guesses = []

    print(f">>> {number}\nNumber Guessing Game -----------------------")
    # repeat the guess until user exceeded amount of guesses or won the game
    while (guessNum < 10 and not won):
        guessNum += 1
        guess = getInput(guessNum, guesses)
        won = checkGuess(guessNum, guess, number)

    if (not won):
        print("YOU LOSE! OUT OF ATTEMPTS!")

# runs the program infinitely without re-calling main() inside main() to avoid memory leak
while True:
    main()
    time.sleep(2) # wait 2 seconds before re-running