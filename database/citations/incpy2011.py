# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1968 import michie1968a
from ..work.y1979 import feldman1979a
from ..work.y2000 import heydon2000a
from ..work.y2004 import saff2004a
from ..work.y2005 import salcianu2005a
from ..work.y2005 import scaffidi2005a
from ..work.y2007 import nethercote2007b
from ..work.y2007 import carver2007a
from ..work.y2007 import oliner2007a
from ..work.y2008 import scheidegger2008b
from ..work.y2009 import acar2009a
from ..work.y2009 import brandt2009a
from ..work.y2009 import gal2009a
from ..work.y2009 import guo2009a
from ..work.y2009 import hammer2009a
from ..work.y2009 import heymann2009a
from ..work.y2009 import kelly2009a
from ..work.y2009 import noble2009a
from ..work.y2010 import guo2010b, guo2010a
from ..work.y2010 import heimerl2010a
from ..work.y2010 import horn2010a
from ..work.y2011 import guo2011b
from ..work.y2011 import ko2011a
from ..work.y2012 import kim2012a
from ..work.y2012 import guo2012d
from ..work.y2014 import gounares2014a
from ..work.y2014 import moreno2014a
from ..work.y2014 import gounares2014b
from ..work.y2014 import gounares2014c
from ..work.y2014 import li2014b
from ..work.y2014 import gounares2014d
from ..work.y2015 import gligoric2015a
from ..work.y2015 import likamwa2015a
from ..work.y2015 import gligoric2015b
from ..work.y2015 import toffola2015a
from ..work.y2015 import gligoric2015c
from ..work.y2016 import hammer2016a
from ..work.y2016 import gounares2016a
from ..work.y2016 import hammer2016b
from ..work.y2016 import moreno2016a


DB(Citation(
    guo2011b,
    Site("IncPy home", "http://www.pgbovine.net/incpy.html"),
    ref="[1]",
    contexts=[
        "We implemented our technique as a custom open-source Python interpreter called IncPy (Incremental Python) [1].",
        "We implemented our technique as an open-source Python interpreter named IncPy [1].",
        
    ],
))
    
DB(Citation(
    guo2011b,
    Site("Official Python wiki", "Large Python Projects http://wiki.python.org/moin/LargePythonProjects"),
    ref="[2]",
    contexts=[
        "Django is a popular framework for building web applications and is one of the largest Python projects, with 59,111 lines of Python code [2]",
        
    ],
))
    
DB(Citation(
    guo2011b,
    Site("TIOBE programming community index", "www.tiobe.com/index.php/content/paperinfo/tpci/index.html"),
    ref="[3]",
    contexts=[
        "A study of US labor statistics predicts that by 2012, 13 million American workers will do programming beyond creating spreadsheet macros and database queries (i.e, not simply end-user programming [18]), but amongst those, only 3 million will be professional software engineers [25]. It is reasonable to assume that a non-trivial percentage of these 10 million programmers who are not software engineers will write scripts to analyze data. Three out of the ten most popular languages today [3] — Python, Perl, and Ruby — are often used for data analysis.",
        
    ],
    accessed="2011",
))
    
DB(Citation(
    guo2011b, acar2009a, ref="[4]",
    contexts=[
        "Self-adjusting computation is a related technique that enables algorithms to run faster in response to small changes in input data, only re-computing outputs for portions that have changed [4, 12].",
        "Its creator mentions,“Although self-adjusting computation can be applied without having to change existing code by tracking all data and all dependences between code and data, this is prohibitively expensive in practice.” [4].",
        
    ],
))


DB(Citation(
    guo2011b, brandt2009a, ref="[5]",
    contexts=[
        "Thus, the creators of data analysis scripts often program using high-level interpreted languages (e.g., Python, Perl, Ruby) because they care more about ﬂexibility, iteration speed, and ease of development than code robustness, maintainability, and run-time performance [5].",
        
    ],
))
    
DB(Citation(
    guo2011b, carver2007a, ref="[6]",
    contexts=[
        "Next, data analysis is often ad-hoc and exploratory in nature, where requirements are ill-deﬁned and constantly changing [6]",
        ". He wrote all scripts in one language (Python), but his datasets were stored in diverse ﬁle formats (e.g., semi-structured plaintext, CSV, SQL database, serialized objects), a typical setup for data analysis workﬂows [6].",
        
    ],
))

