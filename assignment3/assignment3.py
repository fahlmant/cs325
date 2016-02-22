import sys

def div_and_con(array):
    pass

def method1(array1, array2):
    pass

def method2(array1, array2):
    pass

def method3(array1, array2):

    a1 = [(array1[x], 1) for x in range(len(array1))]
    negarray = [-x for x in array2]
    print(a1)
    print(negarray)
    a2 = [(negarray[x], 2) for x in range(len(negarray))]
    biglist = a1 + a2
    biglist.sort() #by first value
    print biglist
    min_num = sys.maxint
    for x in range(len(biglist) - 1):
        if(biglist[x][1] != biglist[x+1][1]):
            min_num = min(abs(min_num), abs(biglist[x][0] - biglist[x-1][0]))

    return min_num



if __name__ == "__main__":
    array1 = [0, 5, 12, 4]
    array2 = [12, -2, 7, 9]
    print method3(array1, array2)
