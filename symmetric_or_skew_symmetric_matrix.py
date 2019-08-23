m=int(input('no of rows :'))
n=int(input('no of cols :'))
mat=[]
for i in range(m):
    mat+=[0]
for i in range(m):
    mat[i]=[0]*n
    
for i in range(m):
    for j in range(n):
        mat[i][j]=int(input('mat['+str(i)+']['+str(j)+']= '))
print(mat)

s=0
ss=0
for i in range(m):
    for j in range(n):
        if mat[i][j]!=mat[j][i] and mat[i][j]!=(mat[j][i]*x):
            print("not symmetric matrix or skew symmetric matrix ")
            exit()
        else:
            if mat[i][j]==mat[j][i]:
                 s+=1
                 
            if mat[i][j]==mat[j][i]*x:
                ss+=1

if s==m*n:
    print("symmetric")
elif ss==m*n:
    print("skew symmetric")
