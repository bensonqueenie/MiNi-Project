import random
def name_to_number(name):
    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    else:
        return 4

def number_to_name(number):
    if number==0:
        return "rock"
    elif number==1:
        return "Spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    else :
        return "scissors"

def rpsls(player_choice):   
    print(" \n")
    print "Player chooses" ,player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,4)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses" ,comp_choice
    x = player_number
    y = comp_number
    if (x==4 and (y==3 or y==2)) or (x==3 and (y==2 or y==1)) or (x==2 and (y==1 or y==0)) or (x==1 and (y==0 or y==4)) or (x==0 and (y==4 or y==3)):
        print "Player wins!"
    elif x==y :
	    print "draw!"
    else :
	    print "Computer wins!"

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
