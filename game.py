import random
import time

def TicTacToe():
    top_row = ['1' , ' | ' , '2' , ' | ', '3']
    horizontal_break = ['-' , ' - ' , '-' , ' - ', '-']
    mid_row = ['4' , ' | ' , '5' , ' | ', '6']
    bottom_row = ['7' , ' | ' , '8' , ' | ', '9']
    available_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    

    def draw_board():       

        print( ''.join(top_row) + '\n' + ''.join(horizontal_break) + '\n' + ''.join(mid_row) + '\n' + ''.join(horizontal_break) + '\n' + ''.join(bottom_row))

    def acceptable_move(move): #check if input move is in the available moves list
        acceptable = False
        for number in available_moves:
            if number == move:
                acceptable = True

        return acceptable

    def remove_from_available(move): #modify available move list
        available_moves.remove(move)

    def win_checker(): #checks all win conditions for a winner or reports a tie if theres a tie
        x = 'X'
        o = 'O'
        if (top_row[0] == x and top_row[2] == x and top_row[4] == x) or (mid_row[0] == x and mid_row[2] == x and mid_row[4] == x) or (bottom_row[0] == x and bottom_row[2] == x and bottom_row[4] == x):
            return "human" #rows
        elif (top_row[0] == x and mid_row[0] == x and bottom_row[0] == x) or (top_row[2] == x and mid_row[2] == x and bottom_row[2] == x) or (top_row[4] == x and mid_row[4] == x and bottom_row[4] == x):
            return "human" #columns
        elif (top_row[0] == x and mid_row[2] == x and bottom_row[4] == x) or (top_row[4] == x and mid_row[2] == x and bottom_row[0] == x):
            return "human" #diags
        elif (top_row[0] == o and top_row[2] == o and top_row[4] == o) or (mid_row[0] == o and mid_row[2] == o and mid_row[4] == o) or (bottom_row[0] == o and bottom_row[2] == o and bottom_row[4] == o):
            return "AI" #rows
        elif (top_row[0] == o and mid_row[0] == o and bottom_row[0] == o) or (top_row[2] == o and mid_row[2] == o and bottom_row[2] == o) or (top_row[4] == o and mid_row[4] == o and bottom_row[4] == o):
            return "AI" #columns
        elif (top_row[0] == o and mid_row[2] == o and bottom_row[4] == o) or (top_row[4] == o and mid_row[2] == o and bottom_row[0] == o):
            return "AI" #diags
        elif len(available_moves) == 0:
            return "tie"

        return False

    def player_move():
        draw_board()
        player_move = input('Player move: ')        
        
        return player_move
    
    def computer_move():
        print('Computer making a move.')
        time.sleep(1)
        return random.choice(available_moves)

    def change_board(move, player): #for AI and human moves inputted, swap number slot for X and O
        for i in range(len(top_row)):
            if top_row[i] == move and player == "human":
                top_row[i] = 'X'
            elif top_row[i] == move and player == "AI":
                top_row[i] = 'O'
        
        for i in range(len(mid_row)):
            if mid_row[i] == move and player == "human":
                mid_row[i] = 'X'
            elif mid_row[i] == move and player == "AI":
                mid_row[i] = 'O'
        
        for i in range(len(bottom_row)):
            if bottom_row[i] == move and player == "human":
                bottom_row[i] = 'X'
            elif bottom_row[i] == move and player == "AI":
                bottom_row[i] = 'O'


    def move_handler():
        players_turn = True
        game_active = True
        while game_active:
            winner = win_checker()
            if winner == "human":
                draw_board()
                print("You are the winner! Congrats!")
                game_active = False
                break
            elif winner == "AI":
                draw_board()
                print("Game over. Computer wins.")  
                game_active = False
                break
            elif winner == "tie":
                draw_board()
                print("Game over. Tie game.")
                game_active = False
                break

            if players_turn:
                players_move = player_move()
                if players_move == 'q':
                    game_active = False
                acceptable = acceptable_move(players_move)
                if acceptable:
                    change_board(players_move, "human")
                    remove_from_available(players_move)
                    players_turn = False
                else:
                    print("Sorry that move is unavailable, please pick again.")
            else:
                computers_move = computer_move()
                change_board(computers_move, "AI")
                remove_from_available(computers_move)
                players_turn = True



    
    draw_board()
    print("You are X and the computer is O, pick your first move!")
    move_handler()


TicTacToe()
