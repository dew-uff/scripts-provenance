# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1988 import korel1988a
from ..work.y1990 import agrawal1990a
from ..work.y1993 import agrawal1993a
from ..work.y1997 import alonso1997a
from ..work.y1997 import woodruff1997a
from ..work.y1998 import meinel1998a
from ..work.y1999 import gyimothy1999a
from ..work.y2000 import cui2000b
from ..work.y2001 import beszedes2001a
from ..work.y2001 import buneman2001a
from ..work.y2001 import marathe2001a
from ..work.y2002 import foster2002a
from ..work.y2002 import karypis2002a
from ..work.y2003 import foster2003a
from ..work.y2003 import stevens2003a
from ..work.y2003 import zhu2003a
from ..work.y2004 import zhang2004a
from ..work.y2005 import bhagwat2005a
from ..work.y2005 import zhang2005a
from ..work.y2005 import zhang2005b
from ..work.y2005 import bose2005a
from ..work.y2005 import frigo2005a
from ..work.y2005 import groth2005a
from ..work.y2007 import zhang2007a
from ..work.y2007 import zhang2007b
from ..work.y2007 import miles2007a


DB(Citation(
    zhang2007a, 
    DB(Site("Buddy, a binary decision diagram package", "http://vlsicad.eecs.umich.edu/BK/Slots/cache/www.itu.dk/research/buddy/", local="Department of Information Technology, Technical University of Denmark")),
    ref="[1]",
    contexts=[
        "Fortunately, recent research on dynamic slicing [27] reveals that reduced ordered Binary Decision Diagram (roBDD) [1] can be used to achieve both space and time eﬃciency in representing sets",
        
    ],
))

DB(Citation(
    zhang2007a, 
    DB(Site("Valgrind", "http://valgrind.org")),
    ref="[2]",
    contexts=[
        "We have implemente the lineage tracing prototype on the tool called Valgrind[2] which was originaly designe for debugging memory errors in x86 binaries.",
        
    ],
))

DB(Citation(
    zhang2007a, 
    DB(Site("bow", "http://www.cs.cmu.edu/mccallum/bow")),
    ref="[3]",
    contexts=[
        ". Rainbow[3] is a program that performs statistical text classiﬁcation",
        
    ],
))

DB(Citation(
    zhang2007a, 
    DB(Site("dq", "http://www.cs.purdue.edu/homes/mgelfeky/dq/")),
    ref="[4]",
    contexts=[
        "Auto-class [4] is an unsupervised Bayesian classiﬁcation system that seeks a maximum posterior probability classiﬁcation.",
        
    ],
))

DB(Citation(
    zhang2007a, 
    DB(Site("lemurproject", "http://www.lemurproject.org/")),
    ref="[5]",
    contexts=[
        "Lemur [5] is a toolkit designed to facilitate research in language modeling and information retrieval (IR), where IR is broadly interpreted as ad hoc and distributed retrieval, structured queries, cross-language IR, summarization, ﬁltering, categorization, and so on",
        
    ],
))

DB(Citation(
    zhang2007a, agrawal1990a, ref="[6]",
    contexts=[
        "Dynamic slices are usually computed by ﬁrst constructing a dynamic program dependence graph [6], in which an edge reveals a data/control dependence between two statement instances, and then traversing the graph to identify the set of reachable statement instances.",
        
    ],
))

DB(Citation(
    zhang2007a, agrawal1993a, ref="[7]",
    contexts=[
        "Apriori [7] is a data mining tool which is able to mine association rules. We used a 4 Mbytes input ﬁle",
        
    ],
))


DB(Citation(
    zhang2007a, alonso1997a, ref="[8]",
    contexts=[
        "Many prototype systems such as Chimera[11], MyGrid[24], and Geo-Opera [8] have been developed.",
        
    ],
))

DB(Citation(
    zhang2007a, beszedes2001a, ref="[9]",
    contexts=[
        "More recently, it has been shown that dynamic slices can be computed in a forward manner [9, 27], in which slices are continuously propagated and updated as the execution proceeds.",
        
    ],
))


