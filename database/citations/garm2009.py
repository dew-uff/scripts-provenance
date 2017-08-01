# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2000 import myers2000a
from ..work.y2001 import buneman2001a
from ..work.y2004 import vachharajani2004a
from ..work.y2005 import newsome2005a
from ..work.y2006 import muniswamy2006a
from ..work.y2006 import zeldovich2006a
from ..work.y2008 import bernstein2008a
from ..work.y2008 import enck2008a
from ..work.y2009 import demsky2009a
from ..work.y2009 import hasan2009a

DB(Citation(
    demsky2009a, bernstein2008a, ref="[1]",
    contexts=[
        "Garm uses the Salsa20 stream cipher as it satisﬁes both requirements [1].",
        
    ],
))

DB(Citation(
    demsky2009a, buneman2001a, ref="[2]",
    contexts=[
        "Researchers have studied the problem of tracking and maintaining provenance in databases [2].",
        
    ],
))

DB(Citation(
    demsky2009a, enck2008a, ref="[3]",
    contexts=[
        "PinUP can enforce policies on how applications use ﬁles at the ﬁle granularity [3].",
        
    ],
))

DB(Citation(
    demsky2009a, hasan2009a, ref="[4]",
    contexts=[
        "Researchers have developed library level tools to produce veriﬁable provenance records for ﬁles [4]",
        
    ],
))

DB(Citation(
    demsky2009a, muniswamy2006a, ref="[5]",
    contexts=[
        "Researchers have developed automated provenance gathering frameworks that operate at the ﬁle granularity [5]",
        
    ],
))

DB(Citation(
    demsky2009a, myers2000a, ref="[6]",
    contexts=[
        "Most current taint frameworks enforce policies at the boundary of the tainting framework [6].",
        
    ],
))

DB(Citation(
    demsky2009a, vachharajani2004a, ref="[7]",
    contexts=[
        "Researchers have developed many taint analyses [8, 7].",
        
    ],
))

DB(Citation(
    demsky2009a, newsome2005a, ref="[8]",
    contexts=[
        "Researchers have developed many taint analyses [8, 7].",
        
    ],
))

DB(Citation(
    demsky2009a, zeldovich2006a, ref="[9]",
    contexts=[
        "The HiStar operating system provides information ﬂow control capabilities [9].",
        
    ],
))