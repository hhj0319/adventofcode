# Binary Diagnostic Part 1
file = open('day3_input.txt', 'r')
input = [line.rstrip('\n') for line in file]
file.close()

total = len(input)
zeros = [0] * len(input[0])

# counting zeros for each position
for num in input:
    for i in range(len(num)):
        if num[i] == '0':
            zeros[i] += 1

# iterate backwards and calculate gamma and epsilon in decimal
gamma = 0
epsilon = 0
two = 1
for zero in zeros[::-1]:
    if total - zero > zero:
        gamma += two
    else:
        epsilon += two
    two *= 2

print('gamma: {0}, epsilon: {1}, multiply: {2}'.format(gamma, epsilon, gamma * epsilon))

# ---------------------------------------------------------------
# Part 2
def countZeros(in_list, in_index):
    count = 0
    for item in in_list:
        if item[in_index] == '0':
            count += 1
    return count

# find oxygen
oxygen = input
for i in range(len(oxygen[0])):
    zero = countZeros(oxygen, i)
    one = len(oxygen) - zero
    most = '1' if one >= zero else '0'
    oxygen = list(filter(lambda x: x[i] == most, oxygen))

    if len(oxygen) == 1:
        oxygen = oxygen[0]
        break
print(oxygen)
# calculate oxygen in decimal
two = 1
d_oxygen = 0
for bit in oxygen[::-1]:
    if bit == '1':
        d_oxygen += two
    two *= 2
print(d_oxygen)

# find co2
co2 = input
for i in range(len(co2[0])):
    zero = countZeros(co2, i)
    one = len(co2) - zero
    least = '0' if zero <= one else '1'
    co2 = list(filter(lambda x: x[i] == least, co2))

    if len(co2) == 1:
        co2 = co2[0]
        break
print(co2)

# calculate co2 in decimal
two = 1
d_co2 = 0
for bit in co2[::-1]:
    if bit == '1':
        d_co2 += two
    two *= 2
print(d_co2)

print('oxygen: {0}, co2: {1}, multiply: {2}'.format(d_oxygen, d_co2, d_oxygen * d_co2))