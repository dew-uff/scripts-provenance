# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2010 import stodden2010a
from ..work.y2011 import guo2011a
from ..work.y2011 import guo2011c
from ..work.y2012 import guo2012b

DB(Citation(
    guo2012b, stodden2010a, ref="[1]",
    contexts=[
        "Although there are many social, cultural,and political barriers that hinderreproducible computational science research,1 one technical barrier to reproducibilityis that it’s hard to distribute scientificcode in a form that other researchers can easilyexecute on their own computers",
        
    ],
))

DB(Citation(
    guo2012b, guo2011c, ref="[2]",
    contexts=[
        "Other articles2,3 provide detailson the design, implementation, and formal evaluationof CDE.",
        "In my experiments, slowdownsranged from negligible to 30 percent.2",
        
    ],
))

DB(Citation(
    guo2012b, guo2011a, ref="[3]",
    contexts=[
        "Other articles2,3 provide detailson the design, implementation, and formal evaluationof CDE.",
        
    ],
))