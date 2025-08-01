import numpy as np 

def is_np_array(obj):
    """
    Check if the given object is a NumPy array.
    
    Parameters:
    obj: The object to check.

    Returns:
    bool: True if the object is a NumPy array, False otherwise.
    """
    return isinstance(obj, np.ndarray)