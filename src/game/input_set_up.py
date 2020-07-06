from src.input.button import Button


# TODO initialize the input stuff here


def create_mode_switch_function(game, function_id):

    def func():
        game.logic.player_control.manual_switch_mode(function_id)

    return func


def create_skip_function(game):

    def func():
        game.logic.player_control.manual_turn_end()

    return func


def set_up_buttons(game):

    ranged_button = Button(game, 'ranged', (1, 6), create_mode_switch_function(game, 'ranged'))
    charge_button = Button(game, 'charge', (2, 6), create_mode_switch_function(game, 'charge'))
    jump_button = Button(game, 'jump', (2, 5), create_mode_switch_function(game, 'jump'))

    skip_turn_button = Button(game, 'skip', (-8, 6), create_skip_function(game), simple=True)

    game.buttons.add_button(ranged_button, 'action_mode')
    game.buttons.add_button(charge_button, 'action_mode')
    game.buttons.add_button(jump_button, 'action_mode')

    game.buttons.add_button(skip_turn_button, 'skip')

