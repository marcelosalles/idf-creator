import csv
import os

def take_epw(files):
    epw_files = []

    for file in files:
        if str(file).endswith(".epw"):
            epw_files.append(file)

    return epw_files
    
# files = os.listdir(os.getcwd())
# files.sort()
# epw_files = take_epw(files)
epw_files = ['C:/Users/LabEEE_1-2/Dropbox/novo RTQ-R/1_planejamento/arq_climaticos/leonardo/BRA_SP_Sao.Paulo.837810_INMET.epw']

for file in epw_files:
    csv_file = open(file, 'r')
    epw_file = csv.reader(csv_file, delimiter=',', quotechar= '|')
        
    jan = 0
    feb = 0
    mar = 0
    apr = 0
    may = 0
    jun = 0
    jul = 0
    aug = 0
    sep = 0
    oct = 0
    nov = 0
    dec = 0

    i_jan = 0
    i_feb = 0
    i_mar = 0
    i_apr = 0
    i_may = 0
    i_jun = 0
    i_jul = 0
    i_aug = 0
    i_sep = 0
    i_oct = 0
    i_nov = 0
    i_dec = 0

    cond = False
    
    for line in epw_file:
    
        if cond:
            #copia os dados desejados:
            if  line[1] == '1':
                jan += float(line[6])
                i_jan += 1
            if  line[1] == '2':
                feb += float(line[6])
                i_feb += 1
            if  line[1] == '3':
                mar += float(line[6])
                i_mar += 1
            if  line[1] == '4':
                apr += float(line[6])
                i_apr += 1
            if  line[1] == '5':
                may += float(line[6])
                i_may += 1
            if  line[1] == '6':
                jun += float(line[6])
                i_jun += 1
            if  line[1] == '7':
                jul += float(line[6])
                i_jul += 1
            if  line[1] == '8':
                aug += float(line[6])
                i_aug += 1
            if  line[1] == '9':
                sep += float(line[6])
                i_sep += 1
            if  line[1] == '10':
                oct += float(line[6])
                i_oct += 1
            if  line[1] == '11':
                nov += float(line[6])
                i_nov += 1
            if  line[1] == '12':
                dec += float(line[6])
                i_dec += 1
        elif line[0] == 'DATA PERIODS':
            cond = True
            
with open('month_means.csv', 'w') as new_file:
                
    new_file.write(('month,mean_temp\n'))
    new_file.write(('jan,'+str(jan/i_jan)+'\n'))
    new_file.write(('feb,'+str(feb/i_feb)+'\n'))
    new_file.write(('mar,'+str(mar/i_mar)+'\n'))
    new_file.write(('apr,'+str(apr/i_apr)+'\n'))
    new_file.write(('may,'+str(may/i_may)+'\n'))
    new_file.write(('jun,'+str(jun/i_jun)+'\n'))
    new_file.write(('jul,'+str(jul/i_jul)+'\n'))
    new_file.write(('aug,'+str(aug/i_aug)+'\n'))
    new_file.write(('sep,'+str(sep/i_sep)+'\n'))
    new_file.write(('oct,'+str(oct/i_oct)+'\n'))
    new_file.write(('nov,'+str(nov/i_nov)+'\n'))
    new_file.write(('dec,'+str(dec/i_dec)+'\n'))
