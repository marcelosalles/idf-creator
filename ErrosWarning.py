import glob
import pandas

FOLDER = 'sobol_single/cluster1'

files = glob.glob(FOLDER+'/*.err')

errors_dict = {
    'file':[],
    'WarningCompleted': [],
    'SevereCompleted': [],
    'WarningWarmup':[],
    'SevereWarmup': [],
    'WarningSizing':[],
    'SevereSizing': []
}
eps_error = 0
for f in files:
    if f != (FOLDER+'/sqlite.err'):
        file_name = f
        fatal = True
        print(f, end='\r')
        errors_dict["file"].append(f)
        f = open(f, 'r').readlines()
        
        for i in f:
                
            if "************* EnergyPlus Warmup Error Summary" in i:
                errors_dict['WarningWarmup'].append(i[i.find(": ")+2:i.find("Warning;")-1]) 
                errors_dict["SevereWarmup"].append(i[i.find("; ")+2:i.find("Severe")-1])
            if "************* EnergyPlus Sizing Error Summary" in i:
                errors_dict["WarningSizing"].append(i[i.find(": ")+2:i.find("Warning;")-1])
                errors_dict["SevereSizing"].append(i[i.find("; ")+2:i.find("Severe")-1])
            if "************* EnergyPlus Completed Successfully--" in i:
                errors_dict["WarningCompleted"].append(i[i.find('-- ')+3:i.find(' Warning;')])
                errors_dict["SevereCompleted"].append(i[i.find("; ")+2:i.find(" Severe")])
                fatal = False
            if "[EPS][thermal_resistance]" in i:
                eps_error += 1
                
        if fatal:
            errors_dict["WarningCompleted"].append('FATAL')
            errors_dict["SevereCompleted"].append('FATAL')

print('\n','R do EPS baixo: 'eps_error)              
for obj in  errors_dict:
    print(obj, len(errors_dict[obj]))
    
errors_dict = pandas.DataFrame(errors_dict)
errors_dict.to_csv("ResumoErros.csv", index=False)
