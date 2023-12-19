email = input('> ')

if email.count('@') == 1 \
    and email[0] != '@' \
    and email.count('.') > 0 \
    and email.find('.') > email.find('@'):
        print('Да')
else:
    print('Нет')
    
# > test@mail.com
# Да

# > dlska@rtav
# Нет