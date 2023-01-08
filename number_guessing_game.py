import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "hard":
    attempts = 5
else:
    attempts = 10

import random
number = random.randint(1, 100)
print(number) 

# If can change the while loop to function
while True:
    for i in range(attempts):
        print(f"You have {attempts-i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {guess}")
            break
        else:
            if guess > number:
                print("Too High.")
            else:
                print("Too Low.")
            if i != attempts-1:
                print("Guess again.")
    if guess != number:
        print("You are run out of guesses. You lose.")
    break
    
    
      

