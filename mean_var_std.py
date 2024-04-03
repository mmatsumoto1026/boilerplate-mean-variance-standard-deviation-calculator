import numpy as np

def calculate(list):
    try:
        narray = np.array(list).reshape(3,3)
        calculated_values_dict = {
            'mean': [narray.mean(axis=0), narray.mean(axis=1), narray.mean()],
            'variance': [narray.var(axis=0), narray.var(axis=1), narray.var()],
            'standard deviation': [narray.std(axis=0), narray.std(axis=1), narray.std()],
            'max': [narray.max(axis=0), narray.max(axis=1), narray.max()],
            'min': [narray.min(axis=0), narray.min(axis=1), narray.min()],
            'sum': [narray.sum(axis=0), narray.sum(axis=1), narray.sum()]
        }
        for key in calculated_values_dict:
            for i,values in enumerate(calculated_values_dict[key]):
                if type(values) is np.ndarray:
                    calculated_values_dict[key][i] = values.tolist()

        return calculated_values_dict
    except ValueError:
        raise ValueError("List must contain nine numbers.")