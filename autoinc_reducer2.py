import sys

# Create a dictionary to map words to counts
acc_rec = {}

# Get input from stdin
for line in sys.stdin:
    # Remove spaces from beginning and end of the line
    line = line.strip()

    # parse the input from mapper.py
    line = line.split('\t')
    make = line[0]
    year = line[1]
    count = line[2]

    count = int(count)

    try:
        acc_rec[(make, year)] = acc_rec[(make, year)] + count
    except:
        acc_rec[(make, year)] = count

for make, year in acc_rec.keys():
    print('%s\t%s\t%s' % (make, year, acc_rec[(make, year)]))