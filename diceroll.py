# Write a python code to simulate dice roll
import random

def roll_dice():
    # Simulate rolling a dice by generating a random number between 1 and 6
    return random.randint(1, 6)


while True:
    input("Press Enter to roll the dice...")
    dice_value = roll_dice()
    print(f"You rolled a {dice_value}!")
    
    # Ask the user if they want to roll again
    roll_again = input("Do you want to roll again? (yes/no): ").lower()
    if roll_again != 'yes':
        print("Thanks for playing!")
        break

