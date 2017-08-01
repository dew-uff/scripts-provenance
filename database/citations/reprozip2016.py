# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2008 import davidson2008a
from ..work.y2009 import donoho2009a
from ..work.y2009 import vandewalle2009a
from ..work.y2011 import freire2011b
from ..work.y2011 import bonnet2011a
from ..work.y2011 import tenopir2011a
from ..work.y2012 import guo2012b, guo2012a
from ..work.y2012 import begley2012a
from ..work.y2012 import davison2012a
from ..work.y2013 import chirigati2013b
from ..work.y2013 import pham2013a
from ..work.y2014 import devecsery2014a
from ..work.y2014 import janin2014a
from ..work.y2014 import murta2014a
from ..work.y2014 import ruiz2014a
from ..work.y2015 import collberg2015a
from ..work.y2015 import nuzzo2015a
from ..work.y2016 import chirigati2016a


DB(Citation(
    chirigati2016a, begley2012a, ref="[1]",
    contexts=[
        "Last but not least, recent studies indicate that reproducibility increases impact, visibility, and research quality [1, 26], and helps defeat self-deception [19].",
        
    ],
)) 

DB(Citation(
    chirigati2016a, bonnet2011a, ref="[2]",
    contexts=[
        "This diﬃculty discourages researchers from creating reproducible experiments, especially if the reason is solely for publication purposes [2, 5, 24].",
        
    ],
)) 

DB(Citation(
    chirigati2016a, 
    DB(Site("Chef", "https://www.chef.io/solutions/configuration-management/")),
    ref="[3]",
    contexts=[
        "Conﬁguration management tools [3, 21, 22] automate the conﬁguration of an experiment (e.g., installation of dependencies) by supporting the creation of “recipes” that can be reused every time a new machine needs to be conﬁgured; these scripts, however, need to be generated manually by researchers.",
        
    ],
))

DB(Citation(
    chirigati2016a, chirigati2013b, ref="[4]",
    contexts=[
        "In contrast to these approaches, ReproZip [4] provides a lightweight solution that makes experiments reproducible without forethought.",
        "The ﬁrst (beta) version of ReproZip was developed in 2013 [4]",
        "Portability is a signiﬁcant new feature of ReproZip, which previously could only unpack and reproduce experiments across Linux systems; more speciﬁcally, we only supported what is now the directory unpacker (see below) in our beta version [4]",
        
    ],
))

DB(Citation(
    chirigati2016a, collberg2015a, ref="[5]",
    contexts=[
        "This diﬃculty discourages researchers from creating reproducible experiments, especially if the reason is solely for publication purposes [2, 5, 24].",
        
    ],
)) 

DB(Citation(
    chirigati2016a, davidson2008a, ref="[6]",
    contexts=[
        "Scientiﬁc workﬂow systems [6] represent an experiment as a dataﬂow (or workﬂow), stitching together its diﬀerent steps and connecting data and processes in an executable representation.",
        
    ],
))

DB(Citation(
    chirigati2016a, davison2012a, ref="[7]",
    contexts=[
        "Last, there is a class of tools aimed at particular domains, e.g., GenePattern [12] is a genomic analysis platform, Madagascar [16] is used to analyze seismic data, Sumatra [7] is used for numerical computations, and noWorkﬂow [18] supports Python scripts only.",
        
    ],
))

DB(Citation(
    chirigati2016a, devecsery2014a, ref="[8]",
    contexts=[
        "Computational platforms, such as Burrito [14] and Arnold [8], capture the provenance of all processes at the operating system (OS) level, recording detailed state information, but only allow experiments to be replayed in the same system.",
        
    ],
))

DB(Citation(
    chirigati2016a, 
    DB(Site("Docker", "https://www.docker.com/")),
    ref="[9]",
    contexts=[
        "Lighterweight solutions exist for deploying and maintaining software containers, such as Docker [9], but similar to VMs, the researcher is faced with the burden of ensuring that all necessary dependencies are in the container",
        "The docker unpacker, on the other hand, unpacks and reproduces E in a Docker [9] container, either on the researcher’s own machine, a remote one, or on a cloud provider",
        
    ],
))

DB(Citation(
    chirigati2016a, donoho2009a, ref="[10]",
    contexts=[
        "In spite of its importance, achieving reproducibility has proved elusive for computational experiments, and this has led to a credibility crisis [10].",
        
    ],
))

DB(Citation(
    chirigati2016a, freire2011b, ref="[11]",
    contexts=[
        "Currently, ReproZip derives workﬂows that can be run on VisTrails [11]",
        
    ],
))

