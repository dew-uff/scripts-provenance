from snowballing.approaches import Group

from ..constants import *
from ...work.y2014 import lerner2014a, lerner2014b
from ...work.y2018 import lerner2018a

approach = Group(
    lerner2014a, lerner2018a,
    display="R  Data  Tracker",
    approach_name="RDataTracker",
    emails="blerner@mtholyoke.edu; boose@fas.harvard.edu; luis.perez.live@gmail.com",
    _cite=False,
    dont_cite=[lerner2014b,],

    _meta=[dict(
        reply=True,
        binary=NO,
        languages=[R],
        goal=COMPREHENSION,
        supports=[COMPREHENSION],
        categories=[COLLECTION, SUMMARIZATION, VISUALIZATION],

        mode=USER_LEVEL,

        tools=[],

        annotations=[],
        execution=[PASSIVE_MONITORING, OVERRIDING],
        deployment=[BEFORE_EXECUTION, DURING_EXECUTION],
        definition=[READING, DYNAMIC],

        execution_granularity=[VARIABLES, COMMANDS, VALUES],
        deployment_granularity=[],
        definition_granularity=[CONTENT, SOURCE],

        cache=NO,
        replay=NO,
        evolution=SEQUENCE,
        pipeline=NO,
        summarization=[FILTERING, CLUSTERING],

        distribution=[INTEROPERABLE.such_as(["PROV"])],
        storage=[INTEROPERABLE.such_as(["PROV"])],
        visualization=[COMBINED_VIEW.such_as(["DDG"])],
        visplace=[EXTERNAL],
        query=[INTEROPERABLE.such_as(["PROV"]), FUNCTIONS, PROPRIETARY.such_as(["DDG"])],
        integration=[],

        granularity=[VARIABLES, COMMANDS, VALUES],
        granularity_text="Commands, Variables, Values, Env. Var., Platform, Modules, Files (I/O)",
        management_text="Interoperable (PROV)",
        generic_query_text="",
        specific_query_text="DDG, PROV, Functions",
        thread=UNKNOWN,
        diff=[PROVENANCE],

        limitations=[],
    )],
    _about="""
        <p>
            RDataTracker (<a href="#lerner2014a" class="reference">lerner2014a</a>, <a href="#lerner2018a" class="reference">lerner2018a</a>) is an R library that collects data provenance for <span class="goal">comprehension</span> in R scripts or console sessions.
            <span class="collection">
                RDataTracker traces the execution and collects variables and statements dependencies.
                It combines the passive monitoring and the overriding strategies for execution provenance collection.
            </span>
            <span class="storage">
                RDataTracker stores provenance in PROV-JSON files.
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

