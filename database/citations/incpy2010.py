# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2000 import gray2000a
from ..work.y2004 import dean2004a
from ..work.y2004 import rigo2004a
from ..work.y2005 import salcianu2005a
from ..work.y2006 import muniswamy2006a
from ..work.y2006 import ludascher2006a
from ..work.y2006 import oinn2006a
from ..work.y2007 import zhang2007a
from ..work.y2008 import scheidegger2008b
from ..work.y2008 import olston2008a
from ..work.y2009 import brandt2009a
from ..work.y2009 import guo2009a
from ..work.y2009 import hammer2009a
from ..work.y2010 import guo2010a
from ..work.y2010 import muniswamy2010b
from ..work.y2010 import clements2010a
from ..work.y2011 import olston2011a
from ..work.y2011 import burckhardt2011a
from ..work.y2012 import ports2012a
from ..work.y2012 import leyshock2012a
from ..work.y2013 import zohrevandi2013a
from ..work.y2014 import leyshock2014a
from ..work.y2014 import moreno2014a
from ..work.y2014 import truskinger2014a
from ..work.y2015 import north2015a
from ..work.y2015 import pinandito2015a
from ..work.y2016 import schone2016a
from ..work.y2016 import moreno2016a


DB(Citation(
    guo2010a,
    Site("Parallel Python", "http://www.parallelpython.com/"),
    ref="[1]",
    contexts=[
        "In recent years, the emergence of libraries like Parallel Python [1], frameworks like MapReduce [5], and new high-level languages like Pig [12] have made it easier to write parallel code.",
        
    ],
))

DB(Citation(
    guo2010a,
    Site("Programming for Scientists (blog)", "http://www.programming4scientists.com/"),
    ref="[2]",
    contexts=[
        "“The primary tension in the life of the scientist-programmer is to just get the science done. What we mean by this is the conﬂict between getting the coding done as quickly as possible so that you can move onto ﬁnishing the science, versus spending that extra week (or however long) making sure that your code is neat, tidy, well-tested and generally a glorious triumph of software engineering.”[2]",
        "(they learn just enough programming skills to write the simplest possible script that “just get[s] the science done”[2])",
        
    ],
))

DB(Citation(
    guo2010a, brandt2009a, ref="[3]",
    contexts=[
        "scientists often write programs in what Brandt et al. call an opportunistic manner, emphasizing speed and ease of development over code robustness and runtime performance [3].",
        "Anecdotes from programmers [3] and ﬁndings from psychology experiments [6] suggest that a short iteration cycle not only results in more rapid completion of tasks but also causes people to subconsciously shift to using more effective problem-solving strategies. Since the problem remains fresh in one’s (short-term) working memory, one can remain intensely concentrated rather than potentially getting distracted and context-switching while waiting for each subsequent script run to complete.",
        
    ],
))

DB(Citation(
    guo2010a, 
    DB(Email(2009, "BRONSON, N.", "discussing hindrances to data subsetting")),
    ref="[4]",
    contexts=[
        "This is sometimes feasible, but oftentimes there isn’t a practical way to avoid running the script on the full dataset, for some of the following reasons [4]",
        "Data processing bugs often manifest on aberrant records that appear in the middle of a large dataset [4] (say, at the end of the ﬁrst year in this example); if the bug ﬁx is sufﬁciently small, then it might be possible to re-start at the buggy record rather than re-computing all the prior (correct) records",
        
    ],
))

DB(Citation(
    guo2010a, dean2004a, ref="[5]",
    contexts=[
       "In recent years, the emergence of libraries like Parallel Python [1], frameworks like MapReduce [5], and new high-level languages like Pig [12] have made it easier to write parallel code.",
         
    ],
))

DB(Citation(
    guo2010a, gray2000a, ref="[6]",
    contexts=[
        "Anecdotes from programmers [3] and ﬁndings from psychology experiments [6] suggest that a short iteration cycle not only results in more rapid completion of tasks but also causes people to subconsciously shift to using more effective problem-solving strategies. Since the problem remains fresh in one’s (short-term) working memory, one can remain intensely concentrated rather than potentially getting distracted and context-switching while waiting for each subsequent script run to complete.",
        "able to re-run and see new results in 8 seconds rather than waiting for several minutes allows the programmer to keep the task in working memory [6] while iterating and debugging",
        
    ],
))

DB(Citation(
    guo2010a, guo2009a, ref="[7]",
    contexts=[
        "We performed an informal preliminary evaluation by using IncPy to run Python scripts that we wrote in 2007– 2008 for a research project to analyze revision control history and static analysis bug reports for the Linux kernel [7].",
        
    ],
))

