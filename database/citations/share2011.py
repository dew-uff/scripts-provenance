# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1984 import knuth1984a
from ..work.y1992 import claerbout1992a
from ..work.y2009 import keahey2009a
from ..work.y2009 import nurmi2009a
from ..work.y2009 import wang2009a
from ..work.y2010 import antoy2010a
from ..work.y2010 import gorp2010a
from ..work.y2011 import gorp2011a
from ..work.y2011 import mazanek2011a


DB(Citation(
    gorp2011a, gorp2010a, ref="[1]",
    contexts=[
        "SHARE [1] has emerged from the organization of the Transformation Tool Contest (TTC, formerly known asGraBaTs), a yearly event aimed at the evaluation and dissemination of advanced transformation techniques and relatedsoftware1.",
        "Eucalyptus [10] and the Grid Virtualization Engine (GVE [11]) are open source cloud computing platforms thatare similar to Nimbus but that put more emphasis on the use ofstandardweb service technologies such as WSDL andBPEL [1]. A",
        "All of the Claerbout-based executable papers, thus,can be made permanently reproducible inside SHARE. [1]",
        "As discussed in [1], onecould install in SHARE virtual machines existing software for tracking events (keybord and mouse actions) toprovide more detailed provenance functionality.",
        
    ],
))

DB(Citation(
    gorp2011a, 
    DB(Site("Business Process Modeling Notation (BPMN)", "http://www.omg.org/spec/BPMN/1.2/(2009)")),
    ref="[2]",
    contexts=[
        "The example SHARE virtual machine2contains a solution for the BPMN-to-BPEL case [2, 3, 4] of the Trans-formation Tool Contest 2009.",
        
    ],
))

DB(Citation(
    gorp2011a, 
    DB(Site("Web Services Business Process Execution Language Version 2.0", "http://docs.oasis-open.org/wsbpel/2.0/wsbpel-v2.0.pdf")),
    ref="[3]",
    contexts=[
        "The example SHARE virtual machine2contains a solution for the BPMN-to-BPEL case [2, 3, 4] of the Trans-formation Tool Contest 2009.",
        
    ],
    accessed="2007",
))

DB(Citation(
    gorp2011a, 
    DB(Site("Case study: BPMN to BPEL model transformation", "http://is.ieis.tue.nl/staff/pvgorp/events/grabats2009/cases/grabats2009synthesis.pdf",
            authors="M. Dumas")),
    ref="[4]",
    contexts=[
        "The example SHARE virtual machine2contains a solution for the BPMN-to-BPEL case [2, 3, 4] of the Trans-formation Tool Contest 2009.",
        
    ],
    accessed="2009",
))

DB(Citation(
    gorp2011a, mazanek2011a, ref="[5]",
    contexts=[
        "A discussion of this solution has been submitted after the contest to a special issue ofElsevier’s “Journal of Visual Languages and Computing” and has been published in the meanwhile [5].",
        
    ],
))

DB(Citation(
    gorp2011a, knuth1984a, ref="[6]",
    contexts=[
        "The article under consideration actually is a literate program [6] and, thus, directly executable.",
        
    ],
))

DB(Citation(
    gorp2011a, 
    DB(Site("Curry: An Integrated Functional Logic Language (Version 0.8.2)", "http://www.curry-language.org/",
            authors="M. Hanus")),
    ref="[7]",
    contexts=[
        "The LATEX filescontain the complete program source code already. The text of the article is realized using comments of the respectiveprogramming language, here Curry [7, 8].",
        
    ],
    accessed="2006",
))

DB(Citation(
    gorp2011a, antoy2010a, ref="[8]",
    contexts=[
        "The LATEX filescontain the complete program source code already. The text of the article is realized using comments of the respectiveprogramming language, here Curry [7, 8].",
        
    ],
))

DB(Citation(
    gorp2011a, keahey2009a, ref="[9]",
    contexts=[
        "As a running example, the authorsdynamically aggregate computational resources from three dierent universities to satisfy the service level agreements(SLAs) for heavyweight biomedical computations [9].",
        
    ],
))

DB(Citation(
    gorp2011a, nurmi2009a, ref="[10]",
    contexts=[
        "Eucalyptus [10] and the Grid Virtualization Engine (GVE [11]) are open source cloud computing platforms thatare similar to Nimbus but that put more emphasis on the use ofstandardweb service technologies such as WSDL andBPEL [1]. A",
        
    ],
))

DB(Citation(
    gorp2011a, wang2009a, ref="[11]",
    contexts=[
        "Eucalyptus [10] and the Grid Virtualization Engine (GVE [11]) are open source cloud computing platforms thatare similar to Nimbus but that put more emphasis on the use ofstandardweb service technologies such as WSDL andBPEL [1]. A",
        
    ],
)) 

DB(Citation(
    gorp2011a, claerbout1992a, ref="[12]",
    contexts=[
        "Seminal work related to executable papers has been contributed by Claerbout et al. in the early nineties [12].",
        
    ],
))