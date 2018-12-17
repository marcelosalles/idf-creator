# Return EHF from multiple simulation results of Operative Temperature


import argparse
import csv
import datetime
import glob
from multiprocessing import Pool
import os
import pandas as pd

FOLDER_STDRD = 'compare'
LEN_FOLDER_NAME = len(FOLDER_STDRD)
BASE_DIR = '/media/marcelo/OS/LabEEE_1-2/idf-creator/sobol_single/'
# BASE_DIR = 'D:/LabEEE_1-2/idf-creator/sobol_single'
MONTH_MEANS = pd.read_csv('month_means_8760.csv')
MAX_THREADS = 1 # 0

# SIMULATIONS = 233
# N_CLUSTERS = 1
# batch = int(SIMULATIONS/N_CLUSTERS)
compare_ok = pd.read_csv('compare_ok.csv')
compare_ok['compare'] = compare_ok['compare'].apply(lambda x: 'compare_'+'{:05.0f}'.format(int(x[-5:]))+'.epJSON')

def process_folder(folder):
    
    line = 0
    folder_name = folder[len(folder)-LEN_FOLDER_NAME:]
    os.chdir(folder)  # BASE_DIR+'/'+
    # epjson_files = glob.glob('*.epJSON')   
    # i_cluster = int(folder[-1]) 
    
    pre_epjson_files = glob.glob('*.epJSON')
    ok_list = [compare_ok['compare'][i] for i in range(len(compare_ok['compare']))]    
    epjson_files = []
    for f in pre_epjson_files:
        if f in ok_list:  # compare_ok['compare']:
            epjson_files.append(f)

    df_temp = {
        'folder': [],
        'file': [],
        'temp': [],
        'ach': [],
        'ehf': []
    }

    for file in epjson_files:
        
        zn = int(compare_ok['zn_number'][compare_ok['compare'] == file])
        
        line += 1
      
        csv_file = file[:-7]+'out.csv' 
        df = pd.read_csv(csv_file)
      
        df_temp['file'].append(file[:-7])
        df_temp['folder'].append(folder_name) 

        df_temp['temp'].append((df['OFFICE_'+'{:02.0f}'.format(zn)+':Zone Operative Temperature [C](Hourly)'][df['SCH_OCUPACAO:Schedule Value [](Hourly)'] > 0]).mean())
        df_temp['ach'].append((df['OFFICE_'+'{:02.0f}'.format(zn)+':AFN Zone Infiltration Air Change Rate [ach](Hourly)'][df['SCH_OCUPACAO:Schedule Value [](Hourly)'] > 0]).mean())
        
        df['E_hot'] = -1
        df['sup_lim'] = MONTH_MEANS['mean_temp'] + 3.5
        df.loc[df['OFFICE_'+'{:02.0f}'.format(zn)+':Zone Operative Temperature [C](Hourly)'] > df['sup_lim'], 'E_hot'] = 1
        df.loc[df['OFFICE_'+'{:02.0f}'.format(zn)+':Zone Operative Temperature [C](Hourly)'] <= df['sup_lim'], 'E_hot'] = 0
        
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

    start_time = datetime.datetime.now()
    
    # print(compare_ok['compare'].tail())

    process_folder(BASE_DIR+FOLDER_STDRD)

    end_time = datetime.datetime.now()

    total_time = (end_time - start_time)
    
    print("Total processing time: " + str(total_time))
