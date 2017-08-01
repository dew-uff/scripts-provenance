# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2004 import hoek2004a
from ..work.y2006 import muniswamy2006a
from ..work.y2007 import diehl2007a
from ..work.y2008 import freire2008a
from ..work.y2008 import bochner2008a
from ..work.y2008 import frew2008a
from ..work.y2009 import mouallem2009a
from ..work.y2010 import koop2010a
from ..work.y2010 import koop2010b
from ..work.y2011 import cheney2011a
from ..work.y2011 import gavish2011a
from ..work.y2011 import macko2011a
from ..work.y2012 import guo2012a
from ..work.y2012 import davison2012a
from ..work.y2012 import tariq2012a
from ..work.y2013 import missier2013a
from ..work.y2013 import huq2013a
from ..work.y2013 import koop2013a
from ..work.y2013 import neves2013a
from ..work.y2014 import murta2014a
from ..work.y2014 import neves2014a
from ..work.y2015 import mcphillips2015a
from ..work.y2015 import chavan2015a
from ..work.y2015 import tosta2015a
from ..work.y2015 import 林晨2015a
from ..work.y2015 import nascimento2015a
from ..work.y2016 import assis2016a
from ..work.y2016 import chirigati2016a
from ..work.y2016 import erickson2016a
from ..work.y2016 import ludascher2016a
from ..work.y2016 import missier2016a
from ..work.y2016 import oliveira2016a
from ..work.y2016 import schreiber2016a
from ..work.y2016 import carvalho2016a
from ..work.y2016 import goehring2016a
from ..work.y2016 import costa2016a
from ..work.y2016 import curcin2016a
from ..work.y2016 import lemieux2016a
from ..work.y2017 import bastos2017a
from ..work.y2017 import alper2017a
from ..work.y2017 import samuel2017a


DB(Citation(
    murta2014a, bochner2008a, ref="1",
    contexts=[
        "Bochner et al. [1] proposed an API and a client library to capture provenance for Python scripts.", 
        "Some of the existing approaches that do not require a WfMS rely on scientists to modify the experiment scripts to include annotations or calls to provenance capture functions [1,3,7]."
    ],
))

DB(Citation(
    murta2014a, cheney2011a, ref="2",
    contexts=[
        "The provenance captured by noWorkflow is of a different nature—it represents dependencies within processes at the function level. In this sense, our approach is closer to the work by Cheney et al. [2]"
    ],
))

DB(Citation(
    murta2014a, davison2012a, ref="3",
    contexts=[
        "Sumatra [3] collects provenance information from Python scripts. It is able to capture input and output data produced by each run (as long as they are explicitly specified by the user), parameters, module dependencies, and platform information. It is also able to detect when a module the script depends on has changed. The source code, however, needs to live in a version control system so that changes from one version to another can be detected", 
        "Others require scientists to use a version control system to track changes to the source code, or are not entirely automatic, requiring input from scientists [3,10].", 
        "Some of the existing approaches that do not require a WfMS rely on scientists to modify the experiment scripts to include annotations or calls to provenance capture functions [1,3,7]."
    ],
))

DB(Citation(
    murta2014a, diehl2007a, ref="4",
    contexts=[
        "Each vertex is labeled with the function name and is colored according to the traffic light scale (shades from green to yellow to red) [4]:"
    ],
))

DB(Citation(
    murta2014a, freire2008a, ref="5",
    contexts=[
        "There are two types of provenance for scientific workflows: prospective and retrospective [5]. Prospective provenance describes the structure of the experiment and corresponds to the workflow definition, the graph of the activities, and their associated parameters. Retrospective provenance captures the steps taken during the workflow execution, and while it has similar (graph) structure, it is constructed using information collected at runtime, including activities invoked and parameter values used, intermediate data produced, the execution start and end times, etc"
    ],
))

DB(Citation(
    murta2014a, frew2008a, ref="6",
    contexts=[
        "There are also approaches that capture provenance at the operating system level [6,8,17], which monitor system calls and track processes and data dependencies between these processes. These systems, however, do not have visibility into what happens inside the scripts underlying the processes.", 
        "Different mechanisms for provenance capture have been proposed, and some can be applied to scripts. Tools that capture provenance at the operating system level [6,8,17] monitor system calls and track processes and data dependencies between these processes. Because the dependencies are recorded at the process level, it can be difficult to reconcile the provenance with the script definition as these systems cannot see what happens inside the processes. The provenance captured by noWorkflow is of a different nature—it represents dependencies within processes at the function level", 
        "One alternative would be to use approaches that capture provenance at the operating system level [6,17]. Since these systems intercept system calls (e.g., file reads and writes, execution of binaries), they produce a high volume of very fine-grained information that represent data dependencies between processes. It can be difficult to explore this information and connect it to the underlying experiment specification. Consequently, identifying which experiment activity influenced the generation of a given data product can be challenging."
    ],
))

DB(Citation(
    murta2014a, gavish2011a, ref="7",
    contexts=[
        "Gavish and Donoho [7] introduce the notion of a Verifiable Computational Result (VCR), where every result is assigned a unique identifier and results produced under the exact same conditions have the same identifier to support reproducibility.", 
        "Some of the existing approaches that do not require a WfMS rely on scientists to modify the experiment scripts to include annotations or calls to provenance capture functions [1,3,7]."
    ],
))

