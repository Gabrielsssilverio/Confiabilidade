import numpy as np

def limitfunction(samples=None):
    g = np.zeros(samples.shape[0])
    for i in range(samples.shape[0]):
        D = samples[i, 0]  # Posição (X1)
        P = samples[i, 1]  # Carga (X2)
        R_const = 0.20 
        
        # O momento fletor (Load Effect) é P * (D - D^2)
        g[i] = R_const - P * (D - D**2) 
    return g