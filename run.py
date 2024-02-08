Introduction = "Welcome to Adventure Line!\n\nYour are in control of what happens in these stories.\n\nThe choices you make will affect the plot but BEWARE, there are dangers and you must decide which choice to make.\nThe wrong decision could end in disaster - or even DEATH.\n"
print(Introduction)

def start_game():
    """
    Get command from user to start game from user.
    User to select the story they want to play.
    """
    while True:
        start = input("Start Game? (y): ")
        if start == "y":
                break
        else:
            print("\nInvalid key. Please enter the (y) to start game")

def select_story():
    """
    Game provides stories available to play for the user.
    User needs to select which story to play to start a game.
    """
    while True:
        story = input("\nChoose a story to play:\n\n1.The Castle\n2.The Plane\n3.The Night-Shift\n\nPlease enter (1, 2 or 3):")
        if story == "1":
            the_castle()
            break
        elif story == "2":
            game_2()
            break
        elif story == "3":
            game_3()
            break
        else:
            print("\nInvalid key. Please enter the (1/ 2 or 3) to select a story")

def the_castle():
    loading = "\nYou have selected 'The Castle'"
    print(loading)

    castle_set = "\nThe kingdom of Pythonland needs your help! The evil Lord Evilton has stolen the King's gold, and we need your help to get it back!"
    print(castle_set)

start_game()
select_story()