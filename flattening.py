from scipy.stats import linregress
import numpy as np


def flattening(data, dt, chunk_l):
    """
    Make flattening of raw data using windows (time chunks) of given size
    
    Parameters
    -------
    
    data: list or np.array
        timeseries data (deflection magnitude)
    dt: float
        time resolution of data
    chunk_l: float
        length of the chunk (in seconds)
        
    Returns
    -------
    data_fit: np.array
        fitting line
    data_flat: np.array
        flattened data
    """
    # get chunk length in datapoints instead of seconds
    chunk_l = int(chunk_l//dt )
    # get size of output flattened data (cut out remaining part after division)
    flat_data_size = len(data)//chunk_l
    data_fit = np.empty((flat_data_size, chunk_l))
    for chunk_i in range(flat_data_size):
        start_i = chunk_i*chunk_l
        end_i = (chunk_i+1)*chunk_l
        y = data[start_i:end_i]
        # make linear regression for each chunk
        k_coef, b_coef, _, _, _ = linregress([i for i in range(len(y))], y)
        yfit = k_coef * np.array([i for i in range(len(y))]) + b_coef
        data_fit[chunk_i] = yfit
    data_flat = data[:(flat_data_size*chunk_l)]-data_fit.flatten()
    return data_fit, data_flat
