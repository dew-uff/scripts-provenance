# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2006 import bowers2006a
from ..work.y2008 import missier2008a
from ..work.y2008 import scheidegger2008a
from ..work.y2010 import osterweil2010a
from ..work.y2010 import silles2010a
from ..work.y2011 import lerner2011a
from ..work.y2012 import runnalls2012a
from ..work.y2014 import lerner2014b
from ..work.y2014 import lerner2014a

DB(Citation(
    lerner2014b, bowers2006a, ref="[BML+06]",
    contexts=[
        "The current state of the art of provenance capture requires scientists to adopt new technologies, most commonly workﬂow systems such as Kepler [BML+06], Vistrails [SKS+08] or Taverna [MBZ+08], among others.",

    ],
))

DB(Citation(
    lerner2014b, lerner2014a, ref="[LB14]",
    contexts=[
        "In this poster, we present two tools aimed at this audience: RDataTracker and DDG Explorer. RDataTracker [LB14] is used to collect data provenance during the execution of an R script.",

    ],
))

DB(Citation(
    lerner2014b, lerner2011a, ref="[LBO+11]",
    contexts=[
        "DDG Explorer has been carefully designed to be language agnostic and also supports the display and querying of provenance graphs created from the execution of Little-JIL processes [OCE+10,LBO+11]. This poster focuses on provenance collected in R.",

    ],
))

DB(Citation(
    lerner2014b, missier2008a, ref="[MBZ+08]",
    contexts=[
        "The current state of the art of provenance capture requires scientists to adopt new technologies, most commonly workﬂow systems such as Kepler [BML+06], Vistrails [SKS+08] or Taverna [MBZ+08], among others.",

    ],
))

DB(Citation(
    lerner2014b, osterweil2010a, ref="[OCE+10]",
    contexts=[
        ". DDG Explorer has been carefully designed to be language agnostic and also supports the display and querying of provenance graphs created from the execution of Little-JIL processes [OCE+10,LBO+11]. This poster focuses on provenance collected in R.",

    ],
))

DB(Citation(
    lerner2014b, runnalls2012a, ref="[RS12]",
    contexts=[
        "This work diﬀers from CXXR [SR10,RS12], an implementation of the R interpreter that includes automated provenance collection.",

    ],
))

DB(Citation(
    lerner2014b, scheidegger2008a, ref="[SKS+08]",
    contexts=[
        "The current state of the art of provenance capture requires scientists to adopt new technologies, most commonly workﬂow systems such as Kepler [BML+06], Vistrails [SKS+08] or Taverna [MBZ+08], among others.",

    ],
))

DB(Citation(
    lerner2014b, silles2010a, ref="[SR10]",
    contexts=[
        "This work diﬀers from CXXR [SR10,RS12], an implementation of the R interpreter that includes automated provenance collection.",

    ],
))
