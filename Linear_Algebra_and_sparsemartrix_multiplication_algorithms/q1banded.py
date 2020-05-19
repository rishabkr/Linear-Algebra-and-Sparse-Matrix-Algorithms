
import numpy as np

def get_bandwidth(matA):
    rows,columns=matA.shape
    upperband=0
    for j in range(columns-1,-1,-1):
        zero_present=True
        for i in range(rows):
            if(i+j==columns):
                break
            elif(matA[i][i+j]!=0):
                zero_present=False
                break
        if(not zero_present):
            upperband=j
            break
    lowerband=0
    for i in range(rows-1,-1,-1):
        zero_present=True
        for j in range(columns):
            if(i+j==rows):
                break
            elif(matA[i+j][j]!=0):
                zero_present=False
                break
        if(not zero_present):
            lowerband=i
            break
    return upperband,lowerband

def convert_to_banded(matA,upper_band,lower_band):
        rows,columns=matA.shape
        mat=np.zeros((upper_band+lower_band+1,columns),dtype=int)
        for i in range(columns):
            start=max(0,i-upper_band-1)
            stop=min(rows-1,i+lower_band)
            for j in range(start,stop+1):
                mat[upper_band+j-i][i]=matA[j][i]
        return mat

def get_value(mat,i,j,upper_band):
    a=upper_band+i-j
    if(a<mat.shape[0] and a>=0):
        return mat[a][j]
    else:
        return 0
def multiply_banded(ra,ca,rb,cb,matA,matB,upper_band_a,lower_band_a,upper_band_b,lower_band_b):
    if(ca!=rb):
        return -1,-1
    result=np.zeros((ra,cb),dtype=int)
    flop_count=0
    for i in range(ra):
        for j in range(cb):
            start=max(max(0,i-lower_band_a),max(0,j-upper_band_b))
            stop=min(min(i+upper_band_a+1,ca),min(j+lower_band_b+1,ca))
            for k in range(start,stop):
                flop_count+=2
                result[i][j]+=get_value(matA,i,k,upper_band_a)*get_value(matB,k,j,upper_band_b)
    return result,flop_count

matA=np.array([[1,-2,0,0,0],[-2,-1,3,0,0],[0,3,0,-1,0],[0,0,-1,1,4],[0,0,0,4,3]])
matB=np.array([[1,3,-2,0,0],[5,7,3,0,0],[0,1,0,9,0],[0,0,21,13,41],[0,0,0,12,7]])
upper_band_a,lower_band_a=get_bandwidth(matA)
banded_a=convert_to_banded(matA,upper_band_a,lower_band_a)

upper_band_b,lower_band_b=get_bandwidth(matB)
banded_b=convert_to_banded(matB,upper_band_b,lower_band_b)
#print(matB)
#print("-------")
#print(banded_b)
result,flop_count=multiply_banded(matA.shape[0],matA.shape[1],matB.shape[0],matB.shape[1],banded_a,banded_b,upper_band_a,lower_band_a,upper_band_b,lower_band_b)
print(result)
print("flop_count",flop_count)
