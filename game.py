import random


class Game:
    def __init__(self):
        symbol = ['X', '0']
        self.player_1 = random.choice(symbol)
        symbol.remove(self.player_1)
        self.player_2 = symbol[0]
        self.first = [player for player in [self.player_1, self.player_2] if player == 'X']
        self.second = [player for player in [self.player_1, self.player_2] if player == '0']
        self.board = {
            1: " ", 2: " ", 3: " ",
            4: " ", 5: " ", 6: " ",
            7: " ", 8: " ", 9: " ",
        }
        # for player in [self.player_1, self.player_2]:
        #     if player == ['X']:
        #         self.first = player
        #     elif player == ['0']:
        #         self.second = player

    def print_board(self):
        print(f"{self.board[1]} | {self.board[2]} | {self.board[3]}\n"
              f"{10 * '-'}\n"
              f"{self.board[4]} | {self.board[5]} | {self.board[6]}\n"
              f"{10 * '-'}\n"
              f"{self.board[7]} | {self.board[8]} | {self.board[9]}\n")

    def winning_conditions(self, board, turn):
        # conditions = (board[1] == board[2] == board[3]) \
        #              or (board[2] == board[3] == board[4]) \
        #              or (board[5] == board[6] == board[7]) \
        #              or (board[1] == board[4] == board[7]) \
        #              or (board[2] == board[5] == board[8]) \
        #              or (board[3] == board[6] == board[9]) \
        #              or (board[1] == board[5] == board[9]) \
        #              or (board[3] == board[5] == board[7])

        conditions = [[board[1], board[2], board[3]],
                      [board[2], board[3], board[4]],
                      [board[5], board[6], board[7]],
                      [board[1], board[4], board[7]],
                      [board[2], board[5], board[8]],
                      [board[3], board[6], board[9]],
                      [board[1], board[5], board[9]],
                      [board[3], board[5], board[7]]
                       ]

        for condition in conditions:
            if condition == ['X', 'X', 'X']:
                print(f"Player {self.first} won")
                return True
            elif condition == ['0', '0', '0']:
                print(f"Player {self.second} won")
                return True
            elif turn == 9:
                print("It's a draw")
                return True
            else:
                return False


    def start_game(self, board):
        turn = 1
        filled = []
        p1 = True

        while turn < 10:
            try:
                if p1:
                    choice = int(input(f"Player {self.first} select number: "))
                    if choice in filled:
                        print("Box already taken")
                    else:
                        filled.append(choice)
                        self.board[choice] = 'X'
                        self.print_board()
                        p1 = False
                        turn += 1
                else:
                    choice = int(input(f"Player {self.second} select number: "))
                    if choice in filled:
                        print("Box already taken")
                    else:
                        filled.append(choice)
                        self.board[choice] = '0'
                        self.print_board()
                        p1 = True
                        turn += 1
            except ValueError:
                print("\nYou have not typed anything")
            except IndexError:
                print("\nNumber must be between 1 and 9")
            else:
                if self.winning_conditions(self.board, turn):
                    break
