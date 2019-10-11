import random

class Missionaries_and_canibals:
    def __init__(self, n_missionaries, n_cannibals, boat_size):
        self.boat_size = boat_size
        self.initial_state = (n_missionaries, n_cannibals,1,0,0)
        self.state = self.initial_state
        self.final_state = (0, 0, 2, n_missionaries, n_cannibals)

    def is_final_state(self):
        return self.state == self.final_state

    def is_valid_transition(self, state,  moved_m, moved_c):
        new_state = self.transition(state, moved_m, moved_c)
        (nm1, nc1, boat_pos, nm2, nc2) = new_state
        # people on each shore
        if (nm1 > 0 and nc1 > nm1) \
         or (nm2 > 0 and nc2 > nm2):
            return False

        # people in boat
        if moved_m > 0 and moved_c > moved_m:
            return False
        if abs(moved_m) + abs(moved_c) < 1 or \
        abs(moved_m) + abs(moved_c) > self.boat_size:
            return False

        # boat on the right side
        if boat_pos == 2 and moved_c >= 0 and moved_m >=0 and moved_c + moved_m > 0:
            return False
        if boat_pos == 1 and moved_c <= 0 and moved_m <= 0 and moved_c + moved_m < 0:
            return False
        return True

    def transition(self, state, moved_m, moved_c):
        new_state = (state[0] + moved_m, state[1] + moved_c, 3 - state[2], state[3] - moved_m , state[4] - moved_c)
        return new_state

    def possible_transitions(self):
        (nm1, nc1, boat_pos, nm2, nc2) = self.state
        states = []
        if boat_pos == 1:
            for m in range(nm1 + 1):
                for c in range(nc1 + 1):
                    if m + c > self.boat_size:
                        break
                    transition = self.transition(self.state, 0 - m, 0 - c)
                    if self.is_valid_transition(self.state, 0 - m, 0 - c):
                        states.append(transition)
        else:
            for m in range(nm2 + 1):
                for c in range(nc2 + 1):
                    if m + c > self.boat_size:
                        break
                    transition = self.transition(self.state, m, c)
                    if self.is_valid_transition(self.state, m, c):
                        states.append(transition)
        return states

    def game_over(self):
        if self.state == self.final_state:
            print('You win!')
        else:
            print('You lose')


class Random_Strategy:
    def __init__(self, game):
        self.visited = []
        self.game = game

    def run(self):
        self.initialize()
        print(f'Starting game. State: {self.game.state}')
        step = 0
        while not self.game.is_final_state() and step < 100:
            possible_transitions = self.game.possible_transitions()
            possible_transitions = [transition for transition in possible_transitions if transition not in self.visited]
            if not possible_transitions:
                self.game.game_over()
                return
            self.game.state = random.choice(possible_transitions)
            self.visited.append(self.game.state)
            print(f'Current state: {self.game.state}')
            step += 1
        self.game.game_over()

    def initialize(self):
        self.visited = [self.game.initial_state]
        self.game.state = self.game.initial_state
