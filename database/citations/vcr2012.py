# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1999 import golub1999a
from ..work.y2003 import ioannidis2003a
from ..work.y2011 import gavish2011a
from ..work.y2012 import gavish2012a
from ..work.y2013 import gavish2013a
from ..work.y2013 import winawer2013a
from ..work.y2013 import gent2013a
from ..work.y2013 import kay2013a
from ..work.y2014 import howe2014a
from ..work.y2015 import heroux2015a
from ..work.y2015 import stodden2015a
from ..work.y2015 import donoho2015a
from ..work.y2015 import cooper2015a
from ..work.y2015 import hermes2015a
from ..work.y2016 import qin2016a

DB(Citation(
    gavish2012a, golub1999a, ref="1",
    contexts=[
        "list all of the classifiers applied to the famous acute lymphoblastic leukemia dataset,1 along with their type-1 and type-2 error rates;",

    ],
))

DB(Citation(
    gavish2012a, gavish2011a, ref="2",
    contexts=[
        "We recently introduced Verifiable Computation Results (VCR), a disciplined approach for computer-based research, and demonstrated a software implementation (www.verifiable- research.org).2",
        "For example, the practice of VCR improves individual and group productivity and creates a much-needed continuity of knowledge within research groups.2",
        "VCR (www.verifi able-research.org)2 is a disciplined approach, with the overall goal of exposing all relevant information about acomputational result.",
        "For example, in the VCR implementation we provide,2 results are RESTful Web services.",
        
    ],
))

DB(Citation(
    gavish2012a, ioannidis2003a, ref="3",
    contexts=[
        "Strong signals can be obtained only by amalgamating p-values, effect sizes, and even actual measurements from multiple studies into one meta-analysis study.3",

    ],
))

DB(Citation(
    qin2016a, gavish2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gavish2013a, gavish2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    howe2014a, gavish2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    heroux2015a, gavish2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stodden2015a, gavish2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    donoho2015a, gavish2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    cooper2015a, gavish2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    winawer2013a, gavish2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gent2013a, gavish2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kay2013a, gavish2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hermes2015a, gavish2012a, ref="",
    contexts=[

    ],
))
