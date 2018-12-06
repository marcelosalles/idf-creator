# Return EHF from multiple simulation results of Operative Temperature


import argparse
import csv
import datetime
import glob
from multiprocessing import Pool
import os
import pandas as pd

FOLDER_STDRD = 'cluster'
LEN_FOLDER_NAME = len(FOLDER_STDRD)+1
BASE_DIR = '/media/marcelo/OS/LabEEE_1-2/idf-creator/sobol_single'
# BASE_DIR = 'D:/LabEEE_1-2/idf-creator/sobol_single'
MONTH_MEANS = pd.read_csv('month_means_8760.csv')
MAX_THREADS = 10

SIMULATIONS = 72000
N_CLUSTERS = 10
batch = SIMULATIONS/N_CLUSTERS

def process_folder(folder):
    
    line = 0
    folder_name = folder[len(folder)-LEN_FOLDER_NAME:]
    os.chdir(folder)  # BASE_DIR+'/'+
    pre_epjson_files = glob.glob('*.epJSON')
    
    i_cluster = int(folder[-1])
    ok_list = ['sobol_single_'+'{:05.0f}'.format(i)+'.epJSON' for i in range(int(i_cluster*batch),int(i_cluster*batch+batch))]
    
    epjson_files = []
    for f in pre_epjson_files:
        if f in ok_list:
            epjson_files.append(f)

    df_temp = {
        'folder': [],
        'file': [],
        'temp': [],
        'ach': [],
        'ehf': []
    }

    for file in epjson_files:
        print(line,' ',file, end='\r')
        line += 1
      
        csv_file = file[:-7]+'out.csv' 
        df = pd.read_csv(csv_file)
      
        df_temp['file'].append(file[:-7])
        df_temp['folder'].append(folder_name) 

        df_temp['temp'].append((df['OFFICE:Zone Operative Temperature [C](Hourly)'][df['SCH_OCUPACAO:Schedule Value [](Hourly)'] > 0]).mean())
        df_temp['ach'].append((df['OFFICE:AFN Zone Infiltration Air Change Rate [ach](Hourly)'][df['SCH_OCUPACAO:Schedule Value [](Hourly)'] > 0]).mean())
        
        df['E_hot'] = -1
        df['sup_lim'] = MONTH_MEANS['mean_temp'] + 3.5
        df.loc[df['OFFICE:Zone Operative Temperature [C](Hourly)'] > df['sup_lim'], 'E_hot'] = 1
        df.loc[df['OFFICE:Zone Operative Temperature [C](Hourly)'] <= df['sup_lim'], 'E_hot'] = 0
        
        df_temp['ehf'].append(df['E_hot'][df['SCH_OCUPACAO:Schedule Value [](Hourly)'] > 0].mean())
    
    df_output = pd.DataFrame(df_temp)
    df_output.to_csv('means_{}.csv'.format(folder_name), index=False)
    print('\tDone processing folder \'{}\''.format(folder_name))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process output data from Energyplus.')
    parser.add_argument('-t',
                        action='store',
                        type=int,
                        help='runs T threads')

    args = parser.parse_args()

    folders = glob.glob(BASE_DIR+'/'+FOLDER_STDRD+'*')

    print('Processing {} folders in \'{}\':'.format(len(folders), BASE_DIR))
    for folder in folders:
        print('\t{}'.format(folder))

    start_time = datetime.datetime.now()

    if args.t:
        p = Pool(args.t)
        p.map(process_folder, folders)
    else:
        num_folders = len(folders)
        p = Pool(min(num_folders, MAX_THREADS))
        p.map(process_folder, folders)

    end_time = datetime.datetime.now()

    total_time = (end_time - start_time)
    
    print("Total processing time: " + str(total_time))
