# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2006 import muniswamy2006a
from ..work.y2006 import ludascher2006a
from ..work.y2008 import frew2008a
from ..work.y2009 import fomel2009a
from ..work.y2011 import freire2011b
from ..work.y2012 import freire2012a
from ..work.y2012 import freire2012b
from ..work.y2012 import guo2012a
from ..work.y2012 import guo2012b
from ..work.y2012 import davison2012a
from ..work.y2013 import chirigati2013a


DB(Citation(
    chirigati2013a, davison2012a, ref="[1]",
    contexts=[
        "Sumatra [1] is used for numerical computations",
        
    ],
))

DB(Citation(
    chirigati2013a, fomel2009a, ref="[2]",
    contexts=[
        "Because no details of the computational steps are given, it is difﬁcult to verify and reproducemanyofthepublishedresults,andthishasled to a credibility crisis in computational science [2].",
        
    ],
))

DB(Citation(
    chirigati2013a, freire2012a, ref="[3]",
    contexts=[
        "In order to reproduce an experiment, we need detailed provenance which includes [5, 3]: (i) a description of the data; (ii) a complete speciﬁcation of the experiment and its steps, preferably as a workflow in which parameters and computational tasks are explicitly deﬁned; and (iii) information about the originating computational environment E (e.g., OS, hardware architecture, and library dependencies) that may be needed if the experiment is to be re executed in a new environment E0.",
        "Thus, even though they support reproducibility, they do not support portability tonewenvironments[3].",
        
    ],
))

DB(Citation(
    chirigati2013a, freire2011b, ref="[4]",
    contexts=[
        "Scientiﬁcworkﬂowsystems[4,9,13], on the other hand, are general and support the speciﬁcation of arbitrary computational experiments.",
        "The experiment can be executed from the command line,andusersmayalsorunthederivedworkﬂow,which can be run by the VisTrails system [4]",
        
    ],
))

DB(Citation(
    chirigati2013a, freire2012b, ref="[5]",
    contexts=[
        "In order to reproduce an experiment, we need detailed provenance which includes [5, 3]: (i) a description of the data; (ii) a complete speciﬁcation of the experiment and its steps, preferably as a workflow in which parameters and computational tasks are explicitly deﬁned; and (iii) information about the originating computational environment E (e.g., OS, hardware architecture, and library dependencies) that may be needed if the experiment is to be re executed in a new environment E0.",
    ],
)) 

DB(Citation(
    chirigati2013a, frew2008a, ref="[6]",
    contexts=[
        "ES3 [6] uses strace to monitor operating system calls and constructs provenance graphs that resemble workﬂow speciﬁcations",
        
    ],
))

DB(Citation(
    chirigati2013a, guo2012b, ref="[7]",
    contexts=[
        "CDE [7] offers a lighter-weight alternative to virtual machines",
        
    ],
))

DB(Citation(
    chirigati2013a, guo2012a, ref="[8]",
    contexts=[
        "Burrito [8] is a Linux-based system that captures OS-level provenance for derived data productsandpresentsthisinformationtousers,whomay add annotations and generate an HTML report that summarizes the computational activities",
        "Our choice of SystemTap and MongoDB was inspired by the Burrito System [8], which successfully used these tools to gather and store provenance for programs run on Linux.",
        
    ],
))

DB(Citation(
    chirigati2013a, ludascher2006a, ref="[9]",
    contexts=[
        "Scientiﬁcworkﬂowsystems[4,9,13], on the other hand, are general and support the speciﬁcation of arbitrary computational experiments.",
        
    ],
))

DB(Citation(
    chirigati2013a,
    Site("MongoDB", "http://www.mongodb.org/"),
    ref="[10]",
    contexts=[
        "ReproZipmakesuseoftwoopen-sourcetoolstocapture the necessary provenance: SystemTap [12] and MongoDB [10].",
        
    ],
)) 

DB(Citation(
    chirigati2013a, muniswamy2006a, ref="[11]",
    contexts=[
        "PASS [11] produces audit trails that are stored in a database and that can be queried.",
        
    ],
))

DB(Citation(
    chirigati2013a,
    Site("SystemTap", "http://sourceware.org/systemtap/"),
    ref="[12]",
    contexts=[
        "ReproZipmakesuseoftwoopen-sourcetoolstocapture the necessary provenance: SystemTap [12] and MongoDB [10].",
        
    ],
)) 

DB(Citation(
    chirigati2013a,
    Site("Taverna", "http://www.taverna.org.uk"),
    ref="[13]",
    contexts=[
        "Scientiﬁcworkﬂowsystems[4,9,13], on the other hand, are general and support the speciﬁcation of arbitrary computational experiments.",
        
    ],
)) 
