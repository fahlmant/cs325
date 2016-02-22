import sys

def summation(array, type):
    sum = 0
    sum_array = []
    if type == "prefix":
        for i in range(len(array)):
            sum = sum + array[i]
            sum_array.append(sum)
    elif type == "suffix":
        for i in range(len(array), 0, -1):
            sum = sum + array[i]
            sum_array.append(sum)

    return sum_array


def div_and_con(array):
    pass

def method1(array1, array2):
    pass

def method2(array1, array2):
    pass

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
    array1 = [0, 5, 12, 4]
    array2 = [12, -2, 7, 9]
    array3 = [31, -41, 59, 26, -53]
    array4 = [58, -6, 97, -93, -23]

    # get summations of the prefix and suffix

    print array1
    print summation(array1, 'prefix')
    print summation(array1, 'suffix')

    # print method3(summation(array1), summation(array2))
    print method3(summation(array3), summation(array4))
