#paradox aniversário
from __future__ import print_function, division
from itertools import count
import random
def has_duplicates(t):
    for i in range(len(s)-1):
        if s[i] ==s[i+1]:
            return True
    return False

def random_bdays(n):
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t
def count_matches(num_students, num_simulations):
    count = 0
    for i in range(num_simulations):

def main():
    num_students = 23
    num_simulations = 1000
    count = count_matches(num_students, num_simulations)
    print('after %d simulations' % num_simulations)
    print('with %d students' %num_students)
    print('there were %d simulations with at least one match' % count)
    
if __name__ == '__main__':
    main()
    
    



















