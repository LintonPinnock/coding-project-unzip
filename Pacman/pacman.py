
grid = []
with open("init_grid.txt") as reader:
    #read number of rows and columns in grid
    rows, cols = [int(x) for x in reader.readline().strip().split()] #used list comphrension to get the rows and the column as int.

    #read initial position of pacman
    init_pos_r,init_pos_c=[int(x) for x in reader.readline().strip().split()]

    #read initial direction of pacman
    facing = reader.readline().strip()

    #read number of obstacles
    num_obstacles = int(reader.readline().strip())
    
    #creating the grid and appending it to a nested list
    for i in range(rows):
        row = []
        for j in range(cols): 
            row.append('.')
        grid.append(row)
    #loop to obtain the locations of all obstacles in the txt file and places all the obstacles
    obstacles = []
    for k in range(num_obstacles):
        obs_row, obs_col = [int(y) for y in reader.readline().strip().split()]
        grid[obs_row][obs_col]="x"
        obstacles.append((obs_row, obs_col))

    #finding the number of items in the grid 
    num_items = int(reader.readline().strip())
    
    #loop to obtain and place items
    items =[]
    for n in range(num_items):
        itm_row, itm_col = [int(z) for z in reader.readline().strip().split()]
        grid[itm_row][itm_col]="o"
        items.append((itm_row,itm_col))
#finding the initial direction of the pacman
if facing == "W":
    pacman = "<"
    grid[init_pos_r][init_pos_c]="<"
elif facing == "E":
    grid[init_pos_r][init_pos_c]=">"
    pacman = ">"
elif facing == "N":
    grid[init_pos_r][init_pos_c]="^"
    pacman = "^"
elif facing == "S":
    grid[init_pos_r][init_pos_c] = "V"
    pacman = "V"

def get_pacman_position(grid):
    
    for i in range(len(grid)): #loop through rows
        for j in range(len(grid[i])): #loop through columns
            if grid[i][j] == '<' or grid[i][j] == '>' \
                    or grid[i][j] == '^' \
                        or grid[i][j] == 'V' or grid[i][j]=='@': #if user found the pacman or the pacman with the item, return it to user
                return (i,j)
    return None


def display_grid(grid): #function to print the grid
    for row in grid:
        print(' '.join(row))
        
        
def update_facing(user_input, pac): 
    
    row, col = get_pacman_position(grid)
    #if the user's input is left
    if user_input == "L":
        if pac=="^": #if facing upwards
        
            return "<" #the tail should face left
            
            
        elif pac== "V" : #if tail faces downward
        
            return">" #the tail should face right
            
            
        elif pac== ">" : #if tail faces right
            return"^" #the tail should face upwards
            
            
        elif pac==  "<": #if tail faces left
            return"V" #the tail should face downwards
        else: 
            print("can't find pacman")
           
            
          #if the user's input Right
    elif user_input == "R":
        
        if pac=="^":#if facing upwards
        
            return">" #the tail should face right 
            
        elif pac== "V": #if tail faces downward
        
            return"<"   #the tail should face left
            
        elif pac == ">":#if tail faces right
            
            return"V"  #the tail should face downwards
            
        elif pac==  "<": #if tail faces left
            
            return"^" #the tail should face upwards
            
        else: 
            
            print("can't find pacman")

