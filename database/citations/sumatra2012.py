# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2003 import hucka2003a
from ..work.y2004 import mcconnell2004a
from ..work.y2007 import brette2007a
from ..work.y2009 import donoho2009a
from ..work.y2009 import drummond2009a
from ..work.y2010 import koop2010a
from ..work.y2011 import guo2011a
from ..work.y2011 import brammer2011a
from ..work.y2011 import gorp2011a
from ..work.y2011 import nowakowski2011a
from ..work.y2011 import stodden2011a
from ..work.y2012 import davison2012a
from ..work.y2012 import freire2012a
from ..work.y2013 import crook2013a
from ..work.y2013 import hunold2013a
from ..work.y2013 import mattioni2013a
from ..work.y2013 import hull2013a
from ..work.y2013 import heiberg2013a
from ..work.y2013 import oxberry2013a
from ..work.y2014 import ruiz2014a
from ..work.y2014 import guerrera2014a
from ..work.y2014 import davison2014a
from ..work.y2014 import stimberg2014a
from ..work.y2014 import howe2014a
from ..work.y2014 import fisch2014a
from ..work.y2014 import arabas2014a
from ..work.y2014 import hull2014a
from ..work.y2014 import pham2014a
from ..work.y2014 import kubilius2014a
from ..work.y2014 import castilho2014a
from ..work.y2014 import neves2014a
from ..work.y2014 import silles2014a
from ..work.y2015 import banati2015a
from ..work.y2015 import hutton2015a
from ..work.y2015 import banati2015b
from ..work.y2015 import buchert2015a
from ..work.y2015 import fisch2015a
from ..work.y2015 import metaxas2015a
from ..work.y2015 import nowke2015a
from ..work.y2015 import mahadev2015a
from ..work.y2015 import stockton2015a
from ..work.y2015 import heroux2015a
from ..work.y2015 import buchert2015b
from ..work.y2015 import hutton2015b
from ..work.y2015 import burkhart2015a
from ..work.y2015 import greff2015a
from ..work.y2015 import smith2015a
from ..work.y2015 import lazzarato2015a
from ..work.y2016 import mcdougal2016a
from ..work.y2016 import smith2016a
from ..work.y2016 import banati2016a
from ..work.y2016 import ledet2016a
from ..work.y2016 import albert2016a
from ..work.y2016 import carver2016a
from ..work.y2016 import bezaire2016a
from ..work.y2016 import banati2016b
from ..work.y2016 import pimentel2016e
from ..work.y2016 import banati2016c
from ..work.y2016 import schulz2016a
from ..work.y2016 import smith2016b
from ..work.y2016 import miksa2016a


DB(Citation(
    davison2012a, brammer2011a, ref="1",
    contexts=[
        "Taking a snapshot of the entire environment [1, 12] has the advantages of simplicity (both in taking the snapshot and in later making use of it to replicate the results) and of guaranteed comprehensiveness.",
    ],
))

DB(Citation(
    davison2012a, brette2007a, ref="2",
    contexts=[
        "I will now present an example of using the Sumatra command line interface, in a scenario of attempting to re-run some simulations that were originally performed several years ago. The code was taken from the SenseLab ModelDB database at http://senselab.med.yale. edu/modeldb/ShowModel.asp?model=83319, and consists of the implementation of a number of benchmark neuronal network models in several diﬀerent simulators, associated with a review article on spiking neuronal network simulators [2].",
    ],
))

DB(Citation(
    davison2012a, crook2013a, ref="3",
    contexts=[
        "The term “reproducible research” in computational science covers a spectrum of activities [3], distinguished by who is doing the reproducing, and to what degree they have access to, or make use of access to, the materials developed by the original researchers.",
    ],
))

DB(Citation(
    davison2012a, donoho2009a, ref="4",
    contexts=[
        "However, it is widely recognized that published research in diverse scientiﬁc domains that rely on numerical computation is too infrequently reproducible, with some commentators speaking of a “credibility crisis” [4, 11]",
        "In this article I have tried to establish (i) that reproducibility/replicability is both necessary in ensuring the credibility of scientiﬁc research (as has been noted elsewhere [4, 11])",
    ],
))

