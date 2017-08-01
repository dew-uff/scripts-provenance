# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1968 import michie1968a
from ..work.y1979 import feldman1979a
from ..work.y1985 import tichy1985a
from ..work.y1991 import chambers1991a
from ..work.y1992 import gehani1992a
from ..work.y1993 import cypher1993a
from ..work.y1996 import fertig1996a
from ..work.y1998 import staelin1998a
from ..work.y1999 import burnett1999a
from ..work.y1999 import horvitz1999a
from ..work.y1999 import olson1999a
from ..work.y1999 import rekimoto1999a
from ..work.y1999 import santry1999a
from ..work.y2000 import galhardas2000a
from ..work.y2000 import heydon2000a
from ..work.y2000 import jain2000a
from ..work.y2001 import lakshmanan2001a
from ..work.y2001 import miller2001a
from ..work.y2001 import raman2001a
from ..work.y2002 import loper2002a
from ..work.y2003 import johnson2003a
from ..work.y2003 import garfinkel2003a
from ..work.y2003 import sapuntzakis2003a
from ..work.y2004 import collins2004a
from ..work.y2004 import dean2004a
from ..work.y2004 import dolstra2004a
from ..work.y2004 import garfinkel2004a
from ..work.y2004 import rinard2004a
from ..work.y2004 import saff2004a
from ..work.y2005 import alpern2005a
from ..work.y2005 import fisher2005a
from ..work.y2005 import kihlen2005a
from ..work.y2005 import king2005a
from ..work.y2005 import mernik2005a
from ..work.y2005 import pike2005a
from ..work.y2005 import saito2005a
from ..work.y2005 import salcianu2005a
from ..work.y2005 import scaffidi2005a
from ..work.y2006 import chang2006a
from ..work.y2006 import cederqvist2006a
from ..work.y2006 import halevy2006a
from ..work.y2006 import jacovi2006a
from ..work.y2006 import konish2006a
from ..work.y2006 import langtangen2006a
from ..work.y2006 import miller2006b
from ..work.y2006 import ludascher2006a
from ..work.y2006 import muniswamy2006a
from ..work.y2006 import myers2006a
from ..work.y2006 import oinn2006a
from ..work.y2007 import aiken2007a
from ..work.y2007 import carver2007a
from ..work.y2007 import decandia2007a
from ..work.y2007 import dontcheva2007a
from ..work.y2007 import heer2007a
from ..work.y2007 import huynh2007a
from ..work.y2007 import laadan2007a
from ..work.y2007 import maclean2007a
from ..work.y2007 import nethercote2007b
from ..work.y2007 import oliner2007a
from ..work.y2007 import perez2007a
from ..work.y2007 import shah2007a
from ..work.y2007 import spillane2007a
from ..work.y2008 import cadar2008a
from ..work.y2008 import freire2008a
from ..work.y2008 import frew2008a
from ..work.y2008 import leshed2008a
from ..work.y2008 import leskovec2008a
from ..work.y2008 import olston2008a
from ..work.y2008 import scheidegger2008b
from ..work.y2008 import tashma2008a
from ..work.y2008 import tuchinda2008a
from ..work.y2008 import sucan2008a
from ..work.y2009 import acar2009a
from ..work.y2009 import altekar2009a
from ..work.y2009 import bolz2009a
from ..work.y2009 import brandt2009b
from ..work.y2009 import gal2009a
from ..work.y2009 import guo2009a
from ..work.y2009 import gyllstrom2009a
from ..work.y2009 import hammer2009a
from ..work.y2009 import hannay2009a
from ..work.y2009 import heymann2009a
from ..work.y2009 import kelly2009a
from ..work.y2009 import lin2009a
from ..work.y2009 import loeliger2009a
from ..work.y2009 import muniswamy2009a
from ..work.y2009 import muniswamy2009b
from ..work.y2009 import noble2009a
from ..work.y2009 import sullivan2009a
from ..work.y2010 import condie2010a
from ..work.y2010 import guo2010a
from ..work.y2010 import guo2010b
from ..work.y2010 import hartmann2010a
from ..work.y2010 import heimerl2010a
from ..work.y2010 import laadan2010a
from ..work.y2010 import lahiri2010a
from ..work.y2010 import lakshman2010a
from ..work.y2010 import patel2010a
from ..work.y2010 import thusoo2010a
from ..work.y2011 import fisher2011a
from ..work.y2011 import gulwani2011a
from ..work.y2011 import guo2011a
from ..work.y2011 import guo2011b
from ..work.y2011 import guo2011c
from ..work.y2011 import guo2011e
from ..work.y2011 import guo2011f
from ..work.y2011 import guo2011g
from ..work.y2011 import harris2011a
from ..work.y2011 import kandel2011a
from ..work.y2011 import kandel2011b
from ..work.y2011 import prabhu2011a
from ..work.y2011 import strong2011a
from ..work.y2012 import guo2012c
from ..work.y2012 import cheslack2012a
from ..work.y2012 import guo2012a
from ..work.y2012 import kandel2012a
from ..work.y2012 import zimmermann2012a
from ..work.y2013 import hunold2013a
from ..work.y2013 import gent2013a
from ..work.y2014 import shcherbakov2014a
from ..work.y2016 import hill2016a
from ..work.y2017 import kery2017a

DB(Citation(
    guo2012c, Site("Apache Hadoop home page", "http://hadoop.apache.org/"), ref="[1]",
    contexts=[
        "Parallel execution of code can vastly speed up scientiﬁc data processing scripts, at the cost of increased diﬃculty in programming and debugging such scripts. In recent years, libraries such as Parallel Python [17], frameworks such as MapReduce [52] and Hadoop [1], and new high-level languages such as Pig [128] and Hive [151] have made it easier to write parallel code and deploy it to run on compute clusters. However, many researchers interviewed by me and others [133] felt that the learning curve for writing parallel code is still high, especially for scientists without much programming experience. It is much easier for people to think about algorithms sequentially, and even experts prefer to write single-threaded prototypes and then only parallelize later when necessary [144].",
        "Google’s MapReduce [52] and the open-source Hadoop [1] frameworks both have a mode that skips over bad records (i.e., those that incite exceptions) when processing data on compute clusters",
        "There is currently a tension between latency and scalability: Software tools already exist to process data at cluster/cloud scales [1, 52, 128, 151], but they are cumbersome to administer and are not designed to support the sorts of seamless rapid iteration that are vital for research programming.",
    ],
))

DB(Citation(
    guo2012c, Site("AT-SPI", "http://projects.gnome.org/accessibility/"), ref="[2]",
    contexts=[
        "The ﬁnal layer of the Burrito core platform records the user’s interactions with the Linux desktop GUI using the Assistive Technology Service Provider Interface (ATSPI) [2].",
    ],
))

DB(Citation(
    guo2012c, Site("Burrito project home page", "http://www.pgbovine.net/burrito.html"), ref="[3]",
    contexts=[
        "We have installed the entire Burrito platform on Fedora 14 and uploaded a demo virtual machine image online [3].",

    ],
))

DB(Citation(
    guo2012c, Site("CDE public source code repository", "https://github.com/pgbovine/CDE."), ref="[4]",
    contexts=[
        "In this chapter, we present a tool called CDE [4] that makes it easy for people such as research programmers to get their software running on other machines without the hassle of manually creating a robust installer or dealing with user complaints about dependencies.",
        "Since we released the ﬁrst version of CDE on November 9, 2010, it has been downloaded at least 5,000 times as of March 2012 [4].",
    ],
))

DB(Citation(
    guo2012c, Site("Coq proof assistant: Bug 2443,", "http://coq.inria.fr/bugs/show_bug.cgi? id=2443"), ref="[5]",
    contexts=[
        "Incorrect output by Coq proof assistant [5",
        "all of their bugs: one that causes the Coq proof assistant to produce incorrect output (coq-bug-2443) [5], one that segfaults the GCC compiler (gcc-bug-46651) [7], and one that makes the LLVM compiler allocate an enormous amount of memory and crash (llvm-bug-8679) [12].",
    ],
))

DB(Citation(
    guo2012c, Site("Dropbox - Simplify your life,", "http://www.dropbox.com/"), ref="[6]",
    contexts=[
        "Research systems such as Elephant [140] and production systems such as NILFS [101] (part of Linux since June 2009) and Dropbox [6] track changes to all ﬁles and allow users to access old versions via readonly snapshots. Techniques such as causality-based versioning [120] can reduce storage and retrieval overheads by keeping only semantically-meaningful versions",

    ],
))

DB(Citation(
    guo2012c, Site("GCC compiler: Bug 46651,", "http://gcc.gnu.org/bugzilla/show_bug.cgi? id=46651"), ref="[7]",
    contexts=[
        "Causes GCC compiler to segfault [7",
        "all of their bugs: one that causes the Coq proof assistant to produce incorrect output (coq-bug-2443) [5], one that segfaults the GCC compiler (gcc-bug-46651) [7], and one that makes the LLVM compiler allocate an enormous amount of memory and crash (llvm-bug-8679) [12].",
    ],
))

DB(Citation(
    guo2012c, Site("Hashtag", "http://en.wikipedia.org/wiki/Hashtag"), ref="[8]",
    contexts=[
        "Right-clicking on any feed item also surfaces a “Copy event hashtag” menu option, which copies a unique hashtag [8] string identifying this event to the clipboard.",

    ],
))

DB(Citation(
    guo2012c, Site("IncPy home page", "http://www.pgbovine.net/incpy.html"), ref="[9]",
    contexts=[
        "We implemented our technique as a custom open-source Python interpreter called IncPy (Incremental Python) [9].",
        "We implemented our technique as an open-source Python interpreter named IncPy [9].",
    ],
))

DB(Citation(
    guo2012c, Site("JSON data format", "http://www.json.org/"), ref="[10]",
    contexts=[
        "JSON [10] is a concise text-based format capable of expressing key-value associations and nested data (e.g., a key mapping to a list of values, which can themselves be mappings).",

    ],
))

