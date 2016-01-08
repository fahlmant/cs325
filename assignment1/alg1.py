array = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

length = len(array)
max = 0
num = 0

for j in range (0, length):
    for i in range (0, j):
        num = 0
        for k in range (i, j):
            num = num + array[k]
            if(num > max):
                max = num

print (max)
