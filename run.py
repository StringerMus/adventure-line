def start_game():
    Introduction = "Welcome to Adventure Line!\n\nYour are in control of what happens in these stories.\n\nThe choices you make will affect the plot…but BEWARE, there are dangers and you must decide which choices to make.\nThe wrong decision could end in disaster - or even DEATH.\n"
    print(Introduction)
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
            the_nightshift()
            break
        else:
            print("\nInvalid key. Please enter the (1/ 2 or 3) to select a story:")

def replay():
    """
    This function will appear whenever the player makes a choice that would lead to failure or death
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
    end = input("\nCongratulations! You made it to the end of the story!\nWe hope you are happy with the ending you have chosen.\n\nWould you like to play again(y)\nor go back to the main menu(n)\n\nEnter here: ")
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
    castle_set = "\nA Princess has been stolen away by a fire breathing Dragon, taking her back to its lair as punishment to the King for not paying his yearly tribute.\nThe King has promised all the treasure and gold the Dragon holds to the hero who rescues the Princess and brings her back to him.\nYou have decided to embark on this daring quest to rescue the Princess and gain riches.\n"
    print(castle_set)

    while True:
        #Situation 1
        sit1 = "\nYou arrive at the Dragon’s Lair in a shining metal armour, with a sword and shield in your hands. The lair is a big castle inside a mountain, you see the entrance guarded by 2 skeletons with swords.\n"
        print(sit1)
        choice1 = input("\nDo you\n\na.Charge and fight the skeletons or\nb.Run away\n\nEnter here: ")
        if choice1 == "b":
            print("\nYou run away, leaving behind the Princess and the gold to the Dragon. Mission Failed.\n")
            replay()
                
        elif choice1 == "a":
            print("\nYou charge at the skeleton guards, swinging your sword. They crumble from the slashes of your mighty sword.\n")
            
            #Situation 2
            sit2 = "\nYou enter the castle and see a set of stairs going up to a tower and another set of stairs going down into a dungeon.\n"
            print(sit2)
            choice2 = input("\nDo you\n\na. Go up the tower or \nb. Go down into the dungeon\n\nEnter here: ")
            if choice2 == "b":
                print("\nYou run down, into the darkness of the dungeon...\nYou suddenly find yourself falling into a pit of emptiness and spikes pierce your body as you meet the bottom. You die.\n")
                replay()

            #if 'aa' is typed - it goes back to sit1    
            elif choice2 == "a":
                print("\nYou go up the winding stairs of the tower and found yourself in front 3 closed doors.\n")

                #Situation3
                choice3 = input("\nDo you go through:\n\na. The first door\nb. The middle door\nc. The last door\n\nEnter here: ")
                if choice3 == "a":
                    print("\nYou open the door...and walk in falling into a pit of lava. You die.\n")
                    replay()
                elif choice3 == "b":
                    print("\nThe door is locked. You bash it down with your shoulders repeatedly, the door gives way and breaks open. The momentum of your push carries you passed the doorway and you are now falling down outside the tower - you fall to your death. You died.\n")
                    replay()

                elif choice3 == "c":
                    print("\nYou kick the door open. The Princess is sitting terrified on her bed, you tell you have come to rescue her.\n")
                    
                    #Situation4
                    sit4 = "\nYou start looking for an exit but then you see a window and look into it.\n\nBelow the window is a great big sleeping dragon on a bed of golden coins in a room full of treasure and underneath the window there are stairs descending down into the room.\n"
                    print(sit4)
                    choice4 = input("\nDo you:\n\na. Go down the stairs to sneak down and take some of the treasure back with you.\nb. Take your sword out and jump on the dragon.\nc.Go back the way you came.\n\nEnter here: ")
                    if choice4 == "a":
                        print("\nYou vault over the window onto the stairs and start sneaking down...\nBut the clunking of your armour awakes the dragon and before you know it your are facing a very angry beast.\nThe Dragon opens its mouth surrounding you in flames and you are burnt to a cinder. You die.\n")
                        replay()
                    elif choice4 == "c":
                        print("\nYou grab the Princess by the hand and lead her back with you down the stairs, you are suddenly met with an army of Skeleton Soldiers.\nYour futile attempt to fight them does nothing as the horde of Skeletons overwhelm you with their attack. You die.\n")
                        replay()

                    elif choice4 == "b":
                        print("\nYou stand on edge of the window with your sword drawn. You leap into the air with both hands on the hilt of the sword.\nYou PLUNGE the sword right into the Dragon's skull!\nYou keep the sword there, holding tight until the Dragon stops thrashing.\nYou have SLAIN the Dragon!\n")

                        #Situation5
                        sit5 = "\nYou find yourself in a room full of priceless treasures, with a slain dragon and the rescued Princess.\n"
                        print(sit5)
                        choice5 = input("\na.Leave The Castle with Princess.\nb.Leave the Castle with the Princess but also fill bags treasure to take back with you as promised by the King.\n\nEnter here: ")
                        if choice5 == "a":
                            print("\nYou take the Princess back to the King - the King showers you with grattitude.\nYou become the Hero of the land for saving the Princess and slaying the Dragon to end its terror over the Kingdom.\nThe Princess falls in love with you for saving her and she marries you.\nEventually you become the Ruler over the Kingdom after the Kings reign as the new king of the Land that you once saved.\nThey build a statue of you to honour your greatness.\n\nThe End.\n")
                            game_end()
                        elif choice5 == "b":
                            print("\nYou take the Princess back to the King - Your name becomes famous for saving the Princess and slaying the Dragon to end its terror over the Kingdom.\nYou become fat and rich, indulging in the finer things for the rest of your life.\n\nThe End.\n")
                            game_end()
        else:
            print("\nInvalid key. Please enter the a valid option to make a choice: ")

#The Night-Shift Story
def the_nightshift():
    nightshift_select = "\nYou have selected 'The Night-Shift'"
    print(nightshift_select)
    """
    Each story will start by setting the scene
    Followed by a situation where the user needs to make a choice
    Options will be provided to the player
    The player will need to enter a valid key to select a choice and progress the story.
    """
    nightshift_set = "\nYou are a Night-Watchmen assigned as security of an abandonned hospital asylum,this is your last shift before your retirement. There is a constant cycle of new guards going in out of the job, it might that the darkness and lonelines gets the best of people. But you don’t mind the time to yourself and are not scared of the dark.\n\nA new guard has started their first shift tonight, you have a radio to communicate with each other. They are making their first round of the hospital while you are at the security booth.\n"
    print(nightshift_set)

    while True:
        #Situation 1
        sit1 = "\nA radio transmission comes in from the New Guard ‘….zzz….I...zz….I…', you can't make out what they are saying, there is too much static. Again a transmission comes in ‘…..hel….zzz….I need…….help…zzz…'. You heard 'help'.\nYou try to communicate back but you don't receive an answer.\n"
        print(sit1)
        choice1 = input("\nWhat do you do?\n\na. Go and investigate to look for your partner or\nb. You are sure it’s nothing as it never is, you’re sure you must have heard wrong. You await for your partner’s return, they should return in an hour from their patrol.\n")
        if choice1 == "b":
            print("\nYou wait for your patner to return, but the New Guard does not appear after an hour. You go to investifate but they are now missing. Failed, you did not help your partner.\n")
        elif choice1 == "a":
            print("\nInto the darkness you go with your flashlight and your radio communicator along the usual patrol route in the hopes of stumbling across your partner.\n")

            #Situation2
            sit2 = "\nYou find your partner’s radio by basement level stairs which is not part of the patrol route, you look around but there is no sight of them in the darkness.\n"
            print(sit2)
            choice2 = input("\na. Go down the basement.\nb. Run away.\nc. Carry on along the path.\n")
            if choice2 == "b":
                print("\n\n")
            elif choice2 == "c":
                print("\n\n")
            elif choice2 == "a":
                print("\nYou go down the basement and find your partner walking towards your direction. They explain they heard a noise down here and went to investigate but found nothing and they must’ve dropped the radio on their way. Your partner denies making a call and says it must’ve been interference or someone playing tricks.\n")

                #Situation3
                sit3 = "\nAfter your patner leaves to carry on with the patrol, another transmission comes in on the radio ‘help me’.\n"
                print(sit3)
                choice3 = input("\na.Reply back and investigate.\nb. Ignore it.\n")
                if choice == "b":
                    print("\nYou ignore the transmission and go back to the booth. You did not investigate the mysterious transmissions and fail to identify if someone is in trouble.\n")
                if choice == "a":
                    print("\nYou ask if they are in the hospital, ‘yes’ is the response, ‘in the basement…help me’. You ask where in the basement, ‘I don’t know’.\n")

                    #Situation4
                    sit4 = "\n\n"
                    print(sit4)

        else:
            print("\nInvalid key. Please enter the a valid option to make a choice: ")

start_game()
select_story()