import subprocess as s

def main():
    f = open('boat_size.txt', 'w')
    for nm in range(3,16):
        for nc in range(3,nm + 1):
            for boat_size in range(2,6):
                output = s.check_output(f'python3 main.py -m {nm} -c {nc} -b {boat_size} -s a_star'.split())
                if len(output) > 0:
                    f.write(str(nm) + ' ' + str(nc) + ' ' + str(boat_size) + '\n')
    f.close()

if __name__ == '__main__':
    main()
