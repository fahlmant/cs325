import sys

def summation(array, type):
    sum = 0
    sum_array = []
    if type == "prefix":
        for i in range(len(array)):
            sum = sum + array[i]
            sum_array.append(sum)
    elif type == "suffix":
        for i in range(len(array) - 1, -1, -1):
            sum = sum + array[i]
            sum_array.insert(0, sum)

    return sum_array


def div_and_con(array):
    pass

def method2(array1, array2):
    s_a1 = sorted(array1)
    s_a2 = sorted(array2)

    len1 = len(array1)
    len2 = len(array2)

    print s_a1
    print s_a2

    best = (0, 0)
    i = 0
    k = len2 - 1

    s = sys.maxint

    while (i < len1 and k >= 0):
        print "i = {}, k = {}".format(i, k)
        if abs(s_a1[i] + s_a2[k]) <= s:
            best = (i, k)
            s = abs(s_a1[i] + s_a2[k])
            print "sum = {}".format(s)

        print s_a1[i] + s_a2[k]
        if s_a1[i] + s_a2[k] > 0:
            k = k - 1
        else:
            i = i + 1

    print s_a1[i], s_a2[k]

    return (s, best)


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



if __name__ == "__main__":
    #  array1 = [0, 5, 12, 4]
    #  array2 = [12, -2, 7, 9]
    array3 = [58, -6, 97, -93, -23]
    array4 = [31, -41, 59, 26, -53]


    # get summations of the prefix and suffix

    #  print summation(array3, 'prefix')
    #  print summation(array4, 'suffix')

    # print method3(summation(array1), summation(array2))
    print method2(summation(array3, 'prefix'), summation(array4, 'suffix'))
