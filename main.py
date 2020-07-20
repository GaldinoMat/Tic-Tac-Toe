# prints the tic-tac-toe table
def table_printer(tic_tac_toe_table):
    print("---------")
    for i in range(len(tic_tac_toe_table)):
        print("| " + " ".join(tic_tac_toe_table[i]) + " |")
    print("---------")


# generates the tic-tac-toe table with a predetermined input from player
def generate_table(list_input, tic_tac_toe_table):
    for _ in range(3):
        if _ == 0:
            tic_tac_toe_table.append([first_line for first_line in list_input[:3]])
        elif _ == 1:
            tic_tac_toe_table.append([second_line for second_line in list_input[3:6]])
        else:
            tic_tac_toe_table.append([third_line for third_line in list_input[6:]])

    return tic_tac_toe_table


# checks which side will take place in filling the predetermined board
def table_filler(cl_place, ln_place, tic_tac_toe_table):
    x_check = 0
    o_check = 0

    for lines in tic_tac_toe_table:
        for letter in lines:
            if letter == 'X':
                x_check += 1
            elif letter == 'O':
                o_check += 1

    if x_check == o_check:
        tic_tac_toe_table[ln_place][cl_place] = 'X'
    if x_check == o_check + 1:
        tic_tac_toe_table[ln_place][cl_place] = 'O'


# checks if the user input returns an occupied place in the matrix
def check_matrix_place(table_column, table_line, tic_tac_toe_table):
    ln_matrix_place, cl_matrix_place = 0, 0

    if table_column == 2:
        cl_matrix_place += 1
    elif table_column == 3:
        cl_matrix_place += 2

    if table_line == 1:
        ln_matrix_place += 2
    elif table_line == 2:
        ln_matrix_place += 1

    place = tic_tac_toe_table[ln_matrix_place][cl_matrix_place]
    if place == 'X' or place == 'O':
        print("This cell is occupied! Choose another one!")
        return False
    else:
        table_filler(cl_matrix_place, ln_matrix_place, tic_tac_toe_table)
        return True


# makes all three checks and add them to collection
# if at least one of them returns false, return false and the while loop continues
def check_for_errors(string, table):
    if string[0].isdigit() and string[1].isdigit():
        if all([int(item) <= 3 for item in string]):
            if check_matrix_place(int(string[0]), int(string[1]), table):
                return True
        print("Coordinates should be from 1 to 3!")
        return False
    print("You should enter numbers!")
    return False


# checks win conditions after ALL user inputs
def check_win_condition(tic_tac_toe_table):

    conditions = (check_line(tic_tac_toe_table), check_column(tic_tac_toe_table), check_diagonal(tic_tac_toe_table))

    if any(conditions):
        return
    else:
        # runs through all indexes of table and return true if any " " is found
        if any(char == " " for line in tic_tac_toe_table for char in line):
            print("Game not finished")
        else:
            print("Draw")


# checks row for win condition
def check_line(tic_tac_toe_table):
    for line in tic_tac_toe_table:
        # check if line has blank characters, if not check if the chars in it are equal
        if all(ch != ' ' for ch in line):
            if all(ch == 'X' for ch in line):
                print("X wins")
                return True
            elif all(ch == 'O' for ch in line):
                print("O wins")
                return True

    return False


# checks column for win condition
def check_column(tic_tac_toe_table):
    column_index = 0
    # runs through matrix' line
    for _ in range(len(tic_tac_toe_table)):
        column_list = []
        line_index = 0
        # runs through matrix' column
        for _ in range(len(tic_tac_toe_table)):
            # appends to temp list value in table's specific index
            column_list.append(tic_tac_toe_table[line_index][column_index])
            line_index += 1
        column_index += 1

        # makes same check from check_line
        if all(ch != " " for ch in column_list):
            if all(ch == 'X' for ch in column_list):
                print("X wins")
                return True
            elif all(ch == 'O' for ch in column_list):
                print("O wins")
                return True
    return False


# gets both diagonals and store in a variable
def check_diagonal(tic_tac_toe_table):
    # gets diagonal from matrix
    diagonal_1 = [letter[index] for index, letter in enumerate(tic_tac_toe_table)]
    diagonal_2 = [letter[-index - 1] for index, letter in enumerate(tic_tac_toe_table)]

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


def main():
    user_input = [letter for letter in input("Enter the coordinates: ").replace("_", " ")]
    table = []
    generate_table(user_input, table)
    table_printer(table)

    user_input = [num for num in input("Enter the coordinates: ").split()]

    while check_for_errors(user_input, table) is not True:
        user_input = [num for num in input("Enter cells: ").split()]

    table_printer(table)
    check_win_condition(table)


if __name__ == "__main__":
    main()
