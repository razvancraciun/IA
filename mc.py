class Missionaries_and_canibals:
    def __init__(self, n_missionaries, n_cannibals, boat_size, strategy):
        self.boat_size = boat_size
        self.initial_state = (n_missionaries, n_cannibals,1,0,0)
        self.final_state = (0, 0, 1, n_missionaries, n_cannibals)
        self.strategy = strategy

    def is_final_state(self,state):
        return state == final_state

    def is_valid_state(self, state,  moved_m, moved_c):
        new_state = self.transition(state, moved_m, moved_c)
        (nm1, nc1, boat_pos, nm2, nc2) = new_state
        if (nm1 > 0 and nc1 > nm1) \
         or (nm2 > 0 and nc2 > nm2):
            return False
        if moved_m > 0 and moved_c > moved_m:
            return False
        if boat_pos == 2 and moved_c >= 0 and moved_m >=0 and moved_c + moved_m > 0:
            return False
        if boat_pos == 1 and moved_c <= 0 and moved_m <= 0 and moved_c + moved_m < 0:
            return False
        return True

    def transition(self, state, moved_m, moved_c):
        new_state = (state[0] + moved_m, state[1] + moved_c, 3 - state[2], state[3] - moved_m , state[4] - moved_c)
        return new_state

    def run():
        strategy.run(self.initial_state)

class Random_Strategy:
    def run(self, state):
        print('running')
