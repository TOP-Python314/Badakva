numb1 = input()
numb2 = input()
x = (((ord(numb1[0]) + int(numb1[1])) % 2 == 0) and ((ord(numb2[0]) + int(numb2[1])) % 2 == 0))
y = (((ord(numb1[0]) + int(numb1[1])) % 2 != 0) and ((ord(numb2[0]) + int(numb2[1])) % 2 != 0))

if x:
    print("да")
elif y:
    print("да")
else: 
    print("нет")
    
# c1
# a6
# нет

# e2
# a8
# да