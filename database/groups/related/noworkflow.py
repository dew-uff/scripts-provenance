from snowballing.approaches import Group

from ..constants import *
from ...work.y2014 import murta2014a
from ...work.y2015 import pimentel2015a
from ...work.y2016 import pimentel2016a, pimentel2016b

approach = Group(
    murta2014a, pimentel2015a, pimentel2016a, pimentel2016b,
    display="no  Work  flow",
    approach_name="noWorkflow",
    _cite=False,

    _meta=[dict(
        binary=NO,
        languages=[PYTHON],
        goal=COMPREHENSION,
        supports=[COMPREHENSION, REPRODUCIBILITY, MANAGEMENT],
        categories=[COLLECTION, EVOLUTION, QUERY, STORAGE, VISUALIZATION],

        mode=USER_LEVEL,

        tools=[],
        
        annotations=[],
        execution=[PASSIVE_MONITORING, OVERRIDING],
        deployment=[BEFORE_EXECUTION],
        definition=[PARSING, READING, STATIC, DYNAMIC],

        execution_granularity=[
            PROC_NAME, PROC_DURATION, PROC_ARGUMENTS,
            INPUT_FILES, OUTPUT_FILES,
            FUNC_ARGUMENTS, FUNC_LINEAGE,
            VARIABLE_LINEAGE,
            STACK,
            PROGRAM_SLICING,
        ],
        deployment_granularity=[
            ENV_VAR, MODULES,
        ],
        definition_granularity=[
            SOURCE, SOURCE_STRUCTURE, BYTECODE, CONTENT
        ],

        cache=NO,
        replay=YES,
        evolution=INTENTION,
        pipeline=YES,
        summarization=[
            CLUSTERING.such_as(["Group Activations"]),
            FILTERING.such_as(["Hide Variables"]),
        ],

        distribution=[
            CONTENT_DATABASE, LOGIC_FILE.such_as([PROLOG])
        ],
        storage=[RELATIONAL_DB.such_as(["SQLite"]), CONTENT_DATABASE],
        visualization=[
            #WEB.such_as([JUPYTER, "NowVis"]),
            LOG_VIEW,
            COMBINED_VIEW.such_as([GRAPHVIZ]),
            PROCESS_VIEW.such_as([
                "Activation graph with summarizations "
                "that group activations and hide variables",
            ]),
        ],
        visplace=[INTERNAL],
        query=[QUERY.such_as([SQL, PROLOG, PYTHON]), FUNCTIONS, WEB.such_as([JUPYTER, "NowVis"])],
        integration=[],
        
        granularity=[
            FUNC_ARGUMENTS, ARGUMENTS, RETURNS,
            VARIABLES, VAR_DEPENDENCIES
        ],
        granularity_text="Functions, Variables, Env. Var., Platform, Modules, Files (I/O)",
        management_text="Content DB, SQLite, Prolog",
        generic_query_text="SQL, Prolog",
        specific_query_text="Functions, Web",
        thread=NO,
        diff=[PROVENANCE],
                    
        limitations=[],
    )],
    _about="""
        <p>
            noWorkflow (<a href="#murta2014a" class="reference">murta2014a</a>; <a href="#pimentel2016a" class="reference">pimentel2016a</a>, <a href="#pimentel2016b" class="reference">pimentel2016b</a>, <a href="#pimentel2015a" class="reference">pimentel2015a</a>) captures provenance from Python scripts for <span class="goal">comprehension</span>.
            <span class="collection">
                It requires no changes in the scripts for provenance collection. noWorkflow collects deployment, definition, and execution provenance.
            </span>
        </p>
        <p>
            <span class="collection">
                noWorkflow collects environment variables and uses the importlib to collect imported modules as deployment provenance.
                It traverses the AST to collect script and functions as definition provenance.
                For execution provenance, noWorkflow applies the overriding and the passive monitoring strategies.
                It overrides the open function to capture all file accesses, and it traces the execution with a Profiler to obtain executed functions with parameters and return values.
                Optionally, noWorkflow also supports reading the bytecode and defining a Tracer for collecting variables and dependencies.
            </span>
        </p>
        <p>
            <span class="evolution">
                In addition to the trial provenance, noWorkflow also tracks the trial evolution by associating each trial provenance with an identifier and using this identifier to track which trials were based on it.
                <span class="management analysis">
                    noWorkflow supports restoring previous trials and visualizing the history.
                </span>
            </span>
        </p>
        <p>
            <span class="storage">
                noWorkflow stores files in a content database structured by SHA1 hash codes and provenance in an SQLite database.
            </span>
            <span class="analysis">
                Thus, it supports SQL queries for analysis.
                In addition to SQL queries, noWorkflow provides a series of command lines for listing and comparing trials, activations, modules and environment variables.
                It also provides a command to export a trial provenance to Prolog with predefined rules, allowing users to run Prolog queries.
                Additionally, noWorkflow provides a web visualization tool that presents an activation graph.
                The activation graph presents the sequence of activations in a trial.
                For fine-grained provenance visualization, noWorkflow exports a dataflow as a dot file that presents all variable dependencies.
            </span>
        </p>
        <p>
            <span class="analysis">
                noWorkflow integrates to IPython, defining diverse IPython magics for provenance collection and querying in IPython cells. In this integration, noWorkflow also implements methods for visualizations in Jupyter. 
                Thus, it is possible to load noWorkflow objects for visualizing activation and dataflow graphs.
            </span>
        </p>
    """,
)