def user_interactive(grid):
    xlist =[]
    grid_path = True # for toggle feature
    display_grid(grid)
    print("__welcome__ to Pacman__\nL: Turn Left\nR: Turn Right\n"
        "[x]: Move x number of steps\n"
        "C: Consume Item \n"
        "P: Place Item \n"
        "S: Show/Hide Path \n"
        "Q: Quit")



    while True:
        row, col = get_pacman_position(grid)    #constantly know pacman's location
        display_grid(grid)


        user_input = input("command: ")
        print()
    
        if user_input == "L" or user_input =="R":
            
            if grid[row][col] !="@":               #if there isnt an item
                pacman = grid[row][col]             
                pacman= update_facing(user_input,pacman)   #apply the L or R input
                grid[row][col] = pacman                     #change the grid 
            elif grid[row][col]=='@':                       #if there is an item
                pacman = update_facing(user_input,pacman)   #use the pacman stored before change it to @ when updating the facing

        elif user_input.isdigit():                          #if the input is steps to move
            user_input=int(user_input)                      #convert to int
            pacman = grid[row][col] 
            if pacman=="^":                                 #if facing upwards
            
                if row-int(user_input) < 0:                    #checking if steps take user off grid
                    print("Invalid")
                    return                                   #exit out of the current loop and starts over
                
                else:                                    #if it doesn't take user off the grid
                
                    for one_step in range(int(user_input)+1): #check for obstacles

                        if grid[row-one_step][col]=="x":  #if facing up, moving up means going backward in rows 
                             print("Invaild")
                                              #exit out of the function
                        
                        #if it doesnt exit the function by now then the move is valid 
                        
                for one_step in range(int(user_input)): #replacing the locs user pass by, this doesnt inlcude the end spot
                    if grid[row-one_step][col]== 'o' or grid[row-one_step][col]== '@': 
                        #while passing an item put it back in place 
                        #the loop with one_step stars with 0
                        # if the pacman is an @ that means the item wasnt picked up
                        grid[row-one_step][col]=='o'
                    else:                                   #otherwise replace with space
                        grid[row-one_step][col]=' '
                        xlist.append((row-one_step,col))    #every ' ' location is saved for the S toggle feature
                    
                    #replace the final destination
                if grid[row-user_input][col]=='o':       #if theres an item
                    pacman = '^'                        # we're still under the if its facing upwards
                    grid[row-user_input][col]='@'        # replace with @
                else:
                    grid[row-user_input][col]='^'
                    
                    
                    
            elif pacman== "V" :# if tail faces downward
            
                try:
                    if row+int(user_input)>len(grid):# checking if steps take me off grid
                            print("Invalid")
                            return

                    else:

                        for one_step in range(int(user_input)+1):
                            if grid[row+one_step][col]=="x":
                                print("invalid")
                                return

                    
                    for one_step in range(int(user_input)): #replacing the locs we pass by

                        if grid[row+one_step][col]=='o' or grid[row+one_step][col]=='@':

                            grid[row+one_step][col]='o'
                        else:

                            grid[row+one_step][col]=' '

                            xlist.append((row+one_step,col))

                    if grid[row+user_input][col]=='o': #replaces the final destination
                        pacman ='V'
                        grid[row+user_input][col]='@'
                    else:
                        grid[row+user_input][col]='V'

                except IndexError:
                    print("Invalid")
            elif pacman== ">" :# if tail faces right
            
                if col+int(user_input)>len(grid[row]):  #checking if steps take me off grid
                        print("Invalid")

                else:
                    
                    for one_step in range(int(user_input)+1):
                        if grid[row][col+one_step]=="x":
                            print("Invalid")

                    
                for one_step in range(int(user_input)): #replacing the locs we pass by
                    if grid[row][col+one_step]=='o'or grid[row][col+one_step]=='@':
                        grid[row][col+one_step]='o'
                    else:
                        grid[row][col+one_step]=' '
                        xlist.append((row,col+one_step))
                        
                    if grid[row][col+user_input]=='o': #replaces the final destination
                        pacman ='>'
                        grid[row][col+user_input]='@'
                    else:
                        grid[row][col+user_input]='>'

            elif pacman ==  "<": #if tail faces left
            
                if col-int(user_input)<0:  #checking if steps take me off grid
                        print("Invalid")
                        return
                else:
                    print(user_input)
                    for one_step in range(int(user_input)):
                        print(grid[row][col-one_step])
                        if grid[row][(col-one_step)] == "x":
                            print('invalid')


                for one_step in range(int(user_input)): #replacing the locs we pass by
                    if grid[row][col-one_step] == 'o' or grid[row][col-one_step]=='@':
                        grid[row][col-one_step] ='o'
                    else:
                        grid[row][col-one_step]=' '
                        xlist.append((row,col-one_step))
                        
                    if grid[row][col-user_input]=='o': #replaces the final destination
                        pacman ='<'
                        grid[row][col-user_input]=='@'

                    else:
                        #if grid[row][col-user_input] == "x":
                            #continue
                            gridrid[row][col-user_input]='<'


        elif user_input =="C":
            if grid[row][col] == '@':
                grid[row][col] = pacman
            else: 
                print('Invalid')


        elif user_input =="P":
            pacman = grid[row][col]
            grid[row][col]='@'
    
        elif user_input =="S":
            pacman = grid[row][col] 
            grid_path = not grid_path 
            if not grid_path:                   #if grid_path is False, add the dots back
                for i in range(len(grid)):               #loop through rows
                    for j in range(len(grid[i])):        #loop through cols
                        if grid[i][j]==' ':               #if  location is ' '
                            grid[i][j]='.'
            elif grid_path:                     #if grid_path is true, place the empty
                for row,col in xlist:           # spaces back using xlist
                    grid[row][col]=' '
                
        elif user_input =="Q":
            exit()                      

def switch_path(gp,g):
        for i in range(len(g)):               #loop through rows
            for j in range(len(g[i])):        #loop through cols
                if g[i][j]==' ': #if  loc is ' '
                    g[i][j]='.'
        return g
    
user_interactive(grid)

    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    