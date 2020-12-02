fid = open('input.txt', 'r')
data = fid.readlines()
fid.close()

for x in range(1, len(data)):
    for y in range(x, len(data)):
        for z in range(y, len(data)):
            if int(data[x]) + int(data[y]) + int(data[z]) == 2020:
                val1 = int(data[x])
                val2 = int(data[y])
                val3 = int(data[z])
print("a: " + str(val1))
print("b: " + str(val2))
print("c: " + str(val3))
print(val1 * val2 * val3)