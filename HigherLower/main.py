#Higher Lower
import random
import game_data
data = game_data.data
#Welcome script
print("Welcome to Higher Lower, the game where we find out who has more followers!")
#make a function that populates the people to compare
def get_random_account():
    return random.choice(data)

def sort_account_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

#Make a function that compares the 2 - If right the correct answer becomes option A and we recycle the correct choice
def compare(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    score = 0
    game_should_continue=True
    account_a = get_random_account()
    account_b = get_random_account()
    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {sort_account_data(account_a)}")
        print("vs")
        print(f"Compare B: {sort_account_data(account_b)}")

        guess = input("Who has more followers? Type 'a' or 'b'.")
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        isCorrect = compare(guess, a_follower_count, b_follower_count)

        if isCorrect:
            score +=1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()
# Track user score

