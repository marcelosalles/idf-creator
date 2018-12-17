BASE_DIR = '/media/marcelo/OS'
DATE = '12-07'
documents_list = ['sa_ehf_1storder_'+DATE+'.csv', 'sa_ehf_2ndorder_'+DATE+'.csv',
    'sa_temp_1storder_'+DATE+'.csv', 'sa_temp_2ndorder_'+DATE+'.csv',
    'sa_ach_1storder_'+DATE+'.csv', 'sa_ach_2ndorder_'+DATE+'.csv']

i_doc = 0
f = ''
first = True
with open(BASE_DIR+'/LabEEE_1-2/idf-creator/sa_raw.csv', 'r') as sa_raw:
    
    for line in sa_raw:
        #line = line.split(' ')
        if line.startswith('Parameter'):
            if not first:
                with open(BASE_DIR+'/BS/'+documents_list[i_doc], 'w') as w:
                    w.write(f)
                i_doc +=1
            first = False
            f = ''
        f += line

with open(BASE_DIR+'/BS/'+documents_list[i_doc], 'w') as w:
    w.write(f)
