# Description: A simple text-based adventure game where the player makes choices to navigate through a forest.
# Function to start the game
def start_game():
    print("Welcome to the Rocky Game!")
    print("You find yourself in a mysterious forest.")
    first_choice()
# Function to handle the first choice
def first_choice():
    print("\nDo you:")
    print("1. Explore the forest")
    print("2. Head towards the sound of water")
    choice = input("Enter 1 or 2: ")
   # Check user input and call the appropriate function 
    if choice == "1":
        explore_forest()
    elif choice == "2":
        sound_of_water()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        first_choice()
        # Function to explore the forest
def explore_forest():
    print("\nYou decide to explore the forest.")
    print("After walking for a while, you find a path that leads to a small village.")
    print("Do you:")
    print("1. Enter the village")
    print("2. Continue exploring the forest")
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        enter_village()
    elif choice == "2":
        continue_exploring()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        explore_forest()
# Function to head towards the sound of water
def sound_of_water():
    print("\nYou head towards the sound of water.")
    print("You find a river.")
    print("Do you:")
    print("1. Follow the river upstream")
    print("2. Follow the river downstream")
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        follow_upstream()
    elif choice == "2":
        follow_downstream()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        sound_of_water()
# Four different endings
# Function to enter the village
def enter_village():
    print("\nYou enter the village and find friendly villagers who offer you food and shelter.")
    print("Congratulations! You found a safe place to stay. The End.")
# Function to continue exploring the forest
def continue_exploring():
    print("\nYou continue exploring the forest but get lost.")
    print("Unfortunately, you couldn't find your way out. The End.")
# Function to follow the river upstream
def follow_upstream():
    print("\nYou follow the river upstream and find a beautiful waterfall.")
    print("You decide to settle here and live peacefully. The End.")
# Function to follow the river downstream
def follow_downstream():
    print("\nYou follow the river downstream and find yourself at the edge of a dangerous cliff.")
    print("You narrowly escape but decide it's best to return to the forest. The End.")

# Start the game
start_game()

