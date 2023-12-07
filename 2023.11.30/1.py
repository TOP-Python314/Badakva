numbers = []
x = 7

while True:
    number = int(input('> '))
    if number % x == 0:
        numbers.append(number)
    else:
        print(' '.join(map(str, reversed(numbers))))
        break

# > 7
# > 14
# > 21
# > 28
# > 30
# 28 21 14 7
