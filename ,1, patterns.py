# Right angled triangle pattern:
# Take input:
print("Half Pyrimad Pattern of Stars (*): ")
n = int(input("Enter your number of rows: "))
# Outer loop to handle the number of rows:
for i in range(n):
    # inner loop to handle the number of colums:
    for j in range(i +1):
        # display the result.
        print("* ", end="")
    print()

# Floyds triangle: # floyds triangle is a right-angled triangle with the arrangemnt starting from 1:
# take input from user:
rows = int(input("Enter how many rows you want : "))
number = 1 # Initilise by 1:
print("Flyods triangle.")
# outer loop
for i in range(1, rows +1):
    # inner loop
    for j in range(i + 1):
        #display result
        print(number, end= ' ')
        number = number +1
    print()

# Diamond pattern:
# take input from user:
rowSize = int(input("enter the number of rows:  "))
if rowSize % 2 == 0: # conditions:
    halfDiamRow = int(rowSize / 2)
else:
    halfDiamRow = int(rowSize / 2)+1
space = halfDiamRow - 1
# loop for upper
for i in range(1, halfDiamRow +1):
    #lets start the inner loop
    for j in range(1, space + 1):
        print(end =" ")
    space = space - 1
    num = 1
    for j in range(2 * i - 1):
        print(end=str(num))
        #increse the number value:
        num = num + 1
    print()
space = 1
# loop for the lower part
for i in range(1, halfDiamRow):
    #lets start the inner loop
    for j in range(1, space + 1):
        print(end =" ")
    space = space + 1
    num = 1
    for j in range(1, 2 * (halfDiamRow - i)):
        print(end=str(num))
        #increse the number value:
        num = num + 1
    print()