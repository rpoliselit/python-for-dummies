"""
Make a program that calculates the sum
of all multiples of 3 in the range from
1 to 500.
"""
sum = 0
for num in range(1,501):
    if num % 3 == 0:
        sum += num
print(sum)
