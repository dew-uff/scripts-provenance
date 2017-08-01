# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2000 import dike2000a
from ..work.y2005 import bellard2005a
from ..work.y2006 import cosmo2006a
from ..work.y2007 import spillane2007a
from ..work.y2009 import donoho2009a
from ..work.y2009 import vandewalle2009a
from ..work.y2010 import mesirov2010a
from ..work.y2010 import roundtable2010a
from ..work.y2010 import roundtable2010a
from ..work.y2011 import guo2011a, guo2011c
from ..work.y2011 import vincent2011a
from ..work.y2012 import freire2012a
from ..work.y2012 import ince2012a
from ..work.y2012 import leveque2012a
from ..work.y2013 import chirigati2013a
from ..work.y2013 import kim2013a
from ..work.y2013 import xavier2013a
from ..work.y2014 import janin2014a


DB(Citation(
    janin2014a,
    Site("CARE project home page", "http://reproducible.io"),
    ref="[1]",
    contexts=[
        "PRoot is GPLv2+ licensed. It can be downloaded directly from [7] (sources or binary packages for popular Linux distributions) or from external maintainer repositories (Debian, Gentoo, ArchLinux). CARE is GPLv2+ licensed and is available at [1].",
        
    ],
)) 

DB(Citation(
    janin2014a,
    Site("CDE project home page", "http://www.pgbovine.net/cde.html"),
    ref="[2]",
    contexts=[
        "CARE bears many similarities with CDE [2, 19, 20] (short for Code, Data and Environment).",
        
    ],
)) 

DB(Citation(
    janin2014a,
    Site("Docker, the Linux Container Engine", "http://www.docker.io"),
    ref="[3]",
    contexts=[
        "Tools empowered for reproducibility have raised signiﬁcant interest, and at least four recent projects can be mentioned: ReproZip [14], Docker [3], CDE, and CARE. These tools considerably diﬀer in their goals, principles and technical maturities. Table 3 summarizes their main technical diﬀerences.",
        
    ],
)) 

DB(Citation(
    janin2014a,
    Site("Docutils, Documentation Utilities", "http://docutils.sourceforge.net"),
    ref="[4]",
    contexts=[
        "See references [4, 6, 10] for source packages",
        
    ],
)) 

DB(Citation(
    janin2014a,
    Site("LXC project home page", "http://www.linuxcontainers.org"),
    ref="[5]",
    contexts=[
        "Since archive building and re-execution are really independent steps, it is possible to propose alternative re-execution modes where PRoot is not used anymore. Two new modes were investigated, the ﬁrst one based on chroot, the second one on the lxc containers [5].",
        
    ],
)) 

DB(Citation(
    janin2014a,
    Site("MoarVM, A VM for NQP And Rakudo Perl 6", "http://moarvm.com"),
    ref="[6]",
    contexts=[
        "See references [4, 6, 10] for source packages",
        
    ],
)) 

DB(Citation(
    janin2014a,
    Site("PRoot project home page", "http://proot.me"),
    ref="[7]",
    contexts=[
        "PRoot is GPLv2+ licensed. It can be downloaded directly from [7] (sources or binary packages for popular Linux distributions) or from external maintainer repositories (Debian, Gentoo, ArchLinux). CARE is GPLv2+ licensed and is available at [1].",
        
    ],
)) 

DB(Citation(
    janin2014a,
    Site("QEMU project home page", "http://www.qemu.org"),
    ref="[8]",
    contexts=[
        "CPU emulation may also be helpful to re-execute archives produced on embedded Linux targets. For instance, QEMU [8, 13, 28] can be used to re-execute ARM archives on x86 64 workstations.",
        
    ],
)) 

DB(Citation(
    janin2014a,
    Site("The Linux man-pages project", "https://www.kernel.org/doc/man-pages"),
    ref="[9]",
    contexts=[
        "CARE relies on two key observations: First, system calls are ’the fundamental interfaces between an application and the Linux kernel’ [9].",
        "Second, system calls can be monitored by the ptrace system call that ’provides a means by which a parent may observe and control the execution of another process’ [9].",
        
    ],
)) 

DB(Citation(
    janin2014a,
    Site("The Perl programming language", "http://www.perl.org"),
    ref="[10]",
    contexts=[
        "See references [4, 6, 10] for source packages",
        
    ],
)) 

DB(Citation(
    janin2014a,
    Site("The Slackware Linux project", "http://www.slackware.com"),
    ref="[11]",
    contexts=[
        "A typical example for a CARE run performed on Slackware64-14.1 Linux distribution [11].",
        
    ],
)) 

DB(Citation(
    janin2014a,
    Site("XZ Utils", "http://tukaani.org/xz"),
    ref="[12]",
    contexts=[
        "d of Perl-5.18.2, conﬁgure.gnu and make -j4 (see Figure 1). For the third test, we built Perl-5.18.2 with make running only a single job. For the fourth test, we used the xz utility [12]",
        
    ],
))

DB(Citation(
    janin2014a, bellard2005a, ref="[13]",
    contexts=[
        "CPU emulation may also be helpful to re-execute archives produced on embedded Linux targets. For instance, QEMU [8, 13, 28] can be used to re-execute ARM archives on x86 64 workstations.",
        
    ],
))

