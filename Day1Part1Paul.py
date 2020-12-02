fid = open('Day1Files/input.txt', 'r')
data = fid.readlines()
fid.close()

for x in range(len(data)):
    for y in range(x, len(data)):
        if int(data[x]) + int(data[y]) == 2020:
            val1 = int(data[x])
            val2 = int(data[y])
            
print(val1 * val2)
