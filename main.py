import random


# check lists from column and line methods for blank spaces and 'X' or 'O' wins
def check_lists(*list_to_check):
    if all(ch != ' ' for ch in list_to_check):
        for lists in list_to_check:
            if all(ch == 'X' for ch in lists):
                print("X wins")
                return True
            elif all(ch == 'O' for ch in lists):
                print("O wins")
                return True
    return False


class Game:
    table_cells = [], [], []
    player1_character = ''
    player2_character = ''
    user_vs_ai = False
    ai_vs_user = False
    ai_vs_ai = False
    user_vs_user = False
    player_turn = False
    game_started = False
    ai_levels = {1: "easy", 0: "Medium", None: "Hard"}
    ai_difficulty = None

    def __init__(self):
        """Sets the game difficulty and starts it"""
        self.ai_difficulty = 1
        self.player_turn = True
        self.play_game()
        self.user_input = ""

    def play_game(self):
        self.table_cells = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]
        self.game_starter()
        self.table_printer()
        while self.game_started:
            while self.user_vs_ai:
                if self.player_turn:
                    self.user_input = [num for num in input("Enter the coordinates: ").split()]
                    while self.check_for_errors(self.user_input) is False:
                        self.user_input = [num for num in input("Enter the coordinates: ").split()]
                    self.table_printer()
                    self.check_win_condition()
                    self.player_turn = False
                else:
                    print(f"Making move level \"{self.ai_levels[self.ai_difficulty]}\"")
                    self.ai_play()
                    self.check_win_condition()
                    self.table_printer()
                    self.player_turn = True

            while self.ai_vs_user:
                if self.player_turn is False:
                    print(f"Making move level \"{self.ai_levels[self.ai_difficulty]}\"")
                    self.ai_play()
                    self.check_win_condition()
                    self.table_printer()
                    self.player_turn = True
                else:
                    self.user_input = [num for num in input("Enter the coordinates: ").split()]
                    while self.check_for_errors(self.user_input) is False:
                        self.user_input = [num for num in input("Enter the coordinates: ").split()]
                    self.table_printer()
                    self.check_win_condition()
                    self.player_turn = False

            while self.user_vs_user:
                if self.player_turn:
                    self.user_input = [num for num in input("Enter the coordinates: ").split()]
                    while self.check_for_errors(self.user_input) is False:
                        self.user_input = [num for num in input("Enter the coordinates: ").split()]
                    self.table_printer()
                    self.check_win_condition()
                    self.player_turn = False
                else:
                    self.user_input = [num for num in input("Enter the coordinates: ").split()]
                    while self.check_for_errors(self.user_input) is False:
                        self.user_input = [num for num in input("Enter the coordinates: ").split()]
                    self.table_printer()
                    self.check_win_condition()
                    self.player_turn = True

            while self.ai_vs_ai:
                if self.player_turn:
                    self.ai_play()
                    self.table_printer()
                    self.check_win_condition()
                    self.player_turn = False
                else:
                    self.ai_play()
                    self.table_printer()
                    self.check_win_condition()
                    self.player_turn = True

    # starts the game and sets game_started to True
    def game_starter(self):
        self.user_input = input("Input command: ").split()

        while self.game_started is not True:
            if self.user_input[0] == "start":
                if self.user_input[1] == "easy":
                    self.ai_difficulty = 1
                    self.player1_character = 'X'
                    self.player_turn = False

                    if self.user_input[2] == "easy":
                        self.player2_character = 'O'
                        self.game_started = True
                        self.ai_vs_ai = True
                        self.player_turn = True
                        return
                    elif self.user_input[2] == "user":
                        self.player2_character = 'O'
                        self.game_started = True
                        self.ai_vs_user = True
                        return
                    else:
                        print("Bad parameters!")
                        self.user_input = input("Input command: ").split()

                elif self.user_input[1] == "user":
                    self.player1_character = 'X'

                    if self.user_input[2] == "easy":
                        self.ai_difficulty = 1
                        self.player2_character = 'O'
                        self.game_started = True
                        self.user_vs_ai = True
                        return
                    elif self.user_input[2] == "user":
                        self.player2_character = 'O'
                        self.game_started = True
                        self.user_vs_user = True
                        return
                    else:
                        print("Bad parameters!")
                        self.user_input = input("Input command: ").split()

                else:
                    print("Bad parameters!")
                    self.user_input = input("Input command: ").split()

            elif self.user_input[0] == "exit":
                exit()
            else:
                print("Bad parameters!")
                self.user_input = input("Input command: ").split()

    # prints the table
    def table_printer(self):
        print("---------")
        for i in range(len(self.table_cells)):
            print("| " + " ".join(self.table_cells[i]) + " |")
        print("---------")

    # checks win conditions after ALL user inputs
    def check_win_condition(self):

        conditions = (self.check_line(), self.check_column(),
                      self.check_diagonal())

        if any(conditions):
            self.game_started = False
            self.play_game()
        else:
            # runs through all indexes of table and return true if any " " is found
            if any(char == " " for line in self.table_cells for char in line):
                return
            else:
                print("Draw")
                self.game_started = False
                self.play_game()
                return

    # makes all three checks and add them to collection
    # if at least one of them returns false, return false and the while loop continues
    def check_for_errors(self, string):
        if string[0].isdigit() and string[1].isdigit():
            if all([int(item) <= 3 for item in string]):
                if self.check_matrix_place(int(string[0]), int(string[1]), self.table_cells):
                    return True
            print("Coordinates should be from 1 to 3!")
            return False
        print("You should enter numbers!")
        return False

    # checks if the user input returns an occupied place in the matrix
    def check_matrix_place(self, column_move, line_move, tic_tac_toe_table):
        ln_matrix_place, cl_matrix_place = 0, 0

        # associates move with place in matrix' column
        if column_move == 2:
            cl_matrix_place += 1
        elif column_move == 3:
            cl_matrix_place += 2

        # same as above but with line
        if line_move == 1:
            ln_matrix_place += 2
        elif line_move == 2:
            ln_matrix_place += 1

        # checks if move made by player or AI is valid
        place = tic_tac_toe_table[ln_matrix_place][cl_matrix_place]
        if self.player_turn:
            if place == 'X' or place == 'O' and self.ai_vs_ai is False:
                print("This cell is occupied! Choose another one!")
                return False
            else:
                if self.user_vs_ai or self.user_vs_user or self.ai_vs_ai:
                    tic_tac_toe_table[ln_matrix_place][cl_matrix_place] = self.player1_character
                    return True
                elif self.ai_vs_user:
                    tic_tac_toe_table[ln_matrix_place][cl_matrix_place] = self.player2_character
                    return True
        else:
            if place == 'X' or place == 'O':
                self.ai_play()
            else:
                if self.user_vs_ai or self.user_vs_user or self.ai_vs_ai:
                    tic_tac_toe_table[ln_matrix_place][cl_matrix_place] = self.player2_character
                    return True
                elif self.ai_vs_user:
                    tic_tac_toe_table[ln_matrix_place][cl_matrix_place] = self.player1_character
                    return True

    # checks row for win condition
    def check_line(self):
        for line in self.table_cells:

            if check_lists(line):
                return True
        return False

    # checks column for win condition
    def check_column(self):
        column_index = 0
        # runs through matrix' line
        for _ in range(len(self.table_cells)):
            column_list = []
            line_index = 0
            # runs through matrix' column
            for _ in range(len(self.table_cells)):
                # appends to temp list value in table's specific index
                column_list.append(self.table_cells[line_index][column_index])
                line_index += 1
            column_index += 1

            if check_lists(column_list):
                return True
        return False

    # gets both diagonals and store in a variable
    def check_diagonal(self):
        # gets diagonal from matrix
        diagonal_1 = [letter[index] for index, letter in enumerate(self.table_cells)]
        diagonal_2 = [letter[-index - 1] for index, letter in enumerate(self.table_cells)]

        if check_lists(diagonal_1, diagonal_2):
            return True

        return False

    # makes the AI move
    def ai_play(self):
        # sets random number according to matrix' length and checks if is valid
        ai_move_ln = random.randint(0, len(self.table_cells))
        ai_move_cl = random.randint(0, len(self.table_cells))
        self.check_matrix_place(ai_move_cl, ai_move_ln, self.table_cells)


def main():
    my_game = Game()
    my_game.__init__()


if __name__ == "__main__":
    main()
