import glob

files = glob.glob('*.csv')

for file in files:

    print(file)

    with open(file, 'r') as file_read:
        x = file_read.readlines()
        print(len(x))