# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2011 import frew2011a
from ..work.y2012 import janee2012a

DB(Citation(
    janee2012a, frew2011a, ref="",
    contexts=[

    ],
))
