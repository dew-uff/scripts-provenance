# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1988 import becker1988a
from ..work.y2010 import runnalls2010a
from ..work.y2010 import silles2010a
from ..work.y2012 import runnalls2012a


DB(Citation(
    runnalls2012a, runnalls2010a, ref="[1]",
    contexts=[
        "CXXR achieves ahigh degree of compatibility with R packages from the CRAN repository, as [1]illustrated.",
        
    ],
))


DB(Citation(
    runnalls2012a, becker1988a, ref="[2]",
    contexts=[
        "The AUDIT facilities [2] that once formed part of S and S-plus were an invaluablefeature, as one of the present authors can testify, and one motivation behindCXXR was to introduce similar but better facilities into the R interpreter. Earlywork on a provenance-enabled variant of CXXR was presented in [3].",
        
    ],
))

DB(Citation(
    runnalls2012a, silles2010a, ref="[3]",
    contexts=[
        "The AUDIT facilities [2] that once formed part of S and S-plus were an invaluablefeature, as one of the present authors can testify, and one motivation behindCXXR was to introduce similar but better facilities into the R interpreter. Earlywork on a provenance-enabled variant of CXXR was presented in [3].",
        
    ],
))
