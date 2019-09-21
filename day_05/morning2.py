import sys

input_file = sys.argv[1]

print("Putput :",input_file)
print()

with open(input_file, 'r', newline='') as filereader:
    for row in filereader:
        print("{}".format(row.strip()))

# $python3 morning2.py music2.txt

