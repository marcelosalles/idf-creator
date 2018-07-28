import numpy as np
import pandas as pd
from SALib.sample import saltelli

# Define the model inputs
problem = {
    'num_vars': 16,
    'names': ['area', 'ratio', 'height', 'wwr', 'h-floor', 'azimuth', 'exp', 'open_fac', 'u_glass', 'fs_glass', 'abs_wall', 'wall', 'roof', 'shading', 'thermal_loads', 'corr_vent'],
    'bounds': [[0, 1],
               [0, 1],
               [0, 1],
               [0, 1],
               [0, 1],
               [0, 1],
               [0, 1],
               [0, 1],
               [0, 1],
               [0, 1],
               [0, 1],
               [0, 1],
               [0, 1],
               [0, 1],
               [0, 1],
               [0, 1]]
}

# Generate samples
param_values = saltelli.sample(problem, 15000)

SAMPLE = {}

for i in range(len(problem['names'])):
    name = problem['names'][i]
    SAMPLE[name] = []
    for j in range(len(param_values)):
        SAMPLE[name].append(param_values[j][i])
      
# SAMPLE as a pandas' Data Frame
output = pd.DataFrame(SAMPLE)

# Save pandas' Data Frame to a .csv file
output.to_csv("sample.csv", index=False)
