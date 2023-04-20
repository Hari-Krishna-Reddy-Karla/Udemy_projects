sum = 0
evensum = 0
for number in range(1, 101):
    sum += number
for number in range(2, 101, 2):
    evensum += number
print(sum)
print(evensum)