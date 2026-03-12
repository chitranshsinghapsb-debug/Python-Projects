import art
import random
print(art.logo_day12)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
e_or_h = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
ans = random.randint(1,100)
no_of_attempts = 0
if e_or_h == "easy":
    no_of_attempts = 10
elif e_or_h == "hard":
   no_of_attempts = 5
else :
    e_or_h = 0
    print("Invalid Input:")

print(f"You have {no_of_attempts} attempts remaining to guess the number.")

lost = True
while no_of_attempts > 0:
    user_guess = int(input("Make a Guess: "))
    if(user_guess > ans):
        print("Too high.")
        no_of_attempts-=1
        print(f"You have {no_of_attempts} attempts remaining to guess the number.")
    elif(user_guess < ans):
        print("Too low.")
        no_of_attempts-=1
        print(f"You have {no_of_attempts} attempts remaining to guess the number.")
    else:
        print(f"You got it! The answer was {ans}.")
        lost = False
        no_of_attempts = 0
    
if lost == True:
    print("You've run out of guesses. Refresh the page to run again.")
    print(f"The correct number was {ans}.")        
        

   