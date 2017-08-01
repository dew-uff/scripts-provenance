# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1997 import abiteboul1997a
from ..work.y1997 import foster1997a
from ..work.y1998 import vahdat1998a
from ..work.y2001 import heydon2001a
from ..work.y2003 import foster2003a
from ..work.y2003 import king2003a
from ..work.y2003 import shepler2003a
from ..work.y2004 import bose2004a
from ..work.y2005 import chanda2005a
from ..work.y2005 import efstathopoulos2005a
from ..work.y2005 import goel2005a
from ..work.y2005 import halcrow2005a
from ..work.y2005 import newsome2005a
from ..work.y2005 import widom2005a
from ..work.y2006 import muniswamy2006a
from ..work.y2006 import zeldovich2006a
from ..work.y2006 import altintas2006a
from ..work.y2007 import fonseca2007a
from ..work.y2007 import krohn2007a
from ..work.y2007 import yin2007a
from ..work.y2008 import braun2008a
from ..work.y2008 import holland2008a
from ..work.y2008 import sundararaman2008a
from ..work.y2009 import muniswamy2009b
from ..work.y2009 import muniswamy2009a
from ..work.y2009 import hasan2009a
from ..work.y2009 import holland2009a
from ..work.y2009 import margo2009a

DB(Citation(
    muniswamy2009a, abiteboul1997a, ref="[1]",
    contexts=[
        "The Lore semistructured database project at Stanford provided us with the Lorel [1] query language and its “OEM” data model.",
        
    ],
))

DB(Citation(
    muniswamy2009a, altintas2006a, ref="[2]",
    contexts=[
        "Tracking provenance at the level provided by workﬂow engines – such as Pasoa [23], Chimera [9], and Kepler [2] – allows users to group collection of related objects into single logical entities.",
        "Next, we decided to explore integrating a provenanceaware workﬂow engine with PASSv2 as most prior provenance systems operated at the level of a workﬂow engine [2, 9, 23]",
        "We selected the Kepler open-source workﬂow enactment engine [2] in which to explore integrating workﬂow provenance with PASSv2.",
        
    ],
))

DB(Citation(
    muniswamy2009a, bose2004a, ref="[3]",
    contexts=[
        "System-call-based systems such as ES3 [3], TREC [28], and PASS [21] operate at the level communicated via system calls – processes and ﬁles.",
        "System level solutions like ES3 [3] and PASSv1 [21] capture information at the operating system level, losing both the semantic information of domain-speciﬁc solutions and also the relationships among data sets and processingunitsfoundinworkﬂowengines",
        
    ],
))

DB(Citation(
    muniswamy2009a, braun2008a, ref="[4]",
    contexts=[
        "however, a related paper presents an in-depth discussion of the problem and our approach to solving it [4].",
        
    ],
))

DB(Citation(
    muniswamy2009a, chanda2005a, ref="[5]",
    contexts=[
        "Chanda et. al. [5] present a mechanism to use causal information ﬂow to introduce new functionality.",
        
    ],
))

DB(Citation(
    muniswamy2009a, efstathopoulos2005a, ref="[6]",
    contexts=[
        "Provenance is not the same as a security label, and provenance systems are different from label-based security systems such as HiStar [31], Asbestos [6], and Flume [18].",
        
    ],
))

DB(Citation(
    muniswamy2009a, fonseca2007a, ref="[7]",
    contexts=[
        "X-Trace [7] is a research prototype built to diagnoseproblemsinnetworkapplicationsthatspanmultipleprotocol layers and administrative domains.",
        
    ],
))

DB(Citation(
    muniswamy2009a, foster1997a, ref="[8]",
    contexts=[
        "Serviceorientedworkﬂow(SOA)approaches[8,9,23],typically associated with workﬂow engines, record provenance at the level of workﬂow stages and data or message exchanges",
        
    ],
))

DB(Citation(
    muniswamy2009a, foster2003a, ref="[9]",
    contexts=[
        "Serviceorientedworkﬂow(SOA)approaches[8,9,23],typically associated with workﬂow engines, record provenance at the level of workﬂow stages and data or message exchanges",
        "Tracking provenance at the level provided by workﬂow engines – such as Pasoa [23], Chimera [9], and Kepler [2] – allows users to group collection of related objects into single logical entities.",
        "Next, we decided to explore integrating a provenanceaware workﬂow engine with PASSv2 as most prior provenance systems operated at the level of a workﬂow engine [2, 9, 23]",
        
    ],
))

DB(Citation(
    muniswamy2009a,
    Site("GenePattern", "http://www.broad.mit.edu/cancer/software/genepattern"),
    ref="[10]",
    contexts=[
        "At the domain-speciﬁc level, systems like GenePattern [10] provide provenance for environments in which biologists perform routine analyses",
        
    ],
))

DB(Citation(
    muniswamy2009a, goel2005a, ref="[11]",
    contexts=[
        "Without Layering: Alice can traverse the provenance graph recorded by PASSv2 (similar to Backtracker [17] andTaser[11])toidentifyandremovethemalwarebinaries and recover any corrupted ﬁles.",
        
    ],
))

DB(Citation(
    muniswamy2009a, halcrow2005a, ref="[12]",
    contexts=[
        "Lasagna is a stackable ﬁle system,basedupontheeCryptfs[12]codebase.",
        
    ],
))

DB(Citation(
    muniswamy2009a, hasan2009a, ref="[13]",
    contexts=[
        "While there has been research showing the use of provenance for auditing and enhancing security [13], there has been little work on security controls for theprovenanceitself.",
        
    ],
))

