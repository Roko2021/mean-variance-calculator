import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    mean = np.array(list).reshape(3,3)
    calculations = {
        "mean":[mean.mean(axis=0).tolist(),mean.mean(axis=1).tolist(),mean.mean().tolist()],
        "variance":[mean.var(axis=0).tolist(),mean.var(axis=1).tolist(),mean.var().tolist()],
        "standard deviation":[mean.std(axis=0).tolist(),mean.std(axis=1).tolist(),mean.std().tolist()],
        "max":[mean.max(axis=0).tolist(),mean.max(axis=1).tolist(),mean.max().tolist()],
        "min":[mean.min(axis=0).tolist(),mean.min(axis=1).tolist(),mean.min().tolist()],
        "sum":[mean.sum(axis=0).tolist(),mean.sum(axis=1).tolist(),mean.sum().tolist()],
    }


    return calculations