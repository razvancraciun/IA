from mc import Missionaries_and_canibals
from mc import Random_Strategy

def main():
    game = Missionaries_and_canibals(3,3,2)
    strategy = Random_Strategy(game)
    while not strategy.game.is_final_state():
        strategy.run()

if __name__ == '__main__':
    main()
