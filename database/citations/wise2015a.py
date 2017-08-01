# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1992 import rivest1992a
from ..work.y1998 import agrawal1998a
from ..work.y2000 import abiteboul2000a
from ..work.y2000 import gansner2000a
from ..work.y2001 import brandes2001a
from ..work.y2003 import lacroix2003a
from ..work.y2004 import deelman2004b
from ..work.y2004 import aalst2004a
from ..work.y2006 import dufour2006a
from ..work.y2006 import hull2006a
from ..work.y2006 import tuffery2006a
from ..work.y2007 import kinsy2007a
from ..work.y2007 import lacroix2007a
from ..work.y2007 import liyong2007a
from ..work.y2007 import yaman2007a
from ..work.y2008 import hoffa2008a
from ..work.y2008 import johnson2008a
from ..work.y2008 import vouk2008a
from ..work.y2009 import bao2009b
from ..work.y2009 import lacroix2009a
from ..work.y2009 import bolz2009a
from ..work.y2009 import burstein2009a
from ..work.y2009 import cock2009a
from ..work.y2009 import gervasio2009a
from ..work.y2009 import lonquety2009a
from ..work.y2010 import goecks2010a
from ..work.y2010 import lou2010a
from ..work.y2010 import miller2010a
from ..work.y2011 import guo2011b
from ..work.y2012 import abouelhoda2012a
from ..work.y2012 import acuna2012a
from ..work.y2012 import madeira2012a
from ..work.y2012 import silva2012a
from ..work.y2013 import huq2013a
from ..work.y2013 import perry2013a
from ..work.y2014 import johnson2014a
from ..work.y2014 import lei2014a
from ..work.y2014 import murta2014a
from ..work.y2015 import acuna2015a


DB(Citation(
    acuna2015a, deelman2004b, ref="[1]",
    contexts=[
        "Large scale computing was first enabled by the adventof Grid computing. Workflow management systems (WFMS)that target Grid computing environments, such as Pegasus[1],",
        
    ],
))

DB(Citation(
    acuna2015a, vouk2008a, ref="[2]",
    contexts=[
        "However, the Gridenvironment has limitations with resource availability andmaintenance overhead [2], [3].",
        
    ],
))

DB(Citation(
    acuna2015a, hoffa2008a, ref="[3]",
    contexts=[
        "However, the Gridenvironment has limitations with resource availability andmaintenance overhead [2], [3].",
        ". Cloud computing has addressedmany of these practical concerns by providing a distributedand uniform environment [3].",
        ". One aspect of cloud computingis to execute workflows on extremely large datasets such asneeded by bioinformatics. Cloud computing can provide bothtractability and scalability for such work (see [3] for a concretecase)",
        
    ],
))

DB(Citation(
    acuna2015a, liyong2007a, ref="[4]",
    contexts=[
        "One approach to legacy workflow reuseis encapsulating them as resources which can be deployed bya larger Cloud or Grid aware workflow [4].",
        
    ],
))

DB(Citation(
    acuna2015a, goecks2010a, ref="[5]",
    contexts=[
        "While systemsadapted to execution on a local system, such as Galaxy [5],are suitable to run on the cloud environment others are lessappropriate (e.g., Taverna [6], oriented to service utilization).",
        
    ],
))

DB(Citation(
    acuna2015a, hull2006a, ref="[6]",
    contexts=[
        "While systemsadapted to execution on a local system, such as Galaxy [5],are suitable to run on the cloud environment others are lessappropriate (e.g., Taverna [6], oriented to service utilization).",
        
    ],
))

DB(Citation(
    acuna2015a, abouelhoda2012a, ref="[7]",
    contexts=[
        "This leads to the need for mapping workflows designed fora given WFMS to another, to benefit from a more efficientenvironment. For instance, Tavaxy [7] provides interoperabilitybetween Taverna and Galaxy.",
        
    ],
))

DB(Citation(
    acuna2015a, huq2013a, ref="[8]",
    contexts=[
        "Although methods for tracking provenancein ad-hoc workflow provide mechanisms to detect and recorddataflow (e.g., [8], [9]),",
        
    ],
))

