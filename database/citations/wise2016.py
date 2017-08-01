# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2000 import abiteboul2000a
from ..work.y2002 import milo2002a
from ..work.y2006 import leoni2006a
from ..work.y2006 import ludascher2006a
from ..work.y2006 import tuffery2006a
from ..work.y2007 import fonseca2007b
from ..work.y2007 import grochow2007a
from ..work.y2007 import kinsy2007a
from ..work.y2008 import navlakha2008a
from ..work.y2009 import bao2009a
from ..work.y2009 import lacroix2009a
from ..work.y2009 import lacroix2009b
from ..work.y2009 import gervasio2009a
from ..work.y2009 import ludascher2009a
from ..work.y2010 import lacroix2010a
from ..work.y2011 import guo2011b
from ..work.y2012 import abdelkafi2012a
from ..work.y2012 import strauser2012a
from ..work.y2012 import szlavik2012a
from ..work.y2013 import horta2013a
from ..work.y2013 import huq2013a
from ..work.y2013 import xu2013a
from ..work.y2014 import chen2014a
from ..work.y2014 import claes2014a
from ..work.y2014 import filguiera2014a
from ..work.y2014 import murta2014a
from ..work.y2014 import starlinger2014a
from ..work.y2015 import acuna2015a
from ..work.y2015 import khan2015a
from ..work.y2015 import pienta2015a
from ..work.y2015 import acuna2015c
from ..work.y2016 import acuna2016a


DB(Citation(
    acuna2016a, abdelkafi2012a, ref="[1]",
    contexts=[
        "In the business domain, there is interest in creating andmining processes (i.e., workflows) from event logs to supportprocess discovery and performance analysis [1].",
        "Specifically, most methods do not provide insightinto the organization that implements the workflow or thestructure of the data it operates over [1].",
        
    ],
))

DB(Citation(
    acuna2016a, abiteboul2000a, ref="[2]",
    contexts=[
        "A related problem occurs in semi-structured data [2].Several approaches have been designed for databases andXML (e.g., [29])",
        
    ],
))

DB(Citation(
    acuna2016a, acuna2015c, ref="[3]",
    contexts=[
        "The overall WISE method is presentedin details on several scientific workflows in [3].",
        
    ],
))

DB(Citation(
    acuna2016a, acuna2015a, ref="[4]",
    contexts=[
        "Legacy workflows are first processed by the WISEmethod, first introduced in [4].",
        "Then, an equivalence analysisnot presented in [4] and described in more details inSection IV in performed in order to identify and merge allsimilar events into a more abstract data dependency graph.",
        
    ],
))

DB(Citation(
    acuna2016a, bao2009a, ref="[5]",
    contexts=[
        "n. The analysis of traces is also studied (e.g., [5]).Provenance tracking has been addressed for Python basedsystems in several ways (e.g., [13], [15], [24])",
        
    ],
))

DB(Citation(
    acuna2016a, chen2014a, ref="[6]",
    contexts=[
        "Previous work on analyzing and understanding dataflowin dynamic languages using compiling-time techniques hasencountered issues stemming from dynamic features (e.g.,[6]).",
        
    ],
))

DB(Citation(
    acuna2016a, claes2014a, ref="[7]",
    contexts=[
        "Instead of event logs, process mining algorithmsmay also consider data provenance (e.g., [7]).",
        
    ],
))

DB(Citation(
    acuna2016a, leoni2006a, ref="[8]",
    contexts=[
        "Workflow modeling, transformationand graph equivalence have been addressed for variousmodels (e.g., [8]).",
        
    ],
)) 

DB(Citation(
    acuna2016a, filguiera2014a, ref="[9]",
    contexts=[
        "Butworkflow authors may take a less structured approach with aworkflow programming language or a general programminglanguage with a workflow framework [9].",
        
    ],
))

DB(Citation(
    acuna2016a, fonseca2007b, ref="[10]",
    contexts=[
        "Some approaches use an ontology orconceptual modeling (e.g., [17], [10]).",
        
    ],
)) 

DB(Citation(
    acuna2016a, gervasio2009a, ref="[11]",
    contexts=[
        "Analysis may alsooccur on a log of user actions such as demonstrated inthe medical model sometimes with the aid on an ontology(see [11])",
        
    ],
))

DB(Citation(
    acuna2016a, grochow2007a, ref="[12]",
    contexts=[
        ". However, graph enumeration is slow and theproblem is similar to graph isomorphism, thus subgraphsare limited to around 15 nodes [12].",
        
    ],
))

DB(Citation(
    acuna2016a, guo2011b, ref="[13]",
    contexts=[
        "n. The analysis of traces is also studied (e.g., [5]).Provenance tracking has been addressed for Python basedsystems in several ways (e.g., [13], [15], [24])",
        
    ],
))

