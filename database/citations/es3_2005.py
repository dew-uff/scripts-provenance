# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1997 import vahdat1997a
from ..work.y1998 import alexandrov1998a
from ..work.y2001 import frew2001a
from ..work.y2005 import valeur2005a


DB(Citation(
    valeur2005a, 
    DB(Site("Alexandria digital library project", "http://www.alexandria.ucsb.edu/")),
    ref="[1]",
    contexts=[
        "ES3 uses the Alexandria Digital Library Middleware [1] to provide the search capabil-ity. ",
    ],
))

DB(Citation(
    valeur2005a, alexandrov1998a, ref="[2]",
    contexts=[
        "The Ufo [2] and Trans-parent result caching [4] projects shows how system tracing can be applied in application with some of the same properties as ES3.",
    ],
))

DB(Citation(
    valeur2005a, frew2001a, ref="[3]",
    contexts=[
        "ESSW  [3]  is  a  system  designed  to  handle  linage  and  metadata  for  objects  in  scientific workflows. ",
    ],
))

DB(Citation(
    valeur2005a, vahdat1997a, ref="[4]",
    contexts=[
        "The Ufo [2] and Trans-parent result caching [4] projects shows how system tracing can be applied in application with some of the same properties as ES3.",
        "Transparent  result  caching  [4]  traps  system  calls  to  determine  the  dependencies  among input files, development tools and output files by tracing the process system calls.",
    ],
))