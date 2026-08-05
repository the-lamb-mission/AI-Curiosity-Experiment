import hiddenrules as hr
import copy

def initialize_board(size = 10):
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            num = str((size-1-i) * size + j)
            if len(num) == 1:
                row.append("0" + num)
            else:
                row.append(num)
        board.append(row)
    return board

def print_board(board, newPos, destPos):
    b = copy.deepcopy(board)
    size = len(b) - 1
    b[size-newPos//len(b)][newPos%len(b)] = "0X"
    b[size-destPos//len(b)][destPos%len(b)] = "0D"
    for row in b:
        print(row)

def main():
    #initialize board
    size = 10
    board = initialize_board(size)

    #game loop
    lastPos = 0
    newPos = 0
    destPos = size * size - 1
    reachDestination = False
    rounds = 0
    while reachDestination == False or rounds < 70:
        rounds += 1
        print(f"The current round is {rounds}.")
        print(f"Your current position is {newPos}.")
        move = input("Enter new position: ")
        print(move)

        if move == "exit":
            #kill switch
            break
        elif move == "up":
            newPos += size
        elif move == "down":
            newPos -= size
        elif move == "left":
            newPos -= 1
        elif move == "right":
            newPos += 1
        else:
            print("question round.")

        if newPos == destPos:
            reachDestination = True
            print("Congratulations! You have reached the destination.")

        #check rules
        lastPos, newPos, destPos = hr.checkRules(lastPos, newPos, destPos, size)

        #check if player reached destination
        if newPos == destPos:
            reachDestination = True
            print("Congratulations! You have reached the destination.")
        else:
            print(f"Your new position is {newPos}. Keep going!")

        lastPos = newPos
        print_board(board, newPos, destPos)
        print()
    print(f"Game over, you used {rounds} rounds. Thanks for playing!")

main()
