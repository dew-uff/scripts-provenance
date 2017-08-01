# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2007 import fonseca2007a
from ..work.y2007 import zhang2007a
from ..work.y2008 import callahan2008a
from ..work.y2008 import callahan2008a
from ..work.y2010 import guo2010a
from ..work.y2011 import zhu2011a
from ..work.y2012 import tariq2012a
from ..work.y2012 import freire2012a
from ..work.y2012 import gehani2012a
from ..work.y2013 import chacko2013a
from ..work.y2013 import moore2013a
from ..work.y2013 import ghoshal2013a
from ..work.y2013 import lee2013a
from ..work.y2014 import saake2014a
from ..work.y2015 import sarikhani2015a
from ..work.y2015 import oliveira2015a
from ..work.y2016 import zawoad2016a
from ..work.y2016 import ji2016a
from ..work.y2016 import pimentel2016e
from ..work.y2016 import stamatogiannakis2016a


DB(Citation(
    tariq2012a, callahan2008a, ref="[1]",
    contexts=[
        "Related research has been performed in a wide variety of domains under the rubrics of data ﬂow analysis, dynamic slicing, data provenance, database lineage, ﬁlesystem lineage, and taint analysis. Some have focused on speciﬁc languages or paradigms, such as Python[3], network operations [2], or graphical interfaces [1],",
    ],
))

DB(Citation(
    tariq2012a, fonseca2007a, ref="[2]",
    contexts=[
        "Related research has been performed in a wide variety of domains under the rubrics of data ﬂow analysis, dynamic slicing, data provenance, database lineage, ﬁlesystem lineage, and taint analysis. Some have focused on speciﬁc languages or paradigms, such as Python[3], network operations [2], or graphical interfaces [1],",
    ],
))

DB(Citation(
    tariq2012a, guo2010a, ref="[3]",
    contexts=[
        "Related research has been performed in a wide variety of domains under the rubrics of data ﬂow analysis, dynamic slicing, data provenance, database lineage, ﬁlesystem lineage, and taint analysis. Some have focused on speciﬁc languages or paradigms, such as Python[3], network operations [2], or graphical interfaces [1],",
    ],
))

DB(Citation(
    tariq2012a,
    Site("LLVM", "http://llvm.org/"),
    ref="[4]",
    contexts=[
        "Our approach for adding provenance instrumentation to a target application is to insert it during compilation. To achieve this, we use the LLVM [4] framework, which was developed to investigate dynamic compilation techniques.",
    ],
))

DB(Citation(
    tariq2012a,
    Site("Open Provenance Model", "http://www.openprovenance.org/"),
    ref="[5]",
    contexts=[
        "To imbue the output with Open Provenance Model (OPM)[5] semantics, we represent a function as an OPM Process and the arguments and return values as OPMArtifacts.",
    ],
))

DB(Citation(
    tariq2012a,
    Site("Support for Provenance Auditing in Distributed Environments", "http://spade.csl.sri.com/"),
    ref="[6]",
    contexts=[
        "SPADE[6] is a modular provenance management infrastructure. Its provenance kernel is agnostic to the domain from which provenance is collected",
        "A user can download SPADE [6], edit the LLVM PATH variable in the Makefile, and invoke make llvm TARGET=<program> to compile and instrument <program>.",
    ],
))

DB(Citation(
    tariq2012a,
    Site("tinyhttpd", "http://sourceforge.net/projects/tinyhttpd/"),
    ref="[7]",
    contexts=[
        "To evaluate our approach, we used tinyhttpd [7] as a target application.",
    ],
))

DB(Citation(
    tariq2012a, zhang2007a, ref="[8]",
    contexts=[
        "Others have tracked dependencies at the X86 binary level, for database lineage [8] and malware tainting [9], for example",
    ],
))

DB(Citation(
    tariq2012a, zhu2011a, ref="[9]",
    contexts=[
        "Others have tracked dependencies at the X86 binary level, for database lineage [8] and malware tainting [9], for example",
    ],
))

DB(Citation(
    zawoad2016a, tariq2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sarikhani2015a, tariq2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    chacko2013a, tariq2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ji2016a, tariq2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    pimentel2016e, tariq2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stamatogiannakis2016a, tariq2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    moore2013a, tariq2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    oliveira2015a, tariq2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ghoshal2013a, tariq2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lee2013a, tariq2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    freire2012a, tariq2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gehani2012a, tariq2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    saake2014a, tariq2012a, ref="",
    contexts=[

    ],
))
