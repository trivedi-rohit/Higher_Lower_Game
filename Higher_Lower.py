import random
import os
import High_Low_DB
import High_Low_Art
print(High_Low_Art.logo)
score = 0

def display_dict(information):
    name = information["name"]
    description = information["description"]
    country = information["country"]
    return (f"{name} is a {description} from {country}.")

def check (guess, followers_1, followers_2):
    if followers_1 < followers_2:
        if guess == 1:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else:
            return False

choice_2 = random.choice(High_Low_DB.data)

flag_status= True
while flag_status:
    choice_1 = choice_2
    choice_2 = random.choice(High_Low_DB.data)
    while choice_1 == choice_2:
        choice_2 = random.choice(High_Low_DB.data)

    # Displaying random choices form database.
    print(f"Compare 1 : {display_dict(choice_1)}")
    print(High_Low_Art.text2ascii_art)
    print(f"Compare 2 : {display_dict(choice_2)}")

    # Guess which has more follower.
    guess = int(input("\nWho has more followers? Type '1' or '2' : "))

    #Fetch follower count from Database file (High_Low_DB).
    follower_count_1 = choice_1["follower_count"]
    follower_count_2 = choice_2["follower_count"]
    print(follower_count_1)
    print(follower_count_2)

    Is_correct = check(guess, follower_count_1, follower_count_2)
    os.system('cls')
    print(High_Low_Art.logo)
    if Is_correct == True:
        score += 1
        print(f"You are right. Your score is : {score}.\n")
    else:
        print(f"You are wrong. Your final score is {score}.\n")
        flag_status = False

