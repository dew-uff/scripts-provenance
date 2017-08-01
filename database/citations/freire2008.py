# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2005 import simmhan2005b
from ..work.y2005 import bose2005a
from ..work.y2006 import muniswamy2006a
from ..work.y2006 import altintas2006a
from ..work.y2006 import cohen2006a
from ..work.y2006 import freire2006a
from ..work.y2006 import oinn2006a
from ..work.y2007 import groth2007a
from ..work.y2007 import scheidegger2007a
from ..work.y2007 import tan2007a
from ..work.y2007 import zhao2007a
from ..work.y2008 import freire2008a
from ..work.y2008 import freire2008b
from ..work.y2008 import simmhan2008a
from ..work.y2008 import bowers2008a
from ..work.y2008 import barga2008a
from ..work.y2008 import biton2008a
from ..work.y2008 import clifford2008a
from ..work.y2008 import frew2008a
from ..work.y2008 import futrelle2008a
from ..work.y2008 import golbeck2008a
from ..work.y2008 import kim2008a
from ..work.y2008 import ludascher2008a
from ..work.y2008 import miles2008a
from ..work.y2008 import zhao2008a


DB(Citation(
    freire2008a, bose2005a, ref="1",
    contexts=[
        "Bose and Frew1 provide a comprehensive overview that covers early work in the area as well as standards used in specific domains, and Simmhan and colleagues2 describe a taxonomy they developed to compare five systems.",
        "The Kepler workflow system stores prospective provenance in the Modeling Markup Language (MoML) format,1",
    ],
))

DB(Citation(
    freire2008a, simmhan2005b, ref="2",
    contexts=[
        "Bose and Frew1 provide a comprehensive overview that covers early work in the area as well as standards used in specific domains, and Simmhan and colleagues2 describe a taxonomy they developed to compare five systems.",
    ],
))

DB(Citation(
    freire2008a, tan2007a, ref="3",
    contexts=[
        "The problem of managing fine-grained provenance recorded for items in a database is out of scope for this survey—a detailed overview appears elsewhere3.",
    ],
))

DB(Citation(
    freire2008a, clifford2008a, ref="4",
    contexts=[
        "When it comes to computational tasks, there are two forms of provenance: prospective and retrospective.4",
    ],
))

DB(Citation(
    freire2008a, groth2007a, ref="5",
    contexts=[
        "Each service or tool in a process-based mechanism must be instrumented to capture provenance, with any information derived from autonomous processes pieced together to provide documentation for complex tasks.5",
        "The Provenance-Aware Service Oriented Architecture (PASOA) project (www.pasoa.org) developed a provenance architecture that relies on individual services to record their own provenance.5",
    ],
))

DB(Citation(
    freire2008a, frew2008a, ref="6",
    contexts=[
        "OS-based mechanisms aren’t coupled with workflows or processes at all, and thus require postprocessing to extract relationships between system calls and tasks.6,7",
        "One advantage of OS-based mechanisms is that they don’t require modifications to existing processes and are agnostic about how tasks are modeled—they rely on the OS environment’s ability to transparently capture data and data-process dependencies at the kernel (via the filesystem interface)7 or user levels (via the system call tracer).6",
        "The ES3 system (http://eil.bren. ucsb.edu), for example, monitors the interactions between arbitrary applications and their environments (via arguments, file I/O, system, and calls), and then uses this information to assemble a provenance graph to describe what actually happened during execution.6",
        "ES3’s goal is to extract provenance information from arbitrary applications by monitoring their interactions with the execution environment.6",
    ],
))

DB(Citation(
    freire2008a, muniswamy2006a, ref="7",
    contexts=[
        "OS-based mechanisms aren’t coupled with workflows or processes at all, and thus require postprocessing to extract relationships between system calls and tasks.6,7",
        "One advantage of OS-based mechanisms is that they don’t require modifications to existing processes and are agnostic about how tasks are modeled—they rely on the OS environment’s ability to transparently capture data and data-process dependencies at the kernel (via the filesystem interface)7 or user levels (via the system call tracer).6",
        "However, because even simple tasks can lead to a large number of low-level calls, the amount of provenance that OS-based approaches record can be prohibitive, making it hard to query and reason about the information.7",
        "When an OS-based approach such as Provenance-Aware Storage Systems (PASS) captures very fine-grained provenance,7 for example, the volume of information can be overwhelming, making it difficult to explore."
    ],
))

DB(Citation(
    freire2008a, altintas2006a, ref="8",
    contexts=[
        
    ],
))

DB(Citation(
    freire2008a, cohen2006a, ref="9",
    contexts=[
        "Researchers have proposed several provenance models in the literature.9,10,12",
    ],
))

