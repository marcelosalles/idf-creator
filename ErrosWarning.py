import glob
import pandas

SIMULATIONS = 72000
N_CLUSTER = 10
BASE_FOLDER = 'sobol_single/'  # without cluster number


errors_dict = {
    'file':[],
    'WarningCompleted': [],
    'SevereCompleted': [],
    'WarningWarmup':[],
    'SevereWarmup': [],
    'WarningSizing':[],
    'SevereSizing': []
}

batch = SIMULATIONS/N_CLUSTER
for cluster in range(N_CLUSTER):
    
    folder = BASE_FOLDER+'cluster'+str(cluster)

    ok_list = [folder+'/sobol_single_'+'{:05.0f}'.format(i)+'out.err' for i in range(int(cluster*batch),int(cluster*batch+batch))]
    files_pre = glob.glob(folder+'/*.err')
    files = []
    for f in files_pre:
        if f in ok_list:
            files.append(f)

    for f in files:
        if f != (folder+'/sqlite.err'):
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

            
for obj in  errors_dict:
    print(obj, len(errors_dict[obj]))
    
errors_dict = pandas.DataFrame(errors_dict)
errors_dict.to_csv("ResumoErros_12-06.csv", index=False)

