# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2006 import callahan2006b
from ..work.y2006 import altintas2006a
from ..work.y2008 import clark2008a
from ..work.y2009 import muniswamy2009a
from ..work.y2009 import spillane2009a
from ..work.y2010 import angelino2010a
from ..work.y2011 import angelino2011a
from ..work.y2011 import macko2011a
from ..work.y2011 import moreau2011c
from ..work.y2012 import macko2012a
from ..work.y2012 import gehani2012a
from ..work.y2013 import becker2013a
from ..work.y2013 import sweeney2013a
from ..work.y2013 import hensley2013a
from ..work.y2013 import carata2013a
from ..work.y2013 import spinuso2013a
from ..work.y2014 import rossiter2014a
from ..work.y2014 import coe2014a
from ..work.y2014 import coe2014b
from ..work.y2014 import hensley2014a
from ..work.y2014 import carata2014a
from ..work.y2014 import saake2014a
from ..work.y2015 import gammack2015a
from ..work.y2015 import balakrishnan2015a
from ..work.y2015 import fekete2015a
from ..work.y2015 import jenness2015a
from ..work.y2015 import bates2015a
from ..work.y2016 import elsethagen2016a
from ..work.y2016 import bates2016b
from ..work.y2016 import ragan2016a
from ..work.y2016 import bortolameotti2016a
from ..work.y2016 import bates2016a
from ..work.y2016 import moyer2016a
from ..work.y2016 import karsai2016a

DB(Citation(
    macko2012a, 
    DB(Site("4 STORE . ORG . 4store - scalable RDF storage", "http://4store.org/")),
    ref="[1]",
    contexts=[
        "We implemented ODBC and SPARQL/RDF [6] drivers, whichwe tested on MySQL, PostgreSQL, and 4store [1].",
        
    ],
    accessed="2012",
))

DB(Citation(
    macko2012a, altintas2006a, ref="[2]",
    contexts=[
        "For example, PASS [9] and Story Book [10] require users to run a modiﬁed version of the operating system, StarFlow [4] requires the use of Python, Kepler [2], VisTrails [5], and many other workﬂow engines require the use of a particular engine – but users are often reluctant to change their work environment",
        "We have used the CPL in two projects: GraphDB Bench (a part of the Tinkubator [11] project) and Kepler [2].",
        "Kepler [2] is a workﬂow engine that automatically collects provenance into one of several storage backends, such as a SQL database, an OPM ﬁle, or a text ﬁle",
        
    ],
))

DB(Citation(
    macko2012a, angelino2011a, ref="[3]",
    contexts=[
        "Taking these and several other previously identiﬁed lessons [3] into account, we developed the Core ProvenanceLibrary(CPL),whichcanbeintegratedeasilyinto existing scripts and applications.",
        "Even though the manual instrumentation adds extra work, we ﬁnd that such work requires little effort and the resulting system solves several problems that plague other systems [3], such as version disconnect and provenance integration",
        "A critical characteristic of this approach is that applicationscandiscloseprovenancetotheCPLinawaythatis most logical and appropriate for them, eliminating several problems that plague other systems [3].",
        
    ],
))

DB(Citation(
    macko2012a, angelino2010a, ref="[4]",
    contexts=[
        "For example, PASS [9] and Story Book [10] require users to run a modiﬁed version of the operating system, StarFlow [4] requires the use of Python, Kepler [2], VisTrails [5], and many other workﬂow engines require the use of a particular engine – but users are often reluctant to change their work environment",
        "Another problem that frequently arise is the disconnectbetweendifferentnotionsofprovenance: Forexample, StarFlow [4] statically analyzes a Python program to determine its call graph and the ﬁles that it reads and writes, instead of capturing dynamic information at runtime",
        
    ],
))

