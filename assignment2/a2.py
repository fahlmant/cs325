#!/usr/bin/env python

from itertools import combinations
from functools import reduce

# NUM_LOCKERS = 0
# NUM_KEYS = 0
# NUM_TENNIS = 0
# KEY_ARRAY = TENNIS_ARRAY = []

def run_tests(function):
    with open('./dp.txt', 'r') as f:
        for i in range(8):
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

def assignment_tests(test_file, function):
    num_lockers = 0
    num_keys = 0
    num_tennis = 0
    key_array = []
    tennis_array = []
    answers = []
    with open(test_file, "r") as f:
        for i in range(8):
            f.readline()
            nums = f.readline().split()
            key_array = [int(x) for x in f.readline().split()]
            tennis_array = [int(x) for x in f.readline().split()]
            num_lockers = int(nums[0])
            num_keys = int(nums[1])
            num_tennis = int(nums[2])
            answer = function(num_lockers, num_keys, num_tennis, key_array, tennis_array)
            # print "{}: Test {} = {}".format(function.__name__, i, answer)
            answers.append(answer)
            f.readline()

    # print "{}: {}".format(function.__name__, answers)

# Algorithm 1
def alg1(num_lockers, num_keys, num_tennis, keys, tennis):
    current_keys = []
    lengths = []
    for i in range(1, num_keys + 1):
        current_keys = current_keys + (list(combinations(range(num_keys), i)))

    for comb in current_keys:
        total = 0
        current_lockers = [0 for x in range(num_lockers)]
        for x in range(0, len(comb)):
            current_lockers[keys[comb[x]] - 1] = 1
        for i in range(0, num_tennis):
            #For each tennis ball
            #Get the position of the tennis ball
            pos = tennis[i] - 1
            distances = []
            #For each locker
            for j in range (num_lockers):
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
    # Init DP table. Set values greater than highest locker.
    DP = [num_lockers + 1 for x in range(num_lockers)]
    KEYS = keys
    TENNIS = tennis

    KEYS.sort()
    TENNIS.sort()
    # print KEYS
    # print TENNIS

    # Setup first key
    if KEYS[0] < TENNIS[0]:
        DP[0] = 0
    else:
        DP[0] = KEYS[0] - TENNIS[0] + 1

    for i in range(1, num_keys):
        for j in range(0, i):
            # calculate least unopened
            least = 0
            for k in range(KEYS[j], KEYS[i]):
                opened = 0
                if KEYS[i] - KEYS[j] == 1:
                    if KEYS[j] in TENNIS:
                        opened = 1
                    else:
                        opened = 0
                else:
                    for n in range(j + 1, i):

                        m = n
                        if n in TENNIS:
                            continue
                        else:
                            while (m+1) not in TENNIS and m < (i - 1):
                                m = m + 1
                            if (m - 1) + 1 > opened:
                                opened = (m - n) + 1
                    least = (i - (j + 1) + 1) - opened


            # Either use or don't use the current key
            if DP[j] + least < DP[i]:
                DP[i] = DP[j] + least

    # Find least function
    if TENNIS[num_tennis - 1] >= KEYS[num_keys - 1]:
        DP[num_keys - 1] = DP[num_keys - 1] + (TENNIS[num_tennis - 1] - KEYS[num_keys - 1]) + 1

    return DP[num_keys - 1]

if __name__ == "__main__":
    run_tests(alg2)
    # assignment_tests('dp_set1.txt', alg1)
    # assignment_tests('dp_set2.txt', alg2)