DB(Citation(
    guo2012c, Site("List of software package management systems,", "http://en.wikipedia.org/ wiki/List_of_software_package_management_systems"), ref="[11]",
    contexts=[
        "Software companies devote considerable resources to creating and testing one-click installers for products such as Microsoft Oﬃce, Adobe Photoshop, and Google Chrome. Similarly, open-source developers meticulously specify and update the proper dependencies in order to integrate their software into package management systems [11].",
        "Package management systems are often used to install open-source software and their dependencies. Generic package managers exist for all major operating systems (e.g., RPM for Linux, MacPorts for Mac OS X, Cygwin for Windows), and specialized package managers exist for ecosystems surrounding many programming languages (e.g., CPAN for Perl, RubyGems for Ruby) [11].",
        "Similarly, open-source developers must carefully specify the proper dependencies in order to integrate their software into package management systems [11] (e.g., RPM on Linux, MacPorts on Mac OS X).",
    ],
))

DB(Citation(
    guo2012c, Site("LLVM compiler: Bug 8679,", "http://llvm.org/bugs/show_bug.cgi?id=8679"), ref="[12]",
    contexts=[
        "Runs LLVM compiler out of memory [12",
        "all of their bugs: one that causes the Coq proof assistant to produce incorrect output (coq-bug-2443) [5], one that segfaults the GCC compiler (gcc-bug-46651) [7], and one that makes the LLVM compiler allocate an enormous amount of memory and crash (llvm-bug-8679) [12].",
    ],
))

DB(Citation(
    guo2012c, Site("Mac OS X Bundle Programming Guide: Introduction,", "http://developer.apple.com/library/mac/#documentation/CoreFoundation/Conceptual/ CFBundles/Introduction/Introduction.html"), ref="[13]",
    contexts=[
        "For example, Mac OS X programmers can create application bundles using Apple’s Developer Tools IDE [13]. Research prototypes such as PDS [36], which creates self-contained Windows applications, and The Collective [141], which aggregates a set of software into a portable virtual appliance, also require the user to manually specify dependencies. VMware ThinApp [32] is a commercial tool that automatically creates self-contained portable Windows applications.",

    ],
))

DB(Citation(
    guo2012c, Site("Mathematica notebook technology,", "http://www.wolfram.com/technology/ nb/"), ref="[14]",
    contexts=[
        "For example, integrated development environments for languages such as Mathematica [14] and Python [131] oﬀer a notebook view where executable code and output graphs are displayed alongside the programmer’s textual notes and always kept in sync",

    ],
))

DB(Citation(
    guo2012c, Site("MongoDB", "http://www.mongodb.org/"), ref="[15]",
    contexts=[
        "After data cleaning, reformatting, and integration, programmers might opt to store post-processed data in databases of either the relational (e.g., SQLite, MySQL, PostgreSQL) or NoSQL (e.g., Berkeley DB [127], MongoDB [15]) ﬂavors.",
        "We use MongoDB [15], a popular schema-free document-oriented database, as the master store for Burrito platform data.",
    ],
))

DB(Citation(
    guo2012c, Site("Official Python wiki: Large Python Projects", "http://wiki.python.org/moin/LargePythonProjects"), ref="[16]",
    contexts=[
        "Django is a popular framework for building web applications and is one of the largest Python projects, with 59,111 lines of Python code [16].",

    ],
))

DB(Citation(
    guo2012c, Site("Parallel Python", "http://www.parallelpython.com/"), ref="[17]",
    contexts=[
        "Parallel execution of code can vastly speed up scientiﬁc data processing scripts, at the cost of increased diﬃculty in programming and debugging such scripts. In recent years, libraries such as Parallel Python [17], frameworks such as MapReduce [52] and Hadoop [1], and new high-level languages such as Pig [128] and Hive [151] have made it easier to write parallel code and deploy it to run on compute clusters. However, many researchers interviewed by me and others [133] felt that the learning curve for writing parallel code is still high, especially for scientists without much programming experience. It is much easier for people to think about algorithms sequentially, and even experts prefer to write single-threaded prototypes and then only parallelize later when necessary [144].",

    ],
))

DB(Citation(
    guo2012c, Site("Python home page: PEP 255 --- Simple Generators", "http://www.python.org/ dev/peps/pep-0255/"), ref="[18]",
    contexts=[
        "In addition, I also hacked the interpreter’s handling of iterators and Python generators [18] (generalized form of iterators) to skip over NA objects rather than emitting them during iteration.",

    ],
))

DB(Citation(
    guo2012c, Site("R benchmark 2.5", "http://r.research.att.com/benchmarks/R-benchmark-25.R"), ref="[19]",
    contexts=[
        "We ran a widely-used performance benchmark for the R numerical analysis environment, which exercises matrix and linear algebra operations [19].",

    ],
))

DB(Citation(
    guo2012c, Site("RescueTime", "https://www.rescuetime.com/"), ref="[20]",
    contexts=[
        "Our colleagues also suggested building other Burrito applications such as a personal productivity monitor [20] and a contextual ﬁle search tool [145].",

    ],
))

DB(Citation(
    guo2012c, Site("Saturn online discussion thread", "https://mailman.stanford.edu/pipermail/saturn-discuss/2009-August/000174.html."), ref="[21]",
    contexts=[
        "The team leader of the Saturn [35] static analysis project admitted in a public email, “As it stands the current release likely has problems running on newer systems because of bit rot — some libraries and interfaces have evolved over the past couple of years in ways incompatible with the release” [21].",
        "Even the saturn team leader admitted in a public email, “As it stands the current release likely has problems running on newer systems because of bit rot — some libraries and interfaces have evolved over the past couple of years in ways incompatible with the release” [21]",
        
    ],
))

DB(Citation(
    guo2012c, Site("SlopPy home page", "http://www.pgbovine.net/SlopPy.html"), ref="[22]",
    contexts=[
        "I implemented my technique for Python, since it is a popular language for writing data analyses [133]. I created a prototype open-source interpreter named SlopPy (Sloppy Python) [22] by adding 500 lines of C code to the Python 2.6 interpreter.",

    ],
))

DB(Citation(
    guo2012c, Site("Spec cpu2006 benchmarks,", "http://www.spec.org/cpu2006/"), ref="[23]",
    contexts=[
        "We ﬁrst ran CDE on the entire SPEC CPU2006 benchmark suite (both integer and ﬂoating-point benchmarks) [23]",

    ],
))

DB(Citation(
    guo2012c, Site("SSH Filesystem,", "http://fuse.sourceforge.net/sshfs.html"), ref="[24]",
    contexts=[
        "When a user wants to run some application that is available on a particular distro, they use sshfs (an ssh-based network ﬁlesystem [24]) to mount the root directory of that distro into a special cde-remote-root/ mount point.",

    ],
))

DB(Citation(
    guo2012c, Site("Supercomputer Event Logs", "http://www.cs.sandia.gov/~jrstear/logs/"), ref="[25]",
    contexts=[
        "To show how SlopPy allows programmers to write simple scripts without worrying about error handling, I wrote a script to analyze an event log from the Spirit supercomputer installed in Sandia National Laboratories [25].",
        "Three example records for xinetd sessions in the Spirit supercomputer event log ﬁle [25].",
    ],
))

DB(Citation(
    guo2012c, Site("SystemTap", "http://sourceware.org/systemtap/"), ref="[26]",
    contexts=[
        "We use the SystemTap tool [26] to collect OS-level provenance. SystemTap allows users to write system monitoring scripts in a C-like language, which it then compiles into a kernel module and injects into a live kernel.",

    ],
))

DB(Citation(
    guo2012c, Site("The Phoenix System for MapReduce Programming", "http://mapreduce. stanford.edu/"), ref="[27]",
    contexts=[
        "My script iterates over 71,768 HTML ﬁles that I downloaded from a 1.3GB public corpus [27], parses each using the HTML parser from the Python standard library, ﬁnds all outgoing links, and builds a graph mapping target URLs to source URLs.",

    ],
))

DB(Citation(
    guo2012c, Site("Tutorial: Static, Shared Dynamic and Loadable Linux Libraries,", "http://www. yolinux.com/TUTORIALS/LibraryArchives-StaticAndDynamic.html"), ref="[28]",
    contexts=[
        "Although this basic static technique only ﬁnds libraries named by constant strings8, it represents what people actually do in practice, since it automates the tedious manual process of “chasing down and copying over dependent libraries” that folk wisdom (e.g., blog posts and forums) suggests as the way to transport Linux binaries across machines [28].",

    ],
))

DB(Citation(
    guo2012c, Site("arachni project home page", "https://github.com/Zapotek/arachni."), ref="[29]",
    contexts=[
        "arachni, a Ruby-based tool that audits web application security [29]",
        "Web app. security scanner framework [29",
    ],
))

DB(Citation(
    guo2012c, Site("graph-tool project home page,", "http://projects.skewed.de/graph-tool/"), ref="[30]",
    contexts=[
        "The website for graph-tool, a Python/C++ module for analyzing graphs, lists these (direct) dependencies: “GCC 4.2 or above, Boost libraries, Python 2.5 or above, expat library, NumPy and SciPy Python modules, GCAL C++ geometry library, and Graphviz with Python bindings enabled” [30].",
        "Lib. for manipulation & analysis of graphs [30",
    ],
))

DB(Citation(
    guo2012c, Site("Viterbi algorithm", "http://en.wikipedia.org/wiki/Viterbi_algorithm"), ref="[31]",
    contexts=[
        "runs the Viterbi dynamic programming algorithm [31] on human genomic data and prints out a textual table of results.",

    ],
))

DB(Citation(
    guo2012c, Site("VMware ThinApp Users Guide,", "http://www.vmware.com/pdf/thinapp46_ manual.pdf"), ref="[32]",
    contexts=[
        "For example, Mac OS X programmers can create application bundles using Apple’s Developer Tools IDE [13]. Research prototypes such as PDS [36], which creates self-contained Windows applications, and The Collective [141], which aggregates a set of software into a portable virtual appliance, also require the user to manually specify dependencies. VMware ThinApp [32] is a commercial tool that automatically creates self-contained portable Windows applications.",
    ],
))

DB(Citation(
    guo2012c, Site("Stopping silent errors with exceptions. Perl training Australia, 2005", "http://perltraining.com.au/tips/2005-04-12.html"), ref="[33]",
    contexts=[
        "Silent errors in programming languages: Some programming languages, most notably Perl, are designed to silence errors as much as possible to avoid crashing scripts [33].",

    ],
))

