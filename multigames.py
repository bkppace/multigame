#def used to define the function code. raw_input allows use of string as input wihtout quotation marks. The next two sections are the core of the b-day program.
#This is the b-day game.
#
#
#

def simpleprogram():
    print("Happy Birthday to you!")
    print("You live in the zoo!")
    print("You look like a monkey!...")
    print("And smell like one too!")

    menu()


def bday():
    print("Is it your birthday? yes/no")
    reply = raw_input()
    
    if reply == "yes":
        simpleprogram()
    
    if reply == "no":
        print("I'm sorry.")
        menu()

    if reply == "quit":
        print("See ya!")
        return

    else:
        ("I'm sorry, that answer doesn't make sense.")
        bday()

########################################################################################
#
#This is the code for the guess the number game.
#

def guessnumber():
    print("Guess a number between 1 and 10.")
    
    

    import random
    x = random.randrange(1,10)
    
    while True:
        try:
            
            answer = input()
            
            if answer < x and answer != 0:
                print("Guess a little higher..")
        
            if answer > x and answer <= 10:
                print("Lower...")
        
            if answer > 10:
                print("uh...Idiot.")
            
            if answer == 0:
                print("That wasn't even an option!")

            if answer == x:
                print("You got it!")
                print("Would you like to play again? yes/no")
                answer = raw_input()
        
                if answer == "yes":
                    import random
                    x = random.randrange(1,10)
                    print("Ok, guess a number 1-10.")
                    continue
            
                if answer == "no":
                    print("Thanks for playing!")
                    menu()
                    break

                else:
                    print("Sorry, I didn't understand. Do you want to play again?")
                    end()
    
                        
        except:
            print("I'm sorry, I didn't catch that. Please give a numberical integer as a response.")
            continue


#####################################################################################
#
#This will take the player to a menu to pick another game or quit after finishing one.

def menu():

    print("Would you like to play a different game? yes/no")
    choice = raw_input()
    
    if choice == "yes":
          print("Would you like to play b-day, guess the number, or rock paper scissors?")
          a = raw_input()
          
          if a == "b-day":
              bday()
          
          if a == "guess the number":
              guessnumber()

          if a == "rock paper scissors":
              rock()

          if a == "quit":
              print("Shucks. See ya next time!")
              return
                
    
    if choice == "no":
        print("Bye! Let's play again sometime!")
          
###########################################################################################
#
# This allows the player to choose which game to play and will activate the game selected.

def start():
    try:
        print("Would you like to play b-day, guess the number, or rock paper scissors?")
        a = raw_input()

        if a == "b-day":
            bday()

        if a == "guess the number":
            guessnumber()

        if a == "rock paper scissors":
            rock()

        if a == "quit":
            print("Alright. Have a good one!")
            return

    except:
        print("I'm sorry, that wasn't a valid response.")
        start()


############################################################################################
#
# Rock, Paper, Scissors game

#function to restart the program when player wants to play again.

def restart():
    c = raw_input()
    if c == "yes":
        rock()
    if c == "no":
        print("Thanks for playing!")
        menu()
    if c != "yes" and c != "no":
        print("Please give a yes or no response.")
        restart()

#function to store main program or restart if round is a tie.

def rock():
    print("Choose rock, paper, or scissors. I have randomly selected one already.")
    x = raw_input()
    
    import random
    options = ["rock", "paper", "scissors"]
    b = random.choice(options)

#if computer picks rock
    if b == "rock" and x == "rock":
        print("We both picked rock! It's a tie! Let's try again.")
        rock()
    
    if b == "rock" and x == "paper":
        print("Shoot. I picked rock. You win! Would you like to play again?")
        restart()
        
    if b == "rock" and x == "scissors":
        print("Ha! Rock beats scissors! I win! Would you like to play again?")
        restart()

#if computer picks paper
        
    if b == "paper" and x == "paper":
        print("We both picked paper! It's a tie! Let's try again.")
        rock()
        
    if b == "paper" and x == "scissors":
        print("Shoot. I picked paper. You win! Would you like to play again?")
        restart()
        
    if b == "paper" and x == "rock":
        print("Ha! Paper beats rock! I win! Would you like to play again?")
        restart()

#if computer picks scissors

    if b == "scissors" and x == "scissors":
        print("We both picked scissors! It's a tie! Let's try again.")
        rock()

    if b == "scissors" and x == "rock":
        print("Shoot. I picked scissors. You win! Would you like to play again?")
        restart()
        
    if b == "scissors" and x == "paper":
        print("Ha! Scissors beats paper! I win! Would you like to play again?")
        restart()

    if x == "quit":
        print("Ok. Bye!")
        return

    if  x != "scissors" and x !="paper" and x !="rock" and x!= "quit":
        print("Sorry, that isn't a valid option. Try again.")
        rock()

#############################################################################################
#
#
#starts the entire program
start()
############################################################################################





