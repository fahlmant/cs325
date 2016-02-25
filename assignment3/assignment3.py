import sys
import math

ARRAY = []

def test():
    global ARRAY
    tests = []
    with open('test_cases_with_solutions.txt', 'r') as f:
        for line in f:
            tests.append(eval(line))

    num = 0
    for t in tests:
        ARRAY = t[0]
        # data = (t[0], 0, 0, 0)
        print t[0]
        print "\n"
        answer = div_and_con(t[0])

        # print t[0]
        # print "\n"

        # f_half = t[0][:(len(t[0]) / 2)]
        # print f_half
        # print "\n"
        # s_half = t[0][(len(t[0]) / 2):]
        # print s_half
        # print "\n"

        # print "method: {}, correct: {}".format(method2(f_half, s_half), (t[1], t[2], t[3]))
        # print "method: {}, correct: {}".format(method3(f_half, s_half), (t[1], t[2], t[3]))
        #
        # print "-----------------------------"


        # if answer[0] != t[1] or answer[1] != t[2] or answer[2] != t[3]:
        #     print "test {} FAILED: Got {}, {}, {} "\
        #             "expected {}, {}, {}".format(num, answer[1], answer[2], answer[3],
        #                                          t[1], t[2], t[3])
        # else:
        #     print "test {} PASSED: GOT {}, {}, {}".format(num, answer[0], answer[1], answer[2])
        #

        if answer != t[1]:
            print "test {} FAILED: Got {} expected {}".format(num, answer, t[1])
        # else:
            # print "test {} PASSED: GOT {}, {}, {}".format(num, answer[0], answer[1], answer[2])

        num = num + 1

def summation(array, type):
    #  print array
    s = 0
    sum_array = []
    if type == "prefix":
        for i in range(len(array)):
            s = s + array[i]
            sum_array.append(s)
    elif type == "suffix":
        for i in range(len(array) - 1, -1, -1):
            s = s + array[i]
            sum_array.insert(0, s)

    return sum_array

def method2(array1, array2):
    s_a1 = sorted(array1)
    s_a2 = sorted(array2)

    sum_a1 = summation(s_a1, 'prefix')
    sum_a2 = summation(s_a2, 'suffix')

    len1 = len(array1)
    len2 = len(array2)

    #  if len1 == 1 and len2 == 1:
        #  return (array1[0] + array2[0], sum_a1[0] + sum_a2[0], 0, 1)

    # print s_a1
    # print s_a2

    best = (0, 0)
    i = 0
    k = len2 - 1

    s = sys.maxint

    while (i < len1 and k >= 0):
        # print "i = {}, k = {}".format(i, k)
        if abs(sum_a1[i] + sum_a2[k]) <= s:
            best = (i, k)
            s = abs(sum_a1[i] + sum_a2[k])
            # print "sum = {}".format(s)

        # print sum_a1[i] + sum_a2[k]
        if sum_a1[i] + sum_a2[k] > 0:
            k = k - 1
        else:
            i = i + 1

    # print s_a1[i], s_a2[k]

    # return (s, best[0], best[1])
    return [s]


def method3(array1, array2):

    array1_index = []
    array2_index = []
    # Store indexes for arrays
    for i in range(len(array1[0])):
        array1_index.append((array1[i], 1, i))
    for i in range(len(array2[0])):
        array1_index.append((array2[i], 2, i))

    print "Array 1 = {}\nArray2 = {}".format(array1, array2)

    # a1 = [(array1[x], 1) for x in range(len(array1_index))]
    for x in range(len(array2_index)):
        array2_index[x][0] = -array2_index[x][0]

    # negarray = [(-x[0], x[1], x[2]) for x in array2]
    # a2 = [(negarray[x], 2) for x in range(len(negarray))]
    biglist = array1_index + array2_index
    sorted_biglist = sorted(biglist, key=lambda x: x[0]) #by first value
    print "biglist"
    print sorted_biglist
    # print "a1: {}".format(a1)
    # print "a2: {}".format(a2)
    # print "biglist: {}".format(biglist)
    min_num = sys.maxint
    if len(sorted_biglist) == 1:
        return sorted_biglist[0]
    smallest = (sys.maxint, 0, 0)

    # (a1: 1, a2: 2)

    for x in range(len(sorted_biglist) - 1):
        if(sorted_biglist[x][1] != sorted_biglist[x+1][1]):
            if abs(sorted_biglist[x][0] + sorted_biglist[x+1][0]) < smallest[0]:
                # (returns value and the two index for the closet to 0) I'm so sorry
                smallest = (abs(sorted_biglist[x][0] + sorted_biglist[x+1][0]), sorted_biglist[x][2], (sorted_biglist[x][2] + sorted_biglist[x+1][2]))

    return smallest

def div_and_con(array):
    """
    Basic data structure:

    input: (array)

    return: (sum, left index, righ index)
    """
    #  print array
    if len(array) == 1:
        return (array[0], 0, 0)

    n = int((len(array) / 2))
    #  print n
    # l_data = (array[0][n:], array[1], array[2], array[3])
    l = div_and_con(array[:n])
    # r_data = (array[0][:n], array[1], array[2], array[3])
    r = div_and_con(array[n:])
    m = method3(l, r)

    print "n = {}, l = {}, r = {}, m = {}".format(n, l, r, m)

    # Compare left, right and suffix/prefix

    best = min(l, r, m, key=lambda x: x[0])
    index = (0, 0)

    if l[0] == best:
        index = l[1], l[2]
    elif r[0] == best:
        index = r[1], r[2]
    else:
        index = m[1], m[2]

    return (array[index[0]:index[1]], index[0], index[1])
    # if l[0] < r[0] and l[0] < m[0]:
    #     return l
    # elif r[0] < l[0] and r < m[0]:
    #     return r
    # else:
    #     return m

if __name__ == "__main__":
    #  array1 = [0, 5, 12, 4]
    #  array2 = [12, -2, 7, 9]
    array3 = [58, -6, 97, -93, -23]
    array4 = [31, -41, 59, 26, -53]

    #  test(array3 + array4)
    test()


    # get summations of the prefix and suffix

    #  print summation(array3, 'prefix')
    #  print summation(array4, 'suffix')

    # print method3(summation(array1), summation(array2))
    #  print method2(summation(array3, 'prefix'), summation(array4, 'suffix'))