DB(Citation(
    acuna2015a, murta2014a, ref="[9]",
    contexts=[
        "Although methods for tracking provenancein ad-hoc workflow provide mechanisms to detect and recorddataflow (e.g., [8], [9]),",
        
    ],
))

DB(Citation(
    acuna2015a, agrawal1998a, ref="[10]",
    contexts=[
        "Constructing process modelswas first presented, for logs produced by IBM Flowmark, in[10].",
        
    ],
))

DB(Citation(
    acuna2015a, aalst2004a, ref="[11]",
    contexts=[
        "Other types of process models such as Petri nets havealso been explored [11]",
        
    ],
))

DB(Citation(
    acuna2015a, lou2010a, ref="[12]",
    contexts=[
        "The issue ofconcurrent workflow logs, by using temporal dependencies andrefinement is addressed in [12].",
        
    ],
))

DB(Citation(
    acuna2015a, yaman2007a, ref="[13]",
    contexts=[
        "For traces produced by an expert user usingservices in a medical domain, [13] presented a model mergingtechnique to learn repetition and branching",
        
    ],
))

DB(Citation(
    acuna2015a, burstein2009a, ref="[14]",
    contexts=[
        "This was exploredmore fully in the POIROT project [14] which combines traceanalysis and learning methods to deduce procedural models.",
        
    ],
))

DB(Citation(
    acuna2015a, gervasio2009a, ref="[15]",
    contexts=[
        "An ontology query method to infer regions of missing dataflowwas used for traces produced by expert users which includeunobservable choices or actions in [15].",
        "The secondary issue of determining what latent decisions115were made or not in a workflow’s execution, dependent oninput, is analogous to that of determining the unobservablechoices made by a human operator when implementing aprocedural workflow, a problem examined in [15]",
        
    ],
))

DB(Citation(
    acuna2015a, bao2009b, ref="[16]",
    contexts=[
        "Analysis of traces forprovenance is also valuable, for instance [16] gives a methodfor differencing executions to understand provenance.",
        
    ],
))

DB(Citation(
    acuna2015a, lacroix2003a, ref="[17]",
    contexts=[
        "Scientific data management and bioinformatics provide anactive application domain for workflows as discussed in [17],[18].",
        
    ],
))

DB(Citation(
    acuna2015a, lacroix2007a, ref="[18]",
    contexts=[
        "Scientific data management and bioinformatics provide anactive application domain for workflows as discussed in [17],[18].",
        
    ],
))

DB(Citation(
    acuna2015a, acuna2012a, ref="[19]",
    contexts=[
        "In [19], we first discussed the various impacts of work-flow transformation and illustrated them with a case study onthe Structural Prediction for pRotein fOlding UTility System(SPROUTS) Workflow [20].",
        "This is partially due to the use of code thatunintentionally invokes many dynamic language features [19].",
        
    ],
))

DB(Citation(
    acuna2015a, lonquety2009a, ref="[20]",
    contexts=[
        "In [19], we first discussed the various impacts of work-flow transformation and illustrated them with a case study onthe Structural Prediction for pRotein fOlding UTility System(SPROUTS) Workflow [20].",
        
    ],
))

DB(Citation(
    acuna2015a, dufour2006a, ref="[21]",
    contexts=[
        "Work such as Shed Skin [21] haveattempted to provide type inference functionality, and in theprocess have demonstrated the issues with static analysis inPython.",
        
    ],
))

DB(Citation(
    acuna2015a, guo2011b, ref="[22]",
    contexts=[
        ". Other work related to dataflow in Pythonprograms has taken the approach of creating an instrumentedinterpreter [22].",
        
    ],
))

DB(Citation(
    acuna2015a, bolz2009a, ref="[23]",
    contexts=[
        "If another interpreter such as PyPy [23] is used, orif the interpreter is running on a different operating system,the instrumentation will still function.",
        
    ],
))

DB(Citation(
    acuna2015a, abiteboul2000a, ref="[24]",
    contexts=[
        "This is a similarsituation as systems trying to determine how data are producedon the Web. Although fully structured by the authority thatdesigned the Web resource, they appear to the other end semistructuredas their structure may have desiccated over time[24].",
        
    ],
))