DB(Citation(
    guo2012c, acar2009a, ref="[34]",
    contexts=[
        "Self-adjusting computation [34, 82] is a technique that enables algorithms to run faster in response to small changes in input data, only re-computing outputs for portions of the input that have changed between runs.",
        "Its creator mentions, “Although self-adjusting computation can be applied without having to change existing code by tracking all data and all dependences between code and data, this is prohibitively expensive in practice” [34",
    ],
))

DB(Citation(
    guo2012c, aiken2007a, ref="[35]",
    contexts=[
        "The team leader of the Saturn [35] static analysis project admitted in a public email, “As it stands the current release likely has problems running on newer systems because of bit rot — some libraries and interfaces have evolved over the past couple of years in ways incompatible with the release” [21].",
        "We used CDE to create portable binary packages for two of our Stanford colleagues’ research tools, which were originally distributed as tarballs of source code: pads [59] and saturn [35].",
        "Static program analysis framework [35",
    ],
))

DB(Citation(
    guo2012c, alpern2005a, ref="[36]",
    contexts=[
        "For example, Mac OS X programmers can create application bundles using Apple’s Developer Tools IDE [13]. Research prototypes such as PDS [36], which creates self-contained Windows applications, and The Collective [141], which aggregates a set of software into a portable virtual appliance, also require the user to manually specify dependencies. VMware ThinApp [32] is a commercial tool that automatically creates self-contained portable Windows applications.",
    ],
))

DB(Citation(
    guo2012c, altekar2009a, ref="[37]",
    contexts=[
        "In our experience, the results of many computational science experiments can be reproduced within CDE packages since the programs are output-deterministic [37], always producing the same outputs (e.g., statistics, graphs) for a given input.",
        "Deterministic replay: CDE does not try to replay exact execution paths like record-replay tools [37, 103, 138] do.",
    ],
))

DB(Citation(
    guo2012c, bolz2009a, ref="[38]",
    contexts=[
        "Just-in-time compilers for dynamic languages (e.g., PyPy [38] for Python, TraceMonkey [64] for JavaScript) can speed up script execution times without requiring programmers to make any annotations (or to switch to a compiled language). However, JIT compilers only focus on micro-optimizations of CPU-bound code such as hot inner loops. No JIT compiler optimizations could speed up I/O or networkbound operations, which is what often consumes time in data analysis scripts [107].",

    ],
))

DB(Citation(
    guo2012c, brandt2009b, ref="[39]",
    contexts=[
        "An observational study of software prototyping that I helped to perform [39].",
        "In addition, Brandt et al. found that web search, information foraging, and copying-and-pasting code are prevalent in programming tasks that resemble research programming [39].",
        "The software engineering process prioritizes writing fast-running, robust, and maintainable code, whereas the research programming process prioritizes fast iteration to maximize the rate of discovery [39].",
    ],
))

DB(Citation(
    guo2012c, burnett1999a, ref="[40]",
    contexts=[
        "Computer Science researchers have proposed numerous strategies for simplifying these sorts of programming tasks, including domain-speciﬁc languages [116], visual programming [40], keyword programming [111], and programming-by-demonstration [49].",
    ],
))

DB(Citation(
    guo2012c, cadar2008a, ref="[41]",
    contexts=[
        "One potential area for future work is a mode where the interpreter forks to take both sides of NA-based branches, but then the obvious challenges of exponential path explosion [41] must be addressed.",
        "Automatic bug ﬁnder & test case generator [41",
        "To ensure that he could later re-run and adjust experiments in response to reviewer critiques for a paper submission [41], our group-mate Cristian took the hard drive out of his computer at paper submission time and archived it in his drawer!",
        "Similarly, we worked with lab-mates to use CDE to deploy the CPU-intensive klee [41] bug ﬁnding tool from the desktop to Amazon’s EC2 cloud computing service without needing to compile Klee on the cloud machines.",
        "Use Klee [41] to symbolically execute a C target program (a STUN server) for 100,000 instructions, which generates 21 test cases.",
    ],
))

DB(Citation(
    guo2012c, carver2007a, ref="[42]",
    contexts=[
        "Case studies of programming habits in ﬁve U.S. government research projects [42].",
        "However, anecdotes and empirical studies [42, 133] indicate that a signiﬁcant amount of research programming is still done on desktop machines with data sets that ﬁt on modern hard drives (i.e., less than a terabyte).",
        "During that summer, I wrote all scripts in one language (Python), but my datasets were stored in diverse ﬁle formats (e.g., semi-structured plaintext, CSV, SQL database, serialized objects), which is a typical heterogeneous setup for data analysis workﬂows [42].",
    ],
))

DB(Citation(
    guo2012c, chambers1991a, ref="[43]",
    contexts=[
        "We used an independent twogroup t-test [43] to determine whether each slowdown was statistically signiﬁcant (i.e., whether the means of two sets of runs diﬀered by a non-trivial amount).",
    ],
))

DB(Citation(
    guo2012c, chang2006a, ref="[44]",
    contexts=[
        "In the past decade, technology companies have developed high-performance fault-tolerant key-value stores such as Bigtable [44] at Google, Dynamo [53] at Amazon, and Cassandra [105] at Facebook.",
    ],
))

DB(Citation(
    guo2012c, cheslack2012a, ref="[45]",
    contexts=[
        "A set of scripts that process event logs from a virtual world for a distributed systems paper [45]",
        "Python scripts (boxes) and data ﬁles (circles) from Ewen’s event log analysis workﬂow [45].",
        "Refactored version of Ewen’s event log analysis workﬂow [45], containing only functions (boxes) and input data ﬁles (circles)",
        "by our colleague Ewen to process event logs from a virtual world system [45].",
        
    ],
))

DB(Citation(
    guo2012c, collins2004a, ref="[46]",
    contexts=[
        "The modern line of version control systems started with RCS [152] in the 1980’s, followed by CVS [56] and Subversion (SVN) [46].",

    ],
))

DB(Citation(
    guo2012c, condie2010a, ref="[47]",
    contexts=[
        "For instance, Condie et al. found the top 10 most frequently occurring words in a 5.5GB corpus of Wikipedia article text after only processing about half of the dataset [47].",
    ],
))

DB(Citation(
    guo2012c, condie2010a, ref="[48]",
    contexts=[
        "Similar problems have been studied in detail in systems such as MapReduce Online [48], and, more generally, aggregation, sampling,",

    ],
))

DB(Citation(
    guo2012c, cypher1993a, ref="[49]",
    contexts=[
        "Computer Science researchers have proposed numerous strategies for simplifying these sorts of programming tasks, including domain-speciﬁc languages [116], visual programming [40], keyword programming [111], and programming-by-demonstration [49].",
        "Computer Science researchers have proposed numerous strategies for simplifying these sorts of programming tasks, including domain-speciﬁc languages [116], visual programming [40], keyword programming [111], and programming-by-demonstration [49].",
        "Another class of targeted data manipulation tools rely on programming by demonstration (PBD) techniques [49]. Potluck [92] uses interactive simultaneous text editing features [118] to help users perform data integration. Karma [153] infers text extractors and transformations for web data from examples entered in a table. Vegemite [110] extends CoScripter [108] to integrate web data, automate the use of web services, and generate shareable scripts. Dontcheva et al. [55] use PBD techniques to enable extraction, integration, and templated search of web data. Gulwani [69] introduces an algorithm for learning expressive string processing programs from input-output examples. PADS [60] infers nuanced data parsers from a set of positive examples.",
    ],
))

DB(Citation(
    guo2012c, johnson2003a, ref="[50]",
    contexts=[
        "A tangentially-related quantitative estimate is that data reformatting and cleaning accounts for up to 80% of the development time and cost in data warehousing projects [50].",

    ],
))

DB(Citation(
    guo2012c, johnson2003a, ref="[51]",
    contexts=[
        "Both prior work [51] and our own conversations with analysts indicate that wrangling is one of the most time-consuming aspects of analysis.",

    ],
))

DB(Citation(
    guo2012c, dean2004a, ref="[52]",
    contexts=[
        "Parallel execution of code can vastly speed up scientiﬁc data processing scripts, at the cost of increased diﬃculty in programming and debugging such scripts. In recent years, libraries such as Parallel Python [17], frameworks such as MapReduce [52] and Hadoop [1], and new high-level languages such as Pig [128] and Hive [151] have made it easier to write parallel code and deploy it to run on compute clusters. However, many researchers interviewed by me and others [133] felt that the learning curve for writing parallel code is still high, especially for scientists without much programming experience. It is much easier for people to think about algorithms sequentially, and even experts prefer to write single-threaded prototypes and then only parallelize later when necessary [144].",
        "Google’s MapReduce [52] and the open-source Hadoop [1] frameworks both have a mode that skips over bad records (i.e., those that incite exceptions) when processing data on compute clusters",
        "Also, frameworks such as MapReduce [52] can automatically skip over bad records.",
        "A reverse web-link graph associates each HTML webpage with a set of webpages that link to it. A search engine can use this graph to compute reputation metrics like PageRank. I took this example from the MapReduce paper [52].",
        "There is currently a tension between latency and scalability: Software tools already exist to process data at cluster/cloud scales [1, 52, 128, 151], but they are cumbersome to administer and are not designed to support the sorts of seamless rapid iteration that are vital for research programming.",
    ],
))

DB(Citation(
    guo2012c, decandia2007a, ref="[53]",
    contexts=[
        "In the past decade, technology companies have developed high-performance fault-tolerant key-value stores such as Bigtable [44] at Google, Dynamo [53] at Amazon, and Cassandra [105] at Facebook.",

    ],
))

DB(Citation(
    guo2012c, dolstra2004a, ref="[54]",
    contexts=[
        "From the user’s perspective, package managers work great as long as the exact desired versions of software exist within the system. However, version mismatches and conﬂicts are common frustrations, and installing new software can lead to a library upgrade that breaks existing software [54].",
        "The Nix package manager is a research project that tries to eliminate dependency conﬂicts via stricter versioning, but it still requires package creators to manually specify dependencies at creation time [54].",
    ],
))

