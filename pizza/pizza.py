import sys
import csv
from tabulate import tabulate


if len(sys.argv) != 2:
    sys.exit()

if sys.argv[1][len(sys.argv[1]) - 4] != '.' or sys.argv[1][len(sys.argv[1]) - 3] != 'c' or sys.argv[1][len(sys.argv[1]) - 2] != 's' or sys.argv[1][len(sys.argv[1]) - 1] != 'v':
    sys.exit()



try:
    with open(sys.argv[1], 'r') as file:
        body = list(csv.DictReader(file))
        print(tabulate(body, headers="keys", tablefmt="grid"))
        
        

except FileNotFoundError:
    sys.exit()
