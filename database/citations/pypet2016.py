# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2002 import wolfram2002a
from ..work.y2004 import cook2004a
from ..work.y2004 import fangohr2004a
from ..work.y2005 import bavoil2005a
from ..work.y2006 import carnevale2006a
from ..work.y2007 import backer2007a
from ..work.y2007 import borcherds2007a
from ..work.y2007 import oliphant2007a
from ..work.y2007 import perez2007a
from ..work.y2008 import davison2008a
from ..work.y2008 import goodman2008a
from ..work.y2009 import stimberg2009a
from ..work.y2011 import mckinney2011a
from ..work.y2011 import stodden2011a
from ..work.y2011 import walt2011a
from ..work.y2012 import davison2012a
from ..work.y2012 import fortin2012a
from ..work.y2012 import ince2012a
from ..work.y2012 import lin2012a
from ..work.y2013 import antolik2013a
from ..work.y2013 import meyerovich2013a
from ..work.y2013 import reimann2013a
from ..work.y2013 import stevens2013a
from ..work.y2014 import gewaltig2014a
from ..work.y2014 import hold2014a
from ..work.y2014 import potjans2014a
from ..work.y2014 import stimberg2014a
from ..work.y2015 import muller2015b
from ..work.y2015 import stockton2015a
from ..work.y2015 import topalidou2015a
from ..work.y2016 import meyer2016a
from ..work.y2016 import geit2016a

DB(Citation(
    meyer2016a, antolik2013a, ref="Antolik and Davison, 2013",
    contexts=[
        "Mozaik (Antolík and Davison, 2013) is a Python data management toolkit especially designed for network simulations of two-dimensional neural sheets.",
    ],
))

DB(Citation(
    meyer2016a, backer2007a, ref="Backer, 2007",
    contexts=[
        "Python is increasingly used in neuroscience (Muller et al., 2015) and other scientiﬁc disciplines (Fangohr, 2004; Bäcker, 2007; Borcherds, 2007; Lin, 2012; Meyerovich and Rabkin, 2013).",
    ],
))

DB(Citation(
    meyer2016a, bavoil2005a, ref="Bavoil et al., 2005",
    contexts=[
        "VisTrails (Bavoil et al., 2005) is a workﬂow and provenance management system written in Python that focuses on automation of visualizations",

    ],
))

DB(Citation(
    meyer2016a, borcherds2007a, ref="Borcherds, 2007",
    contexts=[
        "Python is increasingly used in neuroscience (Muller et al., 2015) and other scientiﬁc disciplines (Fangohr, 2004; Bäcker, 2007; Borcherds, 2007; Lin, 2012; Meyerovich and Rabkin, 2013).",
    ],
))

DB(Citation(
    meyer2016a, carnevale2006a, ref="Carnevale and Hines, 2006",
    contexts=[
        "NeuroManager, written in object-oriented MATLAB, allows the user to specify simulations in terms of pure MATLAB code or MATLAB code wrapping existing simulators like NEURON (Carnevale and Hines, 2006).",
    ],
))

DB(Citation(
    meyer2016a, cook2004a, ref="Cook, 2004",
    contexts=[
        "For example, the prominent rule 110, that is proven to be Turing complete (Cook, 2004), follows the state updates speciﬁed in Table 1",
    ],
))

DB(Citation(
    meyer2016a, davison2008a, ref="Davison, 2008",
    contexts=[
        "It relies on the simulator environment PyNN (Davison, 2008).",

    ],
))

DB(Citation(
    meyer2016a, davison2012a, ref="Davison, 2012",
    contexts=[
        "Sumatra integration, pypet can automatically add one’s simulations to the electronic lab notebook tool Sumatra (Davison, 2012)",
        "The primary goal of Sumatra (Davison, 2012) is to enhance reproducible research.",
        ".Therefore,pypetcouldbecombinedwithGitPython17 for source code version control and with Sumatra (Davison, 2012) to track versions of all applied software.",
    ],
))