DB(Citation(
    guo2012c, dontcheva2007a, ref="[55]",
    contexts=[
        "Another class of targeted data manipulation tools rely on programming by demonstration (PBD) techniques [49]. Potluck [92] uses interactive simultaneous text editing features [118] to help users perform data integration. Karma [153] infers text extractors and transformations for web data from examples entered in a table. Vegemite [110] extends CoScripter [108] to integrate web data, automate the use of web services, and generate shareable scripts. Dontcheva et al. [55] use PBD techniques to enable extraction, integration, and templated search of web data. Gulwani [69] introduces an algorithm for learning expressive string processing programs from input-output examples. PADS [60] infers nuanced data parsers from a set of positive examples.",

    ],
))

DB(Citation(
    guo2012c, cederqvist2006a, ref="[56]",
    contexts=[
        "The modern line of version control systems started with RCS [152] in the 1980’s, followed by CVS [56] and Subversion (SVN) [46].",

    ],
))

DB(Citation(
    guo2012c, feldman1979a, ref="[57]",
    contexts=[
        "“make” is a ubiquitous UNIX tool that allows users to declaratively specify dependencies between commands and ﬁles, so that the minimum set of commands need to be re-run when dependent ﬁles are altered [57].",
        "One possible solution would be to write all of my code and dataset dependencies in a Makeﬁle [57], so that invoking make would only re-run the scripts whose dependent datasets have changed.",
    ],
))

DB(Citation(
    guo2012c, fertig1996a, ref="[58]",
    contexts=[
        "A more radical approach is to get rid of traditional ﬁlenames and directory hierarchies altogether. Research prototypes such as Lifestreams [58] and Time-Machine Computing [135] are GUI desktop environments where the user’s ﬁles are organized in a chronological versioned stream rather than in directories, thus eliminating the need to provide ﬁlenames and directory names.",

    ],
))

DB(Citation(
    guo2012c, fisher2005a, ref="[59]",
    contexts=[
        "Vast amounts of real-world data are stored in ad-hoc formats [59]",
        "Examples of such semi-structured and unstructured data are those scraped from web pages, mined from emails, and logs produced by computer systems and scientiﬁc lab equipment. Ad-hoc data often contains inconsistencies and errors due to lack of well-deﬁned schemas, malfunctioning equipment corrupting logs, non-standard values to indicate missing data, or human errors in data entry [59]",
        "Although domain-speciﬁc data processing languages are being developed in research labs [59, 128, 132], most modern programmers write ad-hoc data processing scripts in general-purpose languages such as Python, Perl, and Ruby due to their ﬂexibility, support for rapid prototyping, and active ecosystems of open-source libraries.",
        "Also, ad-hoc data sources often contain badly-formatted “unclean” records that cause an otherwisecorrect script to fail [59]",
        "We used CDE to create portable binary packages for two of our Stanford colleagues’ research tools, which were originally distributed as tarballs of source code: pads [59] and saturn [35].",
        "Language for processing ad-hoc data [59",
        "Compile a PADS [59] speciﬁcation into C code (the ‘pads (compiler)’ row in Table 8.5), and then infer a speciﬁcation from a data ﬁle (the ‘pads (inferencer)’ row in Table 8.5).",
    ],
))

DB(Citation(
    guo2012c, fisher2011a, ref="[60]",
    contexts=[
        "Another class of targeted data manipulation tools rely on programming by demonstration (PBD) techniques [49]. Potluck [92] uses interactive simultaneous text editing features [118] to help users perform data integration. Karma [153] infers text extractors and transformations for web data from examples entered in a table. Vegemite [110] extends CoScripter [108] to integrate web data, automate the use of web services, and generate shareable scripts. Dontcheva et al. [55] use PBD techniques to enable extraction, integration, and templated search of web data. Gulwani [69] introduces an algorithm for learning expressive string processing programs from input-output examples. PADS [60] infers nuanced data parsers from a set of positive examples.",

    ],
))

DB(Citation(
    guo2012c, freire2008a, ref="[61]",
    contexts=[
        "Laboratory notebooks have been the traditional mechanism for maintaining such information, but because the volume of data manipulated in computational experiments has increased along with the complexity of analysis, manually capturing provenance and writing detailed notes is no longer an option — in fact, it can have serious limitations. [61]",

    ],
))

DB(Citation(
    guo2012c, frew2008a, ref="[62]",
    contexts=[
        "PASS [119, 121] collects such provenance by tracking Linux system calls within a modiﬁed kernel and ﬁlesystem, while ES3 [62] uses the Linux ptrace mechanism to accomplish a similar goal.",

    ],
))

DB(Citation(
    guo2012c, Site("Iddo Friedberg. Email: Skipping a bad record read in SeqIO --- Biopython dev. mailing list, 2009", "http://portal.open-bio.org/pipermail/biopython-dev/2009-June/006189.html."), ref="[63]",
    contexts=[
        "The alternative would be — well, and [sic] ugly hack, which will cause loss of time and research momentum. [63]",

    ],
))

DB(Citation(
    guo2012c, gal2009a, ref="[64]",
    contexts=[
        "Just-in-time compilers for dynamic languages (e.g., PyPy [38] for Python, TraceMonkey [64] for JavaScript) can speed up script execution times without requiring programmers to make any annotations (or to switch to a compiled language). However, JIT compilers only focus on micro-optimizations of CPU-bound code such as hot inner loops. No JIT compiler optimizations could speed up I/O or networkbound operations, which is what often consumes time in data analysis scripts [107].",

    ],
))

DB(Citation(
    guo2012c, galhardas2000a, ref="[65]",
    contexts=[
        "Both database and HCI researchers have devised graphical interfaces [65, 91, 134] for cleaning and reformatting data",
        "Ajax [65] similarly provides an interface for transform speciﬁcation with advanced facilities for entity resolution.",
    ],
))

DB(Citation(
    guo2012c, garfinkel2003a, ref="[66]",
    contexts=[
        "Although CDE isolates target programs in a chroot-like sandbox, it does not guard against attacks to circumvent such sandboxes [66].",

    ],
))

DB(Citation(
    guo2012c, garfinkel2004a, ref="[67]",
    contexts=[
        "System call interposition using ptrace is a wellknown technique that researchers have used for implementing tools such as secure sandboxes [67, 94], record-replay systems [103], and user-level ﬁlesystems [146].",
    ],
))

DB(Citation(
    guo2012c, gehani1992a, ref="[68]",
    contexts=[
        "A study found that 50–70% of the code in reliable systems software was for handling edge cases [68];",

    ],
))

DB(Citation(
    guo2012c, gulwani2011a, ref="[69]",
    contexts=[
        "Another class of targeted data manipulation tools rely on programming by demonstration (PBD) techniques [49]. Potluck [92] uses interactive simultaneous text editing features [118] to help users perform data integration. Karma [153] infers text extractors and transformations for web data from examples entered in a table. Vegemite [110] extends CoScripter [108] to integrate web data, automate the use of web services, and generate shareable scripts. Dontcheva et al. [55] use PBD techniques to enable extraction, integration, and templated search of web data. Gulwani [69] introduces an algorithm for learning expressive string processing programs from input-output examples. PADS [60] infers nuanced data parsers from a set of positive examples.",
        "Wrangler uses programming-by-demonstration methods (c.f., [69, 118]) to specify regular expression patterns and row predicates.",
    ],
))

DB(Citation(
    guo2012c, guo2011c, ref="[70]",
    contexts=[
        "Chapter 8 presents an automatic software packaging tool called CDE [70, 74], which helps researchers easily deploy, archive, and share their experiments. CDE eliminates the problems of “dependency hell” for a large class of Linuxbased software that research programmers are likely to create and use.",
        "Its contents were adapted from a 2011 conference paper that I co-authored with Dawson Engler [74] and a follow-up paper that describes several new features [70].",
    ],
))

DB(Citation(
    guo2012c, guo2011e, ref="[71]",
    contexts=[
        "Chapter 6 presents a Python interpreter called SlopPy [71], which automatically makes existing scripts error-tolerant, thereby speeding up the data analysis scripting cycle. SlopPy supports fail-soft semantics, tracking provenance of code and data errors, and incremental re-processing of error-inducing records.",
        "This chapter presents an enhanced Python interpreter called SlopPy, which automatically makes existing scripts error-tolerant, thereby speeding up the data analysis scripting cycle. Its contents were adapted from a 2011 workshop paper [71]",
    ],
))

DB(Citation(
    guo2012c, guo2009a, ref="[72]",
    contexts=[
        "My own research programming experiences when working on empirical software engineering papers earlier in graduate school (2007–2010) [72, 78, 79, 156].",
        "A script we wrote in 2007–2008 to mine data about the Linux kernel project’s revision control history for an empirical software engineering paper [72].",
        "To show how IncPy enables faster iteration when exploring alternative hypotheses in a data analysis task, we studied a Python script we wrote in 2007–2008 to mine Linux data for a paper [72].",
    ],
))

DB(Citation(
    guo2012c, guo2010a, ref="[73]",
    contexts=[
        "Its contents were adapted from a 2011 conference paper that I coauthored with Dawson Engler [75], which is an extended version of a 2010 workshop paper [73].",

    ],
))

DB(Citation(
    guo2012c, guo2011a, ref="[74]",
    contexts=[
        "Chapter 8 presents an automatic software packaging tool called CDE [70, 74], which helps researchers easily deploy, archive, and share their experiments. CDE eliminates the problems of “dependency hell” for a large class of Linuxbased software that research programmers are likely to create and use.",
        "Its contents were adapted from a 2011 conference paper that I co-authored with Dawson Engler [74] and a follow-up paper that describes several new features [70].",
    ],
))

DB(Citation(
    guo2012c, guo2011b, ref="[75]",
    contexts=[
        "Chapter 5 presents a Python interpreter called IncPy [75], which speeds up the data analysis scripting cycle and helps researchers manage code and data dependencies. To the best of my knowledge, IncPy is the ﬁrst attempt to integrate automatic memoization and persistent dependency management into a general-purpose programming language",
        "Its contents were adapted from a 2011 conference paper that I coauthored with Dawson Engler [75], which is an extended version of a 2010 workshop paper [73].",
    ],
))

