# Import Packages
import random
from tabulate import tabulate
from datetime import datetime
import time

# Create Table
mytable =[['Players','','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'],
         ['Human','',' ',' ',' ',' ',' ',' ','O',' ',' ',' ',' ',' ',' ','O',' ',' ',' ',' ',' ',' '],
         ['Computer','',' ',' ',' ',' ',' ',' ','O',' ',' ',' ',' ',' ',' ','O',' ',' ',' ',' ',' ',' ']]

# Initialize Variables And Players
while True:
    You = {"name": "You", "position": 1}
    C_player = {"name": "Computer", "position": 1}
    players = [You, C_player]
    player = None
    Name=''
    File= None
    you_moves= 0
    computer_moves= 0
    you_hole_hit= 0
    com_hole_hit= 0
    winning_player= None
    User_Name= ''

    # Display the Welcome Screen and Rules
    time.sleep(1.5)
    print("----------------------------------------------------------- WELCOME TO 20x2 BOARD GAME ! ------------------------------------------------------------")
    time.sleep(1)
    print("")
    print("")
    print("                                                              *RULES & REGULATIONS*\n                                                                ")
    time.sleep(1)
    print("                                                             This is 20x2 Board Game                                                                 ")
    time.sleep(0.6)
    print("                                                 The Board Consists Of 20 Blocks And 2 Black_Holes                                                   ")
    time.sleep(0.6)
    print("                                                      There are Two Players Can Play in Once \n                                                      ")
    time.sleep(0.6)
    print("                                                                PLAYER 1 = YOU                                                                       ")
    print("                                                                PLAYER 2 = COMPUTER\n                                                                ")
    time.sleep(0.6)
    print("                                                 The Game Start is Possible If 6 Appears in The Dice                                                 ")
    time.sleep(0.6)
    print("                                                If a Black_Hole Hit User Needs to Move Back to Slot 1                                                ")
    time.sleep(0.6)
    print("                                            The First Person Who Come to 20th Block Or Passes Win The Game \n\n                                      ")
    time.sleep(1)
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------")
    time.sleep(0.6)
    print("                                                            NOW YOU CAN START THE GAME !\n                                                           ")
    time.sleep(1)
    User_Name= input("Please Type Your Name :")
    print("")
        
    # Movement Of 'X' And Setting The Black Holes
    def move_player(player, move):
        black_hole_hit = False
        game_over = False
        
        if player["position"] + move > 20:
            game_over = True
        elif player["position"] + move == 8 or player["position"] + move == 15:
            player["position"] = 2
            black_hole_hit = True
        else:
            player["position"] += move
            game_over = False

        return game_over, move, black_hole_hit

    # Update Table
    def update_table():
        for i in range(1, 22):
            mytable[1][i] = " "
            mytable[2][i] = " "
            mytable[1][You["position"]] = "X"
            mytable[2][C_player["position"]] = "X"
            mytable[1][8] = "O"
            mytable[1][15] = "O"
            mytable[2][8] = "O"
            mytable[2][15] = "O"
            
    # Start The Game
    game_started = { "You": False, "Computer": False }
    just_started = { "You": False, "Computer": False }
    while True:
        
        # Switch Players
        if player == None:
            player = "You"
        elif player == "You":
            player = "Computer"
        else:
            player = "You"
            
        # Display The Masseges And Setting The Dice
        input(f"{player}: Press Enter To Roll The Dice !")
        dice = random.randint(1, 6)
        print(f"{player}: Dice Value = {dice}\n")

        # Check The Dice Value is 6
        if not game_started[player] and dice == 6:
            print(f"{player} Can Start The Game!")
            game_started[player] = True
            just_started[player] = True
            if player == "You":
                You["position"] = 1
            else:
                C_player["position"] = 1
                
        # Setting The Moves After Starting The Game        
        if game_started[player]:
            if just_started[player]:
                just_started[player] = False
            else:
                move = dice // 2
                if player == "You":
                    game_over,move,black_hole_hit = move_player(You, move)
                    you_moves += 1
                    if black_hole_hit:
                        you_hole_hit += 1
                else:
                    game_over,move,black_hole_hit = move_player(C_player, move)
                    computer_moves += 1
                    if black_hole_hit:
                        com_hole_hit += 1
                        
                # Display Massages End Of The Game
                if game_over:
                    print("Congratulations! "f"{player} win The Game!")
                    time.sleep(1)
                    print("\nText File Created Successfully..\n")
                    time.sleep(0.5)
                    print("Game Was Ended !\n")
                    winning_player= player
                    break

        # Print The Updated Table
        update_table()
        print(tabulate(mytable, headers="firstrow", tablefmt="psql"))
        
    # Add The Game Summery To The Text File
    current = datetime.now()
    Name = current.strftime('%Y_%m_%d_%H_%M') + '.txt'

    # Open The Text File And Write
    File = open(Name, 'w')

    # Write The Human Player Details
    write = 'Human\nTotal moves :'+ str(you_moves)+ '\nBlack Hole Hits :'+ str(you_hole_hit)
    if winning_player == "You":
        write += '\nWon the game\n'
    else:
        write += '\nLost the game\n'
        
    # Write The Computer Player Details
    write += '\nComputer\nTotal moves :'+ str(computer_moves)+ '\nBlack Hole Hits :'+ str(com_hole_hit)
    if winning_player == "Computer":
        write += '\nWon the game\n'
    else:
        write += '\nLost the game\n'
    File.write(write)

    # Close The Text File
    File.close()
    
    # Setting The Play Again Loop
    play_again = input("Do You Want To Play Again? (yes/no): ").lower()
    if play_again == "yes" or play_again == "y":
        continue
    else:
        break

input()
# End Of The Program
