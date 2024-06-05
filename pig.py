import random

# to have a random number between 1 to 6.
def roll():
    min_value = 1 
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

# make a loop to ask the user to choose the player number between 2 to 4 if the input is not digit then ask again.
while True:
    player = input("Enter the number of player (2 - 4) : ")
    
    if player.isdigit():
        player = int(player)
        
        if  2 <= player <= 4 :
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")
            
# the player with the score of 50 is the winner.  
max_score = 50

# set 4 scores for 4 users.
player_scores = [0 for _ in range(player)]

# make a loop to run the game till someone reaches 50 and win the game.
while max(player_scores) < max_score:
    
    for player_idx in range(player):
        print('**--------------------------------------------------------------**')
        print("Player  number:", player_idx +1 , "turn has just started!")
        print(" Your total score is:" , player_scores[player_idx])
        print('**--------------------------------------------------------------**')

        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y)? ")
            
            if should_roll.lower() != "y":
                break
            value= roll()
            
            if value == 1 :
                print("you rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a : ", value)
                
            print("Your score is :" , current_score)
            
        player_scores[player_idx] += current_score
        print("Your total score is :" , player_scores[player_idx])
        
max_score = max(player_scores)
wining_idx = player_scores.index(max_score)
print("Player number", wining_idx + 1, "is the winner  with the score of:", max_score)