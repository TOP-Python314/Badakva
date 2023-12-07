numbers = []
stop_number = 00

while True:
    number = int(input('> ')) 
    if number > 0:
        numbers.append(number)

    elif number == stop_number:
        print(sum(numbers))
        break
        
# > 8
# > -2
# > 6
# > -10
# > 7
# > 20
# > 00
# 41