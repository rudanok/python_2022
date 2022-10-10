# Задание 3. Создайте программу для игры в "Крестики-нолики".

def print_board(board):
    print('-------------')
    for i in range(3):
        print('|', board[i*3], '|', board[i*3 + 1], '|', board[i*3 + 2], '|')
        print('-------------')

def itput_symbol(symbol):
    valid = False
    while not valid:
        user_number = int(input('Введите номер клетки для '+ symbol + ': '))
        if user_number >= 1 and user_number <= 9:
            if (str(board[user_number - 1]) not in 'XO'):
                board[user_number-1] = symbol
                valid = True
            else:
                print('Эта клетка уже занята!')
        else:
            print('Введите число от 1 до 9!')

def check(current_position):
    win_positions = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for item in win_positions:
        if current_position[item[0]] == current_position[item[1]] == current_position[item[2]]:
            return current_position[item[0]]
    return False

def play(board):
    counter = 0
    win = False
    while not win:
        if counter % 2 == 0:
            itput_symbol('X')
        else:
            itput_symbol('O')
        print_board(board)
        counter += 1
        if counter > 4:
            symbol = check(board)
            if symbol:
                print(symbol, 'выиграл!')
                win = True
                break
        if counter == 9:
            print('Ничья!')
            break

board = list(range(1, 10))
print_board(board)
play(board)