
import json
import numpy as np
import pandas as pd
from SALib.analyze import sobol
from SALib.sample import saltelli

# Global variables

OUTPUT_FILE = "sample_sobol_12-05.csv"

COL_NAMES = ['area', 'ratio', 'zone_height', 'abs', 'shading', 'azimuth',
	'wall_u', 'wall_ct', 'wwr', 'open_fac', 'people',  # 'thermal_loads', 
    'glass', 'floor_height', 'bldg_ratio', 'room_type', 'ground', 'roof']  # 17 items.

BOUNDS = [-1, 1]

SIMULATIONS = 72000  # 36000

def n_calc(d, n_cases, scnd_order = False):
    # N calculator
    
    if scnd_order:
        n_size = n_cases/(2*d + 2)
    else:
        n_size = n_cases/(d + 2)

    print(n_size)

    return int(n_size)


if __name__ == "__main__":

    # Define the model inputs

    cases = SIMULATIONS
    
    problem = {
        'num_vars': len(COL_NAMES),
        'names': COL_NAMES,
        'bounds': [BOUNDS for x in range(len(COL_NAMES))]
    }

    n_size = n_calc(problem['num_vars'], cases, scnd_order = True)

    # generate samples
    param_values = saltelli.sample(problem, n_size)

    df = pd.DataFrame(param_values, columns=problem['names'])

    ## save pandas' data frame to a .csv file
    df.to_csv(OUTPUT_FILE, index=False)
    
    #### SA
    
    # # df_out = pd.read_csv('/media/marcelo/OS/BS/EHF_12-03.csv')
    # df_out = pd.read_csv('D:/LabEEE_1-2/idf-creator/means_12-05.csv')
    
    # Y = np.array(df_out['ehf'])
    # sa = sobol.analyze(problem, Y, print_to_console=True)

    # for key in sa:
        # sa[key] = list(sa[key])
    # for key in ['S2','S2_conf']:
        # for line in range (len(sa[key])):
            # sa[key][line] = list(sa[key][line])
            
    # # with open('/media/marcelo/OS/BS/sa_ehf_12-05.csv', 'w') as f:
    # with open('D:/LabEEE_1-2/idf-creator/sa_ehf_12-05.csv', 'w') as f:
        # json.dump(sa, f)
    
    # #### SA TEMP and ACH
    
    # #df_out = pd.read_csv('/media/marcelo/OS/BS/temp_11-29.csv')
    
    # #temp
    # Y = np.array(df_out['temp'])
    # sa = sobol.analyze(problem, Y, print_to_console=True)

    # for key in sa:
        # sa[key] = list(sa[key])
    # for key in ['S2','S2_conf']:
        # for line in range (len(sa[key])):
            # sa[key][line] = list(sa[key][line])
            
    # # with open('/media/marcelo/OS/BS/sa_temp_12-05.csv', 'w') as f:
    # with open('D:/LabEEE_1-2/idf-creator/sa_temp_12-05.csv', 'w') as f:
        # json.dump(sa, f)

    # # ach
    # Y = np.array(df_out['ach'])
    # sa = sobol.analyze(problem, Y, print_to_console=True)

    # for key in sa:
        # sa[key] = list(sa[key])
    # for key in ['S2','S2_conf']:
        # for line in range (len(sa[key])):
            # sa[key][line] = list(sa[key][line])
            
    # # with open('/media/marcelo/OS/BS/sa_ach_12-05.csv', 'w') as f:
    # with open('D:/LabEEE_1-2/idf-creator/sa_ach_12-05.csv', 'w') as f:
        # json.dump(sa, f)
    
