from game import Missionaries_and_canibals
from strategies import Random_Strategy
from strategies import Backtracking_Strategy

def main():
    # game = Missionaries_and_canibals(3,3,2)
    game = Missionaries_and_canibals(3,3,2)
    strategy = Backtracking_Strategy(game)
    strategy.run()

if __name__ == '__main__':
    main()
