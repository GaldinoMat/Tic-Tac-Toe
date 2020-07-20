import random


# check lists from column and line methods for blank spaces and 'X' or 'O' wins
def check_lists(list_to_check):
    if all(ch != ' ' for ch in list_to_check):
        if all(ch == 'X' for ch in list_to_check):
            print("X wins")
            return True
        elif all(ch == 'O' for ch in list_to_check):
            print("O wins")
            return True
    return False


class Game:
    table_cells = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]
    player_character = 'X'
    ai_character = 'O'
    player_turn = None
    game_not_finished = True
    game_finished = False
    ai_levels = {1: "easy", 0: "Medium", None: "Hard"}
    ai_difficulty = None

    def __init__(self):
        self.ai_difficulty = 1
        self.player_turn = True
        self.play_game()
        self.user_input = ""

    def play_game(self):
        self.table_printer()
        while self.game_not_finished is True:
            if self.player_turn is True:
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
            self.game_finished = True
            self.game_not_finished = False
            exit()
        else:
            # runs through all indexes of table and return true if any " " is found
            if any(char == " " for line in self.table_cells for char in line):
                return
            else:
                print("Draw")
                self.game_finished = True
                self.game_not_finished = False
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
            if place == 'X' or place == 'O':
                print("This cell is occupied! Choose another one!")
                return False
            else:
                tic_tac_toe_table[ln_matrix_place][cl_matrix_place] = self.player_character
                return True
        else:
            if place == 'X' or place == 'O':
                self.ai_play()
            else:
                tic_tac_toe_table[ln_matrix_place][cl_matrix_place] = self.ai_character
                return

    # checks row for win condition
    def check_line(self):
        for line in self.table_cells:
            line_list = [line]

            check_lists(line_list)

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

            check_lists(column_list)

    # gets both diagonals and store in a variable
    def check_diagonal(self):
        # gets diagonal from matrix
        diagonal_1 = [letter[index] for index, letter in enumerate(self.table_cells)]
        diagonal_2 = [letter[-index - 1] for index, letter in enumerate(self.table_cells)]

        # checks if diagonal has blank spaces, if not check if the chars in it are equal
        if all(s != ' ' for s in diagonal_1) or all(s != ' ' for s in diagonal_2):
            if all(ch == 'X' for ch in diagonal_1):
                print("X wins")
                return True
            elif all(ch == 'O' for ch in diagonal_1):
                print("O wins")
                return True
            if all(ch == 'X' for ch in diagonal_2):
                print("X wins")
                return True
            elif all(ch == 'O' for ch in diagonal_2):
                print("O wins")
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
