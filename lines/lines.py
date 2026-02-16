import sys

if len(sys.argv) != 2:
    sys.exit()

if sys.argv[1][len(sys.argv[1]) - 3] != '.' or sys.argv[1][len(sys.argv[1]) - 2] != 'p' or sys.argv[1][len(sys.argv[1]) - 1] != 'y':
    sys.exit()

try:
    int_line_count = 0
    with open(sys.argv[1], 'r') as file:
        for line in file:
            line = line.replace(' ', '')
            if line != '\n' and line and line[0] != '#':
                int_line_count += 1
    print(f"lines = {int_line_count}")

except FileNotFoundError:
    sys.exit()