DB(Citation(
    guo2011b, feldman1979a, ref="[7]",
    contexts=[
        "One possible solution would be to write all of his code and dataset dependencies in a Makeﬁle [7], so that invoking make would only re-run the scripts whose dependent datasets have changed",
        "make is a ubiquitous UNIX tool that allows users to declaratively specify dependencies between commands and ﬁles, so that the minimum set of commands need to be re-run when dependent ﬁles are altered [7].",
        
    ],
))
    
DB(Citation(
    guo2011b, gal2009a, ref="[8]",
    contexts=[
        "Just-in-time compilers for dynamic languages (e.g., Unladen Swallow for Python, Rubinius for Ruby, TraceMonkey [8] for JavaScript) can speed up script execution times without requiring programmers to make any annotations, which is similar in spirit to IncPy’s goals",
        
    ],
))

DB(Citation(
    guo2011b, guo2009a, ref="[9]",
    contexts=[
        "A script we wrote in 2007–2008 to mine data about the Linux kernel project’s revision control history for an empirical software engineering paper [9].",
        "To show how IncPy enables faster iteration when exploring alternative hypotheses in a data analysis task, we studied a Python script we wrote in 2007–2008 to mine Linux data for a paper [9].",
        
    ],
))

DB(Citation(
    guo2011b, guo2010a, ref="[10]",
    contexts=[
        "In a 2010 workshop paper [10], we presented anecdotes from colleagues who also experienced similar frustrations throughout the data analysis scripting process",
        "We introduced an early version of IncPy in a 2010 workshop paper [10], whose contents diﬀer from this paper in signiﬁcant ways: First, that paper focused on deﬁning the problem space and establishing motivation using anecdotes from interviews with scientists",
        
    ],
))

DB(Citation(
    guo2011b, guo2010b, ref="[11]",
    contexts=[
        ". His project was to analyze software bug databases and employee personnel datasets to quantify people-related factors that aﬀect whether bug reports are ﬁxed (published in ICSE 2010 [11]).",
        "A data analysis workﬂow [11] comprised of Python scripts (boxes) that process and generate data ﬁles (circles).",
        
    ],
))
    
DB(Citation(
    guo2011b, hammer2009a, ref="[12]",
    contexts=[
        "Self-adjusting computation is a related technique that enables algorithms to run faster in response to small changes in input data, only re-computing outputs for portions that have changed [4, 12].",
        "Even with annotations, there is at least a 500% slowdown on the initial (empty cache) run [12].",
        
    ],
))

DB(Citation(
    guo2011b, heimerl2010a, ref="[13]",
    contexts=[
        "A script that post-processes and graphs synchronized mouse input events for an HCI paper [13].",
        
    ],
))

DB(Citation(
    guo2011b, heydon2000a, ref="[14]",
    contexts=[
        "The Vesta software conﬁguration management system [14] provides a pure functional domain-speciﬁc language for writing software build scripts.",
        
    ],
))

DB(Citation(
    guo2011b, heymann2009a, ref="[15]",
    contexts=[
        "A set of information retrieval scripts for a paper contrasting crowdsourced tags with expert annotations for keywords describing books [15].",
        "Datasets (circles) and Python functions (boxes) from Paul’s information retrieval scripts [15]",
        "To show how we can remove manually-written caching code and maintain comparable performance, we studied information retrieval scripts written by our colleague Paul [15].",
        
    ],
))
    
DB(Citation(
    guo2011b, horn2010a, ref="[16]",
    contexts=[
        "A set of scripts that process event logs from a virtual world for a distributed systems paper [16]",
        "Python scripts (boxes) and data ﬁles (circles) from Ewen’s event log analysis workﬂow [16].",
        "Refactored version of Ewen’s event log analysis workﬂow [16], containing only functions (boxes) and input data ﬁles (circles",
        "To show how IncPy can beneﬁt existing ﬁle-based workﬂows (§3.5) and provide an easy transition to a pure-Python workﬂow, we studied Python code written by our colleague Ewen to process event logs from a virtual world system [16].",
        
    ],
))
    
DB(Citation(
    guo2011b, kelly2009a, ref="[17]",
    contexts=[
        "First, the end products of data analysis are insights about a topic [17], whereas the end products of software engineering are (hopefully) robust, welltested, and maintainable pieces of software",
        "A literature search revealed that even veteran computational scientists acknowledged that having to organize code, data, and their dependencies was an impediment to productivity [17, 21].",
        "Veteran data analysts suggest using disciplined ﬁle naming conventions and Makeﬁles as the “best practices” for coping with these dependencies [17, 21].",
        "Some data analysis workﬂows consist of separate programs that coordinate with one another using intermediate data ﬁles [17, 21].",
        
    ],
))

