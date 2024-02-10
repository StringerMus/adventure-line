def start_game():
    Introduction = "Welcome to Adventure Line!\n\nYour are in control of what happens in these stories.\n\nThe choices you make will affect the plot but BEWARE, there are dangers and you must decide which choice to make.\nThe wrong decision could end in disaster - or even DEATH.\n"
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
            game_3()
            break
        else:
            print("\nInvalid key. Please enter the (1/ 2 or 3) to select a story:")

def replay():
    retry = input("\nWould you like to retry? (y/n): ")
    if retry == "y":
        the_castle()
    elif retry == "n":
        start_game()

def game_end():
    end = input("\nCongratulations! You made it to the end of the story! We hope you are happy with the ending you have chosen.\n\nWould you like to play again(y) or go back to the main menu(n): ")
    if end == "y":
        the_castle()
    elif end == "n":
        start_game()

def the_castle():
    loading = "\nYou have selected 'The Castle'"
    print(loading)
    """
    Each story will start by setting the scene
    Followed by a situation where the user needs to make a choice
    Options will be provided to the player
    The player will need to enter a valid key to select a choice and progress the story.
    """
    castle_set = "\nA Princess has been stolen away by a fire breathing Dragon in its lair as punishment to the King for not paying his yearly tribute.\n\nThe King has promised all the gold the dragon holds to the hero who rescues the Princess and brings her back to him.\n\nYou have decided to embark on this bold quest to rescue the Princess and gain riches"
    print(castle_set)

    while True:
        #Situation 1
        sit1 = "\nYou arrive at the Dragons Lair in a shining metal armour, with a sword and shield in your hands. The lair is a big castle inside a mountain, you see the entrance guarded by 2 skeletons with swords\n"
        print(sit1)
        choice1 = input("\nDo you\n\na.Charge and fight the skeletons or\nb.Run away\n\nEnter here: ")
        if choice1 == "b":
            print("\nYou run away, leaving behind the Princess and the gold to the Dragon. Mission Failed.\n")
            replay()
                
        elif choice1 == "a":
            print("You charge at the skeleton guards and they crumble from the hits of your mighty sword.")
            
            #Situation 2
            sit2 = "\nYou enter the castle and see a set of stairs going up to a tower and another set of stairs going down into the dungeon.\n"
            print(sit2)
            choice2 = input("\nDo you\n\na. Go up the tower or \nb. Go down into the dungeon\n\nEnter here: ")
            if choice2 == "b":
                print("\nYou run down, into the darkness of the dungeon you suddenly find yourself falling into emptiness. Suddenly spikes pierce your body as you meet the bottom. You died.\n")
                replay()

            #if 'aa' is typed - it goes back to sit1    
            elif choice2 == "a":
                print("You go up the winding stairs of the tower and found yourself in front 3 closed doors.\n")

                #Situation3
                choice3 = input("\nDo you go through:\n\na. The first door\nb. The middle door\nc. The last door\n\nEnter here: ")
                if choice3 == "a":
                    print("\nYou open the door, walk in and fall into a pit of lava. You died.\n")
                    replay()
                elif choice3 == "b":
                    print("\nThe door is locked. You bash it down with your shoulders repeatedly, the door gives way and breaks open. The momentum of your push carries you passed the doorway and you are now falling down outside the tower - you fall to your death. You died.\n")
                    replay()

                elif choice3 == "c":
                    print("\nYou kick the door open. The Princess is sitting terrified on her bed, you tell you have come to rescue her.\n")
                    
                    #Situation4
                    sit4 = "\nYou start looking for an exit but then you see a window and look into it\n\n Below the window is a great big sleeping dragon on bed of golden coins in a room full of treasure and underneath the window there are stairs descending into the room.\n"
                    print(sit4)
                    choice4 = input("\nDo you:\n\na. Go down the stairs to sneak down and take some of the treasure back with you.\nb. Take your sword out and jump on the dragon.\nc.Go back the way you came.\n")
                    if choice4 == "a":
                        print("\nYou vault over the window onto the stairs and start sneaking down...\nbut the clunking of your armour awakes the dragon and before you know it your are facing a very angry beast.\nThe Dragon opens it mouth and you are burnt to a cinder. You die.\n")
                        replay()
                    elif choice4 == "c":
                        print("\nYou grab the Princess by the hand and lead her back with you down the stairs, you are suddenly met with an army of Skeleton Soldiers.\nYour futile attempt to fight them does nothing as the horde of Skeletons overwhelm you with their attack. You die.\n")
                        replay()

                    elif choice4 == "b":
                        print("\nYou stand on edge of the window with your sword drawn. You leap into the air with both hands on the hilt of the sword.\nYou plunge the sword right into the Dragon's head.\nYou keep the sword there, holding tight until the Dragon stops thrashing.\nYou have SLAIN the Dragon!\n")

                        #Situation5
                        sit5 = ("\nYou find yourself in a room full priceless treasure, a slain dragon and a princess\n")
                        print(sit5)
                        choice5 = input("\na.Leave The Castle with Princess\nb.Leave the Castle with the Princess but also fill bags treasure to take back with you as promised by the King.")
                        if choice5 = "a":
                            print("\nYou take the Princess back to the King - You become the Hero of the land for saving the Princess and slaying the Dragon to end its terror over the Kingdom.\nThe Princess falls in love with you for saving her and she marries you.\nEventually you become the Ruler over the Kingdom after the King passes to reign over the Land you once saved and they build a statue of you to honour your greatness.\n\nThe End.")
                            game_end()
                        elif choice5 = "b":
                            print("\nYou take the Princess back to the King - Your name becomes famous for saving the Princess and slaying the Dragon to end its terror over the Kingdom.\nYou become fat and rich, indulging in the finer things the rest of your life\n\nThe End.\n")
                    break

        else:
            print("\nInvalid key. Please enter the a valid option to make a choice: ")


start_game()
select_story()