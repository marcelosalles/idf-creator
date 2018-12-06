import glob
import os

for i in range(10):
    
    # os.chdir('cluster'+str(i))
    
    files = glob.glob('cluster'+str(i)+'/u*.csv')
    
    print(i, len(files),'\n')
