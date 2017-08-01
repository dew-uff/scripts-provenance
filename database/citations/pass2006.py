# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1981 import moore1981a
from ..work.y1990 import altschul1990a
from ..work.y1995 import seltzer1995a
from ..work.y1997 import foster1997a
from ..work.y1998 import ansi1998a
from ..work.y1998 import baru1998a
from ..work.y1999 import nost1999a
from ..work.y1999 import olson1999a
from ..work.y1999 import zadok1999a
from ..work.y2001 import buneman2001a
from ..work.y2001 import frew2001a
from ..work.y2001 import heydon2001a
from ..work.y2002 import hodges2002a
from ..work.y2003 import foster2003a
from ..work.y2003 import pancerella2003a
from ..work.y2004 import deelman2004a
from ..work.y2004 import kashyap2004a
from ..work.y2005 import simmhan2005a
from ..work.y2005 import cao2005a
from ..work.y2005 import widom2005a
from ..work.y2005 import wright2005a
from ..work.y2006 import braun2006a
from ..work.y2006 import muniswamy2006a
from ..work.y2006 import muniswamy2006b
from ..work.y2008 import clifford2008a


DB(Citation(
    muniswamy2006a, altschul1990a, ref="[1]",
    contexts=[
        "One of our early users was a computational biologist who regularly uses blast [1] to ﬁnd the protein sequences in one species that are closely related to the protein sequences in another species.",
    ],
))

DB(Citation(
    muniswamy2006a, baru1998a, ref="[2]",
    contexts=[
        "San Diego SuperComputer’s Storage Request Broker [2, 25] has a Metadata Catalog similar to the MCS.",
    ],
))

DB(Citation(
    muniswamy2006a, braun2006a, ref="[3]",
    contexts=[
        "We are actively designing a security model for provenance, but its details are beyond the scope of this paper [3].",
        "We wholeheartedly believe that we cannot add security to an already existing system, so we are intentionally designing our next generation PASS (V2) from scratch, incorporating what we have learned about provenance collection as well as what we have ascertained about appropriate security models for PASS [3].",
    ],
))

DB(Citation(
    muniswamy2006a, buneman2001a, ref="[4]",
    contexts=[
        "In digital systems, ownership history includes a description of how the object was derived [4]",
    ],
))

DB(Citation(
    muniswamy2006a, 
    Site("ClearCase", "http://www.ibm.org/software/awdtools/clearcase"),
    ref="[5]",
    contexts=[
        "The source code control systems most similar to PASS are ClearCase (and its predecessor DSEE) and Vesta. ClearCase [5] is a source code control system, and like PASS, it is based on a custom ﬁlesystem.",
    ],
))

DB(Citation(
    muniswamy2006a, deelman2004a, ref="[6]",
    contexts=[
        "The tools that understand these workﬂows collect provenance and transmit it to a grid provenance service. For example, Globus [7] is used widely by high-energy physicists and includes the Metadata Catalog Service(MCS)[6]that stores metadata for logical data objects.",
    ],
))

DB(Citation(
    muniswamy2006a, foster1997a, ref="[7]",
    contexts=[
        "The tools that understand these workﬂows collect provenance and transmit it to a grid provenance service. For example, Globus [7] is used widely by high-energy physicists and includes the Metadata Catalog Service(MCS)[6]that stores metadata for logical data objects.",
    ],
))

DB(Citation(
    muniswamy2006a, foster2003a, ref="[8]",
    contexts=[
        "Chimera [8] is a virtual data system that providing a virtual data language (VDL) and a virtual data catalog (VDC).",
    ],
))

DB(Citation(
    muniswamy2006a, frew2001a, ref="[9]",
    contexts=[
        "Other domains have environments that track work and record provenance as Vesta does for software development. GenePattern [10] is an environment for computational biologists, the Collaboratory for Multi-scale Chemical Sciences (CMCS) [19] is an environment for chemists, and the Earth System Science Workbench (ESSW)[9] is an environment for earth scientists.",
    ],
))

DB(Citation(
    muniswamy2006a, 
    Site("GenePattern", "http://www.broad.mit.edu/cancer/software/genepattern"),
    ref="[10]",
    contexts=[
        "Other domains have environments that track work and record provenance as Vesta does for software development. GenePattern [10] is an environment for computational biologists, the Collaboratory for Multi-scale Chemical Sciences (CMCS) [19] is an environment for chemists, and the Earth System Science Workbench (ESSW)[9] is an environment for earth scientists.",
        "Application-speciﬁc provenance records are like annotations, but provided programmatically from, for example, a driver for a remote data-producing device (e.g., a driver taking data from a telescope) or an application environment such as GenePattern [10]",
    ],
))

DB(Citation(
    muniswamy2006a, heydon2001a, ref="[11]",
    contexts=[
        "Vesta [11] is a second generation build system developed at DEC Systems Research Center (SRC). The key design goals were making builds repeatable, consistent, and incremental.",
    ],
))

DB(Citation(
    muniswamy2006a, hodges2002a, ref="[12]",
    contexts=[
        "We began the PASS implementation with the simplest and lowest-level schema that could meet our query needs. In parallel with development of the prototype, we undertook an evaluation comparing different provenance storage solutions: our existing one, a relational database, XML-based representation, and LDAP-based representation [12].",
    ],
))

DB(Citation(
    muniswamy2006a, kashyap2004a, ref="[13]",
    contexts=[
        "We use an in-kernel port of the Berkeley DB embedded database library [18], called KBDB [13], to store and index provenance.",
    ],
))

