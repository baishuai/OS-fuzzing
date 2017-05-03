import csv
import os
import random
import sys


def split(data_filename, seed, target_dir = 'dataset'):
    data_dir = target_dir + "/data/" + str(seed)
    train_filename = data_dir + "/train.csv"
    test_filename = data_dir + "/test.csv"

    os.system("mkdir -p " + data_dir)
    # seed += 21
    random.seed(seed)

    programs = dict()
    data_size = 0
    csv.field_size_limit(sys.maxsize)

    # we read the list of all programs
    with open(data_filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            data_size += 1
            programs[row[0].split(":")[0]] = 1

    # vuln_size, norm_size = len(vuln_programs.keys()), len(norm_programs.keys())
    print("data size", data_size),
    # print("program sizes", len(programs))
    prog_size = len(programs.keys())

    prog_sample = random.sample(programs.keys(), prog_size)
    train_prop = 0.75

    train_programs = prog_sample[:int(train_prop * prog_size)]
    test_programs = prog_sample[int(train_prop * prog_size):]

    train_size = 0
    test_size = 0
    # we read the list of all programs
    with open(data_filename, 'rb') as csvfile1:
        with open(train_filename, 'wb') as csvfile2:
            with open(test_filename, 'wb') as csvfile3:

                reader1 = csv.reader(csvfile1, delimiter='\t')
                train_csv = csv.writer(csvfile2, delimiter='\t')
                test_csv = csv.writer(csvfile3, delimiter='\t')

                for i, row in enumerate(reader1):
                    if (len(row) != 3):
                        continue
                    if row[0].split(":")[0] in train_programs:
                        train_csv.writerow(row)
                        train_size += 1
                    elif row[0].split(":")[0] in test_programs:
                        test_csv.writerow(row)
                        test_size += 1
                    else:
                        assert (0)

    print("train size", train_size),
    print("test size", test_size)


if __name__ == '__main__':
    data_filename = sys.argv[1]
    seed = sys.argv[2]
