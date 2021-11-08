import csv
from typing import Tuple

header = ['first name: ', 'last name: ', 'job title: ', 'company: ']
a = input('first name: ')
b = input('last name: ')
c = input('job title: ')
d = input('company: ')
data = [a,b,c,d]
#writer.writerow(data)
with open('PRG08 Exercise 02.csv', 'a', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    # writer.writerow(header)

    # write the data
    writer.writerow(data)
