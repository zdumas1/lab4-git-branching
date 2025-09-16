def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("You grab the sword. You hear a growling in front of you. Somewhere within the forest.")
    print("A dog runs out of the forest, followed by a GIANT BEAST!!")
    print("You challenge the beast, having courage with your new weapon. The beast is slain")
    print("You walk away with both a new friend and a new weapon")
def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

if __name__ == "__main__":
    intro()
