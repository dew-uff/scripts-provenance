# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1988 import aho1988a
from ..work.y2002 import viega2002a
from ..work.y2004 import cantrill2004a
from ..work.y2005 import luk2005a
from ..work.y2006 import muniswamy2006a
from ..work.y2007 import cheney2007c
from ..work.y2007 import buneman2007a
from ..work.y2009 import spillane2009a
from ..work.y2009 import demsky2009a
from ..work.y2009 import margo2009a
from ..work.y2010 import kemerlis2010a
from ..work.y2010 import michaelis2010a
from ..work.y2010 import muniswamy2010a
from ..work.y2011 import dietz2011a
from ..work.y2011 import jones2011a
from ..work.y2011 import lakshmanan2011a
from ..work.y2011 import theoharis2011a
from ..work.y2012 import gessiou2012a
from ..work.y2012 import kemerlis2012a


DB(Citation(
    gessiou2012a, 
    DB(Site("Sqlite", "http://www.sqlite.org/")),
    ref="[1]",
    contexts=[
        "The second scenario we consider is in the context of databases and demonstrates the assisted discovery feature of our framework. Our goal is to locate the appropriate point (i.e., function) to log queries in SQLite [1].",
        
    ],
))

DB(Citation(
    gessiou2012a, aho1988a, ref="[2]",
    contexts=[
        "D is C-like but it also resembles AWK [2] a lot in terms of structure.",
        
    ],
))

DB(Citation(
    gessiou2012a, 
    DB(Site("Apple dtrace(1) Mac OS X Manual Page", "http://developer.apple.com/mac/library/documentation/Darwin/Reference/ManPages/man1/dtrace.1.html")),
    ref="[3]",
    contexts=[
        "Initially, DTrace was developed for Sun’s Solaris 10, but it has been integrated also into Apple’s Mac OS X/Darwin (since 10.5/9) [3], FreeBSD (since 7.1) [9], as well as into other microkernel designs such as QNX (i.e., the Unix-like, real-time OS for embedded systems) [20]. Moreover, Oracle Linux latest version included a port of DTrace for Linux [14].",
        
    ],
))

DB(Citation(
    gessiou2012a, buneman2007a, ref="[4]",
    contexts=[
        "Most of the recent work has been on data provenance in database systems [4].",
        
    ],
))

DB(Citation(
    gessiou2012a, cantrill2004a, ref="[5]",
    contexts=[
        "The scoping rules of the language, its intrinsic data types, as well the program structure are explained in great detail in [5].",
        
    ],
))

DB(Citation(
    gessiou2012a, cheney2007c, ref="[6]",
    contexts=[
        "Some representative provenance schemes have been proposed for ﬁle systems [18], databases [6], web applications [13,17,22], cloud computing [19], smart phone operating systems [8], and web browsers [16]",
        "The reason behind choosing these applications is because they have been already studied in the literature [18,6,16].",
        "Also, more theoretical aspects of the provenance notions (where, why and how) have been studied [6].",
        
    ],
))

DB(Citation(
    gessiou2012a, demsky2009a, ref="[7]",
    contexts=[
        "Another system that combines both static and dynamic analysis to trace provenance is Garm [7]. While our framework is transparent, Garm has to rewrite the binary when the binary executed. The main advantage of our approach over Garm’s is that our framework can be applied to any level of the system, capturing even very high-level information. On the other hand, Garm only operates on low level data operations",
        
        
    ],
))

DB(Citation(
    gessiou2012a, dietz2011a, ref="[8]",
    contexts=[
        "Some representative provenance schemes have been proposed for ﬁle systems [18], databases [6], web applications [13,17,22], cloud computing [19], smart phone operating systems [8], and web browsers [16]",
        
    ],
))

DB(Citation(
    gessiou2012a, 
    DB(Site("FreeBSD. DTrace – FreeBSD Wiki", "http://wiki.freebsd.org/DTrace")),
    ref="[9]",
    contexts=[
        "Initially, DTrace was developed for Sun’s Solaris 10, but it has been integrated also into Apple’s Mac OS X/Darwin (since 10.5/9) [3], FreeBSD (since 7.1) [9], as well as into other microkernel designs such as QNX (i.e., the Unix-like, real-time OS for embedded systems) [20]. Moreover, Oracle Linux latest version included a port of DTrace for Linux [14].",
        
    ],
))

DB(Citation(
    gessiou2012a, jones2011a, ref="[10]",
    contexts=[
        "Transient provenance [10] keeps information about emigrant data, like ﬁles that were moved, who moved them, and when they were moved, aiming at facilitating the administrators in case of a leak.",
        
    ],
))

DB(Citation(
    gessiou2012a, kemerlis2010a, ref="[11]",
    contexts=[
        "iLeak [11] is a system proposed for detecting inadvertent information leaks.",
        
    ],
))

