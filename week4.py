import time

def introduction():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a dark forest. You must make choices to survive.")
    print("Each choice you make will determine your fate. Good luck!")

def make_choice(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def forest_path():
    print("You continue down the forest path.")
    time.sleep(2)
    print("You encounter a river. What will you do?")

    choice = make_choice("Choose your action:", ["Try to swim across", "Look for a bridge", "Follow the riverbank"])

    if choice == 1:
        print("You try to swim across the river but get swept away by the current. Game Over!")
    elif choice == 2:
        print("You find a sturdy bridge and safely cross the river.")
        print("You continue on your journey.")
    else:
        print("You follow the riverbank and discover a hidden treasure. You've won the game!")

def cave():
    print("You enter the dark cave.")
    time.sleep(2)
    print("You hear growling. What will you do?")

    choice = make_choice("Choose your action:", ["Investigate the source of the sound", "Retreat slowly"])

    if choice == 1:
        print("You find a friendly bear cub. You've made a new friend!")
        print("You continue your adventure.")
    else:
        print("You retreat safely from the cave.")
        print("You continue on your journey.")

def main():
    introduction()

    choice = make_choice("You come to a fork in the road. Will you go left or right?", ["Go left", "Go right"])

    if choice == 1:
        forest_path()
    else:
        cave()

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
