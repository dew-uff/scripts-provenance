# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1945 import porges1945a
from ..work.y1981 import weiser1981a
from ..work.y1990 import agrawal1990a
from ..work.y2010 import angelino2010a
from ..work.y2012 import tariq2012a
from ..work.y2014 import chen2014a
from ..work.y2014 import lerner2014a
from ..work.y2014 import murta2014a
from ..work.y2015 import pimentel2015a
from ..work.y2016 import pimentel2016a
from ..work.y2016 import pimentel2016b

DB(Citation(
    pimentel2016b, agrawal1990a, ref="[1]",
    contexts=[
        "We capture and analyze dependencies among variables during the script execution (a trial), and apply dynamic program slicing [1] to identify which dependencies actually exist among functions and files.",
        
    ],
))

DB(Citation(
    pimentel2016b, angelino2010a, ref="[2]",
    contexts=[
        "Scientists may use scripts to perform intensive computational tasks such as data analyses and explorations [2].",
        "Some automatic approaches capture provenance at the function level [2, 5, 9].",
        
    ],
))

DB(Citation(
    pimentel2016b, chen2014a, ref="[3]",
    contexts=[
        "Although doing dynamic program slicing over Python is not new [3], we differentiate ourselves by capturing variable values and other provenance data in addition to slices",
        "For instance, when we have n = 10; final = process(n), Chen et al. [3] capture only that final depends on n and the position in memory of these variables to link them.",
        
    ],
))

DB(Citation(
    pimentel2016b, lerner2014a, ref="[4]",
    contexts=[
        "In contrast, RDataTracker [4] captures the occurrence of variable bindings along with function level provenance.",
        
    ],
))

DB(Citation(
    pimentel2016b, murta2014a, ref="[5]",
    contexts=[
        "However, collecting provenance of scripts is challenging [5].",
        "Some automatic approaches capture provenance at the function level [2, 5, 9].",
        "However, as the script calls process before show, function-based approaches [5, 9] would say that show depends on process.",
        "As a preliminary proof of concept, we implemented this approach in noWorkflow [5–7], an open-source system that transparently captures provenance from Python scripts at the function activation level.",
        
    ],
))

DB(Citation(
    pimentel2016b, pimentel2016a, ref="[6]",
    contexts=[
        "As a preliminary proof of concept, we implemented this approach in noWorkflow [5–7], an open-source system that transparently captures provenance from Python scripts at the function activation level.",
        
    ],
))

DB(Citation(
    pimentel2016b, pimentel2015a, ref="[7]",
    contexts=[
        "As a preliminary proof of concept, we implemented this approach in noWorkflow [5–7], an open-source system that transparently captures provenance from Python scripts at the function activation level.",
        
    ],
))

DB(Citation(
    pimentel2016b, porges1945a, ref="[8]",
    contexts=[
        "For instance, Fig. 1 shows an intentionally simple implementation of the happy numbers problem [8], where the code calls two functions, process and show, in sequence (lines 17 and 20), leading to the inference that the show result depends on the process result",
        
    ],
))

DB(Citation(
    pimentel2016b, tariq2012a, ref="[9]",
    contexts=[
        "Some automatic approaches capture provenance at the function level [2, 5, 9].",
        "However, as the script calls process before show, function-based approaches [5, 9] would say that show depends on process.",
        
    ],
))

DB(Citation(
    pimentel2016b, weiser1981a, ref="[10]",
    contexts=[
        "To do so, we use program slicing [10].",
        
    ],
))
