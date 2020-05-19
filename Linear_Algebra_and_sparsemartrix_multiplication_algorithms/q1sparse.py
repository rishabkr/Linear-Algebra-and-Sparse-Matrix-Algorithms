import numpy as np

def get_coo_represetation(matA):
    coo=[]
    alen=len(matA)
    acolen=len(matA[0])
    for i in range(alen):
        for j in range(acolen):
            lst=[]
            if(matA[i][j]!=0):
                lst.append(i)
                lst.append(j)
                lst.append(matA[i][j])
                coo.append(lst)
    return coo

def get_csr_representation(matA):
    rows_index=[]
    columns=[]
    elements=[]
    row_len=len(matA)
    col_len=len(matA[0])
    for i in range(row_len):
        rows_index.append(len(columns))
        for j in range(col_len):
            if(matA[i][j]!=0):
                columns.append(j)
                elements.append(matA[i][j])
    rows_index.append(len(columns))
    return rows_index,columns,elements

def sparse_matrix_multiplication_sparsecoo(cooA,matB):
    n_rows=len(matB)
    n_cols=len(matB[0])
    C=[]
    flop_count=0
    for index in range(n_cols):
        col=[0]*n_rows
        for row in range(len(cooA)):
            i=cooA[row][0]
            j=cooA[row][1]
            element=cooA[row][2]
            flop_count+=2
            col[i]+=element*matB[j][index]
        for r in range(n_rows):
            if(col[r]!=0):
                lst=[]
                lst.append(r)
                lst.append(index)
                lst.append(col[r])
                C.append(lst)
    return  C,flop_count

def sparsecsrmultiplication(matA,matB):
    rows,columns,elements=matA
    rows_count=len(matB)
    col_count=len(matB[0])
    C = [[0 for _ in range(col_count)] for _ in range(rows_count)]
    flop_count=0
    for col in range(col_count):
        for row in range(rows_count):
            for j in range(rows[row],rows[row+1]):
                flop_count+=2
                C[row][col]+=elements[j]*matB[columns[j]][col]
    return C,flop_count

matA=[[0,0,4],[5,6,0],[0,1,0]]
matB=[[0,4],[3,3],[6,0]]
Acoo=get_coo_represetation(matA)
#print(Acoo)
print(sparse_matrix_multiplication_sparsecoo(Acoo, matB))
A_csr = get_csr_representation(matA)
#print(A_csr)
print(sparsecsrmultiplication(A_csr, matB))

