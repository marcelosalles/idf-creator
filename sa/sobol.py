import numpy as np
import pandas as pd
from SALib.sample import saltelli

# Define the model inputs
problem = {
    'num_vars': 13,
    'names': ['area',
              'ratio',
              'height',
              'wwr',
              'h-floor',
              'azimuth',
              'open_fac',
              'glass',
              'abs_wall',
              'wall',
              'shading',
              'thermal_loads',
              'corr_vent'],
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
               [0, 1]]
}
problem_roof = {
    'num_vars': 14,
    'names': ['area',
              'ratio',
              'height',
              'wwr',
              'h-floor',
              'azimuth',
              'open_fac',
              'glass',
              'abs_wall',
              'wall',
              'roof', #*
              'shading',
              'thermal_loads',
              'corr_vent'],
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
               [0, 1]]
}

# Problems list

TYPES = [['TOP',4],['MID',6],['BOT',4],['UNI',2]]#[['TOP',4235],['MID',6750],['BOT',4500],['UNI',1058]]

# Generate samples

SAMPLE = {'type': []}
    
for name in problem_roof['names']:
    SAMPLE[name] = []
    
for i in range(len(TYPES)):
    
    type = TYPES[i][0]
    N = TYPES[i][1]
    
    if type == 'TOP' or type == 'UNI':
        problem_dict = problem_roof
    else:
        problem_dict = problem
        
    param_values = saltelli.sample(problem_dict, N)

    for name in problem_roof['names']:
    
        if name == 'roof' and (type == 'MID' or type == 'BOT'):
            
            for j in range(len(param_values)):
                SAMPLE[name].append(None)
        else:
        
            for j in range(len(param_values)):
                SAMPLE[name].append(param_values[j][i])
                
    for j in range(len(param_values)):
        SAMPLE['type'].append(type)
      
# SAMPLE as a pandas' Data Frame

output = pd.DataFrame(SAMPLE)

# Save pandas' Data Frame to a .csv file
output.to_csv("sample.csv", index=False)
