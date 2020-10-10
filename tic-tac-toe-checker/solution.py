# https://www.codewars.com/kata/525caa5c1bf619d28c000335/train/python

def is_solved(board):
    if found_winning_row(board) != -1:
        return found_winning_row(board)

    elif found_winning_column(board) != -1:
        return found_winning_column(board)

    elif found_diagonal_winner(board) != -1:
        return found_diagonal_winner(board)

    elif not is_finished(board):
        return -1

    elif is_finished(board):
        return 0


def is_finished(board):
    for row in board:
        for num in row:
            if num == 0:
                return False

    return True


def found_winning_row(board):
    for row in board:
        counter = 0
        row_sum = 0
        for num in row:
            if num != 0:
                row_sum += num
                counter += 1

        if row_sum == 3 and counter == 3:
            return 1
        elif row_sum == 6 and counter == 3:
            return 2

    return -1


def found_winning_column(board):
    for column in range(0, len(board)):
        column_sum = 0
        counter = 0
        for row in range(0, len(board)):
            if board[row][column] != 0:
                column_sum += board[row][column]
                counter += 1

        if column_sum == 3 and counter == 3:
            return 1
        elif column_sum == 6 and counter == 3:
            return 2

    return -1


def found_diagonal_winner(board):
    left_diagonal_nums = []
    right_diagonal_nums = []

    for column in range(0, len(board)):
        for row in range(0, len(board)):
            if board[row][column] != 0:
                if row == 0 and column == 0:
                    left_diagonal_nums.append(board[row][column])
                if row == 2 and column == 0:
                    right_diagonal_nums.append(board[row][column])
                if row == 0 and column == 2:
                    right_diagonal_nums.append(board[row][column])
                if row == 2 and column == 2:
                    left_diagonal_nums.append(board[row][column])
                if row == 1 and column == 1:
                    left_diagonal_nums.append(board[row][column])
                    right_diagonal_nums.append(board[row][column])

    if sum(left_diagonal_nums) == 3 or sum(right_diagonal_nums) == 3 and len(left_diagonal_nums) == 3:
        return 1
    if sum(right_diagonal_nums) == 6 or sum(left_diagonal_nums) == 6 and len(right_diagonal_nums) == 3:
        return 2
    else:
        return -1
