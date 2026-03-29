from art import logo_day14, vs
from game_data import data
import random

def format_account(account):
     
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return f"{account_name} , a {account_description} , from {account_country}."

def check_ans(user_guess,a_followers,b_followers):

    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
    
print(logo_day14)
score = 0
game_over = False
account_b = random.choice(data)

while not game_over:

    account_a = account_b
    account_b = random.choice(data)
    
    choice_diff = False
    while not choice_diff:
        if account_a == account_b:
            account_b = random.choice(data)
        else:
            choice_diff = True
    
    print(f"Compare A: {format_account(account_a)}")
    print(vs)
    print(f"Against B: {format_account(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B':").lower()

    print("\n" * 20)
    print(logo_day14)

    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]
    
    is_correct = check_ans(guess,a_followers_count,b_followers_count)

    if is_correct:
        score+=1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"You're wrong! Final score: {score}.")
        game_over = True