DB(Citation(
    zhang2007a, bhagwat2005a, ref="[10]",
    contexts=[
        "Lineage tracing in the context of database systems has been extensively studied [12, 10, 13]",
        "Buneman et al. [12] classiﬁed lineage into why lineage, which speciﬁes why the data is derived, and where lineage, which speciﬁes where the data is copied from. Bhagwat et al.[10] proposed three schemes to propagate annotations attached to attributes in relational data.",
        
    ],
))


DB(Citation(
    zhang2007a, bose2005a, ref="[11]",
    contexts=[
        "ed and a general description of the input and output data. Coarse grained lineage is also referred to as work-ﬂow in literature. To improve scientiﬁc collaboration, Workﬂow Management System and Grid computation are used to simplify access to computational resources and experimental results over distributed systems[15, 14, 24, 11]",
        "Many prototype systems such as Chimera[11], MyGrid[24], and Geo-Opera [8] have been developed.",
        "[11] surveys the use of workﬂows in scientiﬁc computation",
        
    ],
))

DB(Citation(
    zhang2007a, buneman2001a, ref="[12]",
    contexts=[
        "Lineage tracing in the context of database systems has been extensively studied [12, 10, 13]",
        "If the ﬁle is in a semi-structured format such as XML, then the scheme proposed in [12] can be used.",
        "Buneman et al. [12] classiﬁed lineage into why lineage, which speciﬁes why the data is derived, and where lineage, which speciﬁes where the data is copied from. Bhagwat et al.[10] proposed three schemes to propagate annotations attached to attributes in relational data.",
        
    ],
))

DB(Citation(
    zhang2007a, cui2000b, ref="[13]",
    contexts=[
        "Lineage tracing in the context of database systems has been extensively studied [12, 10, 13]",
        "Cui et al. [13] propose ﬁne-grained tracing in the context of data warehousing where all data is produced using relational database queries.",
        
    ],
))


DB(Citation(
    zhang2007a, foster2003a, ref="[14]",
    contexts=[
"ed and a general description of the input and output data. Coarse grained lineage is also referred to as work-ﬂow in literature. To improve scientiﬁc collaboration, Workﬂow Management System and Grid computation are used to simplify access to computational resources and experimental results over distributed systems[15, 14, 24, 11]",
        
    ],
))


DB(Citation(
    zhang2007a, foster2002a, ref="[15]",
    contexts=[
        "ed and a general description of the input and output data. Coarse grained lineage is also referred to as work-ﬂow in literature. To improve scientiﬁc collaboration, Workﬂow Management System and Grid computation are used to simplify access to computational resources and experimental results over distributed systems[15, 14, 24, 11]",
        
    ],
))

DB(Citation(
    zhang2007a, frigo2005a, ref="[16]",
    contexts=[
        "The image processing program takes a cryo-EM image in tiﬀ format and applies Fourier transformation [16] to the image",
        
    ],
))

DB(Citation(
    zhang2007a, groth2005a, ref="[17]",
    contexts=[
        "An important aspect of data provenance is Relationship [23], which has been deﬁned as “Information on how one data item in a process relates to another.” Despite the importance of these relationships between input and output data, acquiring them remains a challenge which has not been addressed by the existing work [17, 23].",
        
    ],
))

DB(Citation(
    zhang2007a, gyimothy1999a, ref="[18]",
    contexts=[
        "that there exist expensive and conservative techniques to compute these invisible dependencies [18].",
        
    ],
))

DB(Citation(
    zhang2007a, karypis2002a, ref="[19]",
    contexts=[
        "Cluto [19] is a software package for clustering low- and high-dimensional datasets and for analyzing the characteristics of the various clusters.",
        
    ],
))

DB(Citation(
    zhang2007a, korel1988a, ref="[20]",
    contexts=[
        "In this section we present our new approach for automatic tracing of ﬁne-grained lineage through run-time analysis. This approach is motivated by the technique of dynamic slicing that is used as a debugging tool [20].",
        "Interested readers are referred to [20] for further details.",
        "Dynamic slicing [20] is a debugging technique that captures the executed statements that are involved in computation of a wrong value",
        
    ],
))

