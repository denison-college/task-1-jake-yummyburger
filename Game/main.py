import random

def play(): 
    choices = ['rock', 'paper', 'scissors'] 
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("invalid choice. You know how rock, paper, scissors works right?")
        return

    print(f"you chose: {user_choice}")
    computer_choice = random.choice(choices)
    print(f"computer_chose: {computer_choice}")

    if user_choice == computer_choice:
        print("Damn, It's a tie.")



if __name__ == "__main__":
    play()
