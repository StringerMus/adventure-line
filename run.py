# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
Introduction = "Welcome to Adventure Line!\n\nYour are in control of what happens in these stories.\n\nThe choices you make will affect the plot but BEWARE, there are dangers and you must decide which choice to make.\nThe wrong decision could end in disaster - or even DEATH."
print(Introduction)

def start_game(): 
    start = input("Start Game (y)")
    if start == "y":
        story = input("Choose the story:\n\n1.The Night-Shift\n2.The Plane\n3.The Castle")



start_game()