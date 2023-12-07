numbers = input('> ')
if len(numbers) != 6:
	print('Вы ввели слишком много цифр!')
else:
	num1 = sum(map(int, numbers[:3]))
	num2 = sum(map(int, numbers[3:]))
	
	if num1 == num2:
		print('Да')
	else:
		print('Нет')
        
# > 172451
# 'Да'
# > 475843
# 'Нет'

