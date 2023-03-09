
min = 1001  # low  user
max = 0   # highest user

with open(input("")) as file:
        data = file.readlines()[1:]#read file and skip the first row
        for line in data:
            arr = line.split()
            friend1 = int(arr[0]) # turn left side of arr to integers
            friend = int(arr[1]) #turn right side of arr to intgers
            if friend1 < min:  # find the minimum value in the textfile
               min = friend1
            if friend > max: #find the maximum value in textfile
                max = friend
            list3 = []
        for num in range(min,max+1): # range from the minimum to maximum that was found in the text file
            list2 = []

            for user in data: # check for user in txt file again
                user = user.split()#split users in two groups
                user1 = int((user[0])) #store each side as integers
                user2 = int((user[1]))
                if num == user1:
                    list2.append(user2) #Store user2 in list2
                if num == user2:
                    list2.append(user1) #Store user1 in in list2
            list3.append(list2)# put list2 in list3

            print(num,':', list2)
while True:

        try:
            print("Enter user id in the range 0 to", max,":(""-1 to quit"")")
            enter = int(input(""))
            if enter == -1:
                print("Goodbye!")
                break

            max1 = 0  #hold the num that has the most mutual friends
            recommended = 0 #store recommended figure
            counter = 0 # store number of mutual friends
            if enter > max: # check enter number if greater the max
                print("input must be an int between 0 to", max)
            else:
                for num in list3: # looping through each friend list for each users

                    if counter > max1 and list3.index(num) -1 != enter: #check the number that is most common in lists3 different from enter.
                        max1 = counter
                        print(max1)
                        recommended = list3.index(num) - 1 # saving the user that is associated with the user friend list
                    counter = 0
                    for index in list3[enter]:# looping through the friend list of the user enter
                        if index in num:# if number enter in list
                            counter += 1
                    if counter > max1 and list3.index(num) != enter:# Check if the number f mutual friends is greater than the previous different from the entered number
                        max1 = counter
                        recommended = list3.index(num)
                print("Your suggest friend is : ", recommended)

        except ValueError:
            print('invalid input')











