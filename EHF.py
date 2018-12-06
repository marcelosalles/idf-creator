
import glob
import os
import pandas as pd

month_means = pd.read_csv('month_means.csv')
month_means['mont_num'] = [1,2,3,4,5,6,7,8,9,10,11,12]

os.chdir('sobol_single/cluster0')

files = glob.glob('*.epJSON')
files = files[:5]

df_EHF = {'file': [], 'EHF': []}

for file in files:
    print(file)  #, end= '\r')
  
    csv_file = file[:-7]+'out.csv' 
    df = pd.read_csv(csv_file)
  
    df['sup_lim'] = -1

    df['ehf'] = -1
    for i in range(len(df)):
        print(i,end = '\r')

        df['sup_lim'][i] = month_means['mean_temp'][int(df['Date/Time'][i][:3])-1] + 3.5
        
        if df['OFFICE:Zone Operative Temperature [C](Hourly)'][i] > df['sup_lim'][i]:
            df['ehf'][i] = 1
        else:
            df['ehf'][i] = 0

    df_EHF['file'].append(file[:-7])

    df_EHF['EHF'].append((df['ehf'][df['SCH_OCUPACAO:Schedule Value [](Hourly)'] > 0]).mean())

    
EHF = pd.DataFrame(df_EHF)
EHF.to_csv("EHF_11-28.csv", index=False)
