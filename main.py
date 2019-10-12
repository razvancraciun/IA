import argparse
from game import Missionaries_and_canibals
from strategies import Random_Strategy
from strategies import Backtracking_Strategy
from strategies import IDDFS_Strategy
from time import time

ap = argparse.ArgumentParser()
ap.add_argument('-m', '--missionaries', type = int, required = True)
ap.add_argument('-c', '--cannibals', type = int, required = True)
ap.add_argument('-b', '--boat_size', type = int, required = True)
args = ap.parse_args()

def main(missionaries, cannibals, boat_size):
    game = Missionaries_and_canibals(missionaries,cannibals,boat_size)
    random_strategy = Random_Strategy(game)
    bkt_strategy = Backtracking_Strategy(game)
    iddfs_strategy = IDDFS_Strategy(game)

    before_bkt = time()
    bkt_strategy.run()
    print(f'Bkt took: + {time() - before_bkt}')

    before_iddfs = time()
    iddfs_strategy.run()
    print(f'IDDFS took: {time() - before_iddfs}')


if __name__ == '__main__':
    main(args.missionaries, args.cannibals, args.boat_size)
