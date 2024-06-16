import numpy as np
from numpy.linalg import linalg

def LU(A):
    n=len(A[0])
    L=np.zeros([n,n])
    U=np.zeros([n,n])
    for i in range (n):
        L[i][i]=1
        if i == 0 :
            U[0][0]=A[0][0]
            for j in range (1,n):
                U[0][j] = A[0][j]
                L[j][0] = A[j][0]/U[0][0]
        else:
            for j in range(i, n):
                temp = 0
                for k in range(0,i):
                    temp += L[i][k]*U[k][j]
                U[i][j]=A[i][j] - temp
            for j in range(i+1,n):
                temp=0
                for k in range(0,i):
                    temp += L[j][k]*U[k][i]
                L[j][i]=(A[j][i]-temp)/U[i][i]
    return L,U
if __name__ == '__main__':
    n=3
    A=[[1,2,3],[3,4,5],[5,6,7]]
    print('A矩阵：\n',A)
    L,U=LU(A)
    print('L矩阵：\n',L,'\nU矩阵：\n',U)
    b=np.array([6,12,18])
    c=linalg.solve(L,b)
    x=linalg.solve(U,c)
    print('方程组的解：\n',x)
