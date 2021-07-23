#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/04/08
Last modification 2015/04/14

@author: Antoine MARTIN
"""
from configparser import ConfigParser
import time


def time_folder():
    """
    get folder name according to the date
    """
    def two_digits(enter):
        """
        Make enter with two digits
        """
        if enter >= 10:
            return str(enter)
        else:
            return "0" + str(enter)

    local_time = time.localtime(time.time())
    year = two_digits(local_time[0])
    month = two_digits(local_time[1])
    day = two_digits(local_time[2])
    hour = two_digits(local_time[3])
    minu = two_digits(local_time[4])
    sec = two_digits(local_time[5])

    folder_name = "_".join(["_".join([
        year, month, day]), ":".join([hour, minu, sec])])

    return folder_name


def read_cfg(cfg_file):
    """
    Read test config file
    """
    cfg = ConfigParser()
    cfg.read(cfg_file)
    return cfg


class switch(object):

    """
    Class which allow to make a switch/case
    operation in Python
    """
    value = None

    def __new__(self, value):
        self.value = value
        return True


def case(*args):
    """case function"""
    return any((arg == switch.value for arg in args))