DB(Citation(
    acuna2016a, horta2013a, ref="[14]",
    contexts=[
        "Data provenance (e.g., [14]) canalso be leveraged to support data validation, reuse andintegration.",
        
    ],
))

DB(Citation(
    acuna2016a, huq2013a, ref="[15]",
    contexts=[
        "n. The analysis of traces is also studied (e.g., [5]).Provenance tracking has been addressed for Python basedsystems in several ways (e.g., [13], [15], [24])",
        
    ],
))

DB(Citation(
    acuna2016a, khan2015a, ref="[16]",
    contexts=[
        ". Cluster approaches (e.g., [16]), where groups of nodesare selected by some property, involve creating super-nodesand/or super-edges representing a more complex subgraph",
        
    ],
))

DB(Citation(
    acuna2016a, kinsy2007a, ref="[17]",
    contexts=[
        "Some approaches use an ontology orconceptual modeling (e.g., [17], [10]).",
        
    ],
))

DB(Citation(
    acuna2016a, lacroix2010a, ref="[18]",
    contexts=[
        "This mappingexploits a semantic map of bioinformatics resources [30],[18], [28].",
        "The workflow skeleton canthen be semantically indexed by identifying the resourcesrecorded by WISE in the library and use their conceptualrepresentation in a semantic map where each resource isregistered with its input and output as a labeled edgebetween its complex datatypes all mapped to a domainontology [18].",
        
    ],
))

DB(Citation(
    acuna2016a, lacroix2009b, ref="[19]",
    contexts=[
        "Finally, workflows representations can be storedin a database such as ProtocolDB [19] that supports thedocumentation of workflows in conceptual terms and thespecific resources used to implement each of their steps.",
        "The workflow may then be expressed asan implementation workflow in the ProtocolDB formalismmapped to a conceptual workflow which captures the aimof the workflow in the terms of a domain ontology [19] asillustrated with an example in Section V",
        
    ],
))

DB(Citation(
    acuna2016a, lacroix2009a, ref="[20]",
    contexts=[
        "The method provides the foundation for searching throughscientific workflows with conceptual queries and support ofreasoning on workflows [20].",
        
    ],
))

DB(Citation(
    acuna2016a, ludascher2006a, ref="[21]",
    contexts=[
        "Nowadays scientists can design and implement workflowswith a Workflow Management System (WFMS) [21]",
        
    ],
))

DB(Citation(
    acuna2016a, ludascher2009a, ref="[22]",
    contexts=[
        "In thebusiness realm, workflows are typically based on Petri nets(e.g., [22])",
        "Many scientificworkflows are not designed with a WFMS, or even a work-flow framework [22]",
        
    ],
))

DB(Citation(
    acuna2016a, milo2002a, ref="[23]",
    contexts=[
        "A more general approach is searching for frequent subgraphs(e.g., [23]).",
        
    ],
))

DB(Citation(
    acuna2016a, murta2014a, ref="[24]",
    contexts=[
        "Provenance trackingin ad-hoc workflows has had success in applying run-timetechniques (e.g., [24]) to record data but does not addressworkflow understanding",
        "n. The analysis of traces is also studied (e.g., [5]).Provenance tracking has been addressed for Python basedsystems in several ways (e.g., [13], [15], [24])",
        
    ],
))

DB(Citation(
    acuna2016a, navlakha2008a, ref="[25]",
    contexts=[
        "Handling these graphs can cause several problems:the graph may be too large to store in memory, graphalgorithms may become slow, and the volume of informationmay prevent understanding [25].",
        
    ],
))

DB(Citation(
    acuna2016a, pienta2015a, ref="[26]",
    contexts=[
        "This can be addressed with graph summarization (see [26] for a survey of existing methods).",
        
    ],
))

DB(Citation(
    acuna2016a, starlinger2014a, ref="[27]",
    contexts=[
        "Thisis similar to workflow similarity: single modules (i.e., tools)and whole workflows in [27]",
        
    ],
))

DB(Citation(
    acuna2016a, strauser2012a, ref="[28]",
    contexts=[
        "This mappingexploits a semantic map of bioinformatics resources [30],[18], [28].",
        
    ],
))

DB(Citation(
    acuna2016a, szlavik2012a, ref="[29]",
    contexts=[
        "A related problem occurs in semi-structured data [2].Several approaches have been designed for databases andXML (e.g., [29])",
        
    ],
))

DB(Citation(
    acuna2016a, tuffery2006a, ref="[30]",
    contexts=[
        "This mappingexploits a semantic map of bioinformatics resources [30],[18], [28].",
        "The method presented in the paper maps theworkflow skeleton produced by WISE to the ProtocolDBmodel with a conceptual representation of resources [30]",
        
    ],
))

DB(Citation(
    acuna2016a, xu2013a, ref="[31]",
    contexts=[
        "Despite using formalisms to model dynamics (e.g.,[31]), the execution of such programs has so few constrainsthat their behavior cannot be predicted.",
        
    ],
))