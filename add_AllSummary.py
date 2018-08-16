
import csv
import os

dir = os.getcwd()
dir = os.chdir(dir+'/pre-analise/')

def take_idf(files):
	idf_files = []

	for file in files:
		if str(file).endswith(".idf"):
			idf_files.append(file)

	return idf_files

def change_idf(files):

	for file in files:
		print(file)
		file_read = open(file, 'r')
		lines = file_read.read()

		lines = lines.replace('!AllSummary','Output:Table:SummaryReports,AllSummary;')

		with open(file, 'w') as file_write:
			file_write.write(lines)

files = os.listdir(dir)
files.sort()
files = take_idf(files)
change_idf(files)
