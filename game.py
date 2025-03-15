from gameparts.parts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def save_result(result):
    file = open('results.txt', 'a', encoding='utf-8')
    file.write(result + '\n')
    file.close()


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()  # Отрисовать поле в терминале.

    while running:
        print(f'Ход делают {current_player}')

        while True:
            try:
                row = int(
                    input(f'Введите номер строки от 1 до {game.field_size}: ')
                    ) - 1
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError

                column = int(
                    input(f'Введите номер столбца от 1 до {game.field_size}: ')
                    ) - 1
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError

                if game.board[row][column] != ' ':
                    raise CellOccupiedError

            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print(
                    'Пожалуйста, введите значения для строки и столбца заново.'
                )
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print(
                    'Пожалуйста, введите значения для строки и столбца заново.'
                )
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
                continue
            else:
                break

        game.make_move(row, column, current_player)
        game.display()
        if game.check_win(current_player):
            winner = f'Победили {current_player}.'
            print(winner)
            save_result(winner)
            running = False
        elif game.is_board_full():
            draw = 'Ничья!'
            print(draw)
            save_result(draw)
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
