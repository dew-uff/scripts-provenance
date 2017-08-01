# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2013 import gandrud2013a
from ..work.y2014 import driemeier2014a
from ..work.y2015 import mcphillips2015a
from ..work.y2015 import nascimento2015a
from ..work.y2016 import cruz2016a

DB(Citation(
    cruz2016a, driemeier2014a, ref="1",
    contexts=[
    	"Despite ongoing agricultural model improvements, many are direct descendants of research investments made three–four decades ago, and many of the major advances in data management of the past decade have not been fully exploited [1].",
        "Our approach aims to allow researchers to manage, share, and enact the statistical workﬂows that encapsulate legacy R scripts [1, 2].",
    ],
))

DB(Citation(
    cruz2016a, nascimento2015a, ref="2",
    contexts=[
    	"Our approach aims to allow researchers to manage, share, and enact the statistical workﬂows that encapsulate legacy R scripts [1, 2].",
    ],
))

DB(Citation(
    cruz2016a, gandrud2013a, ref="3",
    contexts=[
    	"In this paper, we present the SisGExp e-Science platform that enriches the management of agronomic experiments supported by RFlow [2] architecture that wraps R scripts.",
        "There are few mechanisms to collect provenance of statistical scripts without changing its source code [3, 4].",
    ],
))

DB(Citation(
    cruz2016a, mcphillips2015a, ref="4",
    contexts=[
    	"There are few mechanisms to collect provenance of statistical scripts without changing its source code [3, 4].",
    ],
))