DB(Citation(
    meyer2016a, fangohr2004a, ref="Fangohr, 2004",
    contexts=[
        "Python is increasingly used in neuroscience (Muller et al., 2015) and other scientiﬁc disciplines (Fangohr, 2004; Bäcker, 2007; Borcherds, 2007; Lin, 2012; Meyerovich and Rabkin, 2013).",
    ],
))

DB(Citation(
    meyer2016a, fortin2012a, ref="Fortin et al., 2012",
    contexts=[
        "Adaptively exploring the parameter space combining pypet with optimization tools like the evolutionary algorithms framework DEAP (Fortin et al., 2012)",
        "A combination of pypet, SCOOP (Hold-Geoﬀroy et al., 2014), and the evolutionary algorithm toolkit DEAP (Fortin et al., 2012) could be used to optimize hyper parameters of a machine learning application, like image classiﬁcation.",
    ],
))

DB(Citation(
    meyer2016a, gewaltig2014a, ref="Gewaltig and Cannon, 2014",
    contexts=[
        "functionality is well tested (Gewaltig and Cannon, 2014).",
    ],
))

DB(Citation(
    meyer2016a, goodman2008a, ref="Goodman and Brette, 2008",
    contexts=[
        "BRIAN and BRIAN2 quantities and monitors (Goodman and Brette, 2008; Stimberg et al., 2014)",
        "For instance, the SparseParameter is a container for SciPy sparse matrices (Oliphant, 2007) and the BrianParameter can manage quantities of the BRIAN simulator package (Goodman and Brette, 2008).",
    ],
))

DB(Citation(
    meyer2016a, hold2014a, ref="Hold-Geoffroy et al., 2014",
    contexts=[
        "Pypet can be used on computing clusters or multiple servers at once if it is combined with the SCOOP framework (Hold-Geoffroy et al., 2014)",
        "A combination of pypet, SCOOP (Hold-Geoﬀroy et al., 2014), and the evolutionary algorithm toolkit DEAP (Fortin et al., 2012) could be used to optimize hyper parameters of a machine learning application, like image classiﬁcation.",
    ],
))

DB(Citation(
    meyer2016a, ince2012a, ref="Ince et al., 2012",
    contexts=[
        "There is an ongoing debate about the mandatory publication of source code in scientiﬁc research (Ince et al., 2012).",
    ],
))

DB(Citation(
    meyer2016a, lin2012a, ref="Lin, 2012",
    contexts=[
        "Python is increasingly used in neuroscience (Muller et al., 2015) and other scientiﬁc disciplines (Fangohr, 2004; Bäcker, 2007; Borcherds, 2007; Lin, 2012; Meyerovich and Rabkin, 2013).",

    ],
))

DB(Citation(
    meyer2016a, mckinney2011a, ref="McKinney, 2011",
    contexts=[
        "Pandas Series, DataFrame, and Panel (McKinney, 2011)",
        "Moreover, Result containers are less restrictive than Parameters in terms of data they accept. They can also handle Python dictionaries, the Python implementation of a hash map, and Pandas DataFrames (McKinney, 2011), a tabular data structure.",
    ],
))

DB(Citation(
    meyer2016a, meyerovich2013a, ref="Meyerovich and Rabkin, 2013",
    contexts=[
        "Python is increasingly used in neuroscience (Muller et al., 2015) and other scientiﬁc disciplines (Fangohr, 2004; Bäcker, 2007; Borcherds, 2007; Lin, 2012; Meyerovich and Rabkin, 2013).",
    ],
))

DB(Citation(
    meyer2016a, muller2015b, ref="Muller et al., 2015",
    contexts=[
        "Python is increasingly used in neuroscience (Muller et al., 2015) and other scientiﬁc disciplines (Fangohr, 2004; Bäcker, 2007; Borcherds, 2007; Lin, 2012; Meyerovich and Rabkin, 2013).",
    ],
))

