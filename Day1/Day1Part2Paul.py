fid = open('Day1Files/input.txt', 'r')
data = fid.readlines()
fid.close()

for x in range(len(data)):
    for y in range(x + 1, len(data)):
        for z in range(y + 1, len(data)):
            if int(data[x]) + int(data[y]) + int(data[z]) == 2020:
                val1 = int(data[x])
                val2 = int(data[y])
                val3 = int(data[z])
            
print(val1 * val2 * val3)