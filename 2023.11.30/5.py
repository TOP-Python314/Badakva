words = input('> ')
x = len(words.replace(' ', ''))
y = x * 30
answer = f'{y // 100}' + ' руб. ' + f'{y % 100}' + ' коп.'
print(answer)

# > шла саша по шоссе и сосала сушку
# 7 руб. 80 коп.

