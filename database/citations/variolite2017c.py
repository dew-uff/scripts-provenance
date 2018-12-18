# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2017 import kery2017c

from ..work.y2017 import kery2017a

DB(Citation(
    kery2017c, kery2017a, ref="",
    contexts=[

    ],
))
