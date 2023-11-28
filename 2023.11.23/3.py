year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Да")
else:
    print("Нет")
    
# 1995
# Нет

# 2004
# Да