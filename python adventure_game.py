# Text-Based Adventure Game
# Tuple for fixed locations
locations = ("Forest", "Cave", "River", "Treasure Room")

# List for storing player items
inventory = []
# Player health
health = 100

def start_game():
    print("===== Welcome to the Adventure Game =====")
    name = input("Enter your name: ")
    print("Hello", name, "! Your quest is to find the hidden treasure.")
    print("You are standing at the", locations[0])
    forest()


def forest():
    while True:
        print("\nYou are in a dark forest.")
        print("1. Go Left (towards a cave)")
        print("2. Go Right (towards a river)")
        print("3. Check Inventory")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            cave()
            break
        elif choice == "2":
            river()
            break
        elif choice == "3":
            print("Inventory:", inventory)
        else:
            print("Invalid choice. Try again.")


def cave():
    print("\nYou entered the", locations[1])

    if "torch" not in inventory:
        print("You found a torch!")
        inventory.append("torch")

    if "sword" not in inventory:
        print("You found a sword!")
        inventory.append("sword")

    print("Inside the cave you see a door to the treasure room.")
    choice = input("Do you want to enter? (yes/no): ")

    if choice.lower() == "yes":
        treasure_room()
    else:
        forest()


def river():
    global health
    print("\nYou reached the", locations[2])
    print("A monster appears!")

    choice = input("Do you want to fight or run? (fight/run): ")

    if choice.lower() == "fight":
        if "sword" in inventory:
            print("You defeated the monster!")
            print("You found a key!")
            inventory.append("key")
            forest()
        else:
            print("You have no weapon!")
            print("The monster attacked you.")
            health -= 50
            print("Health:", health)

            if health <= 0:
                print("You died. Game Over.")
            else:
                forest()

    elif choice.lower() == "run":
        print("You ran back to the forest.")
        forest()

    else:
        print("Invalid choice.")
        river()


def treasure_room():
    print("\nYou entered the", locations[3])

    if "key" in inventory:
        print("You used the key to open the treasure chest!")
        print("Congratulations! You found the treasure and won the game!")
    else:
        print("The treasure chest is locked.")
        print("Find the key first.")
        forest()


# Start the game
start_game()