# Adventure Line
Adventure Line is an interactive program that has been inspired by the Choose Your Own Adventure series to encourage children to read by placing them in the role of the main character and giving the player the power to influence the line of story and the outcome based on their decisions as the game requires the user's input to progress through a story. This objective fits really well with this type of game as it's an interactive text-based program.


The target audience for Adventure Line would be young children to teens due to the type of stories that would be available to play and the type of game that is likely to engage this age group. This audience will fit the demographic that would be interested in a game like this where the objective of using an interactive text-based app to get them interested in reading stories.


[Visit app here](https://adventure-line-e6e050da4a13.herokuapp.com/)


![Intro-screen](media/intro.png)




### What the user wants
The user would want to be entertained by the game, they would want a good experience being able to make choices within a story, and they would also want a slight challenge and not an easy walkthrough.


### What the developer wants
The developer would want users to have the experience of being the main character in a story and provide them with a variety of decisions they need to make. The developer would want users to re-play the game as much as possible and as much positive experience to get players interested in fictional stories.


## How to play


This is a text-based app game on a console that requires user input on prompts from the game to progress through the story to the ending.


The player has three lives, if a user makes an incorrect decision they get an opportunity to select a different answer on the same scene but if they select 3 incorrect decisions throughout the game, the game is over and the user is given the option of either going back to the main menu or playing the same story again.


There are points to be gained throughout the gameplay, players gain points on correct decisions and lose points on incorrect decisions - players should aim to get the highest score by the end of the story.


Decisions from players are made at the end of scenes where options are provided to the player on what they want to do next and where things will happen - either the user selects the correct decision and progresses to the next scene or if the user chooses the incorrect decision they lose a life, the continues until the ending is reached.




# Development


The idea was to get the Choose Your Adventure theme into a text-based game format. The main thing we needed was the stories and to build everything around the decision element. To make the game fun, add a little bit of challenge and re-playability the elements of points and lives were added to keep the game interesting.


I had first written a story, and cut the story into introduction, scenes, and an ending - the scenes are where the different decisions had to be created for the user to select to go through the story.




## Logic Map


![flowchart](media/al_flowchart.jpg)


The logic map shows how the game functions following user inputs and how the game is affected by incorrect decisions and 0 lives.




## Surface
As this is a text based game, it does not really have a front end and the game is played on a console.




# Features


## Random Variables
This feature has been added as a bit to make the game more fun for users whenever they play when the names of the Princess, King, the dragon, and the kingdom change each time the game is played. It adds a bit of dynamism to the story to have different characters appear each time they play
In the future it would be great to add when different characters appear they would bring a class of their own characteristics that affect the narrative of the story.


![random_variables](media/features/random_names.png)


![random_names](media/features/random_placeholder.png)




## Invalid Key
In every function else statements have been included to ensure users are inputting the correct keys within the game by notifying them an incorrect key has been input and providing them the key/s they need to input to continue.


![invalid_key](media/features/invalid_key.png)




## Start Game
This is essentially the game's main menu - it introduces the player to the game, explaining what the game is about and how it is played.
It prompts the user to start the game to continue to the Select Story section.


![start_game](media/features/start_game.png)




## Select Story
The Select Story function is where a player would have options of the stories available to play, at the moment there is only one story available but there would be a selection to choose from here.


The function prompts the user to press a number to select a story.


![select_story](media/features/select_story.png)




## Game Over
This function will only appear in the game when a player runs out of lives during gameplay, it will give the player the option to either play the story again from the beginning or back to the main menu.


![game_over](media/features/game_over.png)




## Game End
At the end of the game, the game_end function will appear that congratulates the player for reaching the ending and to provide the option to either play through the story again or go back to the main menu.


![game_end](media/features/game_end.png)




## The Castle
Once the player selects the story the_castle function will start. The function begins by providing the setting of the story to the user and introducing the characters involved.


![the_castle](media/features/the_castle.png)




### Lives & Points
This section explains to the users how lives and points work in the game, why they are important, and how it affects the player.


![lives&points](media/features/lives_and_points.png)




### Scenes
Stories will be cut up into scenes during gameplay after the story is introduced to players. At the end of each scene, players will be provided with options for them to take which could lead either lead them to the next scene, death or failure.


Depending on the player's choice they could lose a life, of points or not gain as many points from the other options.


![scenes](media/features/the_game.png)




The last scene will provide the player with an ending to the story and the game_end function will appear for the player to be able to navigate back to the main menu or play the story again.


![ending](media/features/ending.png)




## Features to implement


### Add colour
Since it's a text-based game, the readability could be made better if colour is added to the text to help the reader separate the type of information being provided and bring attention to where the game would want them.




### More stories
More stories need to be added to provide players with a variety which can easily be done as it will follow a similar formula to The Castle but have its own story-line and decisions a player needs to make.




### More variables that affect story-line and outcome
A vast amount of variables can be added to the story and future stories that affect the storyline and outcome. This will make the game more enjoyable and encourage replayability.




# Testing
### Main Menu


When I load up the game I am met with an introduction that explains to me what the game is about. There is a prompt for me to press 'y' to start the game.


![intro](media/testing/intro.png)




### Select Story
When I enter 'y', the game asks me to select a story. Since there is only 1 story available in the game, the prompt is to enter '1' to select The Castle.


![select_story](media/testing/select_story.png)




### Lives and Points
When I enter 'y' the game explains to me that I have 3 lives during game-play and will gain points depending on the decisions I make and will lose points for incorrect decisions.


![lives_and_points](media/testing/lives_and_points.png)




### Scenes
When I continue with the input 'y' I am presented with scene 1 of the story. I am given 2 options to take - a or b.
If I enter 'b' I fail the mission for running away and 1 life is taken away from me, the game then lets me try the scene again.


When I enter 'a' I am taken to the next scene and gain points. I ran through all of the scenes, testing all of the options, there were some bugs and typos which have been listed in the Bugs/Fixes section below.


![gameplay](media/testing/the_castle.png)




### Game Over
I have tested the losing all my lives in every scene, each time I did the game_over function will appear giving me the option to either start the story again or go back to the main menu.


![game_over](media/testing/game_over.png)




### Invalid Key
On every prompt, I tried inputting incorrect keys and received the invalid key message, and will not change until the valid key is entered.


![invalid_key](media/testing/invalid_key.png)




### Random names
With the names being randomised in the list for the kingdom, princess, dragon, and the king are consistent throughout a session of the game and will not change until the game is refreshed as intended.


![intro_names](media/testing/intro_names.png)


![ending_names](media/testing/ending_names.png)




## Bugs/Fixes
There were a couple of bugs I found during testing which have now been fixed -


scene4 - typo in {livess} causes error message comes up.<br>
scene 5 - {king} appears in the game instead of a name from the list.


And there were some typos in spelling and spacing which have been edited.




## Validator Testing
### Pep8
Pep8 has been used to check the code and a lot of errors were found, mainly due to the length of strings.


![pep8](media/validator/pep8_validator.png)




After making the amendments there are no errors or warnings.


![no_errors](media/validator/pep8_no_errors.png)




# Deployment
Adventure Line has been deployed on Heroku;


Create a new app on the Heroku dashboard
<li>Give the app a unique name as it cannot be the same name as existing apps.


### Setting
Once the app has been created go into the settings tab.
<li>On the Config Vars input ‘PORT” in KEY and ‘8000’ in VALUE.
<br>
<br>
In the Buildpacks section of the setting add
<li>heroku/python
<li>heroku/nodejs
<br>
<br>
It needs to be shown in that exact order.




### Deploy


Now go into the Deploy tab


In the Deployment Method section select GitHub, and confirm connect to GitHub.
<li>You will need to copy and paste the GitHub repository name, search, and connect to link the Heroku app to the GitHub repository.


<li>Enable Automatic Deploys for Heroku to update on git push commands.


<li>I also deployed the branch to main.
<br>
<br>


# Credits
## Content
I had help with coding from the following;


User Input - https://codehs.com/tutorial/rachel/user-input-in-python#


Random item from a list - https://betterstack.com/community/questions/python-how-to-randomly-select-list-item/#


Random selection - https://stackoverflow.com/questions/306400/how-can-i-randomly-select-choose-an-item-from-a-list-get-a-random-element


Project idea & story inspiration - https://teachyourkidscode.com/python-choose-your-own-adventure-game-tutorial/


Choose Your Own Adventure books - Extracts of the Introduction have been taken from the book's Introduction.


Python Validator - https://pep8ci.herokuapp.com/




### Technologies Used
The following websites and apps helped build Adventure Line;


Flowchart - https://app.diagrams.net/

GitPod - https://gitpod.io/workspaces

GitHub - https://github.com/

Heroku - https://dashboard.heroku.com/apps

Grammarly


## Thanks
I would like to thank my mentor Harry Dhillon for very good advice and for steering me in the right direction for this project which solved a lot of my problems. I would also like to thank the Slack community for all the useful information and advice that is available there.
