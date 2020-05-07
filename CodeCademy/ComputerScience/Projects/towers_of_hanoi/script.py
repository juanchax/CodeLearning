from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks, set to an empty list
stacks = []
#Create the Stack instances and give them a name
left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')
#Append the Stack instances to the stacks list
stacks += [left_stack, middle_stack, right_stack]

#### Set up the Game ####

#Get user input regarding how many disks the user wants to play with
num_disks = int(input('\nHow many disks would you like to play with?\n'))

#Check that the minimum of 3 disks is entered
while num_disks < 3:
    num_disks = int(input('Enter a number greater than or equal to 3.\n')) #Get User Input

#put the disks in the left stack, range (largest number, to 0, decrementing)
for disk in range(num_disks, 0, -1):
    left_stack.push(disk)
#left_stack.print_items()

#Calculate and print out the minimum number of moves needed to finish
num_optimal_moves = (2 ** num_disks ) - 1
print('\nThe fastest you can solve this game is in {0} moves.'.format(num_optimal_moves))

#### Get user input ####

def get_input():

    #Create a list of the stack names (using the first letter of the stack name)
    choices = [stack.get_name()[0] for stack in stacks]

    #While there's an entry in stacks list print out the choices for the user to pick
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print('Enter {0} for {1}'.format(letter, name))

        user_input = input('')

        #Check that the user input is a valid choice
        if user_input in choices:
            for i in range(len(stacks)):
                return stacks[i]

#### Play the Game ####

num_user_moves = 0

#Keep running while the Right stack does not have all the disks
while right_stack.get_size() != num_disks:

    print('\n\n\n...Current Stacks...')
    #Print the current status of each stack (L M R)
    for stack in stacks:
        stack.print_items()

    while True:

        print('\nWhich stack do you want to move from?\n')
        from_stack = get_input()
        print('\nWhich stack do you want to move to?\n')
        to_stack = get_input()

        #Check if the from stack is already empty
        if from_stack.get_size() == 0:
            print('\n\nInvalid Move. Try Again.')
        #Check that whether the TO stack is either empty OR if the FROM disk is smaller than the TO disk
        elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print('\n\nInvalid Move. Try Again.')

print('\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}'.format(num_user_moves, num_optimal_moves))
