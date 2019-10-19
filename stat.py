import subprocess as s
import random
import time
from tqdm import tqdm
from tabulate import tabulate
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('--reps', type = int, required = True)
args = ap.parse_args()

def valid_boat_size(nm,nc):
    result = []
    f = open('boat_size.txt', 'r')
    line = f.readline()
    while line:
        [m,c,b] = line.split()
        if int(m) == nm and int(c) == nc:
            result.append(b)
        line = f.readline()
    return result

def main(reps):
    strategies = ['random', 'bkt', 'iddfs', 'a_star' ]
    result = []
    for strategy in strategies:
        mean_length = 0
        mean_time = 0
        for _ in tqdm(range(reps)):
            nm = random.randint(3,15)
            nc = random.randint(3, nm)
            boat_size = random.choice(valid_boat_size(nm,nc))
            start_time = time.time()
            output = s.check_output(f'python3 main.py -m {nm} -c {nc} -b {boat_size} -s {strategy}'.split())
            mean_time += (time.time() - start_time) * 1000
            output = output.split(b'\n')
            mean_length += len(output)
        mean_length /= reps
        mean_time /= reps
        result.append([strategy, mean_length, mean_time])

    print(tabulate(result, headers = ['Strategy', 'Avg length(states)', 'Avg time(ms)'], tablefmt='fancy_grid'))

if __name__ == '__main__':
    main(args.reps)
