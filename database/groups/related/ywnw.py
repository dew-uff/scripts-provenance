from snowballing.approaches import Group

from ..constants import *
from ...work.y2015 import dey2015a
from ...work.y2016 import pimentel2016c, pimentel2016d

approach = Group(
    dey2015a, pimentel2016c,
    display="YW*NW",
    approach_name="YW*NW",
    _cite=False,
    dont_cite=[pimentel2016d,],

     _meta=[dict(
        binary=NO,
        languages=[PYTHON],
        goal=COMPREHENSION,
        supports=[COMPREHENSION, REPRODUCIBILITY, MANAGEMENT],
        categories=[COLLECTION, QUERY, VISUALIZATION],

        mode=USER_LEVEL,

        tools=[],
        
        annotations=[PARSEABLE, INTERNAL, INCLUSIVE],
        execution=[PASSIVE_MONITORING, OVERRIDING, INSTRUMENTATION, POST_MORTEM],
        deployment=[BEFORE_EXECUTION],
        definition=[PARSING, READING, STATIC, DYNAMIC],

        execution_granularity=[
            PROC_NAME, PROC_DURATION, PROC_ARGUMENTS,
            INPUT_FILES, OUTPUT_FILES,
            FUNC_ARGUMENTS, FUNC_LINEAGE,
            VARIABLE_LINEAGE,
            STACK,
        ],
        deployment_granularity=[
            ENV_VAR, MODULES,
        ],
        definition_granularity=[
            SOURCE, SOURCE_STRUCTURE, BYTECODE, CONTENT
        ],

        cache=NO,
        replay=YES,
        evolution=NO,
        pipeline=YES,
        summarization=[FILTERING],

        distribution=[
            LOGIC_FILE.such_as(["Datalog"]),
            GRAPH_FILE.such_as([GRAPHVIZ]),
        ],
        storage=[
            RELATIONAL_DB.such_as(["SQLite"]),
            CONTENT_DATABASE,
            LOGIC_FILE.such_as(["Datalog"]),
            GRAPH_FILE.such_as([GRAPHVIZ]),
        ],
        visualization=[
            COMBINED_VIEW.such_as([GRAPHVIZ]),
        ],
        visplace=[INTERNAL],
        query=[QUERY.such_as(["Datalog"])],
        integration=["noWorkflow", "YesWorkflow"],
        
        granularity=[
            VARIABLES, VAR_DEPENDENCIES
        ],
        granularity_text="Variables, Dependencies, User defined",
        management_text="noWorkflow + YesWorkflow",
        generic_query_text="Datalog",
        specific_query_text="",
        thread=NO,
        diff=[],
                    
        limitations=[],
    )],
    _about="""
        <p>
            YW*NW (<a href="#dey2015a" class="reference">dey2015a</a>; <a href="#pimentel2016c" class="reference">pimentel2016c</a>) combines <span class="collection">YesWorkflow definition provenance collection with noWorkflow fine-grained execution provenance collection</span> to <span class="goal">abstract the workflow representation to only what users consider important</span>.
            <span class="analysis">
                It uses datalog inference rules to match YesWorkflow channels to noWorkflow variables.
                Thus, it supports querying both YesWorkflow and noWorkflow data with datalog.
            </span>
        </p>
    """
)
