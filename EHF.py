
import glob
import os
import pandas as pd

month_means = pd.read_csv('month_means.csv')
month_means['mont_num'] = [1,2,3,4,5,6,7,8,9,10,11,12]

os.chdir('pre-analise/')

files = glob.glob('*.idf')
files = files[:21]

EHF = {'file': [], 'EHF': []}

for file in files:
    print(file)
  
    csv_file = file[:-3]+'csv' 
    df = pd.read_csv(csv_file)
  
    df['sup_lim'] = -1

    df['ehf'] = -1
    for i in range(len(df)):
        print(i,end = '\r')

        df['sup_lim'][i] = month_means['mean_temp'][int(df['Date/Time'][i][:3])-1] + 3.5
        
        if df['ZONE_0:Zone Operative Temperature [C](Hourly)'][i] > df['sup_lim'][i]:
            df['ehf'][i] = 1
        else:
            df['ehf'][i] = 0

    df_EHF['file'].append(file[:-4])

    df_EHF['EHF'].append((df['ehf'][df['SCH_OCUPACAO:Schedule Value [](Hourly)'] > 0]).mean())

'''
bounds <- c(-1,1)

n_delta <- 50

'''