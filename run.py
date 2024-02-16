import random

# Randomise names in the story each time it's played
dragon_names = ["Baal", "Samael", "Falkor"]
king_names = ["King Oswald", "King Offa", "King Darius"]
princess_names = ["Hera", "Medea", "Lucilla"]
kingdom_names = ["Resenbol", "Aksum", "Adina"]

dragon = random.choice(dragon_names)
king = random.choice(king_names)
princess = random.choice(princess_names)
kingdom = random.choice(kingdom_names)


def start_game():
    print("\n\nWelcome to Adventure Line!\n")
    print("Your are in control of what happens in these stories.")
    print("The choices you make will affect the plot......but BEWARE,")
    print("there are dangers and you must decide which choices to make.")
    print("The wrong decision could end in disaster - or even DEATH.\n")
    """
    Get command from user to start game from user.
    to start the game and move to select the story they want to play.
    """
    while True:
        start = input("Start Game? (y): ")
        if start == "y":
            select_story()
        else:
            print("\nInvalid key. Please enter the (y) to start game")


def select_story():
    """
    Here the game will provide the stories available to play for the
    user. At the moment there is 1 story available to play.
    User needs to select which story to play to start a game.
    """
    while True:
        print("\nChoose a story to play:\n")
        story = input("\n1. The Castle\n\nPlease enter (1): ")
        if story == "1":
            the_castle()
            break
        else:
            print("\nInvalid key.")
            print("Please enter the (1/ 2 or 3) to select a story: ")


def game_over():
    """
    This function will appear whenever a players Lives reaches "0".
    This will give option for players to either try again from the
    start of story or go back to the main menu.
    """
    while True:
        print("\n\nYou have run out of lives")
        retry = input("Would you like to retry the story? (y/n): ")
        if retry == "y":
            the_castle()
        elif retry == "n":
            start_game()
    else:
        print("\nInvalid key.")
        print("Please enter a valid option to make a choice (y/n): ")


def game_end():
    """
    This function will appear when a player makes it to the end of a story.
    It congratulates the player and provides the option to either play the
    story again for the alternative ending or to go back to the main menu.
    """
    while True:
        print("\nCongratulations! You made it to the end of the story!")
        print("We hope you are happy with the ending you have chosen.\n")
        print("\nWould you like to play again or go back to the main menu?")
        end = input("(y/n)\n\nEnter here: ")
        if end == "y":
            the_castle()
        elif end == "n":
            start_game()
    else:
        print("\nInvalid key.")
        print("Please enter a valid option to make a choice (y/n): ")


