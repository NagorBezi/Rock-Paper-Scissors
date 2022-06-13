import random

print("Welcome to rock, paper, scissors!")
print()

while True:
    user_choice = input("Rock/Paper/Scissors: ").lower().strip()
    print()
    print("Processing...")
    com_choice_num = random.randint(1, 3)
    com_choice = None

    if com_choice_num == 1:
        com_choice = 'rock'

    if com_choice_num == 2:
        com_choice = 'paper'

    if com_choice_num == 3:
        com_choice = 'scissors'

    print()
    print(f"Computer chose {com_choice}")
    print()
    
    if user_choice == com_choice:
        print("Tie!")

    if user_choice == 'scissors' and com_choice == 'paper':
        print("Human Wins!")

    if user_choice == 'scissors' and com_choice == 'rock':
        print("Computer Wins!")

    if user_choice == 'paper' and com_choice == 'rock':
        print("Human Wins!")

    if user_choice == 'paper' and com_choice == 'scissors':
        print("Computer Wins!")

    if user_choice == 'rock' and com_choice == 'scissors':
        print("Human Wins!")

    if user_choice == 'rock' and com_choice == 'paper':
        print("Computer Wins!")

    print()
