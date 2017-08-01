# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1991 import chambers1991a
from ..work.y1998 import staelin1998a
from ..work.y2002 import loper2002a
from ..work.y2003 import sapuntzakis2003a
from ..work.y2004 import dolstra2004a
from ..work.y2005 import alpern2005a
from ..work.y2005 import fisher2005a
from ..work.y2005 import scaffidi2005a
from ..work.y2007 import aiken2007a
from ..work.y2008 import cadar2008a
from ..work.y2009 import sucan2009a
from ..work.y2009 import altekar2009a
from ..work.y2010 import lahiri2010a
from ..work.y2011 import guo2011a
from ..work.y2011 import guo2011c


DB(Citation(
    guo2011c,
    Site("CDE public source code repository", "https://github.com/pgbovine/CDE"),
    ref="[1]",
    contexts=[
        "In this paper, we present an open-source tool called CDE [1] that makes it easy for people of all levels of IT expertise to get their software running on other machines without the hassle of manually creating a robust",
        "Since its release in Nov. 2010, CDE has been downloaded over 3,000 times [1]",
        "OKAPI isalsoavailableasafreestandalonecommandlinetool[1].",
        "Since we released the ﬁrst version of CDE on November 9, 2010, it has been downloaded at least 3,000 times as of September 2011 [1].",
        
    ],
))

DB(Citation(
    guo2011c,
    Site("Coq proof assistant: Bug 2443", "http://coq.inria.fr/bugs/show_bug.cgi?id=2443"),
    ref="[2]",
    contexts=[
        "Incorrect output by Coq proof assistant [2",
        "Three volunteers sent us CDE packages, and we were able to reproduce all of their bugs: one that causes the Coq proof assistant to produce incorrect output (coq-bug-2443) [2], one that segfaults the GCC compiler (gcc-bug-46651) [3], and one that makes the LLVM compiler allocate an enormous amount of memory and crash (llvm-bug-8679) [5].",
        
    ],
))

DB(Citation(
    guo2011c,
    Site("GCC compiler:Bug 46651", "http://gcc.gnu.org/bugzilla/show_bug.cgi?id=46651"),
    ref="[3]",
    contexts=[
        "Causes GCC compiler to segfault [3",
        "Three volunteers sent us CDE packages, and we were able to reproduce all of their bugs: one that causes the Coq proof assistant to produce incorrect output (coq-bug-2443) [2], one that segfaults the GCC compiler (gcc-bug-46651) [3], and one that makes the LLVM compiler allocate an enormous amount of memory and crash (llvm-bug-8679) [5].",
        
    ],
))

DB(Citation(
    guo2011c,
    Site("List of software package management systems", "http://en.wikipedia.org/wiki/List_of_software_package_management_systems"),
    ref="[4]",
    contexts=[
        "Similarly, open-source developers must carefully specify the proper dependencies inordertointegratetheirsoftwareintopackagemanagementsystems[4](e.g.,RPMonLinux,MacPortsonMac OS X).",
        "Generic package managers exist for all major operating systems (e.g., RPM for Linux, MacPorts for Mac OS X, Cygwin for Windows), and specialized package managers exist for ecosystems surrounding many programming languages (e.g., CPAN for Perl, RubyGems for Ruby) [4].",
        
    ],
))

DB(Citation(
    guo2011c,
    Site("LLVM compiler: Bug 8679", "http://llvm.org/bugs/show_bug.cgi?id=8679"),
    ref="[5]",
    contexts=[
        "Runs LLVM compiler out of memory [5",
        "Three volunteers sent us CDE packages, and we were able to reproduce all of their bugs: one that causes the Coq proof assistant to produce incorrect output (coq-bug-2443) [2], one that segfaults the GCC compiler (gcc-bug-46651) [3], and one that makes the LLVM compiler allocate an enormous amount of memory and crash (llvm-bug-8679) [5].",
        
    ],
))

DB(Citation(
    guo2011c,
    Site("Mac OS X Bundle Programming Guide:Introduction", "http://developer.apple.com/library/mac/#documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html"),
    ref="[6]",
    contexts=[
        "For example,MacOSXprogrammerscancreateapplication bundlesusingApple’sdevelopertoolsIDE[6]. Research prototypes like PDS [14], which creates self-contained Windowsapps,andtheCollective[23],whichaggregates a set of software into a portable virtual appliance, also require the user to manually specify dependencies.",
        
    ],
))

