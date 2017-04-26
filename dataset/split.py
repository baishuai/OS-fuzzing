
import os
import sys
import csv
import random


data_filename = sys.argv[1]
seed = sys.argv[2]

data_dir = "data/"+seed
train_filename = data_dir+"/train.csv"
test_filename = data_dir+"/test.csv"

os.system("mkdir -p "+data_dir)

random.seed(seed)
print("seed", seed)

programs = []


csv.field_size_limit(sys.maxsize)

# we read the list of all programs
with open(data_filename, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    programs = [row[0].split(":")[0]+":" for row in reader]

#vuln_size, norm_size = len(vuln_programs.keys()), len(norm_programs.keys())
prog_size = len(programs)

prog_sample = random.sample(programs, prog_size)
train_prop = 0.75

train_programs = prog_sample[:int(train_prop*prog_size)]
test_programs  = prog_sample[int(train_prop*prog_size):]

# we read the list of all programs
with open(data_filename, 'rb') as csvfile1:
 with open(train_filename, 'wb') as csvfile2:
  with open(test_filename, 'wb') as csvfile3:

    reader1 = csv.reader(csvfile1, delimiter='\t')
    train_csv = csv.writer(csvfile2, delimiter='\t')
    test_csv = csv.writer(csvfile3, delimiter='\t')

    for i,row in enumerate(reader1):
      if (len(row) != 3):
        continue
      if row[0].split(":")[0]+":" in train_programs:
        train_csv.writerow(row)
      elif row[0].split(":")[0]+":" in test_programs:
        test_csv.writerow(row)
      else:
        assert(0)
