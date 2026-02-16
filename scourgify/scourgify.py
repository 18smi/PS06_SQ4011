import sys
import csv

if len(sys.argv) != 3:
    sys.exit()

try:
    with open(sys.argv[2], 'a') as output_file:
        with open(sys.argv[1], 'r') as input_file:
            for row in input_file:
                row = row.replace('"', '').replace(' ', '').strip().split(',')
                str_temp = row[0]
                row[0] = row[1]
                row[1] = str_temp
                row = ", ".join(row)
                print(row)
                
                output_file.write(row + '\n') 

except FileNotFoundError:
    sys.exit()

#input = "last, first", "house"

#output = "first", "last", "house"

