# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1988 import becker1988a
from ..work.y1988 import becker1988b
from ..work.y2010 import silles2010a
from ..work.y2011 import runnalls2011a
from ..work.y2012 import talbot2012a

DB(Citation(
    runnalls2011a, becker1988a, ref="[Becker and Chambers (1988)]",
    contexts=[
        "Interestingly one of the ﬁrst provenance-aware applications was S, and [Becker and Chambers (1988)]isoftencitedasapioneerpaper",

    ],
))


DB(Citation(
    runnalls2011a, becker1988b, ref="[Becker, Chambers and Wilks (1988)]",
    contexts=[
        "This audit file could then be analysed using a separate tool, S AUDIT, described in [Becker, Chambers and Wilks (1988)]",

    ],
))


DB(Citation(
    runnalls2011a, Site("Boost C++ Libraries", "http://www.boost.org"), ref="[Boost (2011)]",
    contexts=[
        "At the centre is the CXXR core, which is written as far as possible in idiomatic C++, making free use of the C++ standard library, and some use of the Boost libraries of peer-reviewed, portable C++ [Boost (2011)].",

    ],
))

DB(Citation(
    runnalls2011a, Site("The GNU Multiple Precision Arithmetic Library", "http://gmplib.org"), ref="[GNU MP (2011)]",
    contexts=[
        "The developer is aware that there is a free GNU library, the GNU MP library [GNU MP (2011)] that provides ‘bigint’s, as they are called, for C and C++, and would like to build on that.",

    ],
))

DB(Citation(
    runnalls2011a, Site("Antoine Lucas, Immanuel Scholz, Rainer Boehme and Sylvain Jesson. R BigIntegers", "http://mulcyber.toulouse.inra.fr/projects/gmp, http://cran.r-project.org."), ref="[Lucas et al. (2010)]",
    contexts=[
        "Some readers will be aware that there already is such an R package, the gmp package [Lucas et al. (2010)],whichoffersbigintsandmuchelsebesides.",

    ],
))

DB(Citation(
    runnalls2011a, Site("Andrew R. Runnalls", "http://user2010.org/Slides/Runnalls.pdf"), ref="[Runnalls (2010)]",
    contexts=[
        "A paper [Runnalls (2010)] at the useR!2010 conference explored the extent to which this had been achieved by testing CXXR with 50 key packages (other than the base and ‘recommended’ packages,whichareroutinelymaintainedaspartofCXXRdevelopment)fromthecentralR archive CRAN, namely the packages on which most other packages in the archive depend.",

    ],
))

DB(Citation(
    runnalls2011a, silles2010a, ref="[Silles and Runnalls (2010)]",
    contexts=[
        "A preliminary report on this was given in [Silles and Runnalls (2010)].",

    ],
))

DB(Citation(
    talbot2012a, runnalls2011a, ref="",
    contexts=[

    ],
))
