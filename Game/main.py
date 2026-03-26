import random

def play(): 
    choices = ['rock', 'paper', 'scissors'] 
    user_choice = input("Enter: rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("invalid choice. You know how rock, paper, scissors works, right?")
        return False

    print(f"you chose: {user_choice}")
    computer_choice = random.choice(choices)
    print(f"computer_chose: {computer_choice}")

    you_win = False
    if user_choice == computer_choice:
        print("Damn, It's a tie.")

    if (user_choice == "rock" and computer_choice == "scissors"):
        print("diggity, darn, damn, dang.. You win. how about one more?")
        you_win = True
    if (user_choice == "paper" and computer_choice == "rock"):
        print("Gr.. You're just getting lucky. Let's go again!")
        you_win = True
    if (user_choice == "scissors" and computer_choice == "paper"):
        print("Awh, I lost. Let's go again, I'll get You this time!")
        you_win = True
    if (user_choice == "" and computer_choice == ""):
        print("Screw you bro >:( I'll get you this time")
        you_win = True

    if(not you_win):
       print("haha, you lose!")

    return False

print("Welcome, to Rock, Paper, Scissors or exit")
finished = False
while not finished:
    finished = play()