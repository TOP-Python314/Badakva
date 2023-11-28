numb1 = int(input())
numb2 = int(input())

operation1 = numb1 // numb2
operation2 = numb1 % numb2

a1 = f'{str(numb1) + " делится на " + str(numb2) + " нацело"}'
a2 = f'{"частное: " + str(operation1)}'
b1 = f'{str(numb1) + " не делится на " + str(numb2) + " нацело"}'
b2 = f'{"неполное частное: " + str(operation1)}'
b3 = f'{"остаток: " + str(operation2)}'


if numb2 % 2 == 0:
    print(
        a1,
        a2,
        sep='\n'
)
else:
    print(
        b1,
        b2,
        b3,
        sep='\n'
)
    
# 22
# 5
# 22 не делится на 5 нацело
# неполное частное: 4
# остаток: 2

# 10
# 2
# 10 делится на 2 нацело
# частное: 5
