class Board:
    """Класс, который описывает игровое поле."""

    field_size = 3

    def __init__(self):
        self.board = [
            [' ' for _ in range(self.field_size)]
            for _ in range(self.field_size)
        ]

    def make_move(self, row, col, player):
        """Метод, который обрабатывает ходы игроков."""
        self.board[row][col] = player

    def display(self):
        """Метод, который отрисовывает игровое поле."""
        print('-' * 5)
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def is_board_full(self):
        """Метод, который проверяет игровое поле на наличие свободных ячеек"""
        for row in range(self.field_size):
            for column in range(self.field_size):
                if self.board[row][column] == ' ':
                    return False
        return True

    def check_win(self, player):
        """Метод, который проверяет наличие победной комбинации"""
        for row in range(self.field_size):
            if (all(
                    [self.board[row][column] == player
                        for column in range(self.field_size)]
                ) or
                all(
                    [self.board[column][row] == player
                        for column in range(self.field_size)]
                    )):
                return True

        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True

        return False

    def __str__(self):
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )
