class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def alpha_beta(game, depth, alpha, beta, maximizing):
    # Base cases
    if game.current_winner == 'X': return 1
    elif game.current_winner == 'O': return -1
    elif not game.empty_squares(): return 0
    
    if maximizing:
        best_score = float('-inf')
        for move in game.available_moves():
            game.make_move(move, 'X')
            score = alpha_beta(game, depth + 1, alpha, beta, False)
            game.board[move] = ' '
            game.current_winner = None
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if beta <= alpha: break
        return best_score
    else:
        best_score = float('inf')
        for move in game.available_moves():
            game.make_move(move, 'O')
            score = alpha_beta(game, depth + 1, alpha, beta, True)
            game.board[move] = ' '
            game.current_winner = None
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha: break
        return best_score

def find_best_move(game):
    best_score = float('-inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')
    
    for move in game.available_moves():
        game.make_move(move, 'X')
        score = alpha_beta(game, 0, alpha, beta, False)
        game.board[move] = ' '
        game.current_winner = None
        if score > best_score:
            best_score = score
            best_move = move
        alpha = max(alpha, best_score)
    
    return best_move

def play_game():
    game = TicTacToe()
    current_player = 'X'
    print("Tic Tac Toe with Alpha-Beta Pruning")
    game.print_board()
    
    while game.empty_squares():
        if current_player == 'X':
            move = find_best_move(game)
        else:
            valid_move = False
            while not valid_move:
                try:
                    move = int(input(f"Player {current_player}, enter move (0-8): "))
                    if move not in game.available_moves():
                        raise ValueError
                    valid_move = True
                except ValueError:
                    print("Invalid move.")
        
        game.make_move(move, current_player)
        print(f"\nPlayer {current_player} moves to {move}")
        game.print_board()
        
        if game.current_winner:
            print(f"Player {current_player} wins!")
            return
        
        current_player = 'O' if current_player == 'X' else 'X'
    
    print("It's a tie!")

if __name__ == "__main__":
    play_game()
