import numpy as np

def densemul(matA,matB):
    if(len(matA[0])==len(matB)):
        nrows=len(matA)
        ncols=len(matA[0])
        k_iter=len(matB[0])
        flops=0
        res=[[0 for _ in range(k_iter)] for _ in range(nrows)]
        #print(res)
        for i in range(0,nrows):
            for j in range(0,k_iter):
                for k in range(0,ncols):
                    #print(i,j,k)
                    flops+=2
                    res[i][j]=res[i][j]+matA[i][k]*matB[k][j]
        
    else:
        print("matrix not campatible !!")
        return None
    return res,flops

#matA=np.array([[0,0,4],[5,6,0],[0,1,0]])
#matB=np.array([[0,4],[3,3],[6,0]])
#matC=np.matmul(matA,matB)
#print(matC)

matA=[[1,-2,0,0,0],[-2,-1,3,0,0],[0,3,0,-1,0],[0,0,-1,1,4],[0,0,0,4,3]]
matB=[[1,3,-2,0,0],[5,7,3,0,0],[0,1,0,9,0],[0,0,21,13,41],[0,0,0,12,7]]
matC,nflops=densemul(matA,matB)
print(np.array(matC),nflops)