DB(Citation(
    muniswamy2006a, cao2005a, ref="[14]",
    contexts=[
        "The Lineage File System (LinFS) [14] is most similar to PASS. LinFS is a ﬁle system that automatically tracks provenance at the ﬁle system level, focusing on executables, command lines and input ﬁles as the only source of provenance, ignoring the hardware and software environment in which such processes run. "
        "PASS must provide security for provenance. Provenance can require different access controls than the data it describes. Consider an employee performance review that includes input from others: while the review itself must be readable by the employee, the provenance must not [14].",
    ],
))

DB(Citation(
    muniswamy2006a, moore1981a, ref="[15]",
    contexts=[
        "Our prototype tracks provenance at a ﬁle granularity, but this is not an inherent property of PASS; a system could track provenance at ﬁner or coarser granularities [15] (e.g., bytes, lines, directories or whole volumes).",
    ],
))

DB(Citation(
    muniswamy2006a, muniswamy2006b, ref="[16]",
    contexts=[
        "We found that a Berkeley DB-based implementation provided the best run-time performance, but a relational implementation was more space-efﬁcient[16].",
    ],
)) 

DB(Citation(
    muniswamy2006a, nost1999a, ref="[17]",
    contexts=[
        "One obvious approach to provenance maintenance is to include provenance inside the corresponding data ﬁle. Astronomy’s Flexible Image Transport (FITS) format [17] and the Spatial Data Transfer Standard (SDTS) [23] are examples of this approach.",
    ],
))

DB(Citation(
    muniswamy2006a, olson1999a, ref="[18]",
    contexts=[
        "We use an in-kernel port of the Berkeley DB embedded database library [18], called KBDB [13], to store and index provenance.",
    ],
))

DB(Citation(
    muniswamy2006a, pancerella2003a, ref="[19]",
    contexts=[
        "Other domains have environments that track work and record provenance as Vesta does for software development. GenePattern [10] is an environment for computational biologists, the Collaboratory for Multi-scale Chemical Sciences (CMCS) [19] is an environment for chemists, and the Earth System Science Workbench (ESSW)[9] is an environment for earth scientists.",
    ],
))

DB(Citation(
    muniswamy2006a, 
    Site("Data Dictionary for Preservation Metadata", "http://www.oclc.org/research/projects/pmwg/premis-final.pdf"),
    ref="[20]",
    contexts=[
        "Archivists maintain provenance meta-data to support document viability, renderability, understandability, authenticity, and identity in preservation contexts [20]",
    ],
    accessed="May 2005",
))

DB(Citation(
    muniswamy2006a, 
    Site("The R Project for Statistical Computing", "http://www.r-project.org"),
    ref="[21]",
    contexts=[
        "Discussions with users suggests that building a provenance-aware R environment [21] will make the platform attractive to biologists and social scientists.",
    ],
))

DB(Citation(
    muniswamy2006a, 
    Site("The Scriptome — Protocols for Manipulating Biological Data.", "http://cgr.harvard.edu/cbg/scriptome"),
    ref="[22]",
    contexts=[
        "She further tweaks the output ofblastrunningScriptome[22],asetoftoolsthatﬁlter, format, and merge data in tabular or common biological formats, on the output.",
    ],
))

DB(Citation(
    muniswamy2006a, ansi1998a, ref="[23]",
    contexts=[
        "One obvious approach to provenance maintenance is to include provenance inside the corresponding data ﬁle. Astronomy’s Flexible Image Transport (FITS) format [17] and the Spatial Data Transfer Standard (SDTS) [23] are examples of this approach.",
    ],
))

DB(Citation(
    muniswamy2006a, seltzer1995a, ref="[24]",
    contexts=[
        "We begin with the large and small ﬁle microbenchmarks frequently used to evaluate ﬁle system performance [24].",
    ],
))

DB(Citation(
    muniswamy2006a, 
    Site("FAQ: Frequently Asked Questions on SRB", "http://www.npaci.edu/dice/srb/faq.html"),
    ref="[25]",
    contexts=[
        "San Diego SuperComputer’s Storage Request Broker [2, 25] has a Metadata Catalog similar to the MCS.",
    ],
    accessed="June 2004",
))

DB(Citation(
    muniswamy2006a, widom2005a, ref="[26]",
    contexts=[
        "Trio [26] is to databases what a PASS is to ﬁle systems. Trio is a centralized database system that manages both data and its provenance.",
    ],
))

DB(Citation(
    muniswamy2006a, wright2005a, ref="[27]",
    contexts=[
        "To ensure a cold cache, we reformatted the ﬁle system on which the experiments took place between test runs. We used Auto-pilot [27] to run all our benchmarks.",
    ],
)) 

DB(Citation(
    muniswamy2006a, simmhan2005a, ref="[28]",
    contexts=[
        "Simmhan et al. categorize provenance solutions in terms of their architecture: database-oriented, service-oriented, and “other” [28].",
    ],
))

DB(Citation(
    muniswamy2006a, zadok1999a, ref="[29]",
    contexts=[
        "Pasta uses the FiST [29] toolkit for Linux to layer itself on top of any conventional ﬁle system. We use ext2fs as our underlying ﬁle system.",
    ],
))

# Forward Snowball

DB(Citation(
    clifford2008a, muniswamy2006a, ref="[10]",
    contexts=[
        "Other systems, such as PASS [10] and ES3 [11], capture provenance information at the operating system level—PASS in the kernel, at the ﬁle system interface, and ES3 via the user-level strace interface.",
    ],
))

