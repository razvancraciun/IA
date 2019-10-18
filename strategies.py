import random

class A_Star_Strategy:
    def __init__(self, game, display):
        self.game = game
        self.visited = []
        self.parent = {}
        self.display = display

    def run(self):
        self.initialize()
        states = [self.game.state]
        self.parent[self.game.state] = None
        while states:
            self.game.state = states.pop()
            self.visited.append(self.game.state)
            possible_transitions = self.game.possible_transitions()
            possible_transitions = [transition for transition in possible_transitions if transition not in self.visited]
            possible_transitions = [transition for transition in possible_transitions if transition not in states]
            possible_transitions.sort(key = lambda transition: transition[0] + transition[1], reverse = True)
            for transition in possible_transitions:
                states.append(transition)
                self.parent[transition] = self.game.state
            if self.game.is_final_state():
                self.trace()
                return

    def trace(self):
        trace = []
        state = self.game.state
        while self.parent[state]:
            trace.append(state)
            state = self.parent[state]
        trace.append(self.game.initial_state)
        trace.reverse()
        self.display.display(trace)

    def initialize(self):
        self.game.reset()
        self.visited = []
        self.parent = {}


class IDDFS_Strategy:
    def __init__(self, game, display, depth_step = 3):
        self.game = game
        self.visited = []
        self.parent = {}
        self.depth = {}
        self.depth_step = depth_step
        self.display = display

    def initialize(self):
        self.game.reset()
        self.visited = []
        self.parent = {}
        self.depth = {}
        self.depth[self.game.state] = 0
        self.parent[self.game.state] = None


    def trace(self):
        trace = []
        state = self.game.state
        while self.parent[state]:
            trace.append(state)
            state = self.parent[state]
        trace.append(self.game.initial_state)
        trace.reverse()
        self.display.display(trace)

    def run(self):
        self.initialize()
        shallow = [self.game.state]
        while shallow:
            shallow = self.step(shallow)

    def step(self, shallow):
        deep = []
        while shallow:
            self.game.state = shallow.pop()
            self.visited.append(self.game.state)
            possible_transitions = self.game.possible_transitions()
            possible_transitions = [transition for transition in possible_transitions if transition not in self.visited]
            possible_transitions = [transition for transition in possible_transitions \
                                if transition not in shallow and transition not in deep]
            for transition in possible_transitions:
                self.depth[transition] = self.depth[self.game.state] + 1
                self.parent[transition] = self.game.state
                if self.depth[transition] < self.depth_step:
                    shallow.append(transition)
                else:
                    deep.append(transition)
                if self.game.is_final_state():
                    self.trace()
                    return []
        return deep

class Backtracking_Strategy:
    def __init__(self, game, display):
        self.game = game
        self.visited = []
        self.parent = {}
        self.display = display

    def run(self):
        self.initialize()
        states = [self.game.state]
        self.parent[self.game.state] = None
        while states:
            self.game.state = states.pop()
            self.visited.append(self.game.state)
            possible_transitions = self.game.possible_transitions()
            possible_transitions = [transition for transition in possible_transitions if transition not in self.visited]
            possible_transitions = [transition for transition in possible_transitions if transition not in states]
            for transition in possible_transitions:
                states.append(transition)
                self.parent[transition] = self.game.state
            if self.game.is_final_state():
                self.trace()
                return

    def trace(self):
        trace = []
        state = self.game.state
        while self.parent[state]:
            trace.append(state)
            state = self.parent[state]
        trace.append(self.game.initial_state)
        trace.reverse()
        self.display.display(trace)

    def initialize(self):
        self.game.reset()
        self.visited = []
        self.parent = {}

class Random_Strategy:
    def __init__(self, game, display):
        self.visited = []
        self.game = game
        self.display = display

    def run(self):
        runs = 0
        while runs < 100:
            step = 0
            self.initialize()
            while step < 100:
                possible_transitions = self.game.possible_transitions()
                possible_transitions = [transition for transition in possible_transitions if transition not in self.visited]
                if not possible_transitions:
                    break
                self.game.state = random.choice(possible_transitions)
                self.visited.append(self.game.state)
                if self.game.is_final_state():
                    self.trace()
                    return
                step += 1
            runs += 1

    def initialize(self):
        self.game.reset()
        self.visited = [self.game.state]

    def trace(self):
        self.display.display(self.visited)

class Strategy:
    random = 'random'
    backtracking = 'bkt'
    iddfs = 'iddfs'
    a_star = 'a_star'
    def object(type, depth, game, display):
        if type == Strategy.random:
            return Random_Strategy(game, display)
        if type == Strategy.backtracking:
            return Backtracking_Strategy(game, display)
        if type == Strategy.iddfs:
            return IDDFS_Strategy(game, display, depth)
        if type == Strategy.a_star:
            return A_Star_Strategy(game, display)
