 Tic Tac Toe Grid

r1 = [" "," "," "," "," "," "," ","|"," "," "," "," "," "," "," ","|"," "," "," "," "," "," "," "]
r2 = [" "," "," "," "," "," "," ","|"," "," "," "," "," "," "," ","|"," "," "," "," "," "," "," "]
r3 = ["_","_","_","_","_","_","_","|","_","_","_","_","_","_","_","|","_","_","_","_","_","_","_"]
r4 = [" "," "," "," "," "," "," ","|"," "," "," "," "," "," "," ","|"," "," "," "," "," "," "," "]
r5 = [" "," "," "," "," "," "," ","|"," "," "," "," "," "," "," ","|"," "," "," "," "," "," "," "]
r6 = ["_","_","_","_","_","_","_","|","_","_","_","_","_","_","_","|","_","_","_","_","_","_","_"]
r7 = [" "," "," "," "," "," "," ","|"," "," "," "," "," "," "," ","|"," "," "," "," "," "," "," "]
r8 = [" "," "," "," "," "," "," ","|"," "," "," "," "," "," "," ","|"," "," "," "," "," "," "," "]
r9 = [" "," "," "," "," "," "," ","|"," "," "," "," "," "," "," ","|"," "," "," "," "," "," "," "]

instructions = '''
Instructions: 

To make a move use any of the following numbers(Positions):
    1.1 = Top Left
    1.2 = Top Middle
    1.3 = Top Right
    2.1 = Middle Left
    2.2 = Middle Middle
    2.3 = Middle Right
    3.1 = Bottom Left
    3.2 = Bottom Middle
    3.3 = Bottom Right'''

# Function to print out Grid
def tic_tac_toe():
    new_line1 = ""    
    new_line2 = ""
    new_line3 = ""    
    new_line4 = ""
    new_line5 = ""    
    new_line6 = ""    
    new_line7 = ""    
    new_line8 = ""    
    new_line9 = ""    

    for x in r1:
        new_line1 += x
    for x in r2:
        new_line2 += x
    for x in r3:
        new_line3 += x
    for x in r4:
        new_line4 += x
    for x in r5:
        new_line5 += x
    for x in r6:
        new_line6 += x
    for x in r7:
        new_line7 += x
    for x in r8:
        new_line8 += x
    for x in r9:
        new_line9 += x    
    print(new_line1)    
    print(new_line2)
    print(new_line3)
    print(new_line4)
    print(new_line5)
    print(new_line6)
    print(new_line7)
    print(new_line8)
    print(new_line9)

# Read Player's Input
def moveupdate_p1(x):
    if x == "1.1":
        r2[3] = "X"
    elif x == "1.2":
        r2[11] = "X"
    elif x == "1.3":
        r2[19] = "X"
    elif x == "2.1":
        r5[3] = "X"
    elif x == "2.2":
        r5[11] = "X"
    elif x == "2.3":
        r5[19] = "X"
    elif x == "3.1":
        r8[3] = "X"
    elif x == "3.2":
        r8[11] = "X"
    elif x == "3.3":
        r8[19] = "X"
    else:
        print('Try a valid move.')

def moveupdate_p2(x):
    if x == "1.1":
        r2[3] = "O"
    elif x == "1.2":
        r2[11] = "O"
    elif x == "1.3":
        r2[19] = "O"
    elif x == "2.1":
        r5[3] = "O"
    elif x == "2.2":
        r5[11] = "O"
    elif x == "2.3":
        r5[19] = "O"
    elif x == "3.1":
        r8[3] = "O"
    elif x == "3.2":
        r8[11] = "O"
    elif x == "3.3":
        r8[19] = "O"
    else:
        print('Try a valid move.')
        




# Check for Victory or Draw

def status_check():
    ask_new_round = input('Would you like to play again? (Y or N) ')
    if ask_new_round == 'Y':
        r2[3] = " "
        r2[11] = " "
        r2[19] = " "
        r5[3] = " "
        r5[11] = " "
        r5[19] = " "
        r8[3] = " "
        r8[11] = " "
        r8[19] = " "
        tic_tac_toe()

    elif ask_new_round == 'N':
        print('Thanks for playing!')
        quit()

def endcheck_p1():
        
    if r2[3] == "X" and r2[11] == "X" and r2[19] == "X":
        print('Player 1 Wins!')
        status_check()

    elif r5[3] == "X" and r5[11] == "X" and r5[19] == "X":
        print('Player 1 Wins!')
        status_check()
        
    elif r8[3] == "X" and r8[11] == "X" and r8[19] == "X":
        print('Player 1 Wins!')
        status_check()
        
    elif r2[3] == "X" and r5[3] == "X" and r8[3] == "X":
        print('Player 1 Wins!')
        status_check()
        
    elif r2[11] == "X" and r5[11] == "X" and r8[11] == "X":
        print('Player 1 Wins!')
        status_check()
        
    elif r2[19] == "X" and r5[19] == "X" and r8[19] == "X":
        print('Player 1 Wins!')
        status_check()
        
    elif r2[3] == "X" and r5[11] == "X" and r8[19] == "X":
        print('Player 1 Wins!')
        status_check()
        
    elif r2[19] == "X" and r5[11] == "X" and r8[3] == "X":
        print('Player 1 Wins!')

        

def endcheck_p2():

    if r2[3] == "O" and r2[11] == "O" == "O" and r2[19] == "O":
        print('Player 2 Wins!')
        status_check()
        
    elif r5[3] == "O" and r5[11] == "O" and r5[19] == "O":
        print('Player 2 Wins!')
        status_check()
        
    elif r8[3] == "O" and r8[11] == "O" and r8[19] == "O":
        print('Player 2 Wins!')
        status_check()
        
    elif r2[3] == "O" and r5[3] == "O" and r8[3] == "O":
        print('Player 2 Wins!')
        status_check()
        
    elif r2[11] == "O" and r5[11] == "O" and r8[11] == "O":
        print('Player 2 Wins!')
        status_check()
        
    elif r2[19] == "O" and r5[19] == "O" and r8[19] == "O":
        print('Player 2 Wins!')
        status_check()
        
    elif r2[3] == "O" and r5[11] == "O" and r8[19] == "O":
        print('Player 2 Wins!')
        status_check()
        
    elif r2[19] == "O" and r5[11] == "O" and r8[3] == "O":
        print('Player 2 Wins!')
        status_check()        

def tie_check():
    if r2[3] != " " and r2[11] != " " and r2[19] != " " and r5[3] != " " and r5[11] != " " and r5[19] != " " and r8[3] != " " and r8[11] != " " and r8[19] != " ":
        print('Draw!')
        status_check()



# Running Game

tic_tac_toe()
print(instructions,"\n")

while True:

    prompt_p1 = input('Player 1 - Pick a spot: ' )
    moveupdate_p1(prompt_p1)
    tic_tac_toe()
    endcheck_p1()
    tie_check()

    prompt_p2 = input('Player 2 - Pick a spot: ' )
    moveupdate_p2(prompt_p2)
    tic_tac_toe()
    endcheck_p2()
    tie_check()