DB(Citation(
    guo2012c, guo2011f, ref="[76]",
    contexts=[
        "Chapter 4 presents an interactive graphical tool called Proactive Wrangler [76], which provides semi-automated suggestions to assist research programmers in reformatting and cleaning data prior to analysis.",
        "Research programmers typically perform data cleaning, reformatting, and integration by writing scripts or by manually editing the data within spreadsheets [76]",
        "This chapter presents a web-based interactive graphical tool called Proactive Wrangler, which helps research programmers reformat and clean data prior to analysis. Its contents were adapted from a 2011 conference paper that I co-authored with Sean Kandel, Joseph Hellerstein, and Jeﬀrey Heer [76].",

    ],
))

DB(Citation(
    guo2012c, guo2012a, ref="[77]",
    contexts=[
        "Chapter 7 presents a Linux-based activity monitoring and in-context notetaking system called Burrito [77], which helps research programmers organize, annotate, and recall past insights about their experiments.",
        "Its contents were adapted from a 2012 workshop paper that I co-authored with Margo Seltzer [77].",
    ],
))

DB(Citation(
    guo2012c, guo2010b, ref="[78]",
    contexts=[
        "My own research programming experiences when working on empirical software engineering papers earlier in graduate school (2007–2010) [72, 78, 79, 156].",
        "For example, during a summer internship at Microsoft Research working on a data-driven study of what factors cause software bugs to be ﬁxed [78], I had daily meetings with my supervisor",
        "A data analysis workﬂow from my Summer 2009 internship project [78] comprised of Python scripts (boxes) that process and generate data ﬁles (circles).",
        "This project was later published as three conference papers [78, 79, 156].",
    ],
))

DB(Citation(
    guo2012c, guo2011g, ref="[79]",
    contexts=[
        "My own research programming experiences when working on empirical software engineering papers earlier in graduate school (2007–2010) [72, 78, 79, 156].",
        "This project was later published as three conference papers [78, 79, 156].",
    ],
))

DB(Citation(
    guo2012c, gyllstrom2009a, ref="[80]",
    contexts=[
        "The design of the Activity Context Viewer was directly inspired by a research prototype called Passages [80], which logs all textual documents read and written by the user and enables contextual searches such as, “Which papers and web pages did I read when writing the ‘related work’ section of this paper?”",

    ],
))

DB(Citation(
    guo2012c, halevy2006a, ref="[81]",
    contexts=[
        "Myers et al. [122] provide a survey of end-user programming; Halevy, Rajaraman, and Ordille provide a survey of data integration techniques [81]; Kandel et al. provide a survey of issues related to data quality and uncertainty, and demonstrate how interactive visualizations can aid in the data cleaning process [95].",

    ],
))

DB(Citation(
    guo2012c, hammer2009a, ref="[82]",
    contexts=[
        "Self-adjusting computation [34, 82] is a technique that enables algorithms to run faster in response to small changes in input data, only re-computing outputs for portions of the input that have changed between runs.",
        "Even with annotations, there is at least a 500% slowdown on the initial (empty cache) run [82]",
    ],
))

DB(Citation(
    guo2012c, hannay2009a, ref="[83]",
    contexts=[
        "Surveys at universities indicate that people across dozens of departments ranging from the natural sciences (e.g., astrophysics, geosciences, molecular biology), engineering (e.g., aerospace and mechanical engineering, operations research), and social sciences (e.g., economics, political science, sociology) engage in research programming as part of their daily work [83, 133].",
        "An online survey of computational scientists with 1,972 usable responses from 40 countries [83].",
        "While version control is widely used by professional software engineers, adoption amongst research programmers has been limited by a variety of reasons [83]:",
    ],
))

DB(Citation(
    guo2012c, harris2011a, ref="[84]",
    contexts=[
        "Harris and Gulwani created a system for learning table transformations from an example input-output pair [84].",

    ],
))

DB(Citation(
    guo2012c, hartmann2010a, ref="[85]",
    contexts=[
        "d.note [85] is a visual programming tool where UI designers can tightly integrate annotations, automatic versioning, and visual comparison of alternatives when prototyping mobile device GUI applications.",

    ],
))

DB(Citation(
    guo2012c, heer2007a, ref="[86]",
    contexts=[
        "Lastly, researchers often collaborate with colleagues by sending them partial results to receive feedback and fresh ideas. A variety of logistical and communication challenges arise in research collaborations centered on code and data sharing [86].",
        "For instance, there is a rich body of prior work related to collaborating on data analysis and visualization, embodied by systems such as sense.us [86]",
        
    ],
))

DB(Citation(
    guo2012c, heimerl2010a, ref="[87]",
    contexts=[
        "A script that post-processes and graphs synchronized mouse input events for an HCI paper [87].",

    ],
))

DB(Citation(
    guo2012c, heydon2000a, ref="[88]",
    contexts=[
        "Vesta [88] is a software conﬁguration management system that provides a pure functional domain-speciﬁc language for writing software build scripts. The Vesta interpreter performs automatic memoization and dependency tracking. However, since it is a domain-speciﬁc build scripting language, it has never been used for research programming tasks, to the best of my knowledge.",
    ],
))

DB(Citation(
    guo2012c, heymann2009a, ref="[89]",
    contexts=[
        "A set of information retrieval scripts for a paper contrasting crowdsourced tags with expert annotations for keywords describing books [89].",
        "To show how we can remove manually-written caching code and maintain comparable performance, we studied information retrieval scripts written by our colleague Paul [89]",
    ],
))

DB(Citation(
    guo2012c, horvitz1999a, ref="[90]",
    contexts=[
        "We take a mixed-initiative [90] approach to addressing this aspect of research programming by generating proactive suggestions to improve the suitability of a data set for downstream tools.",
        "While speculative, this observation suggests that future research might examine not only the utility of suggestions to the stated task goal [90], but also how interface design and turn-taking aﬀects user receptiveness to those suggestions",
        "The ﬁve tools I have presented in this dissertation are examples of design along this spectrum of mixed-initiative interfaces [90].",
    ],
))

DB(Citation(
    guo2012c, Site("David Huynh and Stefano Mazzocchi. Google Refine", "http://code.google.com/p/google-refine/"), ref="[91]",
    contexts=[
        "Both database and HCI researchers have devised graphical interfaces [65, 91, 134] for cleaning and reformatting data",
        "Google Reﬁne [91] combines menu-driven commands with faceted histograms for data proﬁling and ﬁltering.",
        "To assist this process, researchers have developed novel interactive tools. Potter’s Wheel [134] and Google Reﬁne [91] are menu-driven interfaces that provide access to common data transforms. Wrangler [96] extends this approach by (a) automatically suggesting applicable transforms in response to direct manipulation of a data table and (b) providing visual previews to aid transform assessment.",
        "Similar to other transformation tools [91, 134], a transform can be speciﬁed manually by selecting a transform type from the tool bar and then entering in desired parameter values.",
    ],
))

DB(Citation(
    guo2012c, huynh2007a, ref="[92]",
    contexts=[
        "Another class of targeted data manipulation tools rely on programming by demonstration (PBD) techniques [49]. Potluck [92] uses interactive simultaneous text editing features [118] to help users perform data integration. Karma [153] infers text extractors and transformations for web data from examples entered in a table. Vegemite [110] extends CoScripter [108] to integrate web data, automate the use of web services, and generate shareable scripts. Dontcheva et al. [55] use PBD techniques to enable extraction, integration, and templated search of web data. Gulwani [69] introduces an algorithm for learning expressive string processing programs from input-output examples. PADS [60] infers nuanced data parsers from a set of positive examples.",
    ],
))

DB(Citation(
    guo2012c, jacovi2006a, ref="[93]",
    contexts=[
        "Combining knowledge of the research programming workﬂow with the rich literature on Computer Supported Cooperative Work [93] could lead to novel research collaboration tools.",
    ],
))

DB(Citation(
    guo2012c, jain2000a, ref="[94]",
    contexts=[
        "System call interposition using ptrace is a wellknown technique that researchers have used for implementing tools such as secure sandboxes [67, 94], record-replay systems [103], and user-level ﬁlesystems [146].",

    ],
))

DB(Citation(
    guo2012c, kandel2011a, ref="[95]",
    contexts=[
        "Myers et al. [122] provide a survey of end-user programming; Halevy, Rajaraman, and Ordille provide a survey of data integration techniques [81]; Kandel et al. provide a survey of issues related to data quality and uncertainty, and demonstrate how interactive visualizations can aid in the data cleaning process [95].",
    ],
))

DB(Citation(
    guo2012c, kandel2011b, ref="[96]",
    contexts=[
        "To assist this process, researchers have developed novel interactive tools. Potter’s Wheel [134] and Google Reﬁne [91] are menu-driven interfaces that provide access to common data transforms. Wrangler [96] extends this approach by (a) automatically suggesting applicable transforms in response to direct manipulation of a data table and (b) providing visual previews to aid transform assessment.",
        "We augmented the Wrangler transformation tool [96] to aid transform discovery and strategy formation, thereby creating a tool called Proactive Wrangler.",
        "In this work, we extend an existing research prototype called Wrangler [96], which combines multiple end-user programming strategies to facilitate speciﬁcation of data transformation scripts",
        "Example parameters include regular expressions matching selected text substrings and row predicates matching selected values, generated using programming-by demonstration methods [96, 118].",
        "For more details regarding the Wrangler inference engine, we refer interested readers to Kandel et al. [96].",
        "When creating data transformation scripts, users often ﬁnd it diﬃcult to understand a transform’s eﬀect prior to executing it [96].",
        "However, observing user activity with Wrangler via both a formal user study and informal anecdotes revealed that analysts have diﬃculty formulating data cleaning strategies [96]",
        "Wrangler parses each cell’s contents into the most speciﬁc possible type, which can be a built-in such as number or date, a user-deﬁned type such as zip code or country name, or a generic string type for those that fail to match a more speciﬁc type (for more details regarding Wrangler’s type inference, see Kandel et al. [96]).",
    ],
))

DB(Citation(
    guo2012c, kandel2012a, ref="[97]",
    contexts=[
        "However, the chore of data reformatting and cleaning can lend insights into what assumptions are safe to make about the data, what idiosyncrasies exist in the collection process, and what models and analyses are appropriate to apply [97].",
    ],
))

