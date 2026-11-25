import numpy as np

def accuracy_score(y_true, y_pred):
    count=0
    for i,j in zip(y_pred,y_true):
        if i==j:
            count+=1
    return count/len(y_pred)