DB(Citation(
    guo2010a, hammer2009a, ref="[8]",
    contexts=[
        "Hammer, Acar, et al. have implemented self-adjusting computation for statically-typed languages (ML and C) [8]",
        "These systems have potential for massive speed-ups but require programmers to write algorithms using new language constructs and forbids the use of existing constructs like returning values from functions (must instead use destination-passing style [8]).",
        
    ],
))

DB(Citation(
    guo2010a, ludascher2006a, ref="[9]",
    contexts=[
        "Scientiﬁc workﬂow systems like Kepler [9], Taverna [11], and VisTrails [15] provide graphical integrated development environments for designing and executing scientiﬁc computations. Scientists create workﬂows by using a GUI to visually connect together blocks of premade functionality in a data-ﬂow graph.",
        
    ],
))

DB(Citation(
    guo2010a, muniswamy2006a, ref="[10]",
    contexts=[
        "Muniswamy-Reddy et al. designed a storage system that tracks coarse-grained provenance about individual ﬁles, which could be the intermediate results of command-line script invocations [10].",
        
    ],
))

DB(Citation(
    guo2010a, oinn2006a, ref="[11]",
    contexts=[
        "Scientiﬁc workﬂow systems like Kepler [9], Taverna [11], and VisTrails [15] provide graphical integrated development environments for designing and executing scientiﬁc computations. Scientists create workﬂows by using a GUI to visually connect together blocks of premade functionality in a data-ﬂow graph.",
        
    ],
))

DB(Citation(
    guo2010a, olston2008a, ref="[12]",
    contexts=[
        "In recent years, the emergence of libraries like Parallel Python [1], frameworks like MapReduce [5], and new high-level languages like Pig [12] have made it easier to write parallel code.",
        
    ],
))

DB(Citation(
    guo2010a, rigo2004a, ref="[13]",
    contexts=[
        "Just-in-time compilers for dynamic languages (e.g., Psyco [13] for Python, Rubinius for Ruby, TraceMonkey for JavaScript) can speed up script execution times without requiring the programmer to learn any new constructs, which is similar in spirit to the goals of IncPy.",
        
    ],
))

DB(Citation(
    guo2010a, salcianu2005a, ref="[14]",
    contexts=[
        "Only pure functions are eligible for memoization. Following the deﬁnition of Salcianu and Rinard, we consider a function pure if it never mutates an object that existed prior to its invocation [14]",
        "Our technique dynamically detects purity during execution, so it avoids the usual obstacles that hinder static (compile-time) purity detection, like conservative full-program pointer analysis and reasoning about dynamically-typed and reﬂective language features [14].",
        
    ],
))

DB(Citation(
    guo2010a, scheidegger2008b, ref="[15]",
    contexts=[
        "Scientiﬁc workﬂow systems like Kepler [9], Taverna [11], and VisTrails [15] provide graphical integrated development environments for designing and executing scientiﬁc computations. Scientists create workﬂows by using a GUI to visually connect together blocks of premade functionality in a data-ﬂow graph.",
        "“While signiﬁcant progress has been made in unifying computations under the workﬂow umbrella, workﬂow systems are notoriously hard to use. They require a steep learning curve: users need to learn programming languages, programming environments, specialized libraries, and best practices for constructing workﬂows.” [15]",
        
    ],
))

DB(Citation(
    guo2010a, 
    DB(Email(2009, "SEO, J.", "discussing sequential vs.parallel scripts")),
    ref="[16]",
    contexts=[
        "Even experts prefer to start off by writing single-threaded prototype scripts and then only parallelize later when necessary [16]",
        "It is much easier for most people to think about algorithms sequentially, and even experts prefer to write single-threaded prototypes and then only parallelize later when necessary [16].",
        
    ],
))

DB(Citation(
    guo2010a, zhang2007a, ref="[17]",
    contexts=[
        "Zhang et al. designed a system to collect very ﬁnegrained provenance at the byte level by tracing the execution of x86-Linux binary executables (usually from C or C++ programs) [17]",
        
    ],
))

DB(Citation(
    north2015a, guo2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    zohrevandi2013a, guo2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    muniswamy2010b, guo2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    clements2010a, guo2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    pinandito2015a, guo2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    schone2016a, guo2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    leyshock2014a, guo2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ports2012a, guo2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    moreno2014a, guo2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    moreno2016a, guo2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    olston2011a, guo2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    truskinger2014a, guo2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    leyshock2012a, guo2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    burckhardt2011a, guo2010a, ref="",
    contexts=[

    ],
))