DB(Citation(
    chirigati2016a, 
    DB(Site("GenePattern", "http://www.broadinstitute.org/cancer/ software/genepattern/")),
    ref="[12]",
    contexts=[
        "Last, there is a class of tools aimed at particular domains, e.g., GenePattern [12] is a genomic analysis platform, Madagascar [16] is used to analyze seismic data, Sumatra [7] is used for numerical computations, and noWorkﬂow [18] supports Python scripts only.",
        
    ],
))

DB(Citation(
    chirigati2016a, guo2012b, ref="[13]",
    contexts=[
        "There are packaging systems that can help with reproducibility in the same without-forethought spirit as ReproZip, including CDE [13], PTU [20], and CARE [15].",
        
    ],
)) 

DB(Citation(
    chirigati2016a, guo2012a, ref="[14]",
    contexts=[
        "Computational platforms, such as Burrito [14] and Arnold [8], capture the provenance of all processes at the operating system (OS) level, recording detailed state information, but only allow experiments to be replayed in the same system.",
        
    ],
))

DB(Citation(
    chirigati2016a, janin2014a, ref="[15]",
    contexts=[
        "There are packaging systems that can help with reproducibility in the same without-forethought spirit as ReproZip, including CDE [13], PTU [20], and CARE [15].",
        
    ],
))

DB(Citation(
    chirigati2016a, 
    DB(Site("Madagascar", "http://www.ahay.org/wiki/Main_Page")),
    ref="[16]",
    contexts=[
        "Last, there is a class of tools aimed at particular domains, e.g., GenePattern [12] is a genomic analysis platform, Madagascar [16] is used to analyze seismic data, Sumatra [7] is used for numerical computations, and noWorkﬂow [18] supports Python scripts only.",
        
    ],
))

DB(Citation(
    chirigati2016a, 
    DB(Site("MongoDB", "http://www.mongodb.org/")),
    ref="[17]",
    contexts=[
        "The previous version of ReproZip used SystemTap [23] for tracing and MongoDB [17] for storage.",
        
    ],
))

DB(Citation(
    chirigati2016a, murta2014a, ref="[18]",
    contexts=[
        "Last, there is a class of tools aimed at particular domains, e.g., GenePattern [12] is a genomic analysis platform, Madagascar [16] is used to analyze seismic data, Sumatra [7] is used for numerical computations, and noWorkﬂow [18] supports Python scripts only.",
        
    ],
))

DB(Citation(
    chirigati2016a, nuzzo2015a, ref="[19]",
    contexts=[
        "Last but not least, recent studies indicate that reproducibility increases impact, visibility, and research quality [1, 26], and helps defeat self-deception [19].",
        
    ],
)) 

DB(Citation(
    chirigati2016a, pham2013a, ref="[20]",
    contexts=[
        "There are packaging systems that can help with reproducibility in the same without-forethought spirit as ReproZip, including CDE [13], PTU [20], and CARE [15].",
        
    ],
)) 

DB(Citation(
    chirigati2016a, 
    DB(Site("Puppet", "http://puppetlabs.com/")),
    ref="[21]",
    contexts=[
        "Conﬁguration management tools [3, 21, 22] automate the conﬁguration of an experiment (e.g., installation of dependencies) by supporting the creation of “recipes” that can be reused every time a new machine needs to be conﬁgured; these scripts, however, need to be generated manually by researchers.",
        
    ],
))

DB(Citation(
    chirigati2016a, ruiz2014a, ref="[22]",
    contexts=[
        "Conﬁguration management tools [3, 21, 22] automate the conﬁguration of an experiment (e.g., installation of dependencies) by supporting the creation of “recipes” that can be reused every time a new machine needs to be conﬁgured; these scripts, however, need to be generated manually by researchers.",
        
    ],
)) 

DB(Citation(
    chirigati2016a, 
    DB(Site("SystemTap", "http://sourceware.org/systemtap/")),
    ref="[23]",
    contexts=[
        "The previous version of ReproZip used SystemTap [23] for tracing and MongoDB [17] for storage.",
        
    ],
))

DB(Citation(
    chirigati2016a, tenopir2011a, ref="[24]",
    contexts=[
        "This diﬃculty discourages researchers from creating reproducible experiments, especially if the reason is solely for publication purposes [2, 5, 24].",
        
    ],
)) 

DB(Citation(
    chirigati2016a, 
    DB(Site("Vagrant", "https://www.vagrantup.com/")),
    ref="[25]",
    contexts=[
        "The vagrant unpacker allows E to be unpacked and reproduced inside a virtual machine automatically created through Vagrant [25].",
        
    ],
))

DB(Citation(
    chirigati2016a, vandewalle2009a, ref="[26]",
    contexts=[
        "Last but not least, recent studies indicate that reproducibility increases impact, visibility, and research quality [1, 26], and helps defeat self-deception [19].",
        
    ],
))