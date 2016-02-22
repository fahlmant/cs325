import sys

def div_and_con(array):
    pass

def method3(array1, array2):

    a1 = [(array1[x], 1) for x in array1]
    negarray = [-x for x in array2]
    print(a1)
    print(negarray)
    a2 = [(negarray[x], 2) for x in negarray]
    biglist = a1 + a2
    sort(biglist) #by first value
    min_num = sys.maxint
    for x in range len(biglist)
    if(biglist[x][0] != biglist[x+1][0]):
        min_num = min(abs(min_num), abs(biglist[x] - biglist[x-1])



if __name__ == "__main__":
    array1 = [0, 5, 12, 4]
    array2 = [12, -2, 7, 9]
    method3(array1, array2)
