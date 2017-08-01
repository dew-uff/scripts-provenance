# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2008 import davidson2008a
from ..work.y2009 import donoho2009a
from ..work.y2009 import leveque2009a
from ..work.y2011 import freire2011b
from ..work.y2012 import freire2012b
from ..work.y2012 import guo2012a
from ..work.y2012 import guo2012b
from ..work.y2012 import davison2012a
from ..work.y2013 import chirigati2013b


DB(Citation(
    chirigati2013b, davidson2008a, ref="[1]",
    contexts=[
        "While these systems maintain provenance information for workﬂow executions and data products derived by workﬂows [1], they fail to capture information about the environment, including software and data dependencies.",
        
    ],
))

DB(Citation(
    chirigati2013b, davison2012a, ref="[2]",
    contexts=[
        "The ability to reproduce and test experiments is critical in the scientiﬁc method [2, 5], both to verify results and to build on them.",
        
    ],
))

DB(Citation(
    chirigati2013b, donoho2009a, ref="[3]",
    contexts=[
        "This has led to a credibility crisis in computational science [3].",
        
    ],
))

DB(Citation(
    chirigati2013b, freire2011b, ref="[4]",
    contexts=[
        "The current implementation of ReproZip derives workﬂows that can be run on the VisTrails system (www.vistrails.org) [4].",
        
    ],
))

DB(Citation(
    chirigati2013b, freire2012b, ref="[5]",
    contexts=[
        "The ability to reproduce and test experiments is critical in the scientiﬁc method [2, 5], both to verify results and to build on them.",
        
    ],
))

DB(Citation(
    chirigati2013b,
    Site("GenePattern", "http://www.broadinstitute.org/ cancer/software/genepattern/"),
    ref="[6]",
    contexts=[
        "Some of these solutions are domain-speciﬁc. For example, GenePattern [6] is a genomic analysis platform, while Madagascar [10] supports multidimensional data analysis and is used to analyze seismic data.",
        
    ],
)) 

DB(Citation(
    chirigati2013b, guo2012b, ref="[7]",
    contexts=[
        "Another class of tools focuses on capturing information about the computational environment. Examples include virtual machines and CDE [7].",
        "It relies on the ptrace call on Linux to identify only the ﬁles required for running a particular command, and creates a package containing these ﬁles [7].",
        
    ],
))

DB(Citation(
    chirigati2013b, guo2012a, ref="[8]",
    contexts=[
        "Our choice of SystemTap and MongoDB was inspired by the Burrito System [8], which successfully uses these tools to capture and store provenance for programs run on Linux",
        
    ],
))

DB(Citation(
    chirigati2013b, leveque2009a, ref="[9]",
    contexts=[
        "Since details of the computational steps are often omitted, it is diﬃcult to verify and reproduce many of the published results [9].",
        
    ],
))

DB(Citation(
    chirigati2013b,
    Site("Madagascar", "http://www.ahay.org/wiki/Main_Page"),
    ref="[10]",
    contexts=[
        "Some of these solutions are domain-speciﬁc. For example, GenePattern [6] is a genomic analysis platform, while Madagascar [10] supports multidimensional data analysis and is used to analyze seismic data.",
        
    ],
)) 

DB(Citation(
    chirigati2013b,
    Site("MongoDB", "http://www.mongodb.org/"),
    ref="[11]",
    contexts=[
        "This information is then collected and stored in MongoDB [11], a NoSQL database, where it can be easily accessed and queried",
        
    ],
)) 

DB(Citation(
    chirigati2013b,
    Site("SystemTap", "http://sourceware.org/systemtap/"),
    ref="[12]",
    contexts=[
        "The system uses SystemTap [12] to transparently capture the provenance of the experiment",
        
    ],
))