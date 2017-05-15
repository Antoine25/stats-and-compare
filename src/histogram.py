#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/04/08
Last modification 2015/04/14

@author: Antoine MARTIN
"""
import os
from matplotlib import pyplot
import numpy
from src.tools import time_folder


class Histogram(object):

    '''
    Histogram class
    '''

    def __init__(self, datas_f1_f2, args, titles):
        self.datas_f1_test = datas_f1_f2[0]
        self.datas_f2_test = datas_f1_f2[1]
        self.test = None
        self.titles = titles
        self.one_curve = False
        if type(self.datas_f1_test) != type(self.datas_f2_test):
            self.datas_f2_test = self.datas_f1_test
            self.one_curve = True
        self.save = args[3]
        self.path = None
        self.blind = args[4]
        self.unit = None
        if self.save is True:
            try:
                self.path = "Results/" + time_folder() + "/"
                os.makedirs(self.path)
            except BaseException:
                pass

    def plot(self, f1_data, f2_data):
        """
        Plot the histogram for f1 and f2 filtering test
        """

        def get_histo_parameters():
            """
            Get histogram parameters
            """
            maxi = max(max(f1_data), max(f2_data)) * 1.5
            mini = min(min(f1_data), min(f2_data)) * 1.5
            if mini < 0 and maxi > 0:
                bins = numpy.linspace(mini, maxi, 100)
            elif mini < 0 and maxi < 0:
                bins = numpy.linspace(mini, 0, 100)
            else:
                bins = numpy.linspace(0, maxi, 100)
            histo_f1 = numpy.histogram(f1_data, bins)
            histo_f2 = numpy.histogram(f2_data, bins)
            label = "Y axe name"
            width = abs(histo_f1[1][1] - histo_f1[1][0])
            if width == 0.0:
                width = 0.05
            return histo_f1, histo_f2, width, label

        histo_f1, histo_f2, width, label = get_histo_parameters()
        pyplot.bar(histo_f1[1][0:-1], histo_f1[0], width, alpha=0.5,
                   label=self.titles[0])
        if self.one_curve is False:
            pyplot.bar(
                histo_f2[1][0:-1], histo_f2[0], width,
                color='#8EC127', alpha=0.5,
                label=self.titles[1])
        pyplot.xlabel(self.test.replace("_", " "))
        pyplot.ylabel(label)
        pyplot.legend(loc='upper right')
        pyplot.grid()
        if self.save is True:
            pyplot.savefig(
                self.path + "/" + self.test)
        if self.blind is False:
            pyplot.show()
        pyplot.close()

    def get_hitogram(self, test):
        """
        Get Histogram datas for f1 and
        f2 filtering test
        """
        self.test = test
        print test
        f2_data = self.datas_f2_test[
            test]
        f1_data = self.datas_f1_test[
            test]
        # print f1_data
        self.plot(f1_data, f2_data)

    def save_or_print(self, test, cpt_f2, cpt_f1):
        """
        log or/and print results
        """
        unit = ""
        if self.save is True:
            output = os.path.abspath(self.path + "/" + test + ".txt")
            with open(output, "a") as log:
                log.write("\n - " + self.test + " :\n")
                log.write(
                    test + " " + self.titles[0] +
                    " = " + str(cpt_f1) + " " + unit + "\n")
                if self.one_curve is False:
                    log.write(
                        test + " " + self.titles[1] +
                        " = " + str(cpt_f2) + " " + unit + "\n")
            log.close()
        if self.blind is False:
            print "     " + test + " " + self.titles[0] + \
                " = " + str(cpt_f1) + " " + unit
            if self.one_curve is False:
                print "     " + test + " " + self.titles[1] + \
                    " = " + str(cpt_f2) + " " + unit
