import subprocess as s
import random
import time
from tqdm import tqdm


def main():
    strategies = ['random', 'bkt', 'iddfs', 'a_star' ]
    reps = 10
    for strategy in strategies:
        mean_length = 0
        mean_time = 0
        for _ in range(reps):
            nm = random.randint(3,15)
            nc = random.randint(3, nm)
            start_time = time.time()
            output = s.check_output(f'python3 main.py -m {nm} -c {nc} -b 5 -s {strategy}'.split())
            mean_time += (time.time() - start_time) * 1000
            output = output.split(b'\n')
            mean_length += len(output)
        mean_length /= reps
        mean_time /= reps
        print(mean_length, mean_time)

if __name__ == '__main__':
    main()
