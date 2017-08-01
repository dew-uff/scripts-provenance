# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1999 import olson1999a
from ..work.y1999 import zadok1999a
from ..work.y2004 import kashyap2004a
from ..work.y2006 import braun2006b
from ..work.y2006 import muniswamy2006a
from ..work.y2008 import moreau2008b
from ..work.y2008 import clifford2008a
from ..work.y2008 import frew2008a
from ..work.y2008 import krenek2008a
from ..work.y2008 import zhao2008a
from ..work.y2008 import holland2008b

DB(Citation(
    holland2008b, braun2006b, ref="[1]",
    contexts=[
        "Handling provenance directly in the storage system offers certain advantages beyond transparency, most notably consistency: the provenance cannot be lost or separated from the data it describes. It also allows automatic collection[1].",
        
    ],
))
    
DB(Citation(
    holland2008b, muniswamy2006a, ref="[2]",
    contexts=[
        "Our ﬁrst prototype PASS[2], developed in 2005, was intended as a vehicle to allow us to explore automatic provenance collection and the uses of provenance at the system level.",
        "(Inreality,theprecisedetailsofversioncreationare much more subtle[2].)",
        
    ],
))


DB(Citation(
    holland2008b, olson1999a, ref="[3]",
    contexts=[
        "This prototype consists of a Linux 2.4.29 kernel modiﬁed for automatic collection, a kernel-level port of Berkeley DB [3,4] for indexing, and a stackable [5] ﬁle system layer called PASTA.",
        "Representation technology: We included an in-kernel port of Berkeley DB[3]and used a set of ﬁve Berkeley DB databases (tables in relational parlance) to store all provenance data and indexes.",
        
    ],
))

DB(Citation(
    holland2008b, kashyap2004a, ref="[4]",
    contexts=[
        "This prototype consists of a Linux 2.4.29 kernel modiﬁed for automatic collection, a kernel-level port of Berkeley DB [3,4] for indexing, and a stackable [5] ﬁle system layer called PASTA.",
        
    ],
))

DB(Citation(
    holland2008b, zadok1999a, ref="[5]",
    contexts=[
        "This prototype consists of a Linux 2.4.29 kernel modiﬁed for automatic collection, a kernel-level port of Berkeley DB [3,4] for indexing, and a stackable [5] ﬁle system layer called PASTA.",
        
    ],
))

DB(Citation(
    holland2008b, moreau2008b, ref="[6]",
    contexts=[
        "In the remainder of this paper, we ﬁrst discuss the PASS approach in terms of the categories presented in the introduction to this issue[6];",
        
    ],
))

DB(Citation(
    holland2008b, krenek2008a, ref="[7]",
    contexts=[
        "PASS is quite different from most of the other challenge systems, such as job provenance (JP)[7], the virtual data grid (VDL)[8], and Taverna[9], which embed provenance collection in workﬂow engines",
        
    ],
))

DB(Citation(
    holland2008b, clifford2008a, ref="[8]",
    contexts=[
        "PASS is quite different from most of the other challenge systems, such as job provenance (JP)[7], the virtual data grid (VDL)[8], and Taverna[9], which embed provenance collection in workﬂow engines",
        
    ],
))

DB(Citation(
    holland2008b, zhao2008a, ref="[9]",
    contexts=[
        "PASS is quite different from most of the other challenge systems, such as job provenance (JP)[7], the virtual data grid (VDL)[8], and Taverna[9], which embed provenance collection in workﬂow engines",
        
    ],
))


DB(Citation(
    holland2008b, frew2008a, ref="[10]",
    contexts=[
        "It is most similar to ES3[10], which uses passive tracing (e.g. strace) to collect provenance from unmodiﬁed applications.",
        
    ],
))
