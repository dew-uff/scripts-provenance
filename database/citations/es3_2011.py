# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2002 import brandes2002a
from ..work.y2005 import bose2005a
from ..work.y2005 import simmhan2005b
from ..work.y2008 import frew2008a
from ..work.y2009 import osterweil2009a
from ..work.y2010 import gil2010a
from ..work.y2010 import moreau2010a
from ..work.y2010 import moreau2010b
from ..work.y2011 import frew2011a

DB(Citation(
    frew2011a, bose2005a, ref="1",
    contexts=[
        "Computational provenance refers to knowledge of the origins and processing history of a computational artifact such as a data product or an implementation of an algorithm [1].",
        "Unlike most other provenance management systems [1,6,9], ES3 captures provenance from running processes, as opposed to extracting or inferring it from static speciﬁcations such as scripts or workﬂows.",
    ],
))

DB(Citation(
    frew2011a, brandes2002a, ref="2",
    contexts=[
        "The graphs are returned serialized in various XML formats (ES3 native, GraphML [2], etc.), which can be rendered by graph visualization clients (e.g., Graphviz6; yEd 7).",

    ],
))

DB(Citation(
    frew2011a, frew2008a, ref="3",
    contexts=[
        "ES3 is a software system for automatically and transparently capturing, managing, and reconstructing the provenance of arbitrary, unmodiﬁed computational sequences [3].",

    ],
))

DB(Citation(
    frew2011a, gil2010a, ref="4",
    contexts=[
        "One of the primary rationales for collecting provenance information is to enable reproducibility of a process [4].",

    ],
))

DB(Citation(
    frew2011a, Site("Guo, P. CDE: Automatically create portable Linux applications", "http://www.stanford.edu/~pgbovine/cde.html"), ref="5",
    contexts=[
        ". CDE [5] uses system call tracing to package the executable code, input data, and Linux environment (system libraries, language interpreters, etc.) necessary to run a process into a single distributable object, runnable on any Linux system.",

    ],
))

DB(Citation(
    frew2011a, moreau2010a, ref="6",
    contexts=[
        "Unlike most other provenance management systems [1,6,9], ES3 captures provenance from running processes, as opposed to extracting or inferring it from static speciﬁcations such as scripts or workﬂows.",
        "While extremely valuableas metadata [6] in its ownright this provenance can also be exploited to help determine an object’s ﬁtness for publication.",
    ],
))

DB(Citation(
    frew2011a, moreau2010b, ref="7",
    contexts=[
        "ES3’s native provenance model is a proper subset of the Open Provenance Model (OPM) [7].",

    ],
))

DB(Citation(
    frew2011a, osterweil2009a, ref="8",
    contexts=[
        "lbsh [8] uses command-line scraping to determine a process’ inputs and outputs, and optionally prepare a (less comprehensive than CDE) package intended to facilitate the process’ re-execution.",
        
    ],
))

DB(Citation(
    frew2011a, simmhan2005b, ref="9",
    contexts=[
        "Unlike most other provenance management systems [1,6,9], ES3 captures provenance from running processes, as opposed to extracting or inferring it from static speciﬁcations such as scripts or workﬂows.",
        
    ],
))
