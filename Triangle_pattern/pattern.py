num = int(input("Enter the number:"))
boarder = input("Enter boarder: ")

for i in range(num):

    if ((i == 0) or (i == num - 1)): # formula to print the top and bottom row

        print(" " * (num - i) + (boarder) * (2 * i + 1))


    else:

        print(" "*(num-i) + (boarder) + (" ")*(2*i-1) + (boarder)) #formula to print the left and right column



