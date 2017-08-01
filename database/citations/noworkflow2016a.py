# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1977 import hunt1977a
from ..work.y1998 import conradi1998a
from ..work.y2003 import collberg2003a
from ..work.y2004 import altintas2004a
from ..work.y2006 import callahan2006b
from ..work.y2007 import murta2007a
from ..work.y2008 import freire2008a
from ..work.y2008 import bochner2008a
from ..work.y2010 import angelino2010a
from ..work.y2010 import mattoso2010a
from ..work.y2012 import davison2012a
from ..work.y2012 import tariq2012a
from ..work.y2013 import koop2013a
from ..work.y2014 import lerner2014a
from ..work.y2014 import murta2014a
from ..work.y2014 import stamatogiannakis2014a
from ..work.y2015 import mcphillips2015a
from ..work.y2015 import pimentel2015a
from ..work.y2016 import pimentel2016a
from ..work.y2016 import pimentel2016b


DB(Citation(
    pimentel2016a, altintas2004a, ref="[1]",
    contexts=[
        "Finally, workflow-based provenance tools [1, 4] track provenance from scientific experiments. Some tools, such as Vistrails [4] and Kepler [1], not only track the provenance, but also track the workflow evolution and offers all the data for users to analyze it",
        
    ],
))

DB(Citation(
    pimentel2016a, angelino2010a, ref="[2]",
    contexts=[
        "In the last decade some approaches emerged for capturing provenance from experiments encoded in scripts [2, 3, 11, 14, 19].",
        "StarFlow [2] and RDataTracker [11] collect provenance from scripts through dynamic analysis and annotations.",
        
    ],
))

DB(Citation(
    pimentel2016a, bochner2008a, ref="[3]",
    contexts=[
        "In the last decade some approaches emerged for capturing provenance from experiments encoded in scripts [2, 3, 11, 14, 19].",
        "Bochner et al. [3] collect provenance from scripts using a library to connect to a remote server and send annotated provenance data.",
        
    ],
))

DB(Citation(
    pimentel2016a, callahan2006b, ref="[4]",
    contexts=[
        "Finally, workflow-based provenance tools [1, 4] track provenance from scientific experiments. Some tools, such as Vistrails [4] and Kepler [1], not only track the provenance, but also track the workflow evolution and offers all the data for users to analyze it",
        
    ],
))

DB(Citation(
    pimentel2016a, collberg2003a, ref="[5]",
    contexts=[
        "Developers can also use external visualization tools to have a broader view of source code evolution [5].",
        
    ],
))

DB(Citation(
    pimentel2016a, conradi1998a, ref="[6]",
    contexts=[
        "Many configuration management tools, such as Git, track the evolution of software through versioning [6].",
        "Conradi and Westfechtel [6] state that a version model should define the organization of the version space (i.e., how a product is versioned) and the interrelation of the product space (i.e., how a product is structured) and the version space",
        "Our version space [6] has two levels of versioning: trial version (i.e., the trial id) and file object version.",
        
    ],
))

DB(Citation(
    pimentel2016a, davison2012a, ref="[7]",
    contexts=[
        "An outstanding exception in this category is Sumatra [7]. It stores each trial in a configuration management tool (either Git or Mercurial) and allows users to tag them and to compare the collected information.",
        
    ],
))

DB(Citation(
    pimentel2016a, freire2008a, ref="[8]",
    contexts=[
        ". Although generic and fast, these tools capture only prospective provenance [8] at coarse grain, when used to version experiment scripts.",
        "In other words, they do not capture fine-grained prospective provenance [8] nor retrospective provenance [8].",
        
    ],
))

DB(Citation(
    pimentel2016a, hunt1977a, ref="[9]",
    contexts=[
        "Then, it applies the longest common subsequence (LCS) algorithm [9] over the lists.",
        
    ],
))

DB(Citation(
    pimentel2016a, koop2013a, ref="[10]",
    contexts=[
        "We already started looking for existing graph matching techniques [10].",
        
    ],
))

DB(Citation(
    pimentel2016a, lerner2014a, ref="[11]",
    contexts=[
        "In the last decade some approaches emerged for capturing provenance from experiments encoded in scripts [2, 3, 11, 14, 19].",
        "StarFlow [2] and RDataTracker [11] collect provenance from scripts through dynamic analysis and annotations.",
        
    ],
))

DB(Citation(
    pimentel2016a, mattoso2010a, ref="[12]",
    contexts=[
        "The life cycle of script-based experiments is usually composed of three main phases [12]: establishing hypotheses and coding scripts that enact the programs involved in the experiment; running the script over input data, which represent a specific context or population for the experiment; and analyzing the produced results through visualizations or queries to confirm the research hypotheses",
        
    ],
))

DB(Citation(
    pimentel2016a, mcphillips2015a, ref="[13]",
    contexts=[
        "YesWorkflow [13] captures prospective provenance from scripts through annotations",
        
    ],
))

DB(Citation(
    pimentel2016a, murta2014a, ref="[14]",
    contexts=[
        "In the last decade some approaches emerged for capturing provenance from experiments encoded in scripts [2, 3, 11, 14, 19].",
        "As a proof of concept, we implemented our version model on top of noWorkflow [14, 16, 17]",
        "noWorkflow [14] collects provenance from scripts without requiring any modifications on the script.",
        "Most of these approaches capture execution provenance (i.e., retrospective provenance) [14] with intermediate data, and support querying and visualizing provenance during analysis",
        "File objects describe the structure of the experiment: that is, all files needed by the experiment, which includes the script itself (definition provenance [14]), imported modules (deployment provenance [14]), and accessed (read/write) files (execution provenance [14]).",
        "We implemented the proposed approach on top of noWorkflow [14].",
        
    ],
))


DB(Citation(
    pimentel2016a, murta2007a, ref="[15]",
    contexts=[
        "On the other hand, this is known to compromise scalability in terms of execution time and storage space [15].",
        
    ],
))

DB(Citation(
    pimentel2016a, pimentel2016b, ref="[16]",
    contexts=[
        "As a proof of concept, we implemented our version model on top of noWorkflow [14, 16, 17]",
        
    ],
))

DB(Citation(
    pimentel2016a, pimentel2015a, ref="[17]",
    contexts=[
        "As a proof of concept, we implemented our version model on top of noWorkflow [14, 16, 17]",
        
    ],
))

DB(Citation(
    pimentel2016a, stamatogiannakis2014a, ref="[18]",
    contexts=[
        "Stamatogiannakis et al. [18] perform dynamic taint analysis on binary files to capture provenance.",
        
    ],
))

DB(Citation(
    pimentel2016a, tariq2012a, ref="[19]",
    contexts=[
        "In the last decade some approaches emerged for capturing provenance from experiments encoded in scripts [2, 3, 11, 14, 19].",
        "Tariq et al. [19] collect provenance from code compiled with a LLVM compiler",
        
    ],
))
