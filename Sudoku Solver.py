def check(todo,hlines,vlines,boxes,arr):
    if len(todo)==0:
        for i in range(9):
            x=list(arr[i])
            print(x)
        return 1
    p=todo.pop()
    x,y=p[0],p[1]
    for i in range(1,10):
        if i not in hlines[x] and i not in vlines[y] and i not in boxes[x//3][y//3]:
            hlines[x].add(i)
            vlines[y].add(i)
            boxes[x//3][y//3].add(i)
            arr[x][y]=str(i)
            if check(todo,hlines,vlines,boxes,arr)==1:
                return 1
            hlines[x].remove(i)
            vlines[y].remove(i)
            boxes[x//3][y//3].remove(i)
    todo.append([x,y])
    return 0
a=[]
sample='''Sample input:
2____3_46
__9__72__
________8
8___591__
_31___8__
_7__316__
_9_______
_84_2_5_9
____953_7

Provide your input:\n'''
print(sample)
for i in range(9):
    a.append(list(input()))
todo=[]
hlines=[set() for i in range(9)]
vlines=[set() for i in range(9)]
boxes=[[set() for i in range(3)] for j in range(3)]
for i in range(9):
    for j in range(9):
        if a[i][j]=='_':
            todo.append([i,j])
        else:
            hlines[i].add(int(a[i][j]))
            vlines[j].add(int(a[i][j]))
            boxes[i//3][j//3].add(int(a[i][j]))
z=check(todo,hlines,vlines,boxes,a)
if z!=1:
    print('Not Possible')
