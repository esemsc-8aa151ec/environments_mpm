import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc



__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'pandas_df_to_markdown']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(image, sigma):
    return gaussian_filter(image, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv() * b

def pandas_df_to_markdown(df):
    return df.to_markdown()
