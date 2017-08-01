# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import tariq2012a
from ..work.y2013 import tsai2013a
from ..work.y2014 import lerner2014a
from ..work.y2014 import murta2014a
from ..work.y2015 import mcphillips2015b
from ..work.y2015 import dey2015a
from ..work.y2016 import pimentel2016c
from ..work.y2016 import pimentel2016b
from ..work.y2016 import pimentel2016d


DB(Citation(
    pimentel2016c, dey2015a, ref="[1]",
    contexts=[
        "Given the contrasting aims of noWorkflow and YesWorkflow and the differencesin the approaches they take, it is not surprising that each supports queries and visualizationsthat the other cannot support on its own [1].",
        
    ],
))

DB(Citation(
    pimentel2016c, lerner2014a, ref="[2]",
    contexts=[
        "Some of these approaches are language-specific, e.g., noWorkflow1[4,5](Python) and RDataTracker [2] (R scripts), while others are language-independent, e.g.,YesWorkflow2[3] and LLVM/SPADE [7].",
        "Using such tools often entails annotating thescripts [2,3], monitoring executing scripts as they run [7,4], or both.",
        
    ],
))

DB(Citation(
    pimentel2016c, mcphillips2015b, ref="[3]",
    contexts=[
        "Some of these approaches are language-specific, e.g., noWorkflow1[4,5](Python) and RDataTracker [2] (R scripts), while others are language-independent, e.g.,YesWorkflow2[3] and LLVM/SPADE [7].",
        "Using such tools often entails annotating thescripts [2,3], monitoring executing scripts as they run [7,4], or both.",
        "We use the Python script described by McPhillips et al. [3] to demonstrate the kinds ofprovenance queries NW, YW, and the combination of both support",
        "The complete script, marked up with YW annotations,is available on GitHub [6]; a more complete explanation is provided in [3]",
        "YW can also answer some retrospective provenance queries [3], including: Whatsamples did the run of the script collect images from? What energies were used duringcollection of images from sample DRT240? Where is the raw image from which correctedimage run/data/DRT322/DRT322_10000eV_001.img is derived? Are there anyraw images for which there are no corresponding corrected images?",
        "This lineage graph can be constructedas a subgraph of the original YW model [3] (restricted to predecessors nodes upstreamof the corrected_image result node), which is then augmented with NW retrospectiveprovenance; see [6] for details and the YW*NW integration queries",
        
    ],
))

DB(Citation(
    pimentel2016c, murta2014a, ref="[4]",
    contexts=[
        "Some of these approaches are language-specific, e.g., noWorkflow1[4,5](Python) and RDataTracker [2] (R scripts), while others are language-independent, e.g.,YesWorkflow2[3] and LLVM/SPADE [7].",
        "Using such tools often entails annotating thescripts [2,3], monitoring executing scripts as they run [7,4], or both.",
        
    ],
))

DB(Citation(
    pimentel2016c, pimentel2016b, ref="[5]",
    contexts=[
        "Some of these approaches are language-specific, e.g., noWorkflow1[4,5](Python) and RDataTracker [2] (R scripts), while others are language-independent, e.g.,YesWorkflow2[3] and LLVM/SPADE [7].",
        
    ],
))

DB(Citation(
    pimentel2016c, pimentel2016d, ref="[6]",
    contexts=[
        "The complete script, marked up with YW annotations,is available on GitHub [6]; a more complete explanation is provided in [3]",
        "This lineage graph can be constructedas a subgraph of the original YW model [3] (restricted to predecessors nodes upstreamof the corrected_image result node), which is then augmented with NW retrospectiveprovenance; see [6] for details and the YW*NW integration queries",
        "A companion GitHub repository for this demonstration is available, along with anexpanded version of this short demo description [6].",
        
    ],
))

DB(Citation(
    pimentel2016c, tariq2012a, ref="[7]",
    contexts=[
        "Some of these approaches are language-specific, e.g., noWorkflow1[4,5](Python) and RDataTracker [2] (R scripts), while others are language-independent, e.g.,YesWorkflow2[3] and LLVM/SPADE [7].",
        "Using such tools often entails annotating thescripts [2,3], monitoring executing scripts as they run [7,4], or both.",
        
    ],
))

DB(Citation(
    pimentel2016c, tsai2013a, ref="[8]",
    contexts=[
        "Although the script only simulates data collection, the order of task execution,the sequence of data production events, and the resulting pattern of dependenciesbetween input, intermediate, and final data items closely mimic those of a real experiment[8].",
        
    ],
))