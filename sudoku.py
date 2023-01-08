board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    
    #above board has nothing to with the gui the solution of board is shown in terminal
    #we may change the board manualy to get solution for that case if soln exists
def backtrack(bo):
    find=findes(bo)
    if not find:
        return True
    else:
        x,y=find
    for i in range(1,10):
        if validcheck(bo,i,(x,y)):
            bo[x][y]=i
            if backtrack(bo):
                return True
            bo[x][y]=0
    return False

def validcheck(bo,n,pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i]==n and pos[1]!=i:
            return False
    for i in range(len(bo[0])):
        if bo[i][pos[1]]==n and pos[0]!=i:
            return False
    x=pos[0]//3;
    y=pos[1]//3;
    for i in range(x*3,x*3+3):
        for j in range(y*3,y*3+3):
            if bo[i][j]==n and (i,j)==pos:
                return False
    return True

def printboard(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if j==8:
                print(bo[i][j]);
            else:
                print(str(bo[i][j])+" ",end="")
    print(" ")

def findes(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if(bo[i][j]==0):
                return(i,j)
    return None





printboard(board)
backtrack(board)
print("solution!!")
printboard(board)