DB(Citation(
    acuna2015a, silva2012a, ref="[25]",
    contexts=[
        "This can be seen as a problem of programslicing [25], where the goal is to determine exactly the partof the workflow orchestrational program which corresponds toan internal tool that manipulates files.",
        
    ],
))

DB(Citation(
    acuna2015a, rivest1992a, ref="[26]",
    contexts=[
        "Atpresent, the filesystem is recorded directly as a snapshot ofthe MD5 [26] hashes for each file in the workflow’s folder",
        
    ],
))

DB(Citation(
    acuna2015a, johnson2014a, ref="[27]",
    contexts=[
        "Four workflowswere selected: HybSeqPipeline [27], Inmembrane [28], Pycoevol[29], and miR-PREFeR [30].",
        
    ],
))

DB(Citation(
    acuna2015a, perry2013a, ref="[28]",
    contexts=[
        "Four workflowswere selected: HybSeqPipeline [27], Inmembrane [28], Pycoevol[29], and miR-PREFeR [30].",
        
    ],
))

DB(Citation(
    acuna2015a, madeira2012a, ref="[29]",
    contexts=[
        "Four workflowswere selected: HybSeqPipeline [27], Inmembrane [28], Pycoevol[29], and miR-PREFeR [30].",
        
    ],
))

DB(Citation(
    acuna2015a, lei2014a, ref="[30]",
    contexts=[
        "Four workflowswere selected: HybSeqPipeline [27], Inmembrane [28], Pycoevol[29], and miR-PREFeR [30].",
        
    ],
))

DB(Citation(
    acuna2015a, brandes2001a, ref="[31]",
    contexts=[
        "The log was then analyzed (see results in Table IV) toproduce the dataflow graph displayed in Figure 2 stored inGraphML [31] and visualized with Graphviz [32] in hierarchicallayout mode",
        
    ],
))

DB(Citation(
    acuna2015a, gansner2000a, ref="[32]",
    contexts=[
        "The log was then analyzed (see results in Table IV) toproduce the dataflow graph displayed in Figure 2 stored inGraphML [31] and visualized with Graphviz [32] in hierarchicallayout mode",
        
    ],
))

DB(Citation(
    acuna2015a, johnson2008a, ref="[33]",
    contexts=[
        "HybSeqPipeline is a sequence assembly workflow. It loadsa data file consisting of many short sequences, distributesthem into groups (using blastx [33]), and then assembleseach of those groups (using velvet [34]).",
        
    ],
))


DB(Citation(
    acuna2015a, miller2010a, ref="[34]",
    contexts=[
        "HybSeqPipeline is a sequence assembly workflow. It loadsa data file consisting of many short sequences, distributesthem into groups (using blastx [33]), and then assembleseach of those groups (using velvet [34]).",
        
    ],
))

DB(Citation(
    acuna2015a, tuffery2006a, ref="[35]",
    contexts=[
        "This canbe implemented by connecting tools discovered in a trace toa resource collection. We aim at mapping the dataflow graphto a semantic map where all tools are represented as edges ina domain ontology [35]. Workflow semantics can be extractedby the analysis of the domain libraries such as BioPython [36]used.",
        
    ],
))

DB(Citation(
    acuna2015a, cock2009a, ref="[36]",
    contexts=[
        "This canbe implemented by connecting tools discovered in a trace toa resource collection. We aim at mapping the dataflow graphto a semantic map where all tools are represented as edges ina domain ontology [35]. Workflow semantics can be extractedby the analysis of the domain libraries such as BioPython [36]used.",
        
    ],
))

DB(Citation(
    acuna2015a, kinsy2007a, ref="[37]",
    contexts=[
        "This would support the documentation of the workflow120in terms of its aim expressed conceptually as proposed in [37]and workflow reuse, optimization, etc. [38].",
        
    ],
))

DB(Citation(
    acuna2015a, lacroix2009a, ref="[38]",
    contexts=[
        "This would support the documentation of the workflow120in terms of its aim expressed conceptually as proposed in [37]and workflow reuse, optimization, etc. [38].",
        
    ],
))