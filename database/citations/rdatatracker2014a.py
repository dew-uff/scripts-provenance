# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2006 import bowers2006a
from ..work.y2008 import scheidegger2008a
from ..work.y2008 import missier2008a
from ..work.y2010 import osterweil2010a
from ..work.y2010 import silles2010a
from ..work.y2011 import lerner2011a
from ..work.y2012 import runnalls2012a
from ..work.y2014 import baumer2014a
from ..work.y2014 import lerner2014a
from ..work.y2014 import r2014a
from ..work.y2014 import lerner2014b
from ..work.y2015 import nascimento2015a
from ..work.y2015 import gammack2015a
from ..work.y2016 import gammack2016a
from ..work.y2016 import lemieux2016a
from ..work.y2016 import missier2016a


DB(Citation(
    lerner2014a, baumer2014a, ref="[1]",
    contexts=[
        "R Markdown [1] is a tool that runs inside the RStudio environment (http://www.rstudio.com/).",
        
    ],
)) 

DB(Citation(
    lerner2014a, bowers2006a, ref="[2]",
    contexts=[
        "Currently, there are numerous systems that helps cientists to collect, visualize, query and use their data provenance, including Kepler [2], Taverna [4], Vistrails [8] and Little-JIL [3, 5], among others",
        
    ],
)) 

DB(Citation(
    lerner2014a, lerner2011a, ref="[3]",
    contexts=[
        "Currently, there are numerous systems that helps cientists to collect, visualize, query and use their data provenance, including Kepler [2], Taverna [4], Vistrails [8] and Little-JIL [3, 5], among others",
        
    ],
))

DB(Citation(
    lerner2014a, missier2008a, ref="[4]",
    contexts=[
        "Currently, there are numerous systems that helps cientists to collect, visualize, query and use their data provenance, including Kepler [2], Taverna [4], Vistrails [8] and Little-JIL [3, 5], among others",
        
    ],
))

DB(Citation(
    lerner2014a, osterweil2010a, ref="[5]",
    contexts=[
        "Currently, there are numerous systems that helps cientists to collect, visualize, query and use their data provenance, including Kepler [2], Taverna [4], Vistrails [8] and Little-JIL [3, 5], among others",
        "The data provenance is stored in a Data Derivation Graph (DDG) [5].",
        
    ],
)) 

DB(Citation(
    lerner2014a, r2014a, ref="[6]",
    contexts=[
        "R [6] is a language that has become very popular among scientists becauseofthestrengthofitssupportforstatisticalanalysisanddata visualization",
        
    ],
))

DB(Citation(
    lerner2014a, runnalls2012a, ref="[7]",
    contexts=[
        "CXXR [7,9]isanimplementationoftheRinterpreterthatcollects provenance by placing hooks within the read-eval-print loop of the interpreter.",
        
    ],
)) 

DB(Citation(
    lerner2014a, scheidegger2008a, ref="[8]",
    contexts=[
        "Currently, there are numerous systems that helps cientists to collect, visualize, query and use their data provenance, including Kepler [2], Taverna [4], Vistrails [8] and Little-JIL [3, 5], among others",
        
    ],
))

DB(Citation(
    lerner2014a, silles2010a, ref="[9]",
    contexts=[
        "CXXR [7,9]isanimplementationoftheRinterpreterthatcollects provenance by placing hooks within the read-eval-print loop of the interpreter.",
        
    ],
))

DB(Citation(
    nascimento2015a, lerner2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gammack2016a, lerner2014a, ref="",
    contexts=[

    ],
))



DB(Citation(
    lemieux2016a, lerner2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gammack2015a, lerner2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    missier2016a, lerner2014a, ref="",
    contexts=[

    ],
))