def the_castle():
    """
    Each story game will start by setting the story
    followed by a scene where the user needs to make a choice
    Options will be provided to the player.
    The player will need to enter a valid key to select a choice and
    progress the story.
    If the incorrect decision is made, the player will lose a life
    and points. If the player reaches "0" lives, the game will end.
    """
    castle_select = "\nYou have selected 'The Castle'"
    print(castle_select)

    # Keeps record users lives and points
    lives = 3
    points = 0

    print("\nThe story:")
    print(f"In the Kingdom of {kingdom}, Princess {princess} has been")
    print(f"stolen away by a fire breathing dragon called {dragon}, taking")
    print(f"her back to its lair as punishment to {king} for not paying")
    print(f"his yearly tribute. {king} has promised all the treasure")
    print(f"and gold that {dragon} holds to the hero who rescues")
    print(f"Princess {princess} and brings her back to him.")
    print("You have decided to embark on this daring")
    print(f"quest to rescue the Princess {princess} and gain riches.\n")

    # Slow down the amount of information the user is receving on screen
    while True:
        lives_points = input("\nContinue? (y): ")
        if lives_points == "y":
            break
        else:
            print("\nInvalid key. Please enter (y) to continue: \n")

    # Explain lives and points
    while True:
        print(f"\nYou have {lives} lives. If you fail three times, the game")
        print("will be over.")
        print("You will accumulate points depending on the decisions you make")
        print("but will lose points if you make the incorrect decision.")
        print("You should try and get the highest points possible")
        start_game = input("\nContinue? (y): ")
        if start_game == "y":
            break
        else:
            print("\nInvalid key. Please enter (y) to continue: \n")

    # Game starts here
    while True:
        # Scene 1
        print("\nScene 1\n")
        print("\nYou arrive at the dragon’s lair in a shining metal armour,")
        print("with a sword and shield in your hands.")
        print("The lair is a big castle inside a mountain, you see the")
        print("entrance guarded by 2 skeletons with swords.\n")
        print("Do you\n\na. Charge and fight the skeletons or\nb. Run away\n")
        choice1 = input("Enter here: ")
        if choice1 == "b":
            points -= 50
            lives -= 1
            print(f"\nYou run away, leaving behind Princess {princess}")
            print(f"and the gold to {dragon}. Mission Failed.\n\n")

            print("\n-1 life")
            print(f"You have {lives} remaining life")
            print("\nTry again")
            if lives == 0:
                game_over()
            continue
        elif choice1 == "a":
            points += 100
            print("\nYou charge at the skeleton guards, swinging your sword.")
            print("They crumble from the slashes of your mighty sword.\n\n")
            break
        else:
            print("\nInvalid key.")
            print("Please enter a valid option to make a choice: \n")

    # Scene 2
    print(f"Lives: {lives}")
    print(f"Points: {points}")
    print("\nScence 2\n")
    while True:
        print("\nYou enter the castle and see a set of stairs going up to a")
        print("tower and another set of stairs going down into a dungeon.\n")
        print("Do you\n\na. Go up the tower or")
        print("b. Go down into the dungeon\n")
        choice2 = input("\nEnter here: ")
        if choice2 == "b":
            lives -= 1
            points -= 50
            print("\nYou run down, into the darkness of the dungeon...")
            print("You suddenly find yourself falling into a pit of emptiness")
            print("and spikes pierce your body as you meet the bottom.")
            print("You die.\n")

            print("-1 life")
            print(f"You have {lives} remaining life")
            print("Try again")
            if lives == 0:
                game_over()
            continue
        elif choice2 == "a":
            print("\nYou go up the winding stairs of the tower and found")
            print("yourself in front 3 closed doors.\n")
            points += 100
            break
        else:
            print("\nInvalid key.")
            print("Please enter a valid option to make a choice: \n")

    # Scene 3
    print(f"Lives: {lives}")
    print(f"Points: {points}")
    print("\n\nScene 3")
    while True:
        print("\nYou need to decide which door to go through.\n")
        print("Do you go through: a. The first door\n")
        print("b. The middle door\nc. The last door\n")
        choice3 = input("\nEnter here: ")
        if choice3 == "a":
            lives -= 1
            points -= 50
            print("\nYou open the door...and walk in falling into a pit of")
            print("lava.\nYou die.\n")

            print("-1 life")
            print(f"You have {lives} remaining life")
            print("Try again")
            if lives == 0:
                game_over()
            continue

        elif choice3 == "b":
            lives -= 1
            points -= 50
            print("\nThe door is locked. You bash it down with your shoulders")
            print("repeatedly, the door gives way and breaks open.")
            print("The momentum of your push carries you passed the doorway")
            print("and you are now falling down outside the tower -")
            print("you fall to your death.")
            print("You died.\n")

            print("\n-1 life")
            print(f"You have {lives} remaining life")
            print("Try again")
            if lives == 0:
                game_over()
            continue

        elif choice3 == "c":
            points += 100
            print(f"\nYou kick the door open. Princess {princess} is sitting")
            print("terrified on her bed, you tell her you have come to")
            print("rescue her.\n")
            break
        else:
            print("\nInvalid key.")
            print("Please enter a valid option to make a choice: \n")

    # Scene 4
    print("\n\nScene 4")
    print(f"Lives: {lives}")
    print(f"Points: {points}")
    while True:
        print("\nYou start looking for an exit but then you see a window and")
        print("look into it.")
        print(f"Below the window is the great big sleeping dragon, {dragon},")
        print("on a bed of golden coins in a room full of treasure.")
        print("Underneath the window there are stairs descending down into")
        print("the room.\n")

        print("\nDo you:\n\na. Sneak down the stairs and take some of the")
        print("treasure back with you.")
        print("b. Take your sword out and to slay the dragon while it sleeps.")
        print("c. Go back the way you came.\n")
        choice4 = input("\nEnter here: ")
        if choice4 == "a":
            lives -= 1
            points -= 50
            print("\nYou vault over the window onto the stairs")
            print("and start sneaking down...")
            print(f"But the clunking of your armour awakes {dragon} and")
            print("before you know it your are facing a very angry dragon.")
            print("The dragon opens its mouth surrounding you in flames and")
            print("you are burnt to a cinder. You die.\n")

            print("\n-1 life")
            print(f"You have {lives} remaining life")
            print("Try again\n\n")
            if lives == 0:
                game_over()
            continue
        elif choice4 == "c":
            lives -= 1
            points -= 50
            print("\nYou grab the Princess by the hand and lead her back with")
            print("you down the stairs, you are suddenly met with an army of")
            print("Skeleton Soldiers. Your futile attempt to fight them does")
            print("nothing as the horde of Skeletons overwhelm you with their")
            print("attack. You die.\n")

            print("\n-1 life")
            print(f"You have {livess} remaining life")
            print("Try again\n\n")
            if lives == 0:
                game_over()
            continue
        elif choice4 == "b":
            points += 100
            print("\nYou stand on the edge of the window with your sword")
            print("drawn. You leap into the air with both hands on the hilt")
            print("of the sword.")
            print("You PLUNGE the sword right into the dragon's skull!")
            print("The dragon is thrashing but you keep the sword there,")
            print("holding tight until the dragon stops.")
            print("You have SLAIN the dragon!\n")
            break
        else:
            print("\nInvalid key.")
            print("Please enter a valid option to make a choice: \n")

    # Scene 5
    print("\n\nScene 5")
    print(f"Lives: {lives}")
    print(f"Points: {points}")
    while True:
        print("\nYou now find yourself in a room full of priceless treasures,")
        print("with a slain dragon and the rescued Princess.\n")

        print(f"a. Hurry, leave The Castle with Princess {princess}.")
        print(f"b. Leave the Castle with Princess {princess}")
        print("but fill bags of treasure to take back")
        print("with you as promised by {king}.\n")
        choice5 = input("\nEnter here: ")
        if choice5 == "a":
            points += 150
            print(f"\nYou take Princess {princess} back to {king} -")
            print("the King showers you with grattitude.")
            print(f"You become the Hero of {kingdom} for saving the Princess")
            print(f"and slaying the dragon, {dragon}, to end its terror over")
            print(f"the kingdom. Princess {princess} falls in love with you")
            print("for saving her and she marries you. Eventually you become")
            print(f"the ruler over {kingdom} after {king}'s reign")
            print(f"ends as the new King of {kingdom} that you once saved.")
            print("They build a statue of you in honour of your greatness.\n")
            print("The End.\n\n")
            print(f"Your final score: {points}\n")
            game_end()
            break
        elif choice5 == "b":
            points += 50
            print(f"\nYou take Princess {princess} back to {king} - Your name")
            print("becomes famous for saving the Princess and slaying the")
            print(f"dragon, {dragon}, to end its terror over the kingdom.")
            print("You become fat and rich, indulging in the finer things for")
            print("the rest of your life.\n\nThe End.\n")
            print(f"Your score: {points}")
            game_end()
            break
        else:
            print("\nInvalid key.")
            print("Please enter the a valid option to make a choice: \n")


start_game()
