lives = 2
points = 0

def display():
    print(f"\n\nLives: {lives}")
    print(f"Points: {points}")

def start_game():
    print("Welcome to Adventure Line!\n")
    print("Your are in control of what happens in these stories.")
    print("The choices you make will affect the plot......but BEWARE, there are dangers and you must decide which choices to make.")
    print("The wrong decision could end in disaster - or even DEATH.\n")
    """
    Get command from user to start game from user.
    User to select the story they want to play.
    """
    while True:
        start = input("Start Game? (y): ")
        if start == "y":
            select_story()
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
            the_nightshift()
            break
        else:
            print("\nInvalid key. Please enter the (1/ 2 or 3) to select a story:")

def game_over():
    """
    This function will appear whenever a players lives reaches 0
    To give opportunity for player to try again and allow them to go back to the main menu.
    """
    retry = input("\nWould you like to retry? (y/n): ")
    if retry == "y":
        the_castle()
    elif retry == "n":
        start_game()

def game_end():
    """
    This function will only appear when a player makes it to the end of a story.
    It congratulates the player and provides the option to either play the story again for the alternative ending
    or to go back to the main menu.
    """
    print("\nCongratulations! You made it to the end of the story!\nWe hope you are happy with the ending you have chosen.\n")
    end = input("\nWould you like to play again(y)\nor go back to the main menu(n)\n\nEnter here: ")
    if end == "y":
        the_castle()
    elif end == "n":
        start_game()

