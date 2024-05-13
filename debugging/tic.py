def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if 0 <= row < 3 and 0 <= col < 3:  # Verificar coordenadas dentro del rango
                if board[row][col] == " ":
                    board[row][col] = player
                    player = "O" if player == "X" else "X"
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Invalid coordinates! Please enter row and column values between 0 and 2.")
        except ValueError:
            print("Invalid input! Please enter numeric values.")

    print_board(board)
    print("Player " + player + " wins!")

tic_tac_toe()
