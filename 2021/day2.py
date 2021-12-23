# Dive! part 1
with open('day2_input.txt','r') as file:
    ins = file.readline()
    horizontal = 0
    depth = 0
    while ins != '':
        direction, amount = ins.split()
        if direction == 'forward':
            horizontal += int(amount)
        elif direction == 'down':
            depth += int(amount)
        elif direction == 'up':
            depth -= int(amount)
        ins = file.readline()

print('horizontal: {0}, dept: {1}, multiply: {2}'.format(horizontal, depth, (horizontal*depth)))

# --------------------------------
# Part 2
with open('day2_input.txt','r') as file:
    ins = file.readline()
    horizontal = 0
    depth = 0
    aim = 0
    while ins != '':
        direction, amount = ins.split()
        if direction == 'forward':
            horizontal += int(amount)
            depth += int(amount) * aim
        elif direction == 'down':
            aim += int(amount)
        elif direction == 'up':
            aim -= int(amount)
        ins = file.readline()

print('horizontal: {0}, dept: {1}, multiply: {2}'.format(horizontal, depth, (horizontal*depth)))
