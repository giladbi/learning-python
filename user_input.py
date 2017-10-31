"""
read 3 numbers from the user and print their total sum

"""



print ("pls enter 3 number")
x = input() #user needs to insert a valu by keyboard
y = input()
z = input()
isintiger = input()

#total = float(x) + float(y) + float(z)
#print ("the total is:",total)

if isintiger == 'y':
    total = int(x)+int(y)+int(z)
    print ("the total is:",total)
else:
    total = float(x)+ float(y)+float(z)
    print ("the total is:",total)