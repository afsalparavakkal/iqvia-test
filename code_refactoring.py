
import os
from time import time
from random import randint

cur_dir = os.path.dirname(__file__)
file_name = os.path.join(cur_dir, 'random_numbers.txt')

a = time()
random_number = ''

f = open(file_name, 'w')

for i in range(5000000):
    random_number = str(randint(0, 9999))
    f.write(random_number+'\n')

f.close()

# with open(file_name, 'w') as f:
#     f.write(random_number)

b = time()
print('Execution time: {}'.format(b - a))

