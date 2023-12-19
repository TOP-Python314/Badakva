words = input('> ')
list1 = []

while True:
    if words == '':
        break
    else:
        list1.append(words)
        words = input('> ')
    
a = len(list1)
x1 = ' и '.join(list1)
x2 = list1[-1] 
y1 = ', '.join(list1[:2])
y2 = ', '.join(list1[:-1])

if a < 3:
    print(x1)
elif a < 4:
    print(f'{y1 + " и " + x2}')
else:
    print(f'{y2 + " и " + x2}')

# > груша
# >
# груша

# > груша
# > яблоко
# >
# груша и яблоко

# > груша
# > яблоко
# > слива
# >
# груша, яблоко и слива

# > груша
# > яблоко
# > слива
# > банан
# >
# груша, яблоко, слива и банан