DB(Citation(
    gessiou2012a, kemerlis2012a, ref="[12]",
    contexts=[
        "Also, tools implemented on top of Pin, like libdft [12] which provides byte-level data ﬂow tracking, could potentially add more features to our framework",
        
    ],
))

DB(Citation(
    gessiou2012a, lakshmanan2011a, ref="[13]",
    contexts=[
        "Some representative provenance schemes have been proposed for ﬁle systems [18], databases [6], web applications [13,17,22], cloud computing [19], smart phone operating systems [8], and web browsers [16]",
        
    ],
))

DB(Citation(
    gessiou2012a, 
    DB(Site("Linux, O. Trying out dtrace", "http://blogs.oracle.com/wim/entry/trying_out_dtrace")),
    ref="[14]",
    contexts=[
        "Initially, DTrace was developed for Sun’s Solaris 10, but it has been integrated also into Apple’s Mac OS X/Darwin (since 10.5/9) [3], FreeBSD (since 7.1) [9], as well as into other microkernel designs such as QNX (i.e., the Unix-like, real-time OS for embedded systems) [20]. Moreover, Oracle Linux latest version included a port of DTrace for Linux [14].",
        
    ],
))

DB(Citation(
    gessiou2012a, luk2005a, ref="[15]",
    contexts=[
        "Combining a more powerful tool in our framework, like the dynamic binary instrumentation of Pin [15], seems suﬃcient to overcome these limitations, but in some extra cost.",
        
    ],
))

DB(Citation(
    gessiou2012a, margo2009a, ref="[16]",
    contexts=[
        "Some representative provenance schemes have been proposed for ﬁle systems [18], databases [6], web applications [13,17,22], cloud computing [19], smart phone operating systems [8], and web browsers [16]",
        "The reason behind choosing these applications is because they have been already studied in the literature [18,6,16].",
        "We treat the notion of data provenance in a browser as it has been proposed in [16].",
        "The authors of [16] describe how a browser enabled with provenance capabilities can improve user experience",
        
    ],
))

DB(Citation(
    gessiou2012a, michaelis2010a, ref="[17]",
    contexts=[
        "Some representative provenance schemes have been proposed for ﬁle systems [18], databases [6], web applications [13,17,22], cloud computing [19], smart phone operating systems [8], and web browsers [16]",
        
    ],
))

DB(Citation(
    gessiou2012a, muniswamy2006a, ref="[18]",
    contexts=[
        "Some representative provenance schemes have been proposed for ﬁle systems [18], databases [6], web applications [13,17,22], cloud computing [19], smart phone operating systems [8], and web browsers [16]",
        "The reason behind choosing these applications is because they have been already studied in the literature [18,6,16].",
        "Data provenance in the context of ﬁle-systems was introduced in PASS [18].",
        "PASS [18] supports provenance at the system level and is a layer grafted in a ﬁle system.",
        
    ],
))

DB(Citation(
    gessiou2012a, muniswamy2010a, ref="[19]",
    contexts=[
        "Some representative provenance schemes have been proposed for ﬁle systems [18], databases [6], web applications [13,17,22], cloud computing [19], smart phone operating systems [8], and web browsers [16]",
        "Recently, the notion of provenance has also been introduced in cloud infrastructures [19].",
        
    ],
))

DB(Citation(
    gessiou2012a, 
    DB(Site("QNX The community portal for qnx software developers", "http://community.qnx.com/sf/projects/dtrace/")),
    ref="[20]",
    contexts=[
        "Initially, DTrace was developed for Sun’s Solaris 10, but it has been integrated also into Apple’s Mac OS X/Darwin (since 10.5/9) [3], FreeBSD (since 7.1) [9], as well as into other microkernel designs such as QNX (i.e., the Unix-like, real-time OS for embedded systems) [20]. Moreover, Oracle Linux latest version included a port of DTrace for Linux [14].",
        
    ],
))

DB(Citation(
    gessiou2012a, spillane2009a, ref="[21]",
    contexts=[
        "Story Book is a system that adds provenance in diﬀerent systems [21",
        
    ],
))

DB(Citation(
    gessiou2012a, theoharis2011a, ref="[22]",
    contexts=[
        "Some representative provenance schemes have been proposed for ﬁle systems [18], databases [6], web applications [13,17,22], cloud computing [19], smart phone operating systems [8], and web browsers [16]",
        
    ],
))

DB(Citation(
    gessiou2012a, viega2002a, ref="[23]",
    contexts=[
        "On the other hand, the function-call level, as provided by OpenSSL [23], has access to the encrypted data stream used by an HTTPS connection",
        "All these three functions can be found in the OpenSSL [23] library which is used as the de facto standard for cryptographic operations.",
        
    ],
))