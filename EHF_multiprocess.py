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
MONTH_MEANS = pd.read_csv('month_means.csv')
MAX_THREADS = 10

def process_folder(folder):
    
    line = 0
    folder_name = folder[len(folder)-LEN_FOLDER_NAME:]
    os.chdir(folder)  # BASE_DIR+'/'+
    epjson_files = glob.glob('*.epJSON')

    df_EHF = {
        'folder': [],
        'file': [],
        'EHF': []
    }

    for file in epjson_files:
        print(line,' ',file, end='\r')
        line += 1
      
        csv_file = file[:-7]+'out.csv' 
        df = pd.read_csv(csv_file)
      
        df['sup_lim'] = -1

        df['E_hot'] = -1
        for i in range(len(df)):
            # print(i, end = '\r')
            
            try:
                df.loc[i, 'sup_lim'] = MONTH_MEANS['mean_temp'][int(df['Date/Time'][i][:df['Date/Time'][i].find('/')])-1] + 3.5
            except:
                print('ERROR on file: ',folder_name,' ',file)
                print(df['Date/Time'][i][:3])
            
            if df['OFFICE:Zone Operative Temperature [C](Hourly)'][i] > df['sup_lim'][i]:
                df.loc[i, 'E_hot'] = 1
            else:
                df.loc[i, 'E_hot'] = 0

        df_EHF['file'].append(file[:-7])
        df_EHF['folder'].append(folder_name) 

        df_EHF['EHF'].append((df['E_hot'][df['SCH_OCUPACAO:Schedule Value [](Hourly)'] > 0]).mean())
    
    df_output = pd.DataFrame(df_EHF)
    df_output.to_csv('df_EHF_{}.csv'.format(folder_name), index=False)
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
