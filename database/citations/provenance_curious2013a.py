# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1987 import ferrante1987a
from ..work.y1992 import horwitz1992a
from ..work.y2003 import newman2003a
from ..work.y2007 import buneman2007a
from ..work.y2007 import shields2007a
from ..work.y2011 import huq2011a
from ..work.y2011 import wada2011a
from ..work.y2012 import huq2012a
from ..work.y2012 import freire2012a
from ..work.y2013 import huq2013a
from ..work.y2016 import schulz2016a
from ..work.y2016 import pimentel2016e


DB(Citation(
    huq2013a, buneman2007a, ref="[1]",
    contexts=[
        "Data provenance refers to the derivation history of data starting from its input sources [1].",
    ],
))

DB(Citation(
    huq2013a, ferrante1987a, ref="[2]",
    contexts=[
        "A program dependence graph (PDG) makes explicit both the data and control dependences for each statement in a program [2].",
    ],
))

DB(Citation(
    huq2013a, horwitz1992a, ref="[3]",
    contexts=[
        "A system dependence graph (SDG) extends the deﬁnition of program dependence graph and it is capable of providing data and control dependences for multi-procedure programs [3].",
    ],
))

DB(Citation(
    huq2013a, huq2012a, ref="[4]",
    contexts=[
        "Having this input from users, the inference engine applies appropriate provenance inference algorithm [5], [4] to formulate the provenance queries.",
    ],
))

DB(Citation(
    huq2013a, huq2011a, ref="[5]",
    contexts=[
        "Having this input from users, the inference engine applies appropriate provenance inference algorithm [5], [4] to formulate the provenance queries.",
        "Therefore, in this case, we apply the basic algorithm described in [5].",
    ],
))

DB(Citation(
    huq2013a, newman2003a, ref="[6]",
    contexts=[
        "Data intensive applications are used to study and better understand complex systems such as physical, geographical, environmental, biological etc. [6].",
    ],
))

DB(Citation(
    huq2013a, shields2007a, ref="[7]",
    contexts=[
        "Execution of a control-ﬂow based operation depends on the successful completion of previous operations [7]",
    ],
))

DB(Citation(
    huq2013a, wada2011a, ref="[8]",
    contexts=[
        "The proposed tool is demonstrated using a hydrological model estimating the global water demand [8].",
        "Suppose, for the model that estimates the global water demand [8], the value is characterized by it’s timestamp (e.g. yyyy-mm) and cell position in 2-d co-ordinates.",
        "The model reported in [8] contains only in-situ and static data.",
        "To evaluate the proposed tool, a scientiﬁc data processing model in hydrological domain reported in [23] is introduced",
        "We consider the model estimating global water demand reported in [8] as our demonstration scenario.",
    ],
))

DB(Citation(
    schulz2016a, huq2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    pimentel2016e, huq2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    freire2012a, huq2013a, ref="",
    contexts=[

    ],
))
