import itertools

def countattack(board):
    n=len(board)
    attack=0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i]==board[j] or abs(board[i]-board[j])==abs(i-j):  #ROW WISE AND DIAGONAL WISE CHECK(SINCE I AM GONNA PLACE QUEENS IN COLUMN WISE)
                attack=attack+1
    return attack

def displayboard(board):
    n=len(board)
    for row in range(n):
        s=""
        for col in range(n):
            if board[col]==row:
                s=s+"Q "
            else:
                s=s+"* "
        print(s)
n = 4
count=0
l=[]
for state in itertools.product(range(n),repeat=n):
    print(state)
    displayboard(state)
    heuristicvalue=countattack(state)
    l.append(heuristicvalue)
    print("Heuristic value:",heuristicvalue)
    count=count+1
    print(count)
    print("----------------------------------------------------------------------------")
count=0
l2=[]
for x in l:
    count=count+1
    if x==0:
        l2.append(count)
print(l2)
print("BY BRUTEFORCE ALGORITHM OUR SOLUTION ARRIVED AT ",l2[0],"TH STATE","AND ITS MIRROR AT",l2[1])   #2 POSSIBLE SOLUTIONS