DB(Citation(
    janin2014a, chirigati2013a, ref="[14]",
    contexts=[
        "Tools empowered for reproducibility have raised signiﬁcant interest, and at least four recent projects can be mentioned: ReproZip [14], Docker [3], CDE, and CARE. These tools considerably diﬀer in their goals, principles and technical maturities. Table 3 summarizes their main technical diﬀerences.",
        
    ],
))

DB(Citation(
    janin2014a, cosmo2006a, ref="[15]",
    contexts=[
        "In general, managing dependency conﬂicts is diﬃcult, and in 2006 Di Cosmo et al. [15] proved that deciding whether a single package can be installed conﬂict-free in a given repository is an NP-complete problem.",
        
    ],
)) 

DB(Citation(
    janin2014a, dike2000a, ref="[16]",
    contexts=[
        "elegant method to solve a variety of software engineering problems has a long history, and many applications were proposed from the use of ptrace to ease ﬁle system developments [26] to User Mode Linux [16] a port of the Linux kernel in userland.",
        
    ],
)) 

DB(Citation(
    janin2014a, donoho2009a, ref="[17]",
    contexts=[
        "The lack of reproducibility in computer science is now recognized as a real problem [17]: workshops or meetings [24, 23] dedicated to the topic are regularly organized and highlyranked conferences have begun promoting new publishing models where reproducibility and artifact evaluation are at the heart of the strategy.",
        
    ],
))

DB(Citation(
    janin2014a, freire2012a, ref="[18]",
    contexts=[
        "A computational experiment is reproducible [18] if (1) it can be re-executed on a machine whose software or hardware stack diﬀer, (2) it can be re-executed on a data set that is similar but not necessarily identical to the original data set",
        
    ],
)) 

DB(Citation(
    janin2014a, guo2011c, ref="[19]",
    contexts=[
        "CARE bears many similarities with CDE [2, 19, 20] (short for Code, Data and Environment).",
        "Performance results in Table 2 (and others not presented in this paper for the sake of brevity) are globally coherent with those published for CDE evaluation [19].",
        
    ],
))

DB(Citation(
    janin2014a, guo2011a, ref="[20]",
    contexts=[
        "CARE bears many similarities with CDE [2, 19, 20] (short for Code, Data and Environment).",
        "Finally, it is worth mentioning that there is a whole class of system calls where CDE and CARE take opposite decisions when building an archive. For instance, if we consider again the very same example rename(”./old”, ”./new”), CDE will suppress old from the archive (assuming that it has previously been stored there) and copy new [20].",
        
    ],
))

DB(Citation(
    janin2014a, ince2012a, ref="[21]",
    contexts=[
        "Although neither a necessary nor a suﬃcient condition, a strong argument in favor of open source or free software [21] stems from the possibility for any user to access the code, data and build systems of every artifact, tool or software package involved in the reproducibility chain.",
        
    ],
)) 

DB(Citation(
    janin2014a, kim2013a, ref="[22]",
    contexts=[
        "The ﬁeld remains active with CDE in 2011 and even more recently MBox [22] described by their authors as a lightweight sandboxing mechanism for non-root users",
        
    ],
))

DB(Citation(
    janin2014a, leveque2012a, ref="[23]",
    contexts=[
        "The lack of reproducibility in computer science is now recognized as a real problem [17]: workshops or meetings [24, 23] dedicated to the topic are regularly organized and highlyranked conferences have begun promoting new publishing models where reproducibility and artifact evaluation are at the heart of the strategy.",
        
    ],
)) 

DB(Citation(
    janin2014a, roundtable2010a, ref="[24]",
    contexts=[
        "The lack of reproducibility in computer science is now recognized as a real problem [17]: workshops or meetings [24, 23] dedicated to the topic are regularly organized and highlyranked conferences have begun promoting new publishing models where reproducibility and artifact evaluation are at the heart of the strategy.",
        
    ],
))

DB(Citation(
    janin2014a, mesirov2010a, ref="[25]",
    contexts=[
        "it is no surprise that scientists from various other backgrounds also expressed their concern or proposed solutions adapted to their domain [25, 27].",
        
    ],
)) 

DB(Citation(
    janin2014a, spillane2007a, ref="[26]",
    contexts=[
        "elegant method to solve a variety of software engineering problems has a long history, and many applications were proposed from the use of ptrace to ease ﬁle system developments [26] to User Mode Linux [16] a port of the Linux kernel in userland.",
        
    ],
))

DB(Citation(
    janin2014a, vandewalle2009a, ref="[27]",
    contexts=[
        "it is no surprise that scientists from various other backgrounds also expressed their concern or proposed solutions adapted to their domain [25, 27].",
        
    ],
))

DB(Citation(
    janin2014a, vincent2011a, ref="[28]",
    contexts=[
        "CPU emulation may also be helpful to re-execute archives produced on embedded Linux targets. For instance, QEMU [8, 13, 28] can be used to re-execute ARM archives on x86 64 workstations.",
        
    ],
))

DB(Citation(
    janin2014a, xavier2013a, ref="[29]",
    contexts=[
        "Therefore, although this point is clearly out of the scope of this paper, we can expect smaller performance penalties [29].",
        
    ],
))