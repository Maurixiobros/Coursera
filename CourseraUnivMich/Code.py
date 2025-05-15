name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_2199168.txt"
handle = open(name)
total = 0
import re
for line in handle:
    line = line.rstrip()
    sum = re.findall('[0-9]+', line)
    for num in sum:
        total += int(num)       
print(total)
