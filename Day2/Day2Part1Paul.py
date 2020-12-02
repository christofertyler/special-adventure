fid = open('Day2Files/input.txt', 'r')
data = fid.readlines()
fid.close()

valid = 0

for x in range(len(data)):
    data[x] = str.split(data[x])
    data[x][0] = str.split(data[x][0], '-')
    data[x][1] = str.split(data[x][1], ':')[0]
    if int(data[x][0][0]) <= data[x][2].count(data[x][1]) <= int(data[x][0][1]):
        valid += 1
        
print(valid)