import numpy as np

def extract_data(file_path):
    data = np.load(file_path, allow_pickle=True)
    return data
