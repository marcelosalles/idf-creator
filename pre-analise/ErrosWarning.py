import glob
import pandas

nomeArquivoGrupoErro = 'group.errgrp'

dadoArquivoGrupoErro = open(nomeArquivoGrupoErro, 'r')
dadoArquivoGrupoErro = dadoArquivoGrupoErro.readlines()

bancoErros = {'IDF':[],'Weather': [],'WarningCompleted': [], 'SevereCompleted': [],
'WarningWarmup':[], 'SevereWarmup': [], 'WarningSizing':[], 'SevereSizing': []}
for i in dadoArquivoGrupoErro:
	if "Input File:     " in i:
		bancoErros["IDF"].append(i[i.rfind("\\")+1:])
	if "Weather File:   " in i:
		bancoErros["Weather"].append(i[i.rfind("\\")+1:])
	if "************* EnergyPlus Warmup Error Summary" in i:
		bancoErros['WarningWarmup'].append(i[i.find(": ")+2:i.find("Warning;")-1]) 
		bancoErros["SevereWarmup"].append(i[i.find("; ")+2:i.find("Severe")-1])
	if "************* EnergyPlus Sizing Error Summary" in i:
		bancoErros["WarningSizing"].append(i[i.find(": ")+2:i.find("Warning;")-1])
		bancoErros["SevereSizing"].append(i[i.find("; ")+2:i.find("Severe")-1])
	if "************* EnergyPlus Completed Successfully--" in i:
		bancoErros["WarningCompleted"].append(i[i.find('-- ')+3:i.find(' Warning;')])
		bancoErros["SevereCompleted"].append(i[i.find("; ")+2:i.find(" Severe")])
	elif "************* EnergyPlus Terminated--Fatal" in i:
		bancoErros["WarningCompleted"].append(i[i.find('-- ')+3:i.find(' Warning;')])
		bancoErros["SevereCompleted"].append(i[i.find("; ")+2:i.find(" Severe")])

bancoErros = pandas.DataFrame(bancoErros)

bancoErros.to_csv("ResumoErros.csv", index=False)
