# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1978 import lamport1978a
from ..work.y1996 import neil1996a
from ..work.y1997 import katcher1997a
from ..work.y2001 import lamport2001a
from ..work.y2005 import simmhan2005b
from ..work.y2005 import widom2005a
from ..work.y2006 import nightingale2006a
from ..work.y2006 import sears2006a
from ..work.y2007 import agrawal2007a
from ..work.y2007 import jermaine2007a
from ..work.y2007 import spillane2007a
from ..work.y2008 import muniswamy2008a
from ..work.y2008 import sears2008a
from ..work.y2009 import spillane2009a
from ..work.y2009 import spillane2009b


DB(Citation(
    spillane2009a, agrawal2007a, ref="[1]",
    contexts=[
        "These numbers are based on the arithmetic mean of ﬁle system size from Agarwal’s 5-year study[1].",
        
    ],
))

DB(Citation(
    spillane2009a,
    Site("Dublin core", "dublincore.org"),
    ref="[2]",
    contexts=[
        "Similarly,StoryBook’simplementationisindependentofthe formatofextendedrecords,allowingapplicationstouse metadatastandardssuchasRDF[19]orDublinCore[2] as theysee ﬁt.",
        
    ],
    accessed="2008",
))

DB(Citation(
    spillane2009a,
    Site("ExP at", "expat.sf.net"),
    ref="[3]",
    contexts=[
        "For example,our.docxinspectorislinkedagainsttheXML parser ExPat [3].",
        
    ],
    accessed="Dec 2008",
))

DB(Citation(
    spillane2009a, jermaine2007a, ref="[4]",
    contexts=[
        "PartitioningtheindexacrossmultipleRoseindexes wouldlessen theimpactofthis problem[4].",
        
    ],
))

DB(Citation(
    spillane2009a, katcher1997a, ref="[5]",
    contexts=[
        "threaded version of Postmark [5] on top of ext3, on top of FuseFS, a “pass through” FUSE ﬁle system that measures Story Book’s instrumentation overhead, and on top of TxtFS, a Story Book provenance ﬁle system that records diffs when .txt ﬁles are modiﬁed.",
        
    ],
))

DB(Citation(
    spillane2009a, lamport1978a, ref="[6]",
    contexts=[
        "We preferthis approach to custom provenance consensus algorithms, as the problem of imposing a partial order over events in a distributed system is well-understood; building a distributed version of Story Book is simply a matter of building a provenance source that makes use of wellknown distributed systems techniques such as logical clocks[6]orPaxos[7]",
        
    ],
)) 

DB(Citation(
    spillane2009a, lamport2001a, ref="[7]",
    contexts=[
        "We preferthis approach to custom provenance consensus algorithms, as the problem of imposing a partial order over events in a distributed system is well-understood; building a distributed version of Story Book is simply a matter of building a provenance source that makes use of wellknown distributed systems techniques such as logical clocks[6]orPaxos[7]",
        
    ],
)) 

DB(Citation(
    spillane2009a,
    Site("FUSE ISO File System", "http: //fuse.sf.net/wiki/index.php/FuseIso"),
    ref="[8]",
    contexts=[
        "FUSE [8] and MySQL [18] intercept ﬁle system and database events",
        
    ],
    accessed="Jan. 2006",
)) 

DB(Citation(
    spillane2009a, muniswamy2008a, ref="[9]",
    contexts=[
        "Although PASSv2 [9] suffers from these issues, it is also the closest system to StoryBook(Figure2).",
        
    ],
)) 

DB(Citation(
    spillane2009a, nightingale2006a, ref="[10]",
    contexts=[
        "Thisapproachisasimpliﬁedversion of Speculator’s [10] external synchrony support, in that itperformsdisksynchronizationbeforepagewrite-back, butunlikeSpeculator,itwillnotsyncthediskbeforeany event which presents information to the user (e.g., via tty1)",
        
    ],
)) 

DB(Citation(
    spillane2009a, neil1996a, ref="[11]",
    contexts=[
        "datausingdatabase-styleno-Force/Stealrecoveryforits hashtables,andcompressedlogstructuredmerge(LSM) trees [11] for its Rose [13] indexes.",
        
    ],
))

DB(Citation(
    spillane2009a, sears2006a, ref="[12]",
    contexts=[
        "These provenance records are then inserted into either Stasis [12] or Berkeley DB [15].",
        
    ],
))

DB(Citation(
    spillane2009a, sears2008a, ref="[13]",
    contexts=[
        "datausingdatabase-styleno-Force/Stealrecoveryforits hashtables,andcompressedlogstructuredmerge(LSM) trees [11] for its Rose [13] indexes.",
        
    ],
)) 

DB(Citation(
    spillane2009a, simmhan2005b, ref="[14]",
    contexts=[
        "A survey of provenance systems [14] provides a taxonomy of existing provenance databases.",
        
    ],
))

DB(Citation(
    spillane2009a,
    Site("Berkeley DB Reference Guide, 4_3_27 edition", "www.oracle.com/technology/documentation/berkeley-db/db/api_c/frame.html"),
    ref="[15]",
    contexts=[
        "These provenance records are then inserted into either Stasis [12] or Berkeley DB [15].",
        
    ],
    accessed="Dec. 2004",
)) 

DB(Citation(
    spillane2009a, spillane2009b, ref="[16]",
    contexts=[
        "Story Book utilizes Valor [16] to maintain write-ordering between its logs and the kernel page cache. This reduces the number of diskﬂushes,greatlyimprovingperformance.",
        
    ],
))

DB(Citation(
    spillane2009a, spillane2007a, ref="[17]",
    contexts=[
        ". Story Book’s FUSE-based design facilitates transparent provenance inspectors that require no applicationmodiﬁcationand donot force developers toportuser-levelfunctionalityintothekernel[17].",
        
    ],
))

DB(Citation(
    spillane2009a,
    Site("MySQL", "www.mysql.com"),
    ref="[18]",
    contexts=[
        "FUSE [8] and MySQL [18] intercept ﬁle system and database events",
        
    ],
    accessed="Dec. 2008",
))

DB(Citation(
    spillane2009a,
    Site("Resource description framework", "w3.org/RDF"),
    ref="[19]",
    contexts=[
        "Similarly,StoryBook’simplementationisindependentofthe formatofextendedrecords,allowingapplicationstouse metadatastandardssuchasRDF[19]orDublinCore[2] as theysee ﬁt.",
        
    ],
    accessed="2008"
))

DB(Citation(
    spillane2009a, widom2005a, ref="[20]",
    contexts=[
        "Databases such as Trio [20] reason about the quality or reliability of input data and processes that modify it overtime.",
        
    ],
))