DB(Citation(
    muniswamy2009a, heydon2001a, ref="[14]",
    contexts=[
        "Another class of systems that maintain dependencies aresoftwarebuildsystemssuchasVesta[14].",
        
    ],
))

DB(Citation(
    muniswamy2009a, holland2009a, ref="[15]",
    contexts=[
        "The PQL reference manual is available online [15].",
        
    ],
))

DB(Citation(
    muniswamy2009a, holland2008a, ref="[16]",
    contexts=[
        "After struggling through three generations of query languages for provenance, we incorporated the input from our users and derived the following list of requirements for a provenance query language [16]:",
        "We present a more in-depth discussion of these issues in a recent publication [16].",
        
    ],
))

DB(Citation(
    muniswamy2009a, king2003a, ref="[17]",
    contexts=[
        "Without Layering: Alice can traverse the provenance graph recorded by PASSv2 (similar to Backtracker [17] andTaser[11])toidentifyandremovethemalwarebinaries and recover any corrupted ﬁles.",
        
    ],
))

DB(Citation(
    muniswamy2009a, krohn2007a, ref="[18]",
    contexts=[
        "Provenance is not the same as a security label, and provenance systems are different from label-based security systems such as HiStar [31], Asbestos [6], and Flume [18].",
        
    ],
))

DB(Citation(
    muniswamy2009a, margo2009a, ref="[19]",
    contexts=[
        "We are currently exploring provenance collection in a Firefox [19].",
        
    ],
))

DB(Citation(
    muniswamy2009a, muniswamy2009b, ref="[20]",
    contexts=[
        "InPASSv2,weuse a more conservative algorithm, called the cycle avoidance algorithm that uses only an object’s local dependency information to avoid cycles. We discuss and analyze this algorithm in detail in earlier work [20].",
        
    ],
))

DB(Citation(
    muniswamy2009a, muniswamy2006a, ref="[21]",
    contexts=[
        "System-call-based systems such as ES3 [3], TREC [28], and PASS [21] operate at the level communicated via system calls – processes and ﬁles.",
        "System level solutions like ES3 [3] and PASSv1 [21] capture information at the operating system level, losing both the semantic information of domain-speciﬁc solutions and also the relationships among data sets and processingunitsfoundinworkﬂowengines",
        "Cycles: In earlier work, we discussed the challenge of detecting and removing cycles in PASSv1 [21].",
        
    ],
))

DB(Citation(
    muniswamy2009a, newsome2005a, ref="[22]",
    contexts=[
        "Several systems have looked at propagating taint informationalongwiththedatainordertodebugapplications or to detect security violations [22, 30].",
        
    ],
))

DB(Citation(
    muniswamy2009a,
    Site("Provenance aware service oriented architecture", "http://twiki.pasoa.ecs.soton.ac.uk/bin/view/PASOA/WebHome"),
    ref="[23]",
    contexts=[
        "Serviceorientedworkﬂow(SOA)approaches[8,9,23],typically associated with workﬂow engines, record provenance at the level of workﬂow stages and data or message exchanges",
        "Tracking provenance at the level provided by workﬂow engines – such as Pasoa [23], Chimera [9], and Kepler [2] – allows users to group collection of related objects into single logical entities.",
        "Next, we decided to explore integrating a provenanceaware workﬂow engine with PASSv2 as most prior provenance systems operated at the level of a workﬂow engine [2, 9, 23]",
        
    ],
))

DB(Citation(
    muniswamy2009a,
    Site("The First Provenance Challenge", "http://twiki.ipaw.info/bin/view/Challenge/FirstProvenanceChallenge"),
    ref="[24]",
    contexts=[
        "Implementing the scenario depicted in Figure 1, we use Kepler to execute the Provenance Challengeworkﬂow [24], reading inputs from one NFS ﬁle server and writing outputs to another",
        
    ],
))

DB(Citation(
    muniswamy2009a,
    Site("The Second Provenance Challenge", "http://twiki.ipaw.info/bin/view/Challenge/SecondProvenanceChallenge"),
    ref="[25]",
    contexts=[
        "However, the Second Provenance Challenge [25] showed that even at a single level of abstraction, uniform object naming is both fundamental to provenance interoperability and nontrivia",
        
    ],
))

DB(Citation(
    muniswamy2009a, shepler2003a, ref="[26]",
    contexts=[
        "We implemented provenance-aware NFS using NFSv4 [26] in Linux 2.6.23.17.",
        
    ],
))

DB(Citation(
    muniswamy2009a, sundararaman2008a, ref="[27]",
    contexts=[
        ". Iftheoperatingsystemiscompromised,wecanensure the integrity of the provenance collected before the compromise by using a selective versioning secure disk system [27].",
        
    ],
))

DB(Citation(
    muniswamy2009a, vahdat1998a, ref="[28]",
    contexts=[
        "System-call-based systems such as ES3 [3], TREC [28], and PASS [21] operate at the level communicated via system calls – processes and ﬁles.",
        
    ],
))

DB(Citation(
    muniswamy2009a, widom2005a, ref="[29]",
    contexts=[
        "Application-level systems, such as Trio [29], record provenance at the semantic level of the application – tuples for a database system",
        
    ],
))

DB(Citation(
    muniswamy2009a, yin2007a, ref="[30]",
    contexts=[
        "Several systems have looked at propagating taint informationalongwiththedatainordertodebugapplications or to detect security violations [22, 30].",
        
    ],
))

DB(Citation(
    muniswamy2009a, zeldovich2006a, ref="[31]",
    contexts=[
        "Provenance is not the same as a security label, and provenance systems are different from label-based security systems such as HiStar [31], Asbestos [6], and Flume [18].",
        
    ],
))