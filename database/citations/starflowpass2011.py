# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2004 import bose2004a
from ..work.y2006 import callahan2006b
from ..work.y2006 import muniswamy2006a
from ..work.y2006 import simmhan2006a
from ..work.y2007 import gil2007b, taylor2007b
from ..work.y2008 import kuehn2008a
from ..work.y2009 import muniswamy2009a
from ..work.y2009 import mcphillips2009a
from ..work.y2009 import moreau2009a
from ..work.y2010 import koop2010a
from ..work.y2010 import angelino2010a
from ..work.y2010 import braun2010a
from ..work.y2010 import gil2010a
from ..work.y2010 import ikeda2010a
from ..work.y2011 import angelino2011a
from ..work.y2012 import boyd2012a
from ..work.y2012 import nguyen2012a
from ..work.y2014 import gehani2014a


DB(Citation(
    angelino2011a, angelino2010a, ref="[1]",
    contexts=[
        "StarFlow [1] is a provenance-enabled Python environment for data analysis. It uses a combination of annotations, static analysis, and dynamic analysis to createdata and control ﬂow dependency graphs.",
        
    ],
))

DB(Citation(
    angelino2011a, bose2004a, ref="[2]",
    contexts=[
        "Datasystemsincreasinglycollectanduseprovenance[4, 7, 9, 10, 12, 15, 2, 14].",
        
    ],
)) 

DB(Citation(
    angelino2011a, braun2010a, ref="[3]",
    contexts=[
        "Interoperability between systems requires the ability to exchange, parse and interpret provenance [3].",
        
    ],
))

DB(Citation(
    angelino2011a, callahan2006b, ref="[4]",
    contexts=[
        "Datasystemsincreasinglycollectanduseprovenance[4, 7, 9, 10, 12, 15, 2, 14].",
        "For example, VisTrails tracks versions of workﬂows [4], and some of the vocabularies introduced by the W3C Provenance Incubator Group include the notion of version [6].",
        
    ],
))

DB(Citation(
    angelino2011a, gil2007b, ref="[5]",
    contexts=[
        "Some workﬂow systems distinguish between workﬂowabstractionsortemplatesandconcreteworkﬂowinstances [5, 8], and in doing so deal with an example of this problem.",
        
    ],
))

DB(Citation(
    angelino2011a, gil2010a, ref="[6]",
    contexts=[
        "For example, VisTrails tracks versions of workﬂows [4], and some of the vocabularies introduced by the W3C Provenance Incubator Group include the notion of version [6].",
        
    ],
)) 


DB(Citation(
    angelino2011a, ikeda2010a, ref="[7]",
    contexts=[
        "Datasystemsincreasinglycollectanduseprovenance[4, 7, 9, 10, 12, 15, 2, 14].",
        
    ],
))

DB(Citation(
    angelino2011a, koop2010a, ref="[8]",
    contexts=[
        "Some workﬂow systems distinguish between workﬂowabstractionsortemplatesandconcreteworkﬂowinstances [5, 8], and in doing so deal with an example of this problem.",
        
    ],
))

DB(Citation(
    angelino2011a, kuehn2008a, ref="[9]",
    contexts=[
        "Datasystemsincreasinglycollectanduseprovenance[4, 7, 9, 10, 12, 15, 2, 14].",
        
    ],
))

DB(Citation(
    angelino2011a, mcphillips2009a, ref="[10]",
    contexts=[
        "Datasystemsincreasinglycollectanduseprovenance[4, 7, 9, 10, 12, 15, 2, 14].",
        
    ],
))

DB(Citation(
    angelino2011a, moreau2009a, ref="[11]",
    contexts=[
        "The Open Provenance Model (OPM) is a solidbasisforthisnextgenerationeffort[11],butitisnot sufﬁcient",
        "Even though there has been substantial effort to standardize provenance representation[11],therehasbeenlittleactualintegrationofprovenance systems.",
        
    ],
))

DB(Citation(
    angelino2011a, muniswamy2009a, ref="[12]",
    contexts=[
        "Datasystemsincreasinglycollectanduseprovenance[4, 7, 9, 10, 12, 15, 2, 14].",
        "We cast the following discussion in the context of the StarFlow and PASS systems, because we are familiar with them, and, to the best of our knowledge, PASS is theonlysystemthatexplicitlyaddressesintegration[12].",
        "PASS intercepts system calls, extracts provenance relationships between ﬁles and processes, and then records this provenance ﬁrst to a log and then ultimately into a set of indexed databases. The PASS architecture is described in detail in earlier work [12].",
        "ThesecondPASSprototype[12]embodiesthisnotion in its Disclosed Provenance API (DPAPI), which makes itpossibletostackprovenancesystemsatoponeanother, map entities at the different layers to each other, and transmit provenance through the multiple systems.",
        
    ],
))

DB(Citation(
    angelino2011a, muniswamy2006a, ref="[13]",
    contexts=[
        "The Provenance-Aware Storage System (PASS) [13] takes an approach quite different from StarFlow. PASS collects and manages provenance at the operating system level, in terms of the operating system’s processes and ﬁle system objects.",
        "We ﬁnd versions essential for representing both objects (OPM artifacts) and processes [13].",
        
    ],
))

DB(Citation(
    angelino2011a, simmhan2006a, ref="[14]",
    contexts=[
        "Datasystemsincreasinglycollectanduseprovenance[4, 7, 9, 10, 12, 15, 2, 14].",
        
    ],
))  

DB(Citation(
    angelino2011a, taylor2007b, ref="[15]",
    contexts=[
        "Datasystemsincreasinglycollectanduseprovenance[4, 7, 9, 10, 12, 15, 2, 14].",
        
    ],
))

DB(Citation(
    gehani2014a, angelino2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    boyd2012a, angelino2011a, ref="",
    contexts=[

    ],
))

DB(Citation(
    nguyen2012a, angelino2011a, ref="",
    contexts=[

    ],
))