DB(Citation(
    davison2012a, drummond2009a, ref="5",
    contexts=[
        "All points on the spectrum are valuable (although some have argued diﬀerently [5]), fully-independent reproduction being critical to the integrity of the scientiﬁc process, while being able to re-run the original code to get the same results (sometimes called “replication” to distinguish it from independent reproduction [5]) is fundamental to software engineering: reuse of existing code (usually organized into libraries) hugely accelerates the process of developing new functionality and hence doing new science.",
    ],
))

DB(Citation(
    davison2012a, guo2011a, ref="6",
    contexts=[
        "Lightweight equivalents to taking a full VM snapshot [6] would also allow using the dual approach for every exploratory computation.",
    ],
))

DB(Citation(
    davison2012a, hucka2003a, ref="7",
    contexts=[
        "In the middle, having a declarative, machine-readable description of the methodology (for example, using SBML [7] in systems biology), someone other than the original author(s) re-running the code, or writing a new implementation from scratch, perhaps in a diﬀerent language, but with access to the original source code.",
    ],
))

DB(Citation(
    davison2012a, koop2010a, ref="8",
    contexts=[
        "(vi) the output data (including graphs, ﬁgures, etc., as well as any log ﬁles), carefully linked to the computation that produced them and again veriﬁed with a cryptographic hash (see [8] for the use of this approach in provenance tracking).",
    ],
))

DB(Citation(
    davison2012a, mcconnell2004a, ref="9",
    contexts=[
        "Strategies for more robust code are widely employed in professional software development and have been described in many places [9]; they include reducing the tightness of the coupling between diﬀerent parts of the code through a modular design and well-deﬁned interfaces, building on established, widely-used and well-tested libraries, writing test suites.",
    ],
))

DB(Citation(
    davison2012a, nowakowski2011a, ref="10",
    contexts=[
        "The majority of articles about, and tools to assist with, reproducible research focus on reproducibility of published research, e.g. [10, 12].",
    ],
))

DB(Citation(
    davison2012a, stodden2011a, ref="11",
    contexts=[
        "However, it is widely recognized that published research in diverse scientiﬁc domains that rely on numerical computation is too infrequently reproducible, with some commentators speaking of a “credibility crisis” [4, 11]",
        "In this article I have tried to establish (i) that reproducibility/replicability is both necessary in ensuring the credibility of scientiﬁc research (as has been noted elsewhere [4, 11])",
    ],
))

DB(Citation(
    davison2012a, gorp2011a, ref="12",
    contexts=[
        "Taking a snapshot of the entire environment [1, 12] has the advantages of simplicity (both in taking the snapshot and in later making use of it to replicate the results) and of guaranteed comprehensiveness.",
        "The majority of articles about, and tools to assist with, reproducible research focus on reproducibility of published research, e.g. [10, 12].",
    ],
))

DB(Citation(
    banati2015a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ruiz2014a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mcdougal2016a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hutton2015a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    guerrera2014a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hunold2013a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    banati2015b, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    buchert2015a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    davison2014a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mattioni2013a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    fisch2015a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stimberg2014a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    freire2012a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    metaxas2015a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    nowke2015a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    howe2014a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mahadev2015a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hull2013a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    fisch2014a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    arabas2014a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    smith2016a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    banati2016a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stockton2015a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    heroux2015a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hull2014a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    pham2014a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kubilius2014a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    castilho2014a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    buchert2015b, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ledet2016a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    albert2016a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    carver2016a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bezaire2016a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    banati2016b, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    heiberg2013a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hutton2015b, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    neves2014a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    burkhart2015a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    pimentel2016e, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    greff2015a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    smith2015a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lazzarato2015a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    silles2014a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    banati2016c, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    schulz2016a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    smith2016b, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    miksa2016a, davison2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    oxberry2013a, davison2012a, ref="",
    contexts=[

    ],
))
