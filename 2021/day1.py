# Sonar Sweep part 1
with open('day1_input.txt','r') as file:
    pre = file.readline()
    curr = file.readline()
    count = 0
    while curr != '':
        if int(curr) > int(pre):
            count += 1
        pre = curr
        curr = file.readline()

print(count)
# -----------------------------------
# Part 2
with open('day1_input.txt','r') as file:
    win_1 = file.readline()
    win_2 = file.readline()
    win_3 = file.readline()
    win_4 = file.readline()
    sum_pre = int(win_1) + int(win_2) + int(win_3)
    count = 0
    while win_4 != '':
        sum_curr = int(win_2) + int(win_3) + int(win_4)
        if sum_curr > sum_pre:
            count += 1
        sum_pre = sum_curr
        win_1 = win_2
        win_2 = win_3
        win_3 = win_4
        win_4 = file.readline()

print(count)