DB(Citation(
    guo2011c,
    Site("Saturnonlinediscussionthread", "https://mailman.stanford.edu/pipermail/saturn-discuss/2009-August/000174.html"),
    ref="[7]",
    contexts=[
        "Even the saturn team leader admitted in a public email, “As it stands the current release likely has problemsrunningonnewersystemsbecauseofbitrot—somelibraries and interfaces have evolved over the past couple of years in ways incompatible with the release.” [7",
        
    ],
))

DB(Citation(
    guo2011c,
    Site("Speccpu2006benchmarks", "http://www.spec.org/cpu2006/"),
    ref="[8]",
    contexts=[
        "benchmark suite (both integer and ﬂoating-point benchmarks)[8].",
        
    ],
))

DB(Citation(
    guo2011c,
    Site("SSHFilesystem", "http://fuse.sourceforge.net/sshfs.html"),
    ref="[9]",
    contexts=[
        "Whenauserwantstorunsomeapplication that is available on a particular distro, they use sshfs (an ssh-based network ﬁlesystem [9]) to mount the root directoryofthatdistrointoaspecial cde-remote-root/ mountpoint on their Linux machine.",
        
    ],
))

DB(Citation(
    guo2011c,
    Site("arachniproject home page", "https://github.com/Zapotek/arachni"),
    ref="[10]",
    contexts=[
        "arachni, a Ruby-based tool that audits web application security [10], requires six hard-to-compile Ruby extension modules, some of which depend on versions of Ruby and libraries that are not available in the pack",
        "Web app. security scanner framework [10",
        
    ],
))

DB(Citation(
    guo2011c,
    Site("graph-toolproject home page", "http://projects.skewed.de/graph-tool/"),
    ref="[11]",
    contexts=[
        "Python2.5orabove, expatlibrary,NumPyandSciPyPythonmodules,GCAL C++ geometry library, and Graphviz with Python bindings enabled.” [11",
        "Lib. for manipulation & analysis of graphs [11",
        
    ],
))

DB(Citation(
    guo2011c,
    Site("VMware ThinApp User’s Guide", "http://www.vmware.com/pdf/thinapp46_manual.pdf"),
    ref="[12]",
    contexts=[
        "However, a user can only create a package by having ThinApp monitor the installation of new software [12].",
        
    ],
))

DB(Citation(
    guo2011c, aiken2007a, ref="[13]",
    contexts=[
        "Static program analysis framework [13",
        "In addition, we used CDE to create portable binary packages for two of our Stanford colleagues’ research tools, which were originally distributed as tarballs of source code: pads [19] and saturn [13]",
        
    ],
))

DB(Citation(
    guo2011c, alpern2005a, ref="[14]",
    contexts=[
        "For example,MacOSXprogrammerscancreateapplication bundlesusingApple’sdevelopertoolsIDE[6]. Research prototypes like PDS [14], which creates self-contained Windowsapps,andtheCollective[23],whichaggregates a set of software into a portable virtual appliance, also require the user to manually specify dependencies.",
        
    ],
))

DB(Citation(
    guo2011c, altekar2009a, ref="[15]",
    contexts=[
        "In our experience, the results of many computational scienceexperimentscanbereproducedwithin CDE packagessincetheprogramsareoutput-deterministic[15],alwaysproducingthesameoutputs(e.g.,statistics,graphs) for a given input.",
        
    ],
))

DB(Citation(
    guo2011c, cadar2008a, ref="[16]",
    contexts=[
        "Automatic bug ﬁnder & test case generator [16",
        "Toensurethathecould later re-run and adjust experiments in response to reviewer critiques for a paper submission [16], our groupmate Cristian took the hard drive out of his computer at paper submission time and archived it in his drawer",
        "Similarly,weworkedwithlab-matestouse CDE todeploy the CPU-intensive klee [16] bug ﬁnding tool from the desktop to Amazon’s EC2 cloud computing service without needing to compile Klee on the cloud machines. Klee can be hard to compile since it depends on LLVM, which is very picky about speciﬁc versions of GCC and other build tools being present before it will compile.",
        "Use Klee [16] to symbolically execute a C target program (a STUN server) for 100,000 instructions, which generates 21 test cases.",
        
    ],
))

