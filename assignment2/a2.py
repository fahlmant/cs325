#!/usr/bin/env python

from itertools import combinations

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
    # print current_keys

    for comb in current_keys:
        total = 0
        for i in range(0, NUM_TENNIS):
            closests = []
            for j in range(0, len(comb)):
                #  print "i = {}".format(i)
                #  print "j = {}".format(j)
                #  print "len of comb = {}, comb = {}".format(len(comb), comb)
                #  print tennis[i]
                #  print comb[j]
                #  print keys
                #  print keys[comb[j]]
                #  print comb
                closests.append(abs(keys[comb[j]] - tennis[i]))
            total = total + min(closests)
        lengths.append(total)

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
