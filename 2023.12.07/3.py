list1 = []
list2 = []
x = 0

num1 = input('> ')
num2 = input('> ')

list1.append(num1)
list2.append(num2)

for i in enumerate(num2):
    if i in enumerate(num1):
        x += 1
        
if x == len(num2):
    print('Да')
else:
    print('Нет')
    
# > 1 2 3 4
# > 1 2
# да

# > 1 2 3 4
# > 2 4
# нет

