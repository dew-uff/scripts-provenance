# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2009 import goodman2009a
from ..work.y2010 import mckinney2010a
from ..work.y2012 import davison2012a
from ..work.y2015 import meyer2015a

DB(Citation(
    meyer2015a, Site("Meyer R, Obermayer K: pypet", "http://pypet.readthedocs.org/"), ref="[1]",
    contexts=[
        "“pypet“ (python parameter exploration toolkit [1])",
    ],
))

DB(Citation(
    meyer2015a, goodman2009a, ref="[2]",
    contexts=[
        "Moreover, special focus is put on managing different neuron models in python network simulations like BRIAN [2].",
        "A rich set of data formats is supported, encompassing native python types, numpy and scipy data, pandas DataFrames [5], and data from BRIAN [2]",
    ],
))

DB(Citation(
    meyer2015a, Site("The HDF Group: Hierarchical Data Format, version 5.", "http://www. hdfgroup.org/HDF5/"), ref="[3]",
    contexts=[
        "Simulation parameters as well as the obtained results are collected by pypet and stored in the widely used HDF5 file format [3].",
    ],
))


DB(Citation(
    meyer2015a, davison2012a, ref="[4]",
    contexts=[
        "For example, among these are multiprocessing for fast parallel simulations, dynamic loading of data, integration of Git version control, and supervision of experiments via the electronic lab notebook Sumatra [4].",
    ],
))

DB(Citation(
    meyer2015a, mckinney2010a, ref="[5]",
    contexts=[
        "A rich set of data formats is supported, encompassing native python types, numpy and scipy data, pandas DataFrames [5], and data from BRIAN [2]",
    ],
))
