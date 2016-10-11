def radiation_length(A, Z):
    """Radiation length (a.k.a. X_0)
    
    The distance over which electrons lose 1/e of their energy.
    
    See: https://en.wikipedia.org/wiki/Radiation_length
    
    Returns
    -------
    The length in g/cm^-2
    """
    
    import numpy as np
    return 1432.8 * A / (Z * (Z + 1) * (11.319 - np.log(Z))
