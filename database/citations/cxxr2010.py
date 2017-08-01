# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1984 import knuth1984a
from ..work.y1988 import becker1988a
from ..work.y1994 import becker1994a
from ..work.y2005 import gentleman2005a
from ..work.y2008 import callahan2008a
from ..work.y2008 import callahan2008a
from ..work.y2009 import moreau2009a
from ..work.y2010 import silles2010a
from ..work.y2013 import nascimento2013a
from ..work.y2013 import runnalls2013a
from ..work.y2013 import huq2013c
from ..work.y2015 import nascimento2015a


DB(Citation(
    silles2010a, moreau2009a, ref="[1]",
    contexts=[
        "This discipline has developed quickly over the last decade, and isnowreachingmaturitywiththeOpenProvenanceModelfortherepresentation and exchange of provenance information [1].",
        "This will require modifying the serialisation formats of CXXR, and draws into question how best the provenance information collected can be mapped to the Open Provenance Model [1].",
        
    ],
))

DB(Citation(
    silles2010a,
    Site("The R Project for Statistical Computing", "http://www.r-project.org"),
    ref="[2]",
    contexts=[
        "In this paper we look at how facilities for recording and retrieving provenance havebeenintroducedtotheinteractivestatisticalenvironmentandprogramming language, CXXR, which is based on the popular R project [2]",
        "R and CXXR. While S as an application continues life as a commercial product called S+ retailed by TIBCO [8], the language, library and environment have been reimplemented as part of the open-source R project [2].",
        
    ],
))

DB(Citation(
    silles2010a, gentleman2005a, ref="[3]",
    contexts=[
        "Recording process documentation for the purpose of reproducible computing in R has previously been researched in Sweave [3], a system based on concepts of literate programming [4].",
        
    ],
))

DB(Citation(
    silles2010a, knuth1984a, ref="[4]",
    contexts=[
        "Recording process documentation for the purpose of reproducible computing in R has previously been researched in Sweave [3], a system based on concepts of literate programming [4].",
        
    ],
))

DB(Citation(
    silles2010a, callahan2008a, ref="[5]",
    contexts=[
        "Making applications provenance-aware is not in itself a new concept [5]; however, CXXR presents some novel challenges, primarily to the way in which provenance is represented conceptually, but also to the way in which provenance needs to be presented to the user, and how the features of the language require modelling in order to capture complete provenance.",
        
    ],
))


DB(Citation(
    silles2010a, becker1994a, ref="[6]",
    contexts=[
        "S. S is a language and interactive environment for statistical computing, graphics, and exploratory data analysis [6].",
        
    ],
))

DB(Citation(
    silles2010a, becker1988a, ref="[7]",
    contexts=[
        "S AUDIT. ‘New S’ was released in 1988 sporting a new feature entitled S AUDIT [7].",
        
    ],
))

DB(Citation(
    silles2010a,
    Site("Spot re S+", "http://spotfire.tibco.com"),
    ref="[8]",
    contexts=[
        "R and CXXR. While S as an application continues life as a commercial product called S+ retailed by TIBCO [8], the language, library and environment have been reimplemented as part of the open-source R project [2].",
        
    ],
))

DB(Citation(
    silles2010a,
    Site("CXXR project", "http://www.cs.kent.ac.uk/projects/cxxr"),
    ref="[9]",
    contexts=[
        "CXXR is a project to reengineer the fundamental components of the R interpreter from C into C++, while fully preserving functionality of the standard R distribution [9].",
        
    ],
))

DB(Citation(
    nascimento2015a, silles2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    nascimento2013a, silles2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    runnalls2013a, silles2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    huq2013c, silles2010a, ref="",
    contexts=[

    ],
))
