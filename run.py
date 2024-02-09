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
        print("\nChoose a story to play:\n")
        story = input("\n1.The Castle\n2.The Plane\n3.The Night-Shift\n\nPlease enter (1, 2 or 3):")
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
            print("\nInvalid key. Please enter the (1/ 2 or 3) to select a story:")

def the_castle():
    loading = "\nYou have selected 'The Castle'"
    print(loading)
    """
    Each story will start by setting the scene
    Followed by a situation where the user needs to make a choice
    Options will be provided to the player
    The player will need to enter a valid key to select a choice and progress the story.
    """
    castle_set = "\nA Princess has been stolen away by a fire breathing Dragon in its lair as punishment to the King for not paying his yearly tribute.\n\nThe King has promised all the gold the dragon holds to the hero who rescues the Princess and brings her back to him.\n\n You have decided to embark on this bold quest to rescue the Princess and gain riches"
    print(castle_set)

    def replay():
        retry = "\nWould you like to retry? (y/n):"
        if retry == "y":
            the_castle(sit1)
        elif retry == "n":
            start_game()

    while True:
        sit1 = "\nYou arrive at the Dragons Lair in a shining metal armour, with a sword and shield in your hands. The lair is a big castle inside a mountain, you see the entrance guarded by 2 skeletons with swords\n"
        print(sit1)
        choice = input("\nDo you\n\na.Charge and fight the skeletons or\nb.Run away\n\nEnter here:")
        if choice == "a":
            print("You charge at the skeleton guards and they crumble from the hits of your mighty sword.")
            break
        if choice == "b":
            print("\nYou run away, leaving behind the Princess and the gold to the Dragon. Mission Failed.\n")
            retry = input("\nWould you like to retry? (y/n):")
            break
            if retry == "y":
                the_castle()
            elif retry == "n":
                start_game()
        #doesnt work - else:
            #print("\nInvalid key. Please enter the (a or b) to make a choice:")


start_game()
select_story()