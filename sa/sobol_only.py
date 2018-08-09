
import csv
import numpy as np
import pandas as pd
from SALib.sample import saltelli
from LHS import Statiscal

lhs = Statiscal()

# Global variables

BLDG_COL_NAMES = ['area','ratio','height','abs','shading','azimuth','u_wall','corr_vent','stairs']

#BLDG_BOUNDS = [[15, 80], [.4, 2.5],[2.4, 2.7],[0.2, .8], [0, 1]]

ROOM_COL_NAMES = ['wwr','open_fac','thermal_loads','glass']

#ROOM_BOUNDS = [[0.1, .5],[0, 1],[0, 1]]

BOUNDS = [-1,1]

SIMULATIONS = 30800


def n_calc(D, type, simulations):
    # N calculator

    if type == 'bldg':

        cases = simulations

    elif type == 'room':

        cases = simulations*(1+2+3+4+5)*(1/5)*6

    N = cases/(D + 2)

    print (N)

    return int(N)

if __name__ == "__main__":

    # Define the model inputs

    bldg_problem = {
        'num_vars': len(BLDG_COL_NAMES),
        'names': BLDG_COL_NAMES,
        'bounds': [BOUNDS for x in range(len(BLDG_COL_NAMES))]
    }

    room_problem = {
        'num_vars': len(ROOM_COL_NAMES),
        'names': ROOM_COL_NAMES,
        'bounds': [BOUNDS for x in range(len(ROOM_COL_NAMES))]
    }

    n_bldg = n_calc(bldg_problem['num_vars'], 'bldg', SIMULATIONS)
    n_room = n_calc(room_problem['num_vars'], 'room', SIMULATIONS)

    # Generate samples

    samples = [[bldg_problem,n_bldg],[room_problem,n_room]]

    for i in range(len(samples)):
        
        problem = samples[i][0]
        n = samples[i][1]

        param_values = saltelli.sample(problem, n, calc_second_order = False)

        df = pd.DataFrame(param_values, columns = problem['names'])

        # Save pandas' Data Frame to a .csv file
        df.to_csv("sample"+str(i)+".csv", index=False)