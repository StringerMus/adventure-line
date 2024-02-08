# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
Introduction = "Welcome to Adventure Line!\n\nYour are in control of what happens in these stories.\n\nThe choices you make will affect the plot but BEWARE, there are dangers and you must decide which choice to make.\nThe wrong decision could end in disaster - or even DEATH."
print(Introduction)

def start_game():
    """
    Get command to start game from user.
    User to select the story they want to play.
    """
    while True:
        start = input("Start Game? (y): ")
        try:
            if start == "y":
                break
        #doesnt work
        except:
            print("Please enter 'y' to start game")

def select_story():
    story = input("\nChoose the story:\n\n1.The Night-Shift\n2.The Plane\n3.The Castle\n\n")
            

start_game()
select_story()