DB(Citation(
    zhang2007a, marathe2001a, ref="[21]",
    contexts=[
        "However, applications such as the scientiﬁc computations in [25, 21] require ﬁne-grained lineage.",
        "A veriﬁcation function is also used to reﬁne the set. Marathe [21] apply rewrite rules to AML (Array Manipulation Language) expression in order to trace ﬁne-grained lineage for array data",
        ". The identiﬁcation task is highly non-trivial and makes the approach impractical. Similarly, the work on lineage tracing for array data [21] is only applicable in a very limited scenario where the high-level operations are written in Array Manipulation Language (AML).",
        
    ],
))

DB(Citation(
    zhang2007a, meinel1998a, ref="[22]",
    contexts=[
        "More speciﬁcally, equivalence tests can be performed in O(1) time [22].",
        "Other binary operations (e.g., union) on two sets whose roBDD representations contain n and m roBDD nodes can be performed in time O(n × m) [22].",
        
    ],
))

DB(Citation(
    zhang2007a, miles2007a, ref="[23]",
    contexts=[
        "An important aspect of data provenance is Relationship [23], which has been deﬁned as “Information on how one data item in a process relates to another.” Despite the importance of these relationships between input and output data, acquiring them remains a challenge which has not been addressed by the existing work [17, 23].",
        
    ],
))


DB(Citation(
    zhang2007a, stevens2003a, ref="[24]",
    contexts=[
        "ed and a general description of the input and output data. Coarse grained lineage is also referred to as work-ﬂow in literature. To improve scientiﬁc collaboration, Workﬂow Management System and Grid computation are used to simplify access to computational resources and experimental results over distributed systems[15, 14, 24, 11]",
        "Many prototype systems such as Chimera[11], MyGrid[24], and Geo-Opera [8] have been developed.",
        
    ],
))


DB(Citation(
    zhang2007a, woodruff1997a, ref="[25]",
    contexts=[
        "However, applications such as the scientiﬁc computations in [25, 21] require ﬁne-grained lineage.",
        "In [25], Wooddruﬀ and Stonebraker use reverse functions to compute the mappings from output to input.",
        "Woodruﬀ and Stonebaker [25] support ﬁne-grainedlineage using inverse or weak inverse functions.",
        
    ],
))

DB(Citation(
    zhang2007a, zhang2007b, ref="[26]",
    contexts=[
        "Further details on how ﬁne-grained lineage can be managed in a RDBMS are discussed in our technical report [26].",
        
    ],
))

DB(Citation(
    zhang2007a, zhang2004a, ref="[27]",
    contexts=[
        "More recently, it has been shown that dynamic slices can be computed in a forward manner [9, 27], in which slices are continuously propagated and updated as the execution proceeds.",
        "Fortunately, recent research on dynamic slicing [27] reveals that reduced ordered Binary Decision Diagram (roBDD) [1] can be used to achieve both space and time eﬃciency in representing sets",
        "Recent research has shown that dynamic slicing is quite eﬀective in locating runtime software errors [28] and dynamic slices can be eﬃciently computed [27].",
        
    ],
))

DB(Citation(
    zhang2007a, zhang2005a, ref="[28]",
    contexts=[
        "More details on how to identify control dependence at runtime can be found in [28].",
        "Recent research has shown that dynamic slicing is quite eﬀective in locating runtime software errors [28] and dynamic slices can be eﬃciently computed [27].",
        
    ],
))

DB(Citation(
    zhang2007a, zhang2005b, ref="[29]",
    contexts=[
        "Liquid Chromatography Mass Spectrometry (LC-MS) is an eﬀective technique used in protein biomarker discovery in cancer research [30, 29].",
        "The code used to process the LC-MS data was obtained from [29]",
        "De-isotope [29] is the program introduced in Section 2",
        
    ],
))

DB(Citation(
    zhang2007a, zhu2003a, ref="[30]",
    contexts=[
        "Liquid Chromatography Mass Spectrometry (LC-MS) is an eﬀective technique used in protein biomarker discovery in cancer research [30, 29].",
        
    ],
))