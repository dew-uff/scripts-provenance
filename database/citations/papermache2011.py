# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1996 import loosemore1996a
from ..work.y1999 import walters1999a
from ..work.y2003 import barham2003a
from ..work.y2003 import figueiredo2003a
from ..work.y2007 import ranger2007a
from ..work.y2008 import watson2008a
from ..work.y2010 import matthews2010a
from ..work.y2011 import brammer2011a


DB(Citation(
    brammer2011a, 
    DB(Site("Easy chair conference system", "http://www.easychair.org",
            authors="A. Voronkov")),
    ref="[1]",
    contexts=[
        "Withinthecomputersciencecommunity,EasyChair[1] is by far the most popular conference management system, due to its ease-of-use and being free. In 2010, there were 3,306 computer science conferences managed using EasyChair [1].",
        
    ],
    accessed="March 2011",
))

DB(Citation(
    brammer2011a, 
    DB(Site("START v2", "http://www.softconf.com/about/")),
    ref="[2]",
    contexts=[
        "Popular commercial options include START [2] andLinklings[3],thelatterwhichisusedbycomputingconferencessuchasSuperComputing(SC)andGraceHopper Celebration of Women in Computing (GHC).",
        
    ],
    accessed="March 2011",
))

DB(Citation(
    brammer2011a, 
    DB(Site("Linklings", "http://www.linklings.com/")),
    ref="[3]",
    contexts=[
        "Popular commercial options include START [2] andLinklings[3],thelatterwhichisusedbycomputingconferencessuchasSuperComputing(SC)andGraceHopper Celebration of Women in Computing (GHC).",
        
    ],
    accessed="March 2011",
))

DB(Citation(
    brammer2011a, 
    DB(Site("ScholarOne manuscripts", "http://scholarone.com/products/",
            authors="T. Reuters")),
    ref="[4]",
    contexts=[
        "Professional organizations for computing such as ACM and IEEE use ScholarOne Manuscripts [4] (formerly Manuscript Central) as their abstract management software",
        
    ],
    accessed="March 2011",
))

DB(Citation(
    brammer2011a, 
    DB(Site("Citeulike: Everyone's library", "http://www.citeulike.org/",
            authors="Springer")),
    ref="[5]",
    contexts=[
        "Web-based systems like CiteULike [5] promote reader interaction within the scientiﬁc community through “social bookmarking”",
        
    ],
    accessed="March 2011",
))

DB(Citation(
    brammer2011a, figueiredo2003a, ref="[6]",
    contexts=[
        "ThenoveltyofPaperMˆach´eistheuseofvirtualmachines(VMs)[6]toimplementanexecutablepaperthatallows authors, reviewers, and readers to interact.",
        
    ],
))

DB(Citation(
    brammer2011a, walters1999a, ref="[7]",
    contexts=[
        "InadditiontocommercialvirtualmachinesoftwaresuchasVMware[7]and Parallels [8], fully-functioning open source alternatives such as VirtualBox [9] and Xen [10] are available",
        
    ],
))

DB(Citation(
    brammer2011a, 
    DB(Site("Virtualization and automation solutions for desktops, servers, hosting, saas - parallels optimized computing", "http://www.parallels.com/",
            authors="P. H. LTD")),
    ref="[8]",
    contexts=[
        "InadditiontocommercialvirtualmachinesoftwaresuchasVMware[7]and Parallels [8], fully-functioning open source alternatives such as VirtualBox [9] and Xen [10] are available",
        
    ],
    accessed="March 2011",
))

DB(Citation(
    brammer2011a, watson2008a, ref="[9]",
    contexts=[
        "InadditiontocommercialvirtualmachinesoftwaresuchasVMware[7]and Parallels [8], fully-functioning open source alternatives such as VirtualBox [9] and Xen [10] are available",
        
    ],
))

DB(Citation(
    brammer2011a, barham2003a, ref="[10]",
    contexts=[
        "InadditiontocommercialvirtualmachinesoftwaresuchasVMware[7]and Parallels [8], fully-functioning open source alternatives such as VirtualBox [9] and Xen [10] are available",
        
    ],
))

DB(Citation(
    brammer2011a, matthews2010a, ref="[11]",
    contexts=[
        "Figure 3 shows a sample prototype of a Paper Mˆach´e virtual machine executing a published paper describing a MapReduce inspired algorithm called MrsRF [11].",
        
    ],
))

DB(Citation(
    brammer2011a, ranger2007a, ref="[12]",
    contexts=[
        "TheMrsRFsourcecodetakesadvantageofPhoenix[12],anunderlyingMapReduceframeworkwhichwasoriginally designed for the Solaris operating system.",
        
    ],
))

DB(Citation(
    brammer2011a, loosemore1996a, ref="[13]",
    contexts=[
        "However, if the readers and reviewers do not have access to those versions of Linux (or the correct version of the Gnu C Library [13]), then they cannot run our software properly.",
        
    ],
))
