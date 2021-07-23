#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/04/08
Last modification 2015/04/14

@author: Antoine MARTIN
"""
try:
    import argparse
    from src.tools import read_cfg
    from src.histogram import Histogram
    import pandas
except ImportError as error:
    print("Import Error")
    print(error)
    exit()


def main(args):
    """
    CSV Comparison - MAIN
    """
    cfg = read_cfg(args[0])
    titles = [cfg.get('Histogram', 'File1'), cfg.get('Histogram', 'File2')]
    label = cfg.get('Histogram', 'Label')
    print("Reading data...")
    datas_f1_test = pandas.read_csv(args[1], delimiter=',', engine='c')
    if args[2] is None:
        datas_f2_test = None
    else:
        datas_f2_test = pandas.read_csv(args[2], delimiter=',', engine='c')
    datas_f1_f2 = [datas_f1_test, datas_f2_test]
    histogram = Histogram(datas_f1_f2, args, titles, label)
    for test in datas_f1_test.columns.values:
        print(test)
        histogram.get_hitogram(test)


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description='Test Information')
    PARSER.add_argument("-c", "--configFile", dest="configFile",
                        default="TestsComparison.cfg",
                        help="Test config file")
    PARSER.add_argument("-f1", "--file1", dest="file1",
                        default="file1.csv",
                        help="CSV file 1")
    PARSER.add_argument("-f2", "--file2", dest="file2",
                        help="CSV file 2")
    PARSER.add_argument("-s", "--save", dest="save", action='store_true',
                        default=False,
                        help="Save log & graph")
    PARSER.add_argument("-b", "--blind", dest="blind", action='store_true',
                        default=False,
                        help="don't display graph")
    PARSER.add_argument("-n", "--normalized", dest="normalized",
                        action='store_true', default=False,
                        help="absolue scale in graph")
    ARGS = PARSER.parse_args()
    ALL_ARG = [
        ARGS.configFile, ARGS.file1, ARGS.file2,
        ARGS.save, ARGS.blind, ARGS.normalized]
    main(ALL_ARG)
