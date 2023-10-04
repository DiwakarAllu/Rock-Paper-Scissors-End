
import random

# Define the game images
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
choices = ["Rock", "Paper", "Scissors"]

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (
        (user_choice == 0 and computer_choice == 2)
        or (user_choice == 1 and computer_choice == 0)
        or (user_choice == 2 and computer_choice == 1)
    ):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "You lose!"

# Main game loop
while True:
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
    
    if user_choice < 0 or user_choice > 2:
        print("Invalid choice. Please choose again.")
        continue

    print("You chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    result = determine_winner(user_choice, computer_choice)
    print(result)

    print(f"Your score: {user_score} | Computer's score: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing!")

