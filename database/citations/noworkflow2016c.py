# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import pimentel2016c

from ..work.y2016 import pimentel2016c
from ..work.y2017 import samuel2017a

DB(Citation(
    pimentel2016c, pimentel2016c, ref="",
    contexts=[

    ],
))

DB(Citation(
    samuel2017a, pimentel2016c, ref="",
    contexts=[

    ],
))
