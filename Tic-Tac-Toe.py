# Tic Tac Toe Grid

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
def moveupdate(x,symbol):
    if x == "1.1" and r2[3] == " ":
        r2[3] = symbol
    elif x == "1.2" and r2[11] == " ":
        r2[11] = symbol
    elif x == "1.3" and r2[19] == " ":
        r2[19] = symbol
    elif x == "2.1" and r5[3] == " ":
        r5[3] = symbol
    elif x == "2.2" and r5[11] == " ":
        r5[11] = symbol
    elif x == "2.3" and r5[19] == " ":
        r5[19] = symbol
    elif x == "3.1" and r8[3] == " ":
        r8[3] = symbol
    elif x == "3.2" and r8[11] == " ":
        r8[11] = symbol
    elif x == "3.3" and r8[19] == " ":
        r8[19] = symbol
    else:
        print('Try a valid move.')
        return True

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
        return True

    elif ask_new_round == 'N':
        print('Thanks for playing!')
        quit()

def end_check(symbol):
    if r2[3] == symbol and r2[11] == symbol and r2[19] == symbol:
        if symbol == "X":
            print('Player 1 Wins!')
        elif symbol == "O":
            print('Player 2 Wins!')
        if status_check():
            return True

    elif r5[3] == symbol and r5[11] == symbol and r5[19] == symbol:
        if symbol == "X":
            print('Player 1 Wins!')
        elif symbol == "O":
            print('Player 2 Wins!')
        if status_check():
            return True
        
    elif r8[3] == symbol and r8[11] == symbol and r8[19] == symbol:
        if symbol == "X":
            print('Player 1 Wins!')
        elif symbol == "O":
            print('Player 2 Wins!')
        if status_check():
            return True
        
    elif r2[3] == symbol and r5[3] == symbol and r8[3] == symbol:
        if symbol == "X":
            print('Player 1 Wins!')
        elif symbol == "O":
            print('Player 2 Wins!')
        if status_check():
            return True
        
    elif r2[11] == symbol and r5[11] == symbol and r8[11] == symbol:
        if symbol == "X":
            print('Player 1 Wins!')
        elif symbol == "O":
            print('Player 2 Wins!')
        if status_check():
            return True
        
    elif r2[19] == symbol and r5[19] == symbol and r8[19] == symbol:
        if symbol == "X":
            print('Player 1 Wins!')
        elif symbol == "O":
            print('Player 2 Wins!')
        if status_check():
            return True
        
    elif r2[3] == symbol and r5[11] == symbol and r8[19] == symbol:
        if symbol == "X":
            print('Player 1 Wins!')
        elif symbol == "O":
            print('Player 2 Wins!')
        if status_check():
            return True
        
    elif r2[19] == symbol and r5[11] == symbol and r8[3] == symbol:
        if symbol == "X":
            print('Player 1 Wins!')
        elif symbol == "O":
            print('Player 2 Wins!')
        if status_check():
            return True

def tie_check():
    if r2[3] != " " and r2[11] != " " and r2[19] != " " and r5[3] != " " and r5[11] != " " and r5[19] != " " and r8[3] != " " and r8[11] != " " and r8[19] != " ":
        print('Draw!')
        if status_check():
            return True



# Running Game

tic_tac_toe()
print(instructions,"\n")
running_game = True

while running_game:

    prompt_p1 = input('Player 1 - Pick a spot: ' )
    while moveupdate(prompt_p1, "X"):
        prompt_p1 = input('Player 1 - Pick a spot: ' )
    tic_tac_toe()
    if end_check("X"):
        continue
    if tie_check():
        continue

    prompt_p2 = input('Player 2 - Pick a spot: ' )
    while moveupdate(prompt_p2, "O"):
        prompt_p2 = input('Player 2 - Pick a spot: ' )
    tic_tac_toe()
    if end_check("O"):
        continue
    if tie_check():
        continue