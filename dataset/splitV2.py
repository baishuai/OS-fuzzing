import csv
import os
import random
import sys

data_filename = sys.argv[1]
seed = sys.argv[2]

data_dir = "data/" + seed
train_filename = data_dir + "/train.csv"
test_filename = data_dir + "/test.csv"

os.system("mkdir -p " + data_dir)

random.seed(seed)
print("seed", seed)

testcases = []

csv.field_size_limit(sys.maxsize)

# we read the list of all programs
with open(data_filename, 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    testcases = [row for row in reader]

testcases_size = len(testcases)

testcases_sample = random.sample(testcases, testcases_size)
train_prop = 0.75

train_testcases = testcases_sample[:int(train_prop * testcases_size)]
test_testcases = testcases_sample[int(train_prop * testcases_size):]

# we read the list of all programs
with open(train_filename, 'wb') as csvfile:
    train_csv = csv.writer(csvfile, delimiter='\t')
    for row in train_testcases:
        train_csv.writerow(row)

with open(test_filename, 'wb') as csvfile:
    test_csv = csv.writer(csvfile, delimiter='\t')
    for row in testcases:
        test_csv.writerow(row)
