# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2005 import bavoil2005a
from ..work.y2011 import guo2011a
from ..work.y2011 import moreau2011b
from ..work.y2011 import bonnet2011a
from ..work.y2012 import freire2012a
from ..work.y2012 import best2012a
from ..work.y2012 import pham2012a
from ..work.y2012 import stodden2012a
from ..work.y2013 import murphy2013a
from ..work.y2013 import pham2013a


DB(Citation(
    pham2013a, bonnet2011a, ref="[1]",
    contexts=[
        "However, as documented by recent experiments, repeatability testing can be arduous and time consuming for both authors and testers [1, 2]",
        
    ],
))

DB(Citation(
    pham2013a, freire2012a, ref="[2]",
    

    texts=[
        "However, as documented by recent experiments, repeatability testing can be arduous and time consuming for both authors and testers [1, 2]",
        
    ],
))

DB(Citation(
    pham2013a, 
    DB(Site("Repeatability & Workability for the Software Community: Challenges, Experiences, and the Future", "http://www.cs.utah.edu/~eeide/archive10/slides/shasha.pd",
            authors="Sasha, D.")),
    ref="[3]",
    contexts=[
        "But more so, as experiments become data and computation intensive, the testing time can be significant [3].",
        
    ],
))

DB(Citation(
    pham2013a, guo2011a, ref="[4]",
    contexts=[
        "Recently tools have emerged that aid authors and testers in making their software and thus experiments repeatable. CDE helps authors package the code, data, and environment for Linux programs so that they can be run and deployed on other machines without installation or configuration [4].",
        "PTU uses CDE [4] to create and run a package",
        "By doing so, CDE creates a chroot-like sandbox that tricks the target program into ‘believing’ that it is executing on the original machine [4]",
        
    ],
))

DB(Citation(
    pham2013a, bavoil2005a, ref="[5]",
    contexts=[
        "VisTrails provides provenance support for exploratory computational tasks, maintaining detailed history information about the steps followed in during exploration [5].",
        
    ],
))

DB(Citation(
    pham2013a, stodden2012a, ref="[6]",
    contexts=[
        "RunMyCode.org provides repeatability and workability of computer codes [6] associated with a publication through a companion website",
        
    ],
))

DB(Citation(
    pham2013a, pham2012a, ref="[7]",
    contexts=[
        "Finally, SOLE allows an author to associate their code and data directly with text phrases in the publication, obviating the need for detailed documentation, yet improving readability and understandability for testers [7]",
        
    ],
))

DB(Citation(
    pham2013a, 
    DB(Site("PTU: Using Provenance for Repeatability Testing", "http://www.ci.uchicago.edu/SOLE/PTU.html",
            authors="Pham, Q.")),
    ref="[8]",
    contexts=[
        "Provenance-To-Use (PTU) [8] is a tool for accelerating and simplifying repeatability testing.",
        "The provenance graphs and configuration files for the programs are available online [8]. Figures",
        
    ],
    accessed="2013",
))

DB(Citation(
    pham2013a, moreau2011b, ref="[9]",
    contexts=[
        "This information can be displayed in a browser in the form of an Open Provenance Model (OPM) [9] compliant provenance graph.",
        
    ],
))

DB(Citation(
    pham2013a, best2012a, ref="[10]",
    contexts=[
        "To test PTU we took two papers [10, 11] in which authors shared data, tools and software. We constructed meaningful testing scenarios and determined if PTU provides performance improvements.",
        "In the first paper, Best et. al. [10] describes PEEL0, a three step workflow process implemented as an R-program",
        
    ],
))

DB(Citation(
    pham2013a, murphy2013a, ref="[11]",
    contexts=[
        "To test PTU we took two papers [10, 11] in which authors shared data, tools and software. We constructed meaningful testing scenarios and determined if PTU provides performance improvements.",
        "Our second program, TextAnalyzer, is based on the Java-based Unstructured Information Management Architecture (UIMA) and runs a named-entity recognition analysis program using several data dictionaries [11].",
        
    ],
)) 