DB(Citation(
    guo2011b, ko2011a, ref="[18]",
    contexts=[
        "A study of US labor statistics predicts that by 2012, 13 million American workers will do programming beyond creating spreadsheet macros and database queries (i.e, not simply end-user programming [18]), but amongst those, only 3 million will be professional software engineers [25]. It is reasonable to assume that a non-trivial percentage of these 10 million programmers who are not software engineers will write scripts to analyze data. Three out of the ten most popular languages today [3] — Python, Perl, and Ruby — are often used for data analysis.",
        
    ],
))

DB(Citation(
    guo2011b, michie1968a, ref="[19]",
    contexts=[
        "The interpreter automatically memoizes [19] (caches) the inputs, outputs, and dependencies of certain function calls to disk, only doing so when it is safe (pure and deterministic call) and worthwhile (faster to re-use cached results than to re-run) to do the memoization.",
        "Memoization is an optimization ﬁrst introduced in a 1968 Nature paper [19]:",
        
    ],
))
    
DB(Citation(
    guo2011b, nethercote2007b, ref="[20]",
    contexts=[
        "Thus, to make IncPy work with users’ already-installed extensions, we re-implemented using a shadow memory approach [20].",
        
    ],
))
    
DB(Citation(
    guo2011b, noble2009a, ref="[21]",
    contexts=[
        "A literature search revealed that even veteran computational scientists acknowledged that having to organize code, data, and their dependencies was an impediment to productivity [17, 21].",
        "Veteran data analysts suggest using disciplined ﬁle naming conventions and Makeﬁles as the “best practices” for coping with these dependencies [17, 21].",
        "Some data analysis workﬂows consist of separate programs that coordinate with one another using intermediate data ﬁles [17, 21].",
        
    ],
))
    
DB(Citation(
    guo2011b, oliner2007a, ref="[22]",
    contexts=[
        "A script that processes a 2.5 GB supercomputer error log for an anomaly detection paper [22].",
        
    ],
))
    
DB(Citation(
    guo2011b, saff2004a, ref="[23]",
    contexts=[
        "This might make it feasible for tests to run continuously during development, which has been shown to reduce wasted time and allow bugs to be caught faster [23].",
        
    ],
))
    
DB(Citation(
    guo2011b, salcianu2005a, ref="[24]",
    contexts=[
        "Following the deﬁnition of Salcianu and Rinard, we consider a function call pure if it never mutates a value that existed prior to its invocation [24].",
        "Unlike static analysis [24], IncPy dynamically detects impurity of individual execution paths",
        "Static purity and escape analyses [24], and other compile-time optimizations, might be needed to achieve reasonable overheads on compiled code.",
        
    ],
))
    
DB(Citation(
    guo2011b, scaffidi2005a, ref="[25]",
    contexts=[
        "A study of US labor statistics predicts that by 2012, 13 million American workers will do programming beyond creating spreadsheet macros and database queries (i.e, not simply end-user programming [18]), but amongst those, only 3 million will be professional software engineers [25]. It is reasonable to assume that a non-trivial percentage of these 10 million programmers who are not software engineers will write scripts to analyze data. Three out of the ten most popular languages today [3] — Python, Perl, and Ruby — are often used for data analysis.",
        
    ],
))

DB(Citation(
    guo2011b, scheidegger2008b, ref="[26]",
    contexts=[
        "Scientiﬁc workﬂow systems such as VisTrails [26] are graphical development environments for designing and executing scientiﬁc computations.",
        "They require a steep learning curve: users need to learn programming languages, programming environments, specialized libraries, and best practices for constructing workﬂows [26].”",
        
    ],
))

DB(Citation(
    hammer2016a, guo2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    gounares2014a, guo2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    gounares2016a, guo2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    hammer2016b, guo2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    moreno2014a, guo2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    moreno2016a, guo2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    gligoric2015a, guo2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    gounares2014b, guo2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    likamwa2015a, guo2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    gligoric2015b, guo2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    toffola2015a, guo2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    gounares2014c, guo2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    gligoric2015c, guo2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    kim2012a, guo2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    li2014b, guo2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    gounares2014d, guo2011b, ref="",
    contexts=[

    ],
))

DB(Citation(
    guo2012d, guo2011b, ref="",
    contexts=[

    ],
))
