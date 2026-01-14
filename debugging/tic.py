#!/usr/bin/python3

def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board.

    Parameters:
    board (list of list of str): The 3x3 game board.

    Returns:
    None
    """
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)


def check_winner(board):
    """
    Checks whether there is a winning condition on the board.

    Parameters:
    board (list of list of str): The 3x3 game board.

    Returns:
    bool: True if a player has won, False otherwise.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


def check_draw(board):
    """
    Checks whether the game has ended in a draw.

    Parameters:
    board (list of list of str): The 3x3 game board.

    Returns:
    bool: True if the board is full and no winner exists.
    """
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    """
    Runs the Tic-Tac-Toe game loop.

    Handles player turns, input validation, win detection,
    and draw detection.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            if row not in range(3) or col not in range(3):
                print("Invalid position. Row and column must be 0, 1, or 2.")
                continue

        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    """
    Entry point of the program.
    """
    tic_tac_toe()