DB(Citation(
    guo2012c, kelly2009a, ref="[98]",
    contexts=[
        "A literature search revealed that even veteran computational scientists acknowledged that having to organize code, data, and their dependencies was an impediment to productivity [98, 124].",
        "The “state-of-the-art” solution that veteran data analysts suggest is to simply use disciplined ﬁle naming conventions and Makeﬁles as the “best practices” for coping with these dependencies [98, 124].",
        "Some data analysis workﬂows consist of separate programs that coordinate with one another using intermediate data ﬁles [98, 124].",
    ],
))

DB(Citation(
    guo2012c, kihlen2005a, ref="[99]",
    contexts=[
        "Some scientiﬁc research organizations purchase or custom-build electronic lab notebook (ELN) software [99].",

    ],
))

DB(Citation(
    guo2012c, king2005a, ref="[100]",
    contexts=[
        "DejaView [102] augments Linux with a virtual display driver and virtual execution environment to eﬃciently capture a rich history of user activity and enable execution to restore to any time in the past. Others have augmented virtual machines with ﬁne-grained checkpoints to enable a similar form of “time travel” [100, 150].",
    ],
))

DB(Citation(
    guo2012c, konish2006a, ref="[101]",
    contexts=[
        "Research systems such as Elephant [140] and production systems such as NILFS [101] (part of Linux since June 2009) and Dropbox [6] track changes to all ﬁles and allow users to access old versions via readonly snapshots. Techniques such as causality-based versioning [120] can reduce storage and retrieval overheads by keeping only semantically-meaningful versions",
        "The base layer of the Burrito core platform is NILFS, a log-structured ﬁlesystem that performs continuous snapshotting of every ﬁle write [101].",
    ],
))

DB(Citation(
    guo2012c, laadan2007a, ref="[102]",
    contexts=[
        "DejaView [102] augments Linux with a virtual display driver and virtual execution environment to eﬃciently capture a rich history of user activity and enable execution to restore to any time in the past. Others have augmented virtual machines with ﬁne-grained checkpoints to enable a similar form of “time travel” [100, 150].",

    ],
))

DB(Citation(
    guo2012c, laadan2010a, ref="[103]",
    contexts=[
        "System call interposition using ptrace is a wellknown technique that researchers have used for implementing tools such as secure sandboxes [67, 94], record-replay systems [103], and user-level ﬁlesystems [146].",
        "Deterministic replay: CDE does not try to replay exact execution paths like record-replay tools [37, 103, 138] do.",
    ],
))

DB(Citation(
    guo2012c, lahiri2010a, ref="[104]",
    contexts=[
        "Genetic algorithm for social networks [104",
        "A robotics researcher used CDE to make the experiments for his motion planning paper (kpiece) [149] fully reproducible. Similarly, we helped a social networking researcher create a reproducible package for his genetic algorithm paper (gadm) [104].",
        "Reproduce the GADM experiment [104]: Compile its C++ source code (‘C++ comp’), run genetic algorithm (‘algorithm’), and use the R statistics software to visualize output data (‘make plots’).",
    ],
))

DB(Citation(
    guo2012c, lakshman2010a, ref="[105]",
    contexts=[
        "In the past decade, technology companies have developed high-performance fault-tolerant key-value stores such as Bigtable [44] at Google, Dynamo [53] at Amazon, and Cassandra [105] at Facebook.",

    ],
))

DB(Citation(
    guo2012c, lakshmanan2001a, ref="[106]",
    contexts=[
        "The language is the direct descendant of the Potter’s Wheel language [134] and draws on concepts introduced in SchemaSQL [106]",
        "This prior work [106, 134] also provides formal proofs of the language’s expressiveness, showing it is capable of expressing any one-to-one or one-to-many transform of cell values.",
    ],
))

DB(Citation(
    guo2012c, langtangen2006a, ref="[107]",
    contexts=[
        "In closing, the following excerpt from the introduction of the book Python Scripting for Computational Science [107] summarizes the extent of data preparation chores",
        "Such tasks are much faster to accomplish in a language like Python than in Fortran, C, C++, C#, or Java. [107]",
        "In this dissertation, I will refer to these kinds of programs as data analysis scripts, since research programmers often prefer to use interpreted “scripting” languages such as Python, Perl, R, and MATLAB [107, 133]",
        "Just-in-time compilers for dynamic languages (e.g., PyPy [38] for Python, TraceMonkey [64] for JavaScript) can speed up script execution times without requiring programmers to make any annotations (or to switch to a compiled language). However, JIT compilers only focus on micro-optimizations of CPU-bound code such as hot inner loops. No JIT compiler optimizations could speed up I/O or networkbound operations, which is what often consumes time in data analysis scripts [107].",
    ],
))

DB(Citation(
    guo2012c, leshed2008a, ref="[108]",
    contexts=[
        "Another class of targeted data manipulation tools rely on programming by demonstration (PBD) techniques [49]. Potluck [92] uses interactive simultaneous text editing features [118] to help users perform data integration. Karma [153] infers text extractors and transformations for web data from examples entered in a table. Vegemite [110] extends CoScripter [108] to integrate web data, automate the use of web services, and generate shareable scripts. Dontcheva et al. [55] use PBD techniques to enable extraction, integration, and templated search of web data. Gulwani [69] introduces an algorithm for learning expressive string processing programs from input-output examples. PADS [60] infers nuanced data parsers from a set of positive examples.",
    ],
))

DB(Citation(
    guo2012c, leskovec2008a, ref="[109]",
    contexts=[
        "The main problem that programmers face in data acquisition is keeping track of provenance, i.e., where each piece of data comes from and whether it is still up-todate [119].",
        "Image from Leskovec’s Ph.D. dissertation [109] showing four variants of a social network model (one in each column) tested on four data sets (one in each row).",
        "Figure 2.3 shows an example set of graphs from social network analysis research, where four variants of a model algorithm are tested on four diﬀerent input data sets. This example is the ﬁnal result from a published paper and Ph.D. dissertation [109];",
    ],
))

DB(Citation(
    guo2012c, lin2009a, ref="[110]",
    contexts=[
        "Another class of targeted data manipulation tools rely on programming by demonstration (PBD) techniques [49]. Potluck [92] uses interactive simultaneous text editing features [118] to help users perform data integration. Karma [153] infers text extractors and transformations for web data from examples entered in a table. Vegemite [110] extends CoScripter [108] to integrate web data, automate the use of web services, and generate shareable scripts. Dontcheva et al. [55] use PBD techniques to enable extraction, integration, and templated search of web data. Gulwani [69] introduces an algorithm for learning expressive string processing programs from input-output examples. PADS [60] infers nuanced data parsers from a set of positive examples.",
        
    ],
))

DB(Citation(
    guo2012c, miller2006b, ref="[111]",
    contexts=[
        "Computer Science researchers have proposed numerous strategies for simplifying these sorts of programming tasks, including domain-speciﬁc languages [116], visual programming [40], keyword programming [111], and programming-by-demonstration [49].",

    ],
))

DB(Citation(
    guo2012c, loeliger2009a, ref="[112]",
    contexts=[
        "In the past decade, decentralized version control systems such as Git [112] and Mercurial [129] have become more popular, especially in open-source software projects where developers work in multiple geographic locations.",
        "One ideal vision is to aspire to do for research programming what Google Docs has done for collaborative text editing or what Git [112] has done for team software engineering.",
    ],
))

DB(Citation(
    guo2012c, loper2002a, ref="[113]",
    contexts=[
        "ahul, a Stanford grad student, was using NLTK [113], a Python module for natural language processing, to build a semantic email search engine (email-search) for a machine learning class.",

    ],
))

DB(Citation(
    guo2012c, ludascher2006a, ref="[114]",
    contexts=[
        "Scientiﬁc workﬂow systems such as Kepler [114], Taverna [125], and VisTrails [143] are graphical development environments for designing and executing scientiﬁc computations.",

    ],
))

DB(Citation(
    guo2012c, maclean2007a, ref="[115]",
    contexts=[
        "MacLean’s shadowing of computational scientists at Harvard [115].",
        "The scientists rely heavily on graphs — they graph the output and distributions of their tests, they graph the sequenced genomes next to other, existing sequences. [115]",
        "In contrast, research programmers often work in a heterogeneous environment where they cobble together a patchwork of improvised ad-hoc scripts and “sloppy” prototype code written in multiple languages, interfacing with a mix of 3rd-party libraries and executables from disparate sources within a UNIX-like command-line environment [115, 133]",
        
    ],
))

DB(Citation(
    guo2012c, mernik2005a, ref="[116]",
    contexts=[
        "Computer Science researchers have proposed numerous strategies for simplifying these sorts of programming tasks, including domain-speciﬁc languages [116], visual programming [40], keyword programming [111], and programming-by-demonstration [49].",
    ],
))

DB(Citation(
    guo2012c, michie1968a, ref="[117]",
    contexts=[
        "Memoization is a classic optimization technique ﬁrst introduced in a 1968 Nature paper [117].",
        "The interpreter automatically memoizes [117] (caches) the inputs, outputs, and dependencies of certain function calls to disk, only doing so when it is safe (pure and deterministic call) and worthwhile (faster to re-use cached results than to re-run) to do the memoization.",
    ],
))

DB(Citation(
    guo2012c, miller2001a, ref="[118]",
    contexts=[
        "Another class of targeted data manipulation tools rely on programming by demonstration (PBD) techniques [49]. Potluck [92] uses interactive simultaneous text editing features [118] to help users perform data integration. Karma [153] infers text extractors and transformations for web data from examples entered in a table. Vegemite [110] extends CoScripter [108] to integrate web data, automate the use of web services, and generate shareable scripts. Dontcheva et al. [55] use PBD techniques to enable extraction, integration, and templated search of web data. Gulwani [69] introduces an algorithm for learning expressive string processing programs from input-output examples. PADS [60] infers nuanced data parsers from a set of positive examples.",
        "Wrangler uses programming-by-demonstration methods (c.f., [69, 118]) to specify regular expression patterns and row predicates.",
        "Example parameters include regular expressions matching selected text substrings and row predicates matching selected values, generated using programming-by demonstration methods [96, 118].",
    ],
))

