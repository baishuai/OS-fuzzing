import argparse
import os

import numpy as np
import pandas as pd

from plt import plt_speedup


def Analyze(testf, predf):
    test = pd.read_table(testf, header=None)
    pred = pd.read_table(predf, header=None)
    testv = test[2]
    predv = pred[1]

    tv = [len(testv) - testv.sum(), testv.sum()]

    sumv = testv + predv
    pv = []
    pv.append(len(np.where(sumv == 0)[0]))
    pv.append(tv[0] - pv[0])
    pv.append(len(np.where(sumv == 2)[0]))
    pv.append(tv[1] - pv[2])
    tv = np.array(tv).astype(np.float64)
    pv = np.array(pv).astype(np.float64)
    print(tv, pv)
    plt_speedup(tv, pv)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Vulnerability Detection Procedure')
    parser.add_argument("dir", help="dir of prediction result", default=None, type=str)

    option = parser.parse_args()

    sep = "" if option.dir.endswith(os.sep) else os.sep
    test = option.dir + sep + 'test.csv'
    pred = option.dir + sep + 'pred.csv'

    ana_plt(test, pred)

