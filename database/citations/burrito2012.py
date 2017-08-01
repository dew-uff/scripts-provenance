# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2006 import muniswamy2006a
from ..work.y2006 import konish2006a
from ..work.y2007 import maclean2007a
from ..work.y2008 import freire2008a
from ..work.y2011 import macko2011a
from ..work.y2011 import prabhu2011a
from ..work.y2012 import guo2012a


DB(Citation(
    guo2012a, freire2008a, ref="[1]",
    contexts=[
    	"Related work such as scientiﬁc workﬂow systems (e.g., Kepler, Taverna, VisTrails) provide similar provenance collection and annotation features for researchers who work exclusively within those environments [1].",
    ],
))

DB(Citation(
    guo2012a, konish2006a, ref="[2]",
    contexts=[
        "The NILFS versioning ﬁlesystem [2] automatically preserves all old versions of her source code and data files, so that she no longer needs to use version control or embed metadata within ﬁlenames.",
    ],
))

DB(Citation(
    guo2012a, macko2011a, ref="[3]",
    contexts=[
        "We have built four applications atop the BURRITO platform. These applications provide innovative ways of interactingwithprovenancebeyondsimplyexploringatraditional interactive graph-based visualization [3].",
    ],
))


DB(Citation(
    guo2012a, maclean2007a, ref="[4]",
    contexts=[
    	"all struggle with the same problems in their experimental workﬂow [4, 6]: - test hypothesis ... - consult myriad of resources ... - maintain up-to-date notes",
        
    ],
))

DB(Citation(
    guo2012a, muniswamy2006a, ref="[5]",
    contexts=[
    	"An OS-level provenance collection daemon capturesexecutioncontext,suchaswhichprocessesread from and wrote to which ﬁles, and builds up a provenance graph similar to PASS [5]",
    ],
))

DB(Citation(
    guo2012a, prabhu2011a, ref="[6]",
    contexts=[
    	"all struggle with the same problems in their experimental workﬂow [4, 6]: - test hypothesis ... - consult myriad of resources ... - maintain up-to-date notes",
    	"Researchers often work in a heterogeneous environment where they cobble together a patch work of ad-hoc scripts written in multiple languages, interfacing with a mix of 3rd-party libraries and executables from disparate sources within a command-line environment [6].",
    ],
))