DB(Citation(
    guo2012c, muniswamy2009a, ref="[119]",
    contexts=[
        "PASS [119, 121] collects such provenance by tracking Linux system calls within a modiﬁed kernel and ﬁlesystem, while ES3 [62] uses the Linux ptrace mechanism to accomplish a similar goal.",
        "The middle layer in the Burrito core collects OS-level provenance [119], which includes information such as which ﬁles were read, written, and renamed by each process, and which sub-processes were forked and exec’ed.",
    ],
))

DB(Citation(
    guo2012c, muniswamy2009b, ref="[120]",
    contexts=[
        "Research systems such as Elephant [140] and production systems such as NILFS [101] (part of Linux since June 2009) and Dropbox [6] track changes to all ﬁles and allow users to access old versions via readonly snapshots. Techniques such as causality-based versioning [120] can reduce storage and retrieval overheads by keeping only semantically-meaningful versions",
        "another process reads the given source ﬁle (causality-based versioning [120]),",
        "Estimating based on these two months of development activity, Burrito uses ∼2 GB of extra disk space per month when dotﬁle-only snapshots are pruned. More aggressive snapshot pruning [120] can further reduce space usage.",
    ],
))

DB(Citation(
    guo2012c, muniswamy2006a, ref="[121]",
    contexts=[
        "PASS [119, 121] collects such provenance by tracking Linux system calls within a modiﬁed kernel and ﬁlesystem, while ES3 [62] uses the Linux ptrace mechanism to accomplish a similar goal.",
    ],
))

DB(Citation(
    guo2012c, myers2006a, ref="[122]",
    contexts=[
        "Myers et al. [122] provide a survey of end-user programming; Halevy, Rajaraman, and Ordille provide a survey of data integration techniques [81]; Kandel et al. provide a survey of issues related to data quality and uncertainty, and demonstrate how interactive visualizations can aid in the data cleaning process [95].",
        
    ],
))

DB(Citation(
    guo2012c, nethercote2007b, ref="[123]",
    contexts=[
        "To make IncPy work with users’ already-installed extensions, we re-implemented using a shadow memory approach [123].",

    ],
))

DB(Citation(
    guo2012c, noble2009a, ref="[124]",
    contexts=[
        "For instance, scientiﬁc lab equipment can generate hundreds or thousands of data ﬁles that scientists must name and organize before running computational analyses on them [124].",
        "A literature search revealed that even veteran computational scientists acknowledged that having to organize code, data, and their dependencies was an impediment to productivity [98, 124].",
        "The “state-of-the-art” solution that veteran data analysts suggest is to simply use disciplined ﬁle naming conventions and Makeﬁles as the “best practices” for coping with these dependencies [98, 124].",
        "Some data analysis workﬂows consist of separate programs that coordinate with one another using intermediate data ﬁles [98, 124].",
    ],
))

DB(Citation(
    guo2012c, oinn2006a, ref="[125]",
    contexts=[
        "Scientiﬁc workﬂow systems such as Kepler [114], Taverna [125], and VisTrails [143] are graphical development environments for designing and executing scientiﬁc computations.",

    ],
))

DB(Citation(
    guo2012c, oliner2007a, ref="[126]",
    contexts=[
        "A script that processes a 2.5 GB supercomputer error log for an anomaly detection paper [126].",
        "In 2007, Oliner and Stearley released event logs from 5 supercomputers [126]; for this experiment, I used the log for Spirit since it is the largest in size (37 GB).",
        "System administrators routinely write ad-hoc scripts to query supercomputer event logs to monitor system health, discover aberrations, and diagnose failures. Oliner and Stearley describe how log ﬁles contain inconsistent or ill-deﬁned structure, corrupted records, and duplicated records, all of which make it harder to write robust log analysis scripts [126].",
        "To avoid biases due to duplicated records, my script coalesces all events within a 5-second interval into one, which Oliner and Stearley also do in their analyses [126]",
    ],
))

DB(Citation(
    guo2012c, olson1999a, ref="[127]",
    contexts=[
        "After data cleaning, reformatting, and integration, programmers might opt to store post-processed data in databases of either the relational (e.g., SQLite, MySQL, PostgreSQL) or NoSQL (e.g., Berkeley DB [127], MongoDB [15]) ﬂavors.",

    ],
))

DB(Citation(
    guo2012c, olston2008a, ref="[128]",
    contexts=[
        "Parallel execution of code can vastly speed up scientiﬁc data processing scripts, at the cost of increased diﬃculty in programming and debugging such scripts. In recent years, libraries such as Parallel Python [17], frameworks such as MapReduce [52] and Hadoop [1], and new high-level languages such as Pig [128] and Hive [151] have made it easier to write parallel code and deploy it to run on compute clusters. However, many researchers interviewed by me and others [133] felt that the learning curve for writing parallel code is still high, especially for scientists without much programming experience. It is much easier for people to think about algorithms sequentially, and even experts prefer to write single-threaded prototypes and then only parallelize later when necessary [144].",
        "Although domain-speciﬁc data processing languages are being developed in research labs [59, 128, 132], most modern programmers write ad-hoc data processing scripts in general-purpose languages such as Python, Perl, and Ruby due to their ﬂexibility, support for rapid prototyping, and active ecosystems of open-source libraries.",
        "One unique challenge in this space is that these systems are often comprised of multiple layers implemented in diﬀerent languages (e.g., SQL, Hive [151], Pig [128], Java, Python), so error handling, propagation, and reporting must cross language boundaries.",
        "There is currently a tension between latency and scalability: Software tools already exist to process data at cluster/cloud scales [1, 52, 128, 151], but they are cumbersome to administer and are not designed to support the sorts of seamless rapid iteration that are vital for research programming.",
    ],
))

DB(Citation(
    guo2012c, sullivan2009a, ref="[129]",
    contexts=[
        "In the past decade, decentralized version control systems such as Git [112] and Mercurial [129] have become more popular, especially in open-source software projects where developers work in multiple geographic locations.",

    ],
))

DB(Citation(
    guo2012c, patel2010a, ref="[130]",
    contexts=[
        "Gestalt [130] is an integrated development environment for prototyping and evaluating machine learning algorithms. It allows programmers to visually compare the outputs of diﬀerent algorithm variants and to quickly test alternatives",

    ],
))

DB(Citation(
    guo2012c, perez2007a, ref="[131]",
    contexts=[
        "For example, integrated development environments for languages such as Mathematica [14] and Python [131] offer a notebook view where executable code and output graphs are displayed alongside the programmer’s textual notes and always kept in sync",

    ],
))

DB(Citation(
    guo2012c, pike2005a, ref="[132]",
    contexts=[
        "The Sawzall [132] domain-speciﬁc language (built on top of MapReduce) can skip over portions of bad records, but it lacks the ﬂexibility of a general-purpose language.",
        "Although domain-speciﬁc data processing languages are being developed in research labs [59, 128, 132], most modern programmers write ad-hoc data processing scripts in general-purpose languages such as Python, Perl, and Ruby due to their ﬂexibility, support for rapid prototyping, and active ecosystems of open-source libraries.",
    ],
))

DB(Citation(
    guo2012c, prabhu2011a, ref="[133]",
    contexts=[
        "Surveys at universities indicate that people across dozens of departments ranging from the natural sciences (e.g., astrophysics, geosciences, molecular biology), engineering (e.g., aerospace and mechanical engineering, operations research), and social sciences (e.g., economics, political science, sociology) engage in research programming as part of their daily work [83, 133].",
        "Interviews of over 100 computational researchers across 20 academic disciplines at Princeton University [133].",
        "However, anecdotes and empirical studies [42, 133] indicate that a signiﬁcant amount of research programming is still done on desktop machines with data sets that ﬁt on modern hard drives (i.e., less than a terabyte).",
        "In this dissertation, I will refer to these kinds of programs as data analysis scripts, since research programmers often prefer to use interpreted “scripting” languages such as Python, Perl, R, and MATLAB [107, 133]",
        "The main goal of software engineering is to create robust, well-tested, maintainable pieces of production-quality software. In contrast, the main goal of research programming is to obtain insights about a topic; code is simply a means to this end [133]",
        "In contrast, research programmers often work in a heterogeneous environment where they cobble together a patchwork of improvised ad-hoc scripts and “sloppy” prototype code written in multiple languages, interfacing with a mix of 3rd-party libraries and executables from disparate sources within a UNIX-like command-line environment [115, 133]",
        "In summarizing their comprehensive interviews of over 100 research programmers at Princeton University, Prabhu et al. conclude: “Presently, programming tools are designed for professional programmers, and need to be carefully tailored to meet the needs of scientists” [133].",
        "A large amount of research programming is being done on data sets less than a terabyte in size, which ﬁt on one single modern desktop machine [133].",
        "Parallel execution of code can vastly speed up scientiﬁc data processing scripts, at the cost of increased diﬃculty in programming and debugging such scripts. In recent years, libraries such as Parallel Python [17], frameworks such as MapReduce [52] and Hadoop [1], and new high-level languages such as Pig [128] and Hive [151] have made it easier to write parallel code and deploy it to run on compute clusters. However, many researchers interviewed by me and others [133] felt that the learning curve for writing parallel code is still high, especially for scientists without much programming experience. It is much easier for people to think about algorithms sequentially, and even experts prefer to write single-threaded prototypes and then only parallelize later when necessary [144].",
        "I implemented my technique for Python, since it is a popular language for writing data analyses [133]. I created a prototype open-source interpreter named SlopPy (Sloppy Python) [22] by adding 500 lines of C code to the Python 2.6 interpreter.",
        
    ],
))

DB(Citation(
    guo2012c, raman2001a, ref="[134]",
    contexts=[
        "Both database and HCI researchers have devised graphical interfaces [65, 91, 134] for cleaning and reformatting data",
        "Potter’s Wheel [134] is a graphical interface for authoring statements in a declarative transformation language and oﬀers extensible facilities for data type inference.",
        "To assist this process, researchers have developed novel interactive tools. Potter’s Wheel [134] and Google Reﬁne [91] are menu-driven interfaces that provide access to common data transforms. Wrangler [96] extends this approach by (a) automatically suggesting applicable transforms in response to direct manipulation of a data table and (b) providing visual previews to aid transform assessment.",
        "The language is the direct descendant of the Potter’s Wheel language [134] and draws on concepts introduced in SchemaSQL [106]",
        "This prior work [106, 134] also provides formal proofs of the language’s expressiveness, showing it is capable of expressing any one-to-one or one-to-many transform of cell values.",
        "Similar to other transformation tools [91, 134], a transform can be speciﬁed manually by selecting a transform type from the tool bar and then entering in desired parameter values.",
    ],
))

