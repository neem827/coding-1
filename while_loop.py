# Loop - a loop is a construct (special function) that repeats itself
# In programming, a loop allows to repeat code instructctions

# There are two types of loops: for loop and while loop

# while lop - a type of loop where so long as a condition is equal
# to ture it will keep runing forever.

# the key word is while --> do while 

# syntax
num = 4
while 2+2 == num: # condtiion --> operations - must be ture
    # print(num == 4)
    print('the program is runing...')
    num = int(input("please type in a new number:"))

    #while loops will always run unless you change the condition!
    #we can do this by wrriting instructions to manually change it.


def vending_machine():
    # Define the vending machine menu using a dictionary
    menu = {
        "B3": "Nacho Chips",
        "G4": "BBQ Chips",
        "G7": "Plain Chips",
        "D3": "Water",
        "G5": "Cola Soda"
    }
    
    while :
        # Prompt the user for an item code or to quit
        user_input = input("Enter a vending machine code (or 'q' to quit): ").strip().upper()
        
        # Check if the user wants to end the loop
        if user_input == 'Q':
            print("Thank you for using the vending machine. Goodbye!")
            break
            
        # Check if the entered code exists in our menu
        if user_input in menu:
            print(f"Dispensing: {menu[user_input]}")
        else:
            print("Invalid code. Please try again.")
        
        print("-" * 30)  # Visual separator for the next loop iteration

# Run the function
if __name__ == "__main__":
    vending_machine()













import random

def dice_game():
    # Initialize the player's score
    score = 0
    
    print("Welcome to the Dice-Rolling Game!")
    print("Enter 'r' to roll or 'q' to quit.")
    
    while True:
        # Get user input and convert to lowercase to handle capitals smoothly
        choice = input("\nRoll or Quit? (r/q): ").strip().lower()
        
        if choice == 'q':
            print(f"Thanks for playing! Your final score is: {score}")
            break
            
        elif choice == 'r':
            # Generate a random number between 1 and 7
            roll = random.randint(1, 7)
            print(f"You rolled a: {roll}")
            
            # Check the win condition
            if roll == 7:
                score += 10
                print(f"Winner! You gained 10 points. Current score: {score}")
            else:
                score -= 5
                print(f"You lost 5 points. Current score: {score}")
                
        else:
            print("Invalid input. Please enter 'r' to roll or 'q' to quit.")

# To run the game, call the function:
# dice_game()