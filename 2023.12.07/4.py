code = input('> ')
data = {}

while True:
    if code == '':
        print(code.upper())
        code = input('> ')
        keys = list(filter(lambda key: data[key] == code, data))
        for i in data.values():
            for j in i:
                if code in i:
                    print(*keys, sep=' ')
                else:
                    print('! value error !')
                break
            break
        break    
    elif code == ' ':
        data[code] = code[1:4]
    else:
        data[code[0:4]] = code[5:]
        code = input('> ')

# > 1022 ER_DUP_KEY
# > 1016 ER_CANT_OPEN_FILE
# > 1010 ER_DB_DROP_RMDIR
# > 1008 ER_DB_DROP_EXISTS
# >

# > ER_DUP_KEY
# 1022


# > 4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
# > 4108 ER_GIPK_COLUMN_EXISTS
# > 4111 ER_DROP_PK_COLUMN_TO_DROP_GIPK
# >

# > ER_CANT_OPEN_FILE
# ! value error !

