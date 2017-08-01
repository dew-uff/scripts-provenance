# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2000 import jain2000a
from ..work.y2005 import alpern2005a
from ..work.y2005 import fisher2005a
from ..work.y2007 import aiken2007a
from ..work.y2007 import spillane2007a
from ..work.y2008 import cadar2008a
from ..work.y2009 import sucan2009a
from ..work.y2010 import laadan2010a
from ..work.y2010 import lahiri2010a
from ..work.y2011 import guo2011a
from ..work.y2011 import guo2011d


DB(Citation(
    guo2011a,
    Site("CDE project home page", "http://www.pgbovine.net/cde.html"),
    ref="[1]",
    contexts=[
        "To alleviate these frustrations, we have created an open-sourcetoolnamed CDE thatmonitorsprogramexecution using ptrace and automatically packages up the Code, Data, and Environment required to run a set of x86-Linux programs on other x86-Linux machines [1].",
         "Sincewereleasedtheﬁrstversionofthe CDE executable online on Nov 9, 2010, it has been downloaded at least 2,000 times (as of April 2011) [1].",
        
    ],
))

DB(Citation(
    guo2011a,
    Site("Coq proof assistant: Bug 2443", "http://coq.inria.fr/bugs/show_bug.cgi?id=2443"),
    ref="[2]",
    contexts=[
        "Three bug reporters sent us CDE packages, and we were able to reproduce all of their bugs: one that causes the Coq proof assistant to produce incorrect output (coq-bug) [2], one thatsegfaultstheGCCcompiler(gcc-bug)[3], andone that makes the LLVM compiler allocate an enormous amount of memory and crash (llvm-bug) [4].",
        "coq-bug [2",
        
    ],
))

DB(Citation(
    guo2011a,
    Site("GCC compiler: Bug 46651", "http://gcc.gnu.org/bugzilla/show_bug.cgi?id=46651"),
    ref="[3]",
    contexts=[
        "Three bug reporters sent us CDE packages, and we were able to reproduce all of their bugs: one that causes the Coq proof assistant to produce incorrect output (coq-bug) [2], one thatsegfaultstheGCCcompiler(gcc-bug)[3], andone that makes the LLVM compiler allocate an enormous amount of memory and crash (llvm-bug) [4].",
        "gcc-bug [3",
        
    ],
))

DB(Citation(
    guo2011a,
    Site("LLVM compiler: Bug 8679", "http://llvm.org/bugs/show_bug.cgi?id=8679"),
    ref="[4]",
    contexts=[
        "Three bug reporters sent us CDE packages, and we were able to reproduce all of their bugs: one that causes the Coq proof assistant to produce incorrect output (coq-bug) [2], one thatsegfaultstheGCCcompiler(gcc-bug)[3], andone that makes the LLVM compiler allocate an enormous amount of memory and crash (llvm-bug) [4].",
        "llvm-bug [4",
        
    ],
))

DB(Citation(
    guo2011a,
    Site("arachniproject home page", "https://github.com/Zapotek/arachni"),
    ref="[5]",
    contexts=[
        "Distributingresearchsoftware: Thecreatorsoftworesearch tools — the arachni web app. security scanner [5] and the graph-tool math library [6]",
        "arachni [5]",
        
    ],
))

DB(Citation(
    guo2011a,
    Site("graph-toolproject home page", "http://projects.skewed.de/graph-tool/"),
    ref="[6]",
    contexts=[
        "Distributingresearchsoftware: Thecreatorsoftworesearch tools — the arachni web app. security scanner [5] and the graph-tool math library [6]",
        "graph-tool [6]",
        
    ],
))

DB(Citation(
    guo2011a,
    Site("VMware ThinApp User’s Guide", "http://www.vmware.com/pdf/thinapp46_manual.pdf"),
    ref="[7]",
    contexts=[
        "Windows applications. However,ausercanonlycreateapackagebyhavingThinAppmonitortheinstallationofnewsoftware[7].",
        
    ],
))

DB(Citation(
    guo2011a, aiken2007a, ref="[8]",
    contexts=[
        "In addition, we used CDE to create portable binary packages for two of our Stanford colleagues’ research tools, which were originally distributed as hard-tocompilesourcecodetarballs: pads[11]andsaturn[8].",
        "saturn [8",
        
    ],
))

DB(Citation(
    guo2011a, alpern2005a, ref="[9]",
    contexts=[
        "PDS is a prototype toolforcreatingself-containedWindowsapps,whichrequirestheusertomanuallyspecifyadependencylist[9].",
        
    ],
))

DB(Citation(
    guo2011a, cadar2008a, ref="[10]",
    contexts=[
        "Similarly,weworkedwithlab-matestouse CDE todeploy the CPU-intensive klee [10] bug ﬁnding tool from the desktop to Amazon’s EC2 cloud computing service without needing to compile Klee on the cloud machines.",
        "klee [10",
        
    ],
))

DB(Citation(
    guo2011a, fisher2005a, ref="[11]",
    contexts=[
        "In addition, we used CDE to create portable binary packages for two of our Stanford colleagues’ research tools, which were originally distributed as hard-tocompilesourcecodetarballs: pads[11]andsaturn[8].",
        "pads [11",
        
    ],
))

DB(Citation(
    guo2011a, guo2011d, ref="[12]",
    contexts=[
        "Due tospaceconstraints, wesummarizeourmain experimental results. Full details are in our tech report [12].",
        
    ],
))

DB(Citation(
    guo2011a, jain2000a, ref="[13]",
    contexts=[
        "Finally, system call interposition using ptrace is a well-knowntechniquethathasbeenusedforimplementing tools such as secure sandboxes [13], record-replay systems [14], and user-level ﬁlesystems [16].",
        
    ],
))

DB(Citation(
    guo2011a, laadan2010a, ref="[14]",
    contexts=[
        "Finally, system call interposition using ptrace is a well-knowntechniquethathasbeenusedforimplementing tools such as secure sandboxes [13], record-replay systems [14], and user-level ﬁlesystems [16].",
        
    ],
))

DB(Citation(
    guo2011a, lahiri2010a, ref="[15]",
    contexts=[
        "Similarly,wehelpeda social networking researcher create a reproducible package for his genetic algorithm paper (gadm) [15]",
        "gadm [15",
        
    ],
))

DB(Citation(
    guo2011a, spillane2007a, ref="[16]",
    contexts=[
        "When a target processﬁrstmakesasyscall,cde-execforcesittomakeanothersyscalltoattacha16KBsharedmemorysegment (atrickfrom[16]).",
        "Finally, system call interposition using ptrace is a well-knowntechniquethathasbeenusedforimplementing tools such as secure sandboxes [13], record-replay systems [14], and user-level ﬁlesystems [16].",
        "Thanks to Fernando Perez for the serendipitous discussion of reproducible research that plantedtheseedsoftheideafor CDE,toRichardSpillane forsharinghisGoannacode[16],toImranHaqueforthe Slashdot publicity, to our users for their bug reports and feedback, and to {ridddlr, paboonst, cbird, TomZ, ewencp, ihaque, daramos}for editorial help",
        
    ],
))

DB(Citation(
    guo2011a, sucan2009a, ref="[17]",
    contexts=[
        "A robotics researcher used CDE to make the experiments for his motion planning paper (kpiece)[17]fully-reproducibe",
        "kpiece [17",
        
    ],
))