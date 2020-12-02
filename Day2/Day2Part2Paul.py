fid = open('Day2Files/input.txt', 'r')
data = fid.readlines()
fid.close()

valid = 0

for x in range(len(data)):
    data[x] = str.split(data[x])
    data[x][0] = str.split(data[x][0], '-')
    data[x][1] = str.split(data[x][1], ':')[0]
    firstChar = data[x][2][int(data[x][0][0]) - 1]
    secondChar = data[x][2][int(data[x][0][1]) - 1]
    if (firstChar == data[x][1] or secondChar == data[x][1]) and not (secondChar == firstChar):
        valid += 1
        
print(valid)