#!/usr/bin/env python

from itertools import combinations
from functools import reduce


NUM_LOCKERS = 0
NUM_KEYS = 0
NUM_TENNIS = 0
KEY_ARRAY = TENNIS_ARRAY = []

def run_tests(function):
    with open('./dp.txt', 'r') as f:
        for i in range(0, 4):
            test_num = f.readline().split()
            nums = f.readline().split()
            keys = [int(x) for x in f.readline().split()]
            tennis = [int(x) for x in f.readline().split()]
            answer = function(int(nums[0]), int(nums[1]), int(nums[2]), keys, tennis)
            f.readline()
            correct = int(f.readline())
            if answer != correct:
                print "Test {}, Got {}, expected {}".format(test_num[-1], answer, correct)
            else:
                print "Test {} passed".format(test_num[-1])
            f.readline()

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
def alg1(num_lockers, num_keys, num_tennis, keys, tennis):
    current_keys = []
    lengths = []
    for i in range(1, NUM_KEYS + 1):
        current_keys = current_keys + (list(combinations(range(0, NUM_KEYS ), i)))

    for comb in current_keys:
        total = 0
        current_lockers = [0 for x in range(0,lockers)]
        for x in range(0, len(comb)):
            current_lockers[keys[comb[x]] - 1] = 1
        for i in range(0, NUM_TENNIS):
            #For each tennis ball
            #Get the position of the tennis ball
            pos = tennis[i] - 1
            distances = []
            #For each locker
            for j in range (0, lockers):
                #If the locker is open
                if(current_lockers[j] == 1):
                    #Find the distance between the ball and the locker
                    distances.append(((abs(pos - j)), j))
            #Find the minimum distance between ball and locker
            minimum_distance = reduce(lambda a,b: min(a, b), distances)
            locker_pos = minimum_distance[1]
            if(locker_pos < pos):
                for x in range (locker_pos, pos + 1):
                    current_lockers[x] = 1
            else:
                for x in range (pos, locker_pos):
                    current_lockers[x] = 1
        lengths.append(sum(int (i) for i in current_lockers))

    return min(lengths)

def alg2(num_lockers, num_keys, num_tennis, keys, tennis):
    # Init DP table
    DP = [0 for x in range(0, num_lockers)]
    answer = 0

    # Fill in lockers that have keys
    for k in range(0, num_keys):
        DP[keys[k] - 1] = 1

    for i in range(0, num_lockers):
        min_table = []
        # if DP[i] == 1:
        #     continue
        # else:
        for j in range(0, num_keys):
            # print DP
            # print "j = {}, keys[j] = {}".format(j, keys[j])
            min_table.append(abs(i - (keys[j] - 1)))

        DP[i] = min(min_table) + 1
        print DP


    for t in range(0, num_tennis):
        # print DP
        # print "Adding {}".format(tennis[t] - 1)
        answer = answer + DP[tennis[t] - 1]


    return answer

def alg_test(num_lockers, num_keys, num_tennis, keys, tennis):

    left_most = min(tennis)
    DP = []
    total = 0

    for x in range(0, num_keys):
        DP[x] = (keys[x] - left_most) - 1


    total = DP[-1]
    for i in range(len(DP) - 1, 0):
        total = total - DP[i] 

    print total

if __name__ == "__main__":
    run_tests(alg_test)
