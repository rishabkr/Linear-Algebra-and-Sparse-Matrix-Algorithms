
import numpy as np
import scipy.linalg as sp

def solveaxb(A,b):
    L=U=factorize(A)
    print(L)
    x=solve_lub(L,U,b)
    return np.array(x).astype('float')

def solve_lub(L,U,b):
    y=forward_substitution(L,b)
    x=backward_substitution(U,y)
    return np.array(x).astype('float')

def factorize(A):
    n=len(A)
    for k in range(0,n):
        A[k+1:n,k]=A[k+1:n,k]/A[k,k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i,j]=A[i,j]-A[i,k]*A[k,j]
    return A

def vec_factorize(A):
    n=len(A)
    for k in range(0,n):
        A[k+1:n,k]=A[k+1:n,k]/A[k,k]
        for i in range(k+1,n):
            A[i,k+1:n]=A[i,k+1:n]-A[i,k]*A[k,k+1:n]       
    return A

def backward_substitution(U,y):
    y_len=len(y)
    x=[0]*y_len
    x[y_len-1]=y[y_len-1]/U[y_len-1,y_len-1]
    for i in range(y_len-1,-1,-1):
        sum=y[i]
        for j in range(i+1,y_len):
            sum=sum-U[i,j]*x[j]
        x[i]=sum/U[i,i]
    print("x:",x)    
    return np.array(x).astype('float')

def forward_substitution(L,b):
    y=[]
    b_len=len(b)
    for i in range(b_len):
        y.append(b[i])
    for i in range(b_len):
        temp=b[i]
        for j in range(i):
            temp=temp-L[i,j]*y[j]
        y[i]=temp
    #print("y",y)    
    return y


A=np.array([ [2,4,7], [3,5,1], [4,8,5] ]).astype('float')
b=np.array([2,5,3]).astype('float')
newA=A.copy()
calA=A.copy()
x=solveaxb(calA,b)
error = np.linalg.norm(b - np.dot(newA,x.reshape(len(x),1)).flatten())
print("Error: {0}".format(error))