DB(Citation(
    freire2008a, golbeck2008a, ref="10",
    contexts=[
        "Researchers have proposed several provenance models in the literature.9,10,12",
        "A common feature across many approaches to querying provenance is that their solutions are closely tied to the storage models used. Hence, they require users to write queries in languages such as SQL,16 Prolog,20 and SPARQL.10,11",
        "Some provenance models use Semantic Web technology both to represent and query provenance information.10,11,15,22",
    ],
))

DB(Citation(
    freire2008a, kim2008a, ref="11",
    contexts=[
        "For systems that schedule scientific workflow execution on the grid (such as Pegasus11), it’s important to save scheduling information as well as execution provenance.",
        "A common feature across many approaches to querying provenance is that their solutions are closely tied to the storage models used. Hence, they require users to write queries in languages such as SQL,16 Prolog,20 and SPARQL.10,11",
        "Some provenance models use Semantic Web technology both to represent and query provenance information.10,11,15,22",
        "Pegasus (http://pegasus.isi.edu) is a workflowmapping engine that, while taking into account resource efficiency and dynamic availability, automatically maps high-level workflow specifications into executable plans that run on distributed infrastructures such as the TeraGrid.11",
    ],
))

DB(Citation(
    freire2008a, freire2006a, ref="12",
    contexts=[
        "Researchers have proposed several provenance models in the literature.9,10,12",
        "Some models, for example, store a workflow’s specification once for all of its executions;12,16 in models with a single layer, such as Kepler’s, the specification of a workflow instance must be saved to the provenance model every time the workflow is executed along with any runtime information.17",
        "VisTrails includes an additional layer that records information about workflow evolution.12",
        "VisTrails provides a visual interface to compare workflows side by side12 and a mechanism for refining workflows by analogy",
    ],
))

DB(Citation(
    freire2008a, miles2008a, ref="13",
    contexts=[
        
    ],
))

DB(Citation(
    freire2008a, simmhan2008a, ref="14",
    contexts=[
        "Karma (www.extreme.indiana.edu/karma) was developed to support dynamic workflows in weather forecasting simulations, where the execution path can change rapidly due to external events.14",
    ],
))

DB(Citation(
    freire2008a, zhao2008a, ref="15",
    contexts=[
        "Some provenance models use Semantic Web technology both to represent and query provenance information.10,11,15,22",
    ],
))

DB(Citation(
    freire2008a, barga2008a, ref="16",
    contexts=[
        "The ability to represent provenance at different levels of abstraction also leads to simpler queries and more intuitive results. Consider the REDUX system,16 which uses the layered model depicted in Figure 3.",
        "Some models, for example, store a workflow’s specification once for all of its executions;12,16 in models with a single layer, such as Kepler’s, the specification of a workflow instance must be saved to the provenance model every time the workflow is executed along with any runtime information.17",
        "A common feature across many approaches to querying provenance is that their solutions are closely tied to the storage models used. Hence, they require users to write queries in languages such as SQL,16 Prolog,20 and SPARQL.10,11",
    ],
))

DB(Citation(
    freire2008a, ludascher2008a, ref="17",
    contexts=[
        "Some models, for example, store a workflow’s specification once for all of its executions;12,16 in models with a single layer, such as Kepler’s, the specification of a workflow instance must be saved to the provenance model every time the workflow is executed along with any runtime information.17",
    ],
))

DB(Citation(
    freire2008a, oinn2006a, ref="18",
    contexts=[
        "To support higher-level semantic queries, it might be useful to add additional layers of application-specific metadata and ontologies, such as in Taverna.18",
    ],
))

DB(Citation(
    freire2008a, biton2008a, ref="19",
    contexts=[
        "Biton and colleagues proposed a solution that uses abstractions through the creation of user views.19",
    ],
))

DB(Citation(
    freire2008a, bowers2008a, ref="20",
    contexts=[
        "A common feature across many approaches to querying provenance is that their solutions are closely tied to the storage models used. Hence, they require users to write queries in languages such as SQL,16 Prolog,20 and SPARQL.10,11",
    ],
))

DB(Citation(
    freire2008a, scheidegger2007a, ref="21",
    contexts=[
        "The VisTrails query-by-example (QBE) interface (see Figure 6) addresses this problem by letting users quickly construct expressive queries using the same familiar interface they use to build workflow.21",
        "users can modify workflows by example without having to directly edit their definitions.21",
    ],
))

DB(Citation(
    freire2008a, futrelle2008a, ref="22",
    contexts=[
        "Some provenance models use Semantic Web technology both to represent and query provenance information.10,11,15,22",
    ],
))

DB(Citation(
    freire2008a, zhao2007a, ref="23",
    contexts=[
        "Swift (www.ci.uchicago.edu/swift) builds on and includes technology previously distributed as the GriPhyN VDS.23",
    ],
))

DB(Citation(
    freire2008a, freire2008b, ref="24",
    contexts=[
        "The “wisdom of the crowds,” in the context of scientific exploration, can avoid duplication and encourage continuous, documented, and reproducible scientific progress.24",
    ],
))
