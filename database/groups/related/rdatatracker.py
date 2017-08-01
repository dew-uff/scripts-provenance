from snowballing.approaches import Group

from ..constants import *
from ...work.y2014 import lerner2014a, lerner2014b
    
approach = Group(
    lerner2014a,
    display="R  Data  Tracker",
    approach_name="RDataTracker",
    _cite=False,
    dont_cite=[lerner2014b,],

    _meta=[dict(
        binary=NO,
        languages=[R],
        goal=COMPREHENSION,
        supports=[COMPREHENSION],
        categories=[COLLECTION, SUMMARIZATION, VISUALIZATION],

        mode=USER_LEVEL,

        tools=[],
        
        annotations=[EXECUTABLE, INTERNAL, INCLUSIVE],
        execution=[PASSIVE_MONITORING, INSTRUMENTATION],
        deployment=[],
        definition=[],

        execution_granularity=[VARIABLES, COMMANDS, VALUES],
        deployment_granularity=[],
        definition_granularity=[],

        cache=NO,
        replay=NO,
        evolution=NO,
        pipeline=NO,
        summarization=[FILTERING.such_as(["annotations"]), CLUSTERING.such_as(["manual"])],

        distribution=[GRAPH_FILE.such_as(["DDG"]), PROPRIETARY],
        storage=[GRAPH_FILE.such_as(["DDG"]), PROPRIETARY],
        visualization=[COMBINED_VIEW.such_as(["DDG"]), PROPRIETARY],
        visplace=[INTERNAL],
        query=[PROPRIETARY.such_as(["DDG"])],
        integration=[],
        
        granularity=[VARIABLES, COMMANDS, VALUES],
        granularity_text="Commands, Variables, Values",
        management_text="Proprietary (DDG)",
        generic_query_text="",
        specific_query_text="DDG",
        thread=UNKNOWN,
        diff=[],
                    
        limitations=[],
    )],
    _about="""
        <p>
            RDataTracker (<a href="#lerner2014a" class="reference">lerner2014a</a>) is an R library that collects data provenance for <span class="goal">comprehension</span> in R scripts or console sessions.
            <span class="collection">
                <span title='source("ddg-library.r");ddg.init("daily-solar-radiation.r", "ddg", enable.console=TRUE);...;ddg.save()'>
                    With RDataTracker, users need to annotate their scripts to specify when to start and finish the collection.
                </span> 
                When the library is active, it traces the execution and collects variables and statements dependencies. 
                It combines the passive monitoring and the instrumentation strategies for execution provenance collection.
            </span>
        </p>
        <p>
            <span class="collection">
                RDataTracker traces the execution of commands and function calls. 
                During the tracing, it collects the runtime state, including call stack and variables bindings to capture detailed provenance information. 
                <span class="summarization" title='ddg.start("read.data");...;ddg.finish("read.data")'>
                    In addition to the automatic collection, RDataTracker enables enhancing provenance with instrumentations that indicate important parts of the execution and instrumentations that create abstraction units for summarizations.
                </span>
            </span>
        </p>
        <p>
            <span class="analysis">
                The result of provenance collection in RDataTracker is a data derivation graph that presents procedural and data nodes.
                <span title="Connected with control flow edges; Yellow">
                    Procedural nodes represent start and end of procedural blocks and operational steps (i.e. statements).
                </span>
                <span title="Connected to procedural nodes with input and output edges; Purple">
                    On the other hand, data nodes represent simple data, files, URLs, and errors.
                </span>
                Procedural nodes appear sequentially linked in the graph. Data nodes appear with input and output edges to procedural nodes.
                The graph browser supports collapsing and expanding some procedural nodes, such as abstraction units and procedural blocks.
            </span>
        </p>
    """,
)

