
import csv
import numpy as np
import pandas as pd
from SALib.sample import saltelli
from LHS import Statiscal

lhs = Statiscal()

# Global variables

BLDG_COL_NAMES = ['area','ratio','height','abs','shading']
ROOM_COL_NAMES = ['wwr','open_fac','thermal_loads']

SIMULATIONS = 30800

VECTORS = 'vectors.csv'

def n_calc(D, type, simulations):
    # N calculator

    if type == 'bldg':

        cases = simulations

    elif type == 'room':

        cases = simulations*(1+2+3+4+5)*(1/5)*6

    N = cases/(D + 2)

    print (N)

    return int(N)

def csvToHash(vectors):
    # Reads the vectors file, and returns a dictionary with the values
    # of each vector, and the header

    firstTime = True
    i = 0
    possibleValues = {}
    csvFile = open(vectors, 'r')
    csvReader = csv.reader(csvFile, delimiter=',', quotechar='|')

    for row in csvReader:
        while i < len(row):
            if not firstTime:
                if row[i] not in possibleValues[i] and row[i] != "":
                    possibleValues[i].append(row[i])
            else:
                headerCsv = row
                possibleValues[i] = []
            i += 1

        firstTime = False
        i = 0

    return (possibleValues,headerCsv)
        
def writeMappedValues(mappedValues, sample_file, headerCsv):
    newFile = open(sample_file, 'w', newline="")
    csvWriter = csv.writer(newFile, delimiter=',', quotechar='|')

    csvWriter.writerow(headerCsv)

    for values in mappedValues:
        csvWriter.writerow(values)

if __name__ == "__main__":

    # Define the model inputs

    bldg_problem = {
        'num_vars': 5,
        'names': BLDG_COL_NAMES,
        'bounds': [[15, 80],   # area
                   [.4, 2.5],  # ratio
                   [2.4, 2.7], # height
                   [0.2, .8],  # abs
                   [0, 1]]     # shading
    }

    room_problem = {
        'num_vars': 3,
        'names': ROOM_COL_NAMES,
        'bounds': [[0.1, .5],  # wwr
                   [0, 1],     # open_fac
                   [0, 1]],    # thermal_loads
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

    # LHS

    ReadCSV = csvToHash(VECTORS)

    possibleValues = ReadCSV[0]
    headerCsv = ReadCSV[1]

    lhd = lhs.lhsValues(possibleValues, SIMULATIONS)

    mappedValues = lhs.mapValues(lhd, possibleValues, SIMULATIONS)

    writeMappedValues(mappedValues, 'lhs_sample.csv', headerCsv)