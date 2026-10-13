from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

class TicTacToe(TwoPlayerGame):
    def __init__(self, players):
        self.players = players
        self.board = [0] * 9
        self.current_player = 1  # Player 1 starts

    def possible_moves(self):
        return [str(i + 1) for i in range(9) if self.board[i] == 0]

    def make_move(self, move):
        self.board[int(move) - 1] = self.current_player

    def unmake_move(self, move):
        self.board[int(move) - 1] = 0

    def lose(self):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        return any(all(self.board[i] == self.opponent_index for i in line) for line in wins)

    def is_over(self):
        return self.lose() or self.possible_moves() == []

    def show(self):
        symbols = ['.', 'O', 'X']  # 0: empty, 1: O, 2: X
        print("\nCurrent board:")
        for i in [6, 3, 0]:
            row = [symbols[self.board[j]] for j in range(i, i + 3)]
            print(" | ".join(row))
        print()

    def scoring(self):
        return -100 if self.lose() else 0

if __name__ == "__main__":
    ai_algo = Negamax(6)
    game = TicTacToe([Human_Player(), AI_Player(ai_algo)])
    game.play()

    if game.lose():
        print(f"\nPlayer {game.opponent_index} wins!")
    else:
        print("\nIt's a draw!")
