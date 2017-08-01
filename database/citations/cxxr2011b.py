# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1988 import becker1988a
from ..work.y1990 import detreville1990a
from ..work.y1996 import meyers1996a
from ..work.y1998 import meyers1998a
from ..work.y2006 import becker2006a
from ..work.y2009 import lang2009a
from ..work.y2010 import samperi2010a
from ..work.y2011 import runnalls2011b
from ..work.y2011 import eddelbuettel2011a
from ..work.y2013 import runnalls2013a
from ..work.y2013 import eddelbuettel2013a
from ..work.y2016 import michielon2016a

DB(Citation(
    runnalls2011b, becker1988a, ref="(Becker et al. 1988)",
    contexts=[
        "An important motivation for the project was to provide a basis for introducing provenance tracking into R, so that for any R data object, an R user can determine exactlywhichprimarydatasourcesitisbasedon,andexactlywhichsequenceofoperations was used to produce it from the primary data, thus emulating and extending the AUDIT facility of S (Becker et al. 1988).1",

    ],
))

DB(Citation(
    runnalls2011b, becker2006a, ref="(Becker 2006)",
    contexts=[
        "At the centre is the CXXRcore, which contains functionality that has been fully refactored into C++, following as far as possible the programming idioms of that language, and making free use of the C++ standard library, including someuseoftheTR1libraryextensions(Becker2006)",

    ],
))

DB(Citation(
    runnalls2011b, detreville1990a, ref="(DeTreville 1990)",
    contexts=[
        "The third of these approaches, which is comparable to that in (DeTreville 1990), has moved onto the development trunk as from release 0.21-2.8.1 of CXXR.",

    ],
))

DB(Citation(
    runnalls2011b, Site("Dimitri van Heesch. Doxygen", "http://www.doxygen.org"), ref="(van Heesch 1997)",
    contexts=[
        "Theinterfacestothecorearedeﬁnedbyheader ﬁlesin src/include/CXXR andhavebeencarefullydocumentedusingtheDoxygen documentation tool (van Heesch 1997)",
        "This means that the onlypossiblewayofcreatingsuchanobjectisdynamicallocationusingthenewoperation (cf. Meyers 1996, Item 27).",
        
    ],
))

DB(Citation(
    runnalls2011b, meyers1996a, ref="(Meyers 1996)",
    contexts=[
        "When one GCNodeneedstorefertoanother,itdoessonotwithanordinarypointer but with a ‘smart pointer’ (cf. Meyers 1996, Item 28) from the GCEdge<T> class template;suchapointerautomaticallyadjuststhereferencecountofthenodereferred to.",

    ],
))

DB(Citation(
    runnalls2011b, meyers1998a, ref="(Meyers 1998)",
    contexts=[
        "Requests for smallerblocksareservicedfrompoolsofpreallocatedcellscarvedoutof‘superblocks’ of about 4 kB (cf. Meyers 1998, Item 10).",

    ],
))

DB(Citation(
    runnalls2011b, Site("R Development Core Team (2009a) R Internals. ISBN 3-900051-14-3.", "http://www.r-project.org"), ref="(RCore2009a)",
    contexts=[
        "This paper will refer to the standard R interpreter as CR, and will assume some familiarity with the internals and interfaces of the standard interpreter,asdocumentedin‘RInternals’(RCore2009a)and‘WritingRExtensions’ (R Core 2009b).",

    ],
))

DB(Citation(
    runnalls2011b, Site("R Development Core Team (2009b) Writing R Extensions. ISBN 3-900051-11-9.", "http://www.r-project.org"), ref="(RCore2009b)",
    contexts=[
        "This paper will refer to the standard R interpreter as CR, and will assume some familiarity with the internals and interfaces of the standard interpreter,asdocumentedin‘RInternals’(RCore2009a)and‘WritingRExtensions’ (R Core 2009b).",

    ],
))

DB(Citation(
    runnalls2011b, Site("Duncan Temple Lang (2001) User-Defined Tables in the R Search Path", "http://www.omegahat.org/RObjectTables/RObjectTables.pdf"), ref="(Temple Lang 2001)",
    contexts=[
        "Similarly,functionalitysimilartoR’sRObjectTables package (Temple Lang 2001) is readily obtainable",

    ],
))

DB(Citation(
    runnalls2011b, lang2009a, ref="(Temple Lang 2009)",
    contexts=[
        "Although CXXRwasinitiatedindependentlyoftheproposalsin(TempleLang2009),itreﬂects very similar aspirations.",

    ],
))

DB(Citation(
    runnalls2011b, Site("Simon Urbanek. R Benchmarks", "http://r.research.att.com/benchmarks"), ref="(Urbanek 2008)",
    contexts=[
        "If we consider Jan de Leeuw’s benchmark bench.R (Urbanek 2008), then CR andCXXRareaboutthesamespeed.Butsincemostoftheworkin bench.R isdone in C functions that are essentially unchanged in CXXR, that is unsurprising.",

    ],
))

DB(Citation(
    runnalls2011b, Site("Valgrind Developers. Cachegrind: a Cache and Branch-Prediction Pro?ler", "http://valgrind.org/docs/manual/cg-manual.html"), ref="(Valgrind Developers 2009)",
    contexts=[
        "The table was obtained using cachegrind (Valgrind Developers 2009) running kaltime10.R but with just 100 000 iterations.",

    ],
))

DB(Citation(
    michielon2016a, runnalls2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    samperi2010a, runnalls2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    runnalls2013a, runnalls2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    eddelbuettel2013a, runnalls2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    eddelbuettel2011a, runnalls2011b, ref="",
    contexts=[

    ],
))
