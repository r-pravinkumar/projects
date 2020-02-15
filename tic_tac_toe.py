import random

x_value = 'x'
o_value = 'o'  # type: str
position_list = [1 * i for i in range(1, 10)]
player_chosen = input('Who do you want to be (X/O)?\n')
if player_chosen == 'X' or player_chosen == 'x':
    print('Player Chose X!')
    human_value = x_value
    computer_value = o_value
else:
    print('Player Chose O!')
    human_value = o_value
    computer_value = x_value

twoD_arr = [[' ' for i in range(3)] for j in range(3)]


def update_position_list(value):
    position_list.remove(value)


def get_player_value(player):
    if player == 'human':
        return human_value
    else:
        return computer_value


def get_board():
    print('TIC TAC TOE Board\n')
    print(' ' + twoD_arr[0][0] + ' | ' + twoD_arr[0][1] + ' | ' + twoD_arr[0][2])
    print('-----------')
    print(' ' + twoD_arr[1][0] + ' | ' + twoD_arr[1][1] + ' | ' + twoD_arr[1][2])
    print('-----------')
    print(' ' + twoD_arr[2][0] + ' | ' + twoD_arr[2][1] + ' | ' + twoD_arr[2][2])


def get_value_to_board(value_position, current_player):
    current_player_value = get_player_value(current_player)
    if value_position <= 3:
        twoD_arr[0][value_position - 1] = current_player_value
    elif 3 < value_position <= 6:
        twoD_arr[1][value_position - 4] = current_player_value
    elif 6 < value_position <= 9:
        twoD_arr[2][value_position - 7] = current_player_value
    update_position_list(value_position)
    get_board()


def get_player_move():
    player = 'human'
    print('Available positions are: ', position_list)
    position = int(input('Enter your position?\n'))
    get_value_to_board(position, player)
    return check_match_status(player)


''' no logic written. Just choosing a random value from position and printing the value on the position'''


def get_computer_move():
    player = 'PC'
    computer_position = random.choices(position_list)
    print(computer_position)
    get_value_to_board(computer_position[0], player)
    return check_match_status(player)


def check_match_status(player):
    won_status = False
    current_player_value = get_player_value(player)
    if ((twoD_arr[0][0] == current_player_value and twoD_arr[0][1] == current_player_value and
         twoD_arr[0][2] == current_player_value) or
            (twoD_arr[1][0] == current_player_value and twoD_arr[1][1] == current_player_value and
             twoD_arr[1][2] == current_player_value) or
            (twoD_arr[2][0] == current_player_value and twoD_arr[2][1] == current_player_value and
             twoD_arr[2][2] == current_player_value) or
            (twoD_arr[0][0] == current_player_value and twoD_arr[1][0] == current_player_value and
             twoD_arr[2][0] == current_player_value) or
            (twoD_arr[0][1] == current_player_value and twoD_arr[1][1] == current_player_value and
             twoD_arr[2][1] == current_player_value) or
            (twoD_arr[0][2] == current_player_value and twoD_arr[1][2] == current_player_value and
             twoD_arr[2][2] == current_player_value) or
            (twoD_arr[0][0] == current_player_value and twoD_arr[1][1] == current_player_value and
             twoD_arr[2][2] == current_player_value) or
            (twoD_arr[0][2] == current_player_value and twoD_arr[1][1] == current_player_value and
             twoD_arr[2][0] == current_player_value)):
        won_status = True
        if player == 'human':
            print('You won!! Congratulations')
        else:
            print('PC won over you.')
    return won_status


def can_board_hold():
    return len(position_list) > 0


get_board()
loop = True
while loop:
    if can_board_hold():
        player_status = get_player_move()
        if not player_status and can_board_hold():
            computer_status = get_computer_move()
            if not computer_status and can_board_hold():
                loop = True
            else:
                loop = False
        else:
            loop = False
    else:
        loop = False
