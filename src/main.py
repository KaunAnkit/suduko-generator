from generator import generate_full_board, remove_numbers


def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != -1 else "." for num in row))


def main():
    print("Generating Sudoku...\n")

   
    full_board = generate_full_board()

    print("Solved Board:\n")
    print_board(full_board)
    puzzle = remove_numbers(full_board)

    print("\nGenerated Puzzle:\n")
    print_board(puzzle)


if __name__ == "__main__":
    main()

