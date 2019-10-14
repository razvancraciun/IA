import argparse
from game import Missionaries_and_canibals
from strategies import Random_Strategy
from strategies import Backtracking_Strategy
from strategies import IDDFS_Strategy
from strategies import Strategy
from display import Display
from display import ConsoleDisplay
from display import GuiDisplay
from time import time

ap = argparse.ArgumentParser()
ap.add_argument('-m', '--missionaries', type = int, required = True)
ap.add_argument('-c', '--cannibals', type = int, required = True)
ap.add_argument('-b', '--boat_size', type = int, required = True)
ap.add_argument('-s', '--strategy', choices = [Strategy.random, Strategy.backtracking, Strategy.iddfs], required = True)
ap.add_argument('--depth', type = int,  default = 3)
ap.add_argument('-d', '--display', default = Display.console, choices = [Display.gui, Display.console])
args = ap.parse_args()

def main(missionaries, cannibals, boat_size, strat, depth, display):
    game = Missionaries_and_canibals(missionaries,cannibals,boat_size)
    strategy = Strategy.object(strat,depth,game, Display.object(display))
    strategy.run()


if __name__ == '__main__':
    main(args.missionaries, args.cannibals, args.boat_size, args.strategy, args.depth, args.display)
