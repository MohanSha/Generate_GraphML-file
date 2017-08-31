import csv
import glob
files = glob.glob('*.txt')
for file in files:
with open('result.txt', 'w') as result:
result.write(str(file)+'\n')