DB(Citation(
    meyer2016a, oliphant2007a, ref="Oliphant, 2007",
    contexts=[
        "SciPy sparse matrices (Oliphant, 2007)",
        "For instance, the SparseParameter is a container for SciPy sparse matrices (Oliphant, 2007) and the BrianParameter can manage quantities of the BRIAN simulator package (Goodman and Brette, 2008).",
    ],
))

DB(Citation(
    meyer2016a, perez2007a, ref="Perez and Granger, 2007",
    contexts=[
        "Lancet (Stevens et al., 2013) constitutes a more general approach to workﬂow management and integrates with IPython notebooks (Perez and Granger, 2007)",

    ],
))

DB(Citation(
    meyer2016a, potjans2014a, ref="Potjans and Diesmann, 2014",
    contexts=[
        "Similarly, Potjans and Diesmann (2014) built a full-scale spiking neuron network model of a cortical microcircuit.",
        "Furthermore, simulations are usually highly parameterized, with up to hundreds of parameters (Reimann et al., 2013; Potjans and Diesmann, 2014).",
    ],
))

DB(Citation(
    meyer2016a, reimann2013a, ref="Reimann et al., 2013",
    contexts=[
        "For instance, Reimannetal.(2013)simulatedlocalﬁeldpotentialsinaneuralnetworkofmorethan12,000multicompartmental cells.",
        "Furthermore, simulations are usually highly parameterized, with up to hundreds of parameters (Reimann et al., 2013; Potjans and Diesmann, 2014).",
    ],
))

DB(Citation(
    meyer2016a, stevens2013a, ref="",
    contexts=[
        "Lancet (Stevens et al., 2013) constitutes a more general approach to workﬂow management and integrates with IPython notebooks (Perez and Granger, 2007)",
    ],
))

DB(Citation(
    meyer2016a, stimberg2014a, ref="Stimberg et al., 2014",
    contexts=[
        "BRIAN and BRIAN2 quantities and monitors (Goodman and Brette, 2008; Stimberg et al., 2014)",
    ],
))

DB(Citation(
    meyer2016a, stimberg2009a, ref="Stimberg et al., 2009",
    contexts=[
        "For instance, the visual cortex network model by Stimberg et al. (2009) is based on several tens of parameters, but the authors varied only two of these comprehensively.",
    ],
))

DB(Citation(
    meyer2016a, stockton2015a, ref="Stockton and Santamaria, 2015",
    contexts=[
        "NeuroManager (Stockton and Santamaria, 2015) facilitates automated scheduling of simulations in MATLAB with heterogeneous computational resources.",
    ],
))

DB(Citation(
    meyer2016a, stodden2011a, ref="Stodden, 2011",
    contexts=[
        "These conditions make numerical experiments hard to reproduce. Stodden (2011) even speaks of a “credibility crisis” of computational results.",
    ],
))

DB(Citation(
    meyer2016a, topalidou2015a, ref="Topalidou et al., 2015",
    contexts=[
        "Even when researchers are willing to inspect source code, ill-documentation often prohibits them from successfully reimplementing published models (Topalidou et al., 2015).",
    ],
))

DB(Citation(
    meyer2016a, walt2011a, ref="van der Walt et al., 2011",
    contexts=[
        "• NumPy arrays and matrices (van der Walt et al., 2011)",
    ],
))

DB(Citation(
    meyer2016a, geit2016a, ref="Van Geit et al., 2016",
    contexts=[
        "If the user does not care about these, but she is only interested in the ﬁnal best parameters, DEAP—alone or in combination with BluePyOpt (Van Geit et al., 2016) for optimizing neural models—is already sufficient.",
    ],
))

DB(Citation(
    meyer2016a, wolfram2002a, ref="Wolfram, 2002",
    contexts=[
        "We will simulate one dimensional elementary cellular automata (Wolfram, 2002).",
    ],
))