DB(Citation(
    macko2012a, callahan2006b, ref="[5]",
    contexts=[
        "For example, PASS [9] and Story Book [10] require users to run a modiﬁed version of the operating system, StarFlow [4] requires the use of Python, Kepler [2], VisTrails [5], and many other workﬂow engines require the use of a particular engine – but users are often reluctant to change their work environment",
        
    ],
))

DB(Citation(
    macko2012a, clark2008a, ref="[6]",
    contexts=[
        "We implemented ODBC and SPARQL/RDF [6] drivers, whichwe tested on MySQL, PostgreSQL, and 4store [1].",
        
    ],
))

DB(Citation(
    macko2012a, macko2011a, ref="[7]",
    contexts=[
        "The CPL distribution also includes a command-line tool for issuing simple provenance queries on ﬁles, and it is also integrated with Orbiter [7] for visualization.",
        
    ],
))

DB(Citation(
    macko2012a, moreau2011c, ref="[8]",
    contexts=[
        "The second problem CPL addresses is provenance integration: Cooperating applications can share and reference the GUIDs of their objects, eliminating many uses of the alternate relation from the W3C provenance standard [8].",
        
    ],
))

DB(Citation(
    macko2012a, muniswamy2009a, ref="[9]",
    contexts=[
        "For example, PASS [9] and Story Book [10] require users to run a modiﬁed version of the operating system, StarFlow [4] requires the use of Python, Kepler [2], VisTrails [5], and many other workﬂow engines require the use of a particular engine – but users are often reluctant to change their work environment",
        "The library automatically versions each object using the Cycle Avoidance algorithm [9] to avoid creating cycles in provenance and so that applications can reference older versions of objects as appropriate",
        "SystemssuchasPASS[9]thatcollectprovenancebyobservingsystemcallsfrequentlymissthisconnectionandtreat the old and the new version of the document as different objects,eventhoughtheversionconnectionisobviousto theuser",
        "PASS [9] enables applications to disclose their provenance using the Disclosed Provenance API (DPAPI) and to integrate it with the provenance that it automatically infers from observing system calls",
        
    ],
))

DB(Citation(
    macko2012a, spillane2009a, ref="[10]",
    contexts=[
        "For example, PASS [9] and Story Book [10] require users to run a modiﬁed version of the operating system, StarFlow [4] requires the use of Python, Kepler [2], VisTrails [5], and many other workﬂow engines require the use of a particular engine – but users are often reluctant to change their work environment",
        
    ],
))

DB(Citation(
    macko2012a, 
    DB(Site("Tinkubator wiki", "https://github.com/tinkerpop/tinkubator/wiki")),
    ref="[11]",
    contexts=[
        "We have used the CPL in two projects: GraphDB Bench (a part of the Tinkubator [11] project) and Kepler [2].",
        "GraphDB Bench [11] is a tool for benchmarking graph databases – both to compare different databases to each other and to better understand performance of a single databasesystem.",
        
    ],
    accessed="2012",
))

DB(Citation(
    macko2012a, 
    DB(Site("VisTrails SDK", "http://www.vistrails.com/sdk.html")),
    ref="[12]",
    contexts=[
        "In terms of the scope and the purpose of the project, the CPL is perhaps closest to VisTrails SDK [12], whichallows VisTrails’s OEM partners to embed the VisTrails Provenance Engine within their applications, enabling provenance capture without the need of substantial changes to their products. The SDK is currently under development and thus not publicly available, so we are unfortunately unable to compare it to the CPL.",
        
    ],
    accessed="2012",
))

DB(Citation(
    becker2013a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    rossiter2014a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gammack2015a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sweeney2013a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    elsethagen2016a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bates2016b, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    balakrishnan2015a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    coe2014a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hensley2013a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    fekete2015a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    coe2014b, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    carata2013a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hensley2014a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    spinuso2013a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    jenness2015a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ragan2016a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bates2015a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    carata2014a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gehani2012a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    saake2014a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bortolameotti2016a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bates2016a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    moyer2016a, macko2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    karsai2016a, macko2012a, ref="",
    contexts=[

    ],
))