DB(Citation(
    guo2012c, rekimoto1999a, ref="[135]",
    contexts=[
        "A more radical approach is to get rid of traditional ﬁlenames and directory hierarchies altogether. Research prototypes such as Lifestreams [58] and Time-Machine Computing [135] are GUI desktop environments where the user’s ﬁles are organized in a chronological versioned stream rather than in directories, thus eliminating the need to provide ﬁlenames and directory names.",

    ],
))

DB(Citation(
    guo2012c, rinard2004a, ref="[136]",
    contexts=[
        "Failure-oblivious computing is a technique that silently hides memory access errors in C programs by ignoring out-ofbounds writes and returning fake (small integer) values for out-of-bounds reads [136].",
        "Note that this technique is most eﬀective on scripts with short error propagation distances, like those that process each record independently of one another [136]",
    ],
))

DB(Citation(
    guo2012c, saff2004a, ref="[137]",
    contexts=[
        "This might make it feasible for tests to run continuously during development, which has been shown to reduce wasted time and allow bugs to be caught faster [137].",

    ],
))

DB(Citation(
    guo2012c, saito2005a, ref="[138]",
    contexts=[
        "Deterministic replay: CDE does not try to replay exact execution paths like record-replay tools [37, 103, 138] do.",

    ],
))

DB(Citation(
    guo2012c, salcianu2005a, ref="[139]",
    contexts=[
        "Following the deﬁnition of Salcianu and Rinard, we consider a function call pure if it never mutates a value that existed prior to its invocation [139].",
        "Unlike static analysis [139], IncPy dynamically detects impurity of individual execution paths.",
        "IncPy’s run-time overhead is reasonable (mean of 16% on our benchmarks) because interpreters are already slow compared to executing compiled code. Static purity and escape analyses [139], and other compile-time optimizations, might be needed to achieve reasonable overheads on compiled code.",
    ],
))

DB(Citation(
    guo2012c, santry1999a, ref="[140]",
    contexts=[
        "Research systems such as Elephant [140] and production systems such as NILFS [101] (part of Linux since June 2009) and Dropbox [6] track changes to all ﬁles and allow users to access old versions via readonly snapshots. Techniques such as causality-based versioning [120] can reduce storage and retrieval overheads by keeping only semantically-meaningful versions",

    ],
))

DB(Citation(
    guo2012c, sapuntzakis2003a, ref="[141]",
    contexts=[
        "For example, Mac OS X programmers can create application bundles using Apple’s Developer Tools IDE [13]. Research prototypes such as PDS [36], which creates self-contained Windows applications, and The Collective [141], which aggregates a set of software into a portable virtual appliance, also require the user to manually specify dependencies. VMware ThinApp [32] is a commercial tool that automatically creates self-contained portable Windows applications.",
    ],
))

DB(Citation(
    guo2012c, scaffidi2005a, ref="[142]",
    contexts=[
        "Research programming is ubiquitous: By some estimates, the number of people who perform research programming exceeds the number of professional software engineers by over a factor of three [142], and this disparity is likely to grow as more science, engineering, and business-related ﬁelds rely on computational techniques",
        "Speciﬁcally, an analysis of U.S. Bureau of Labor Statistics data estimates that by the year 2012, 13 million Americans will do programming in their jobs, but only 3 million will be professional software engineers [142].",
    ],
))

DB(Citation(
    guo2012c, scheidegger2008b, ref="[143]",
    contexts=[
        "Scientiﬁc workﬂow systems such as Kepler [114], Taverna [125], and VisTrails [143] are graphical development environments for designing and executing scientiﬁc computations.",
        "They require a steep learning curve: users need to learn programming languages, programming environments, specialized libraries, and best practices for constructing workﬂows” [143].",
    ],
))

DB(Citation(
    guo2012c, Email(2009, "Jiwon Seo", "discussing sequential vs. parallel scripts"), ref="[144]",
    contexts=[
        "Parallel execution of code can vastly speed up scientiﬁc data processing scripts, at the cost of increased diﬃculty in programming and debugging such scripts. In recent years, libraries such as Parallel Python [17], frameworks such as MapReduce [52] and Hadoop [1], and new high-level languages such as Pig [128] and Hive [151] have made it easier to write parallel code and deploy it to run on compute clusters. However, many researchers interviewed by me and others [133] felt that the learning curve for writing parallel code is still high, especially for scientists without much programming experience. It is much easier for people to think about algorithms sequentially, and even experts prefer to write single-threaded prototypes and then only parallelize later when necessary [144].",
    ],
))


DB(Citation(
    guo2012c, shah2007a, ref="[145]",
    contexts=[
        "Research in context-aware personal ﬁle search [145] can help address this issue.",
        "Our colleagues also suggested building other Burrito applications such as a personal productivity monitor [20] and a contextual ﬁle search tool [145].",
    ],
))

DB(Citation(
    guo2012c, spillane2007a, ref="[146]",
    contexts=[
        "System call interposition using ptrace is a wellknown technique that researchers have used for implementing tools such as secure sandboxes [67, 94], record-replay systems [103], and user-level ﬁlesystems [146].",
    ],
))

DB(Citation(
    guo2012c, staelin1998a, ref="[147]",
    contexts=[
        "A banal but tricky detail that package creators must worry about is adhering to platform-speciﬁc idioms for pathnames and avoiding hard-coding non-portable paths into their programs [147].",
    ],
))

DB(Citation(
    guo2012c, strong2011a, ref="[148]",
    contexts=[
        "Interviews of computational scientists at Los Alamos National Laboratory [148].",

    ],
))

DB(Citation(
    guo2012c, sucan2008a, ref="[149]",
    contexts=[
        "Robot motion planning algorithm [149",
        "A robotics researcher used CDE to make the experiments for his motion planning paper (kpiece) [149] fully reproducible. Similarly, we helped a social networking researcher create a reproducible package for his genetic algorithm paper (gadm) [104].",
    ],
))

DB(Citation(
    guo2012c, tashma2008a, ref="[150]",
    contexts=[
        "DejaView [102] augments Linux with a virtual display driver and virtual execution environment to eﬃciently capture a rich history of user activity and enable execution to restore to any time in the past. Others have augmented virtual machines with ﬁne-grained checkpoints to enable a similar form of “time travel” [100, 150].",

    ],
))

DB(Citation(
    guo2012c, thusoo2010a, ref="[151]",
    contexts=[
        "Parallel execution of code can vastly speed up scientiﬁc data processing scripts, at the cost of increased diﬃculty in programming and debugging such scripts. In recent years, libraries such as Parallel Python [17], frameworks such as MapReduce [52] and Hadoop [1], and new high-level languages such as Pig [128] and Hive [151] have made it easier to write parallel code and deploy it to run on compute clusters. However, many researchers interviewed by me and others [133] felt that the learning curve for writing parallel code is still high, especially for scientists without much programming experience. It is much easier for people to think about algorithms sequentially, and even experts prefer to write single-threaded prototypes and then only parallelize later when necessary [144].",
        "One unique challenge in this space is that these systems are often comprised of multiple layers implemented in diﬀerent languages (e.g., SQL, Hive [151], Pig [128], Java, Python), so error handling, propagation, and reporting must cross language boundaries.",
        "There is currently a tension between latency and scalability: Software tools already exist to process data at cluster/cloud scales [1, 52, 128, 151], but they are cumbersome to administer and are not designed to support the sorts of seamless rapid iteration that are vital for research programming.",
    ],
))

DB(Citation(
    guo2012c, tichy1985a, ref="[152]",
    contexts=[
        "The modern line of version control systems started with RCS [152] in the 1980’s, followed by CVS [56] and Subversion (SVN) [46].",

    ],
))

DB(Citation(
    guo2012c, tuchinda2008a, ref="[153]",
    contexts=[
        "Another class of targeted data manipulation tools rely on programming by demonstration (PBD) techniques [49]. Potluck [92] uses interactive simultaneous text editing features [118] to help users perform data integration. Karma [153] infers text extractors and transformations for web data from examples entered in a table. Vegemite [110] extends CoScripter [108] to integrate web data, automate the use of web services, and generate shareable scripts. Dontcheva et al. [55] use PBD techniques to enable extraction, integration, and templated search of web data. Gulwani [69] introduces an algorithm for learning expressive string processing programs from input-output examples. PADS [60] infers nuanced data parsers from a set of positive examples.",
    ],
))

DB(Citation(
    guo2012c, Site("Hal Varian on how the Web challenges managers. McKinsey Quarterly, Jan 2009", "http://www.mckinsey.com/industries/high-tech/our-insights/hal-varian-on-how-the-web-challenges-managers"), ref="[154]",
    contexts=[
        "The increasing scale and accessibility of data—including government records, web data, and system logs—provides an under-exploited resource for improving governance, public policy, organizational strategy, and even our personal lives [154].",

    ],
))

DB(Citation(
    guo2012c, Email(2010, "Tao Yue", "personal email communication, July 11"), ref="[155]",
    contexts=[
        "Going back to something I did just three months ago, I often ﬁnd out I have absolutely no idea what the output ﬁles mean, and end up having to repeat it to ﬁgure it out. [155]",

    ],
))

DB(Citation(
    guo2012c, zimmermann2012a, ref="[156]",
    contexts=[
        "My own research programming experiences when working on empirical software engineering papers earlier in graduate school (2007–2010) [72, 78, 79, 156].",
        "This project was later published as three conference papers [78, 79, 156].",
    ],
))


DB(Citation(
    hill2016a, guo2012c, ref="",
    contexts=[

    ],
))

DB(Citation(
    kery2017a, guo2012c, ref="",
    contexts=[

    ],
))

DB(Citation(
    hunold2013a, guo2012c, ref="",
    contexts=[

    ],
))

DB(Citation(
    gent2013a, guo2012c, ref="",
    contexts=[

    ],
))

DB(Citation(
    shcherbakov2014a, guo2012c, ref="",
    contexts=[

    ],
))
