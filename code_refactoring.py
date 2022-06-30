import os
from time import time
from random import randint
cur_dir = os.path.dirname(__file__)
file_name = os.path.join(cur_dir, 'random_numbers.txt')
a = time()

random_numbers = []
with open(file_name, 'w') as f:
    for i in range(5000000):
        random_numbers.append(str(randint(0, 9999)))
        
    f.writelines(random_numbers)

b = time()
print('Execution time: {}'.format(b - a))