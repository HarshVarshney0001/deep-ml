import numpy as np

def to_categorical(x, n_col=None):
    if n_col==None:
        n_col=max(x)+1
        mat=np.zeros((len(x),n_col))
        j=0
        for i in x:
            mat[j,i]=1
            j=j+1
        return mat
    else:
        mat=np.zeros((len(x),n_col))
        j=0
        for i in x:
            mat[j,i]=1
            j=j+1
        return mat