DB(Citation(
    guo2011c, chambers1991a, ref="[17]",
    contexts=[
        "We ran each benchmark ﬁve times under each condition and reportmeanrunningtimes. Weusedanindependenttwogroup t-test [17] to determine whether each slowdown was statistically signiﬁcant (i.e., whether the means of two sets of runs differed by a non-trivial amount).",
        
    ],
))

DB(Citation(
    guo2011c, dolstra2004a, ref="[18]",
    contexts=[
        "However, version mismatches andconﬂictsarecommonfrustrations,andinstallingnew softwarecanleadtoalibraryupgradethatbreaksexisting software [18].",
        "The Nix package manager is a research project that tries to eliminate dependency conﬂicts via stricterversioning,butitstillrequirespackagecreatorsto manually specify dependencies at creation time [18].",
        
    ],
))

DB(Citation(
    guo2011c, fisher2005a, ref="[19]",
    contexts=[
        "Language for processing ad-hoc data [19",
        "In addition, we used CDE to create portable binary packages for two of our Stanford colleagues’ research tools, which were originally distributed as tarballs of source code: pads [19] and saturn [13]",
        "Compile a PADS [19] speciﬁcation into C code (the “pads (compiler)” row in Table 3), and theninferaspeciﬁcationfromadataﬁle(the“pads (inferencer)” row in Table 3).",
        
    ],
))

DB(Citation(
    guo2011c, guo2011a, ref="[20]",
    contexts=[
        "of CDE in a short paper [20], this paper presents a more complete CDE system with three new features:",
        "We described the details of CDE’s design and implementation in a prior paper and its accompanying technical report [20].",
        "However, unlike chroot, CDE does not require root access to run, and its sandbox policies are ﬂexible and user-customizable [20].",
        "Encapsulating scripts and theirdependencieswithina CDE packagecanmakethem portable across distros and minor kernel versions; we have been able to take CDE packages created on 2010era Linux distros and run them on 2006-era distros [20",
        
    ],
))

DB(Citation(
    guo2011c, lahiri2010a, ref="[21]",
    contexts=[
        "Genetic algorithm for social networks [21",
        "Similarly,wehelpeda social networking researcher create a reproducible package for his genetic algorithm paper (gadm) [21]",
        "Reproduce the GADM experiment [21]: CompileitsC++sourcecode(‘C++comp’),rungenetic algorithm (‘algorithm’), and use the R statisticssoftwaretovisualizeoutputdata(‘makeplots’).",
        
    ],
))

DB(Citation(
    guo2011c, loper2002a, ref="[22]",
    contexts=[
        "Two users sent us CDE packages they created for collaboratingonclassassignments. Rahul,aStanfordgradstudent, was using NLTK [22], a Python module for natural language processing, to build a semantic email search engine(email-search)foramachinelearningclass.",
        
    ],
))

DB(Citation(
    guo2011c, sapuntzakis2003a, ref="[23]",
    contexts=[
        "For example,MacOSXprogrammerscancreateapplication bundlesusingApple’sdevelopertoolsIDE[6]. Research prototypes like PDS [14], which creates self-contained Windowsapps,andtheCollective[23],whichaggregates a set of software into a portable virtual appliance, also require the user to manually specify dependencies.",
        
    ],
))

DB(Citation(
    guo2011c, scaffidi2005a, ref="[24]",
    contexts=[
        "In addition, a study of US labor statistics predicts that by 2012, 13 million American workers will do programmingintheirjobs,butamongstthose,only3millionwill beprofessionalsoftwaredevelopers[24].",
        
    ],
))

DB(Citation(
    guo2011c, staelin1998a, ref="[25]",
    contexts=[
        "Abanalbuttricky detailthatpackagecreatorsmustworryaboutisadhering to platform-speciﬁc idioms for pathnames and avoiding hard-coding non-portable paths into their programs[25].",
        
    ],
))

DB(Citation(
    guo2011c, sucan2009a, ref="[26]",
    contexts=[
        "Robot motion planning algorithm [26",
        "A robotics researcher used CDE to make the experiments for his motion planning paper (kpiece)[26]fully-reproducible.",
        
    ],
))