
import pandas as pd
from SALib.sample import saltelli

# Global variables

COL_NAMES = ['area', 'ratio', 'room_height', 'abs', 'shading', 'azimuth', 'wall', 'wwr', 'open_fac', 'thermal_loads',
             'glass', 'room_type', 'ground', 'roof', 'floor_height']  # 15 items.

BOUNDS = [-1, 1]

SIMULATIONS = 30600
cases = SIMULATIONS*6  # SIMULATIONS*33


def n_calc(d, n_cases):
    # N calculator

    n_size = n_cases/(d + 2)

    print(n_size)

    return int(n_size)


if __name__ == "__main__":

    # Define the model inputs

    problem = {
        'num_vars': len(COL_NAMES),
        'names': COL_NAMES,
        'bounds': [BOUNDS for x in range(len(COL_NAMES))]
    }

    n_size = n_calc(problem['num_vars'], cases)

    # Generate samples
    param_values = saltelli.sample(problem, n_size)

    df = pd.DataFrame(param_values, columns=problem['names'])

    # Save pandas' Data Frame to a .csv file
    df.to_csv("sample_sobol.csv", index=False)
