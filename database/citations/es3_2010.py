# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2003 import kunze2003a
from ..work.y2005 import bose2005a
from ..work.y2005 import maritorena2005a
from ..work.y2008 import frew2008a
from ..work.y2008 import kunde2008a
from ..work.y2008 import moore2008a
from ..work.y2009 import abrams2009a
from ..work.y2009 import gretarsson2009a
from ..work.y2010 import frew2010a
from ..work.y2011 import plalea2011a
from ..work.y2011 import cruz2011a
from ..work.y2011 import belhajjame2011a
from ..work.y2013 import liu2013a
from ..work.y2013 import aktas2013a
from ..work.y2014 import lagoze2014a
from ..work.y2014 import eltabakh2014a

DB(Citation(
    frew2010a, abrams2009a, ref="[1]",
    contexts=[
        "Microservices [1, 8] are an architectural pattern, originally developed in the digital curation community, in which a system’s functionality is devolved into small, self-contained, interoperable services.",
    ],
))

DB(Citation(
    frew2010a, bose2005a, ref="[2]",
    contexts=[
        "ESDRs represent a blurring of the historic distinction between data creators and data providers [2]",

    ],
))

DB(Citation(
    frew2010a, frew2008a, ref="[3]",
    contexts=[
        "The ES3 system [3] collects provenance information from executing code, using a combination of system call tracing, transparent wrapping, and application environment instrumentation.",

    ],
))

DB(Citation(
    frew2010a, gretarsson2009a, ref="[4]",
    contexts=[
        "We are therefore exploring connecting the ES3 database to a generic web-based graph browsing system [4].",

    ],
))

DB(Citation(
    frew2010a, kunde2008a, ref="[5]",
    contexts=[
        "ES3 currently provides post-processors that convert the ES3 native provenance graph format to GraphML9 or DOT10, for visualizing in tools such as yEd11 or Graphviz12. However, we realize that diﬀerent kinds of queries or user communities may require alternative provenance renderings [5].",

    ],
))

DB(Citation(
    frew2010a, kunze2003a, ref="[6]",
    contexts=[
        "We are developing an approach to version-aware identity management that satisﬁes these requirements and that is built on two technologies: well-known persistent identiﬁer schemes such as Archival Resource Keys (ARKs) [6], and HTTP redirection.",

    ],
))

DB(Citation(
    frew2010a, maritorena2005a, ref="[7]",
    contexts=[
        "Many of the products are derived by merging data from multiple satellite sensor systems [7].",

    ],
))

DB(Citation(
    frew2010a, moore2008a, ref="[8]",
    contexts=[
        "Microservices [1, 8] are an architectural pattern, originally developed in the digital curation community, in which a system’s functionality is devolved into small, self-contained, interoperable services.",

    ],
))

DB(Citation(
    plalea2011a, frew2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lagoze2014a, frew2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    liu2013a, frew2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    eltabakh2014a, frew2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    cruz2011a, frew2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    aktas2013a, frew2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    belhajjame2011a, frew2010a, ref="",
    contexts=[

    ],
))
