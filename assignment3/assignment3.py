import sys
import math

def test():
    tests = []
    with open('test_cases_with_solutions.txt', 'r') as f:
        for line in f:
            tests.append(eval(line))

    num = 0
    for t in tests:
        data = (t[0], 0, 0, 0)
        answer = div_and_con(data)

        if answer[0] != t[1] or answer[1] != t[2] or answer[2] != t[3]:
            print "test {} FAILED: Got {}, {}, {} "\
                    "expected {}, {}, {}".format(num, answer[0], answer[1], answer[2],
                                                 t[1], t[2], t[3])
        else:
            print "test {} PASSED: GOT {}, {}, {}".format(num, answer[0], answer[1], answer[2])

        num = num + 1

def summation(array, type):
    print array
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
    s_a1 = sorted(array1[0])
    s_a2 = sorted(array2[0])

    sum_a1 = summation(s_a1, 'prefix')
    sum_a2 = summation(s_a2, 'suffix')

    len1 = len(array1)
    len2 = len(array2)

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

    return (array1[0] + array2[0], s, best[0], best[1])


def method3(array1, array2):


    a1 = [(array1[x], 1) for x in range(len(array1))]
    negarray = [-x for x in array2]
    a2 = [(negarray[x], 2) for x in range(len(negarray))]
    biglist = a1 + a2
    biglist.sort() #by first value
    print "a1: {}".format(a1)
    print "a2: {}".format(a2)
    print "biglist: {}".format(biglist)
    min_num = sys.maxint
    for x in range(len(biglist) - 1):
        if(biglist[x][1] != biglist[x+1][1]):
            min_num = min(abs(min_num), abs(biglist[x][0] - biglist[x-1][0]))

    return min_num

def div_and_con(array):
    """
    Basic data structure:

    (array, sum, left index, right index)
    """
    print array
    if len(array[0]) == 1:
        return array

    n = int(math.floor(len(array[0]) / 2))
    print n
    l_data = (array[0][n:], array[1], array[2], array[3])
    l = div_and_con(l_data)
    r_data = (array[0][:n], array[1], array[2], array[3])
    r = div_and_con(r_data)

    m = method2(l, r)

    # Compare left, right and suffix/prefix
    if l[1] < r[1] and l[1] < m[1]:
        return l
    elif r[1] < l[1] and r < m[1]:
        return r
    else:
        return m

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
