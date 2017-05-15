===============
Stats & Compare
===============

Presentation
============

:version: 0.1
:Author: Antoine MARTIN
:Contact: antoine.martin222@gmail.com

This tool permit to compare paramaters from 2 CSV files or make some stats with one CSV file


The following libraries must be install on your computer :

- matplotlib
- pandas
- Numpy


Launch TestsComparison
----------------------

.. code-block:: console

    python TestsComparison.py [-h] [-c CONFIG_FILE] [-f1 CSV_FILE_1] [-f2 CSV_FILE_2]  [-s] [-n] [-b]

Arguments :

- [-h] (optional) display help and exit

- [-c CONFIGFILE] (required) is to specify the path of the configuration file. If not specified, the default configuration file path is "./TestsComparison.cfg".

- [-f1 CSV_FILE_1] (required) define the path of the first csv file. If not specified, the default value is "file1.csv".

- [-f2 CSV_FILE_2] (optional) define the path of the second csv file. If not specified, the default value is "None".

- [-s] (optional) permit to save the graphs in a "Results" folder.

- [-n] (optional) permit to normalize the histogram.

- [-b] (optional) don't display the graphs.