def the_castle():
    castle_select = "\nYou have selected 'The Castle'"
    print(castle_select)
    """
    Each story will start by setting the scene
    Followed by a situation where the user needs to make a choice
    Options will be provided to the player
    The player will need to enter a valid key to select a choice and progress the story.
    """
    #Keeps record users lives and points
    lives = 2
    points = 0

    print("\nA Princess has been stolen away by a fire breathing Dragon, taking her back to its lair as punishment to the King for not paying his yearly tribute.")
    print("\nThe King has promised all the treasure and gold the Dragon holds to the hero who rescues the Princess and brings her back to him.")
    print("\nYou have decided to embark on this daring quest to rescue the Princess and gain riches.\n")

    #Game starts here
    while True:
        print(f"Lives: {lives}")
        print(f"Points: {points}")
        #Situation 1
        print("\nYou arrive at the Dragon’s Lair in a shining metal armour, with a sword and shield in your hands.")
        print("The lair is a big castle inside a mountain, you see the entrance guarded by 2 skeletons with swords.\n")
        choice1 = input("\nDo you\n\na.Charge and fight the skeletons or\nb.Run away\n\nEnter here: ")
        if choice1 == "b":
            points -= 50
            lives -= 1
            print("\nYou run away, leaving behind the Princess and the gold to the Dragon. Mission Failed.\n")
            print("-1 life")
            print(f"You have {lives} remaining life")
            print("Try again")
            continue
        elif choice1 == "a":
            points += 100
            print("\nYou charge at the skeleton guards, swinging your sword. They crumble from the slashes of your mighty sword.\n")
            break
        else:
            print("\nInvalid key. Please enter the a valid option to make a choice: \n")

    #Situation 2
    print(f"Lives: {lives}")
    print(f"Points: {points}")
    while True:
        print("\nYou enter the castle and see a set of stairs going up to a tower and another set of stairs going down into a dungeon.\n")
        choice2 = input("\nDo you\n\na. Go up the tower or \nb. Go down into the dungeon\n\nEnter here: ")
        if choice2 == "b":
            lives -= 1
            points -= 50
            print("\nYou run down, into the darkness of the dungeon...")
            print("You suddenly find yourself falling into a pit of emptiness and spikes pierce your body as you meet the bottom. You die.\n")
            print("-1 life")
            print(f"You have {lives} remaining life")
            print("Try again")
            continue
        elif choice2 == "a":
            print("\nYou go up the winding stairs of the tower and found yourself in front 3 closed doors.\n")
            points += 100
            break
        else:
            print("\nInvalid key. Please enter the a valid option to make a choice: ")
    
    #Situation 3
    print(f"Lives: {lives}")
    print(f"Points: {points}")
    while True:
        choice3 = input("\nDo you go through:\n\na. The first door\nb. The middle door\nc. The last door\n\nEnter here: ")
        if choice3 == "a":
            lives -= 1
            points -= 50
            print("\nYou open the door...and walk in falling into a pit of lava. You die.\n")
            print("-1 life")
            print(f"You have {lives} remaining life")
            print("Try again")
            continue
        elif choice3 == "b":
            lives -= 1
            points -= 50
            print("\nThe door is locked. You bash it down with your shoulders repeatedly, the door gives way and breaks open.")
            print("The momentum of your push carries you passed the doorway and you are now falling down outside the tower - you fall to your death.")
            print("You died.\n")
            print("\n-1 life")
            print(f"You have {lives} remaining life")
            print("Try again")
            continue
        elif choice3 == "c":
            points += 100
            print("\nYou kick the door open. The Princess is sitting terrified on her bed, you tell you have come to rescue her.\n")
            break
        else:
            print("\nInvalid key. Please enter the a valid option to make a choice: ")

    #Situation 4
    print(f"Lives: {lives}")
    print(f"Points: {points}")
    while True:
        print("\nYou start looking for an exit but then you see a window and look into it.")
        print("Below the window is a great big sleeping dragon on a bed of golden coins in a room full of treasure.")
        print("Underneath the window there are stairs descending down into the room.\n")
            
        print("\nDo you:\n\na. Go down the stairs to sneak down and take some of the treasure back with you.")
        print("b. Take your sword out and jump on the dragon.\nc.Go back the way you came.\n")
        choice4 = input("\nEnter here: ")
        if choice4 == "a":
            lives -= 1
            points -= 50
            print("\nYou vault over the window onto the stairs and start sneaking down...")
            print("But the clunking of your armour awakes the dragon and before you know it your are facing a very angry beast.")
            print("The Dragon opens its mouth surrounding you in flames and you are burnt to a cinder. You die.\n")
            print("\n-1 life")
            print(f"You have {lives} remaining life")
            print("Try again\n\n")
            continue
        elif choice4 == "c":
            lives -= 1
            points -= 50
            print("\nYou grab the Princess by the hand and lead her back with you down the stairs, you are suddenly met with an army of Skeleton Soldiers.")
            print("Your futile attempt to fight them does nothing as the horde of Skeletons overwhelm you with their attack. You die.\n")
            print("\n-1 life")
            print(f"You have {lives} remaining life")
            print("Try again\n\n")
        elif choice4 == "b":
            points += 100
            print("\nYou stand on edge of the window with your sword drawn. You leap into the air with both hands on the hilt of the sword.")
            print("You PLUNGE the sword right into the Dragon's skull!\nYou keep the sword there, holding tight until the Dragon stops thrashing.")
            print("You have SLAIN the Dragon!\n")
            break
        else:
            print("\nInvalid key. Please enter the a valid option to make a choice: ")

    #Situation 5
    print(f"Lives: {lives}")
    print(f"Points: {points}")
    while True:
        print("\nYou find yourself in a room full of priceless treasures, with a slain dragon and the rescued Princess.\n")
            
        print("a. Leave The Castle with Princess.\nb. Leave the Castle with the Princess but also fill bags treasure to take back with you as promised by the King.\n")
        choice5 = input("\nEnter here: ")
        if choice5 == "a":
            points += 150
            print("\nYou take the Princess back to the King - the King showers you with grattitude.")
            print("You become the Hero of the land for saving the Princess and slaying the Dragon to end its terror over the Kingdom.")
            print("The Princess falls in love with you for saving her and she marries you.")
            print("Eventually you become the Ruler over the Kingdom after the Kings reign as the new king of the Land that you once saved.")
            print("They build a statue of you to honour your greatness.\n\nThe End.\n")
            #score - change to just points
            print(f"{points}")
            game_end()
            break
        elif choice5 == "b":
            points += 50
            print("\nYou take the Princess back to the King - Your name becomes famous for saving the Princess and slaying the Dragon to end its terror over the Kingdom.")
            print("You become fat and rich, indulging in the finer things for the rest of your life.\n\nThe End.\n")
            #score - change to just points
            print(f"{points}")
            game_end()
            break
        else:
            print("\nInvalid key. Please enter the a valid option to make a choice: ")
            
start_game()