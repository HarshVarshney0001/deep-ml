import numpy as np

def log_softmax(scores: np.ndarray) -> np.ndarray:
    return np.log((np.exp(scores)/sum(np.exp(scores))))