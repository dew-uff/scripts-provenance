# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2006 import zhao2006a
from ..work.y2008 import clifford2008a


DB(Citation(
    clifford2008a, zhao2006a, ref="3",
    contexts=[
    	"This integration of three types of provenance data— program structure, runtime logs, and annotation—into a uniﬁed relational schema [3] enables powerful discovery and analysis operations",
        "Provenance queries of this form combine what we call prospective provenance–the speciﬁcation of the workﬂows procedure calls and data dependencies—and retrospective provenance information—the recordings of when and where each procedure ran, and how each invocation behaved [3]",
    ],
))