DB(Citation(
    murta2014a, guo2012a, ref="8",
    contexts=[
        "There are also approaches that capture provenance at the operating system level [6,8,17], which monitor system calls and track processes and data dependencies between these processes. These systems, however, do not have visibility into what happens inside the scripts underlying the processes.", 
        "Different mechanisms for provenance capture have been proposed, and some can be applied to scripts. Tools that capture provenance at the operating system level [6,8,17] monitor system calls and track processes and data dependencies between these processes. Because the dependencies are recorded at the process level, it can be difficult to reconcile the provenance with the script definition as these systems cannot see what happens inside the processes. The provenance captured by noWorkflow is of a different nature—it represents dependencies within processes at the function level"
    ],
))

DB(Citation(
    murta2014a, hoek2004a, ref="9",
    contexts=[
        "Borrowing terms from software engineering, where software goes through three phases, i.e., definition, deployment, and execution [9], we define three types of provenance needed for scripts:"
    ],
))

DB(Citation(
    murta2014a, huq2013a, ref="10",
    contexts=[
        "ProvenanceCurious [10] is another tool that can infer data provenance from Python scripts. It also uses AST analysis to capture every node of the syntax tree, and it uses a graph to provide query capabilities. However, for every operation, it requires input from the users regarding whether or not the operation reads or writes persistent data—this information is transparently captured by noWorkflow",
        "Others require scientists to use a version control system to track changes to the source code, or are not entirely automatic, requiring input from scientists [3,10]."
    ],
))

DB(Citation(
    murta2014a, koop2013a, ref="11",
    contexts=[
        "One direction we plan to explore in future work is how to integrate provenance at different levels (e.g., operating system level with function level). We also plan to further investigate techniques for summarizing and visualizing provenance graphs [11,14], including all three types of provenance"
    ],
))

DB(Citation(
    murta2014a, koop2010a, ref="12",
    contexts=[
        "Scientists often fall back on Workflow Management Systems (WfMSs), which provide infrastructure to automatically capture the input, intermediate, and output data involved in computations, allowing experiments to be managed, assessed, and reproduced [12,16,18]"
    ],
))

DB(Citation(
    murta2014a, koop2010b, ref="13",
    contexts=[
        "Because the wrapped libraries are integrated with the WfMS, it is possible for the system to track and control them, e.g., to detect that a wrapped library has changed and to upgrade the workflows accordingly [13]."
    ],
))

DB(Citation(
    murta2014a, macko2011a, ref="14",
    contexts=[
        "One direction we plan to explore in future work is how to integrate provenance at different levels (e.g., operating system level with function level). We also plan to further investigate techniques for summarizing and visualizing provenance graphs [11,14], including all three types of provenance"
    ],
))

DB(Citation(
    murta2014a, missier2013a, ref="15",
    contexts=[
        "including all three types of provenance, as well as for contrasting different trials [15]"
    ],
))

DB(Citation(
    murta2014a, mouallem2009a, ref="16",
    contexts=[
        "Scientists often fall back on Workflow Management Systems (WfMSs), which provide infrastructure to automatically capture the input, intermediate, and output data involved in computations, allowing experiments to be managed, assessed, and reproduced "
    ],
))

DB(Citation(
    murta2014a, muniswamy2006a, ref="17",
    contexts=[
        "There are also approaches that capture provenance at the operating system level [6,8,17], which monitor system calls and track processes and data dependencies between these processes. These systems, however, do not have visibility into what happens inside the scripts underlying the processes.",
        "Different mechanisms for provenance capture have been proposed, and some can be applied to scripts. Tools that capture provenance at the operating system level [6,8,17] monitor system calls and track processes and data dependencies between these processes. Because the dependencies are recorded at the process level, it can be difficult to reconcile the provenance with the script definition as these systems cannot see what happens inside the processes. The provenance captured by noWorkflow is of a different nature—it represents dependencies within processes at the function level", 
        "One alternative would be to use approaches that capture provenance at the operating system level [6,17]. Since these systems intercept system calls (e.g., file reads and writes, execution of binaries), they produce a high volume of very fine-grained information that represent data dependencies between processes. It can be difficult to explore this information and connect it to the underlying experiment specification. Consequently, identifying which experiment activity influenced the generation of a given data product can be challenging."
    ],
))

DB(Citation(
    murta2014a, neves2013a, ref="18",
    contexts=[
        "Workflow Management Systems (WfMSs), which provide infrastructure to automatically capture the input, intermediate, and output data involved in computations, allowing experiments to be managed, assessed, and reproduced [12,16,18]"
    ],
))

DB(Citation(
    murta2014a, tariq2012a, ref="19",
    contexts=[
        "The approach taken by Tariq et al. [19] makes use of the LLVM compiler framework to automatically insert provenance capture at each function entry and exit. Thus, similar to noWorkflow, their approach is transparent—users do not need to manually annotate their code. However, there are important differences between the two approaches. Since Tariq et al. rely on a compiler, they are  restricted to capturing static information. noWorkflow, on the other hand, captures both static and dynamic information"
    ],
))

# Snowball 2016/07/24

DB(Citation(
    林晨2015a, murta2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    assis2016a, murta2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    chavan2015a, murta2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    erickson2016a, murta2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ludascher2016a, murta2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    missier2016a, murta2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    neves2014a, murta2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    oliveira2016a, murta2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    schreiber2016a, murta2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    tosta2015a, murta2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bastos2017a, murta2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    carvalho2016a, murta2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    nascimento2015a, murta2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    goehring2016a, murta2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    costa2016a, murta2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    curcin2016a, murta2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    alper2017a, murta2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    samuel2017a, murta2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lemieux2016a, murta2014a, ref="",
    contexts=[

    ],
))
