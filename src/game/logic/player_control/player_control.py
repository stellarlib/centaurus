from .standard_control import StandardControl
from .jump_control import JumpControl
from .ranged_control import RangedControl
from .charge_control import ChargeControl
from .action_cost import *


class PlayerControl(object):

    STD = 0
    RANGED = 1
    JUMP = 2
    CHARGE = 3

    str_to_enum = {
        'std': STD,
        'ranged': RANGED,
        'jump': JUMP,
        'charge': CHARGE,
    }

    action_cost = {
        STD: MOVE_COST,
        RANGED: RANGED_COST,
        JUMP: JUMP_COST,
        CHARGE: CHARGE_COST
    }

    def __init__(self, logic):

        self.game = logic.game
        self.logic = logic

        cls = PlayerControl
        self.mode = cls.STD

        self.controls = {
            cls.STD: StandardControl(self),
            cls.RANGED: RangedControl(self),
            cls.JUMP: JumpControl(self),
            cls.CHARGE: ChargeControl(self)
        }

        self._player_turn = True
        self._animating = False

    @property
    def player(self):
        return self.logic.player

    @property
    def active(self):
        return self._player_turn and not self._animating

    @property
    def button_map(self):
        return self.game.buttons

    #####################
    # Routing input #
    #################
    def switch_mode(self, mode_name):

        # this models the panel of buttons where the player toggles between action types

        cls = PlayerControl
        mode = cls.str_to_enum[mode_name]

        if self.mode == mode:

            self.mode = cls.STD

            #print('switched to standard mode')
            self.reset_mode_panel()

        else:

            cost = cls.action_cost[mode]
            if cost > self.player.actions:

                #print("can't switch to ", mode_name, " mode - insufficient player actions")
                button = self.button_map.get_button_by_id(mode_name)
                button.rumble()

            else:

                self.mode = mode
                self.controls[self.mode].init_mode()

                # print('switched to ', mode_name, ' mode')
                self.reset_mode_panel()

                if mode_name != 'std':
                    button = self.button_map.get_button_by_id(mode_name)
                    button.button_down()

    def reset_mode_panel(self):
        [button.button_up() for button in self.button_map.get_button_group('action_mode')]

    def handle_click(self, pos):
        if self.active:
            self.controls[self.mode].handle_click(pos)

    def manual_switch_mode(self, mode_name):
        if self.active:
            self.switch_mode(mode_name)
        else:
            button = self.button_map.get_button_by_id(mode_name)
            button.rumble()

    def manual_turn_end(self):
        if self.active:
            self.rest()
            button = self.button_map.get_button_by_id('skip')
            button.button_down()

    def start_animating(self):
        self._animating = True

    def end_animating(self):
        self._animating = False

    ##########################################################
    # Player controls
    ####################

    def move_player(self, pos):

        def resolve_func():
            self.spend_action(MOVE_COST)
            self.end_animating()

        self.start_animating()
        self.player.start_move(pos, resolve_func)

    def player_exits_level(self, pos):

        def resolve_func():
            self.end_animating()
            self.player.travel_component.travel_to_next_level(pos)
            # get next level according to pos
            # get the new player pos on that level
            # start the new level, put player in new pos
            # refresh the turn so it is player start turn, full AP

        self.start_animating()
        self.player.start_exit_move(pos, resolve_func)

    def jump_player(self, pos):

        def resolve_func():
            self.spend_action(JUMP_COST)
            self.end_animating()

        self.start_animating()
        self.player.start_jump(pos, resolve_func)

    def player_jump_attacks(self, pos):

        foe = self.logic.get_actor_at(pos)

        def resolve_func():
            self.player.melee_attack(foe)
            self.spend_action(JUMP_COST)
            self.end_animating()

        self.start_animating()
        self.player.start_jump_attack(pos, resolve_func)

    def player_attacks(self, pos):

        foe = self.logic.get_actor_at(pos)
        assert foe != self.player

        def resolve_func():
            self.spend_action(MELEE_COST)
            self.end_animating()

        self.start_animating()
        self.player.start_melee_attack(foe, resolve_func)

    def player_ranged_attacks(self, pos):

        foe = self.logic.get_actor_at(pos)
        assert foe != self.player

        def resolve_func():
            self.spend_action(RANGED_COST)
            self.end_animating()

        self.player.start_ranged_attack(pos, resolve_func)

    def charge_player(self, charge_path):

        def resolve_func():
            self.spend_action(CHARGE_COST)
            self.end_animating()

        self.start_animating()
        self.player.start_charge(charge_path, resolve_func)

    ###################################################
    # Game Logic #
    ##############

    def spend_action(self, x):

        self.switch_mode('std')

        assert x <= self.player.actions
        self.player.spend_actions(x)
        if self.player.actions == 0:
            self.end_turn()

    def start_player_turn(self):

        self._player_turn = True
        self.set_up_turn()

    def set_up_turn(self):

        self.player.restore(2)

    def tear_down_turn(self):

        print('player turn over')
        self.logic.start_ai_turn()

    def end_turn(self):
        self.tear_down_turn()
        self._player_turn = False

    def rest(self):
        self.player.restore(1)
        self.end_turn()
