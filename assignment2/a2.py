#!/usr/bin/env python

from itertools import combinations
from functools import reduce


NUM_LOCKERS = 0
NUM_KEYS = 0
NUM_TENNIS = 0
KEY_ARRAY = TENNIS_ARRAY = []

def read_input(file):
    global NUM_LOCKERS
    global NUM_KEYS
    global NUM_TENNIS
    global KEY_ARRAY
    global TENNIS_ARRAY
    with open(file, "r") as f:
        nums = f.readline().split()
        KEY_ARRAY = [int(x) for x in f.readline().split()]
        TENNIS_ARRAY = [int(x) for x in f.readline().split()]
        NUM_LOCKERS = int(nums[0])
        NUM_KEYS = int(nums[1])
        NUM_TENNIS = int(nums[2])

# Algorithm 1
def alg1(lockers, keys, tennis):
    current_keys = []
    lengths = []
    for i in range(1, NUM_KEYS + 1):
        current_keys = current_keys + (list(combinations(range(0, NUM_KEYS), i)))

    for comb in current_keys:
        total = 0
        current_lockers = [0 for x in range(0,lockers)]
        for x in range(0, len(comb)):
            current_lockers[comb[x] - 1] = 1
        for i in range(0, NUM_TENNIS):
            pos = tennis[i]
            distances = []
            for j in range (0, lockers):
                if(current_lockers[j] == 1):
                    distances.append(((abs(pos - j)), j))
            minimum_distance = reduce(lambda a,b: min(a, b), distances)
            locker_pos = minimum_distance[1]
            if(locker_pos < pos):
                for x in range (locker_pos, pos):
                    current_lockers[x] = 1
            else:
                for x in range (pos, locker_pos):
                    current_lockers[x] = 1
            
        lengths.append(sum(current_lockers))

    print lengths
    return min(lengths)


    # for x in range(0, lockers):
    #  for i in range(0, keys):
        #  for j in range(i, keys):
            #  for k in range(i, j):
                #  if k = i:

                #  elif k < j:

                #  elif k > i






if __name__ == "__main__":
    read_input("./test.txt")
    #  print NUM_LOCKERS
    #  print NUM_KEYS
    #  print NUM_TENNIS
    #  print KEY_ARRAY
    #  print TENNIS_ARRAY
    print alg1(NUM_LOCKERS, KEY_ARRAY, TENNIS_ARRAY)
