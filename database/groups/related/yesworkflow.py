from snowballing.approaches import Group

from ..constants import *
from ...work.y2015 import mcphillips2015a, mcphillips2015b

approach = Group(
    mcphillips2015a, mcphillips2015b,
    display="Yes  Work  flow",
    approach_name="YesWorkflow",
    emails="tmcphillips@absoluteflow.org; bowers@gonzaga.edu; Khalid.Belhajjame@dauphine.fr; ludaesch@illinois.edu",
    to="McPhillips, Timothy and Bowers, Shawn and Belhajjame, Khalid and Ludäscher, Bertram",
    _cite=False,

    _meta=[dict(
        reply=True,
        binary=NO,
        languages=[AGNOSTIC],
        goal=COMPREHENSION,
        supports=[COMPREHENSION],
        categories=[COLLECTION, QUERY, STORAGE, VISUALIZATION],

        mode=USER_LEVEL,

        tools=[],

        annotations=[PARSEABLE, INTERNAL, EXTERNAL, INCLUSIVE, MANDATORY, DEFINITION],
        execution=[INSTRUMENTATION, POST_MORTEM],
        deployment=[],
        definition=[],

        execution_granularity=[
            INPUT_FILES.star("*user"),
            OUTPUT_FILES.star("*user"),
        ],
        deployment_granularity=[],
        definition_granularity=[
            FUNCTIONS.star("Program Blocks"),
            ARGUMENTS.star("Ports and Channels"),
            FUNC_LINEAGE.star("*user"),
            VARIABLE_LINEAGE.star("*user"),
            COMMAND_LINEAGE.star("*user"),
        ],

        cache=NO,
        replay=NO,
        evolution=NO,
        pipeline=YES,
        summarization=[],

        distribution=[
            INTEROPERABLE.such_as([PROV]),
            LOGIC_FILE.such_as(["Datalog"]),
            GRAPH_FILE.such_as([GRAPHVIZ])
        ],
        storage=[
            INTEROPERABLE.such_as([PROV]),
            LOGIC_FILE.such_as(["Datalog"]),
            GRAPH_FILE.such_as([GRAPHVIZ])
        ],
        visualization=[
            INTEROPERABLE.such_as([PROV]),
            COMBINED_VIEW.such_as([GRAPHVIZ]), 
            PROCESS_VIEW.such_as([GRAPHVIZ]), 
            DATA_VIEW.such_as([GRAPHVIZ]), 
        ],
        visplace=[INTERNAL, EXTERNAL],
        query=[
            INTEROPERABLE.such_as([PROV]),
            QUERY.such_as(["Datalog"]),
        ],
        integration=[],
        
        granularity=[USER_DEFINED],
        granularity_text="User defined",
        management_text="PROV, Datalog, Graphviz",
        generic_query_text="Datalog",
        specific_query_text="PROV",
        thread=NO,
        diff=[],
                    
        limitations=[],
    )],
    _about="""
        <p>
            YesWorkflow (<a href="#mcphillips2015a" class="reference">mcphillips2015a</a>, <a href="#mcphillips2015b" class="reference">mcphillips2015b</a>) collects definition provenance based on simple user annotations embedded inside comments of any programming language for <span class="goal">comprehension</span>.
            <span class="collection">
                It uses the annotations to build a workflow model that represents the script.
                These annotations should specify program blocks with ports, and channels to connect the blocks.
                While such simple annotations allow a low entry bar for adoption, they may not represent what the scripts really do.
                For capturing the definition provenance from theses annotations, YesWorkflow parses the script.
            </span>
        </p>
        <p>
            <span class="collection">
                In addition to definition provenance, YesWorkflow also collects execution provenance through the <span class="strategy">post mortem</span> strategy.
                YesWorkflow supports using URI templates in channels to define input and output files.
                The URI templates are based on the idea that many scientists already use directory structures and file names to organize data produced by scripts.
                After the script execution, YesWorkflow checks which files match the URI templates and collect them as execution provenance.
            </span>
        </p>
        <p>
            <span class="analysis">
                YesWorkflow exports the resulting provenance to PROV, Datalog, and GraphViz dot files.
                For graph visualization, it supports three formats: process-centric, data-centric and combined view.
                The process-centric format presents blocks as nodes and channels as edges.
                The data-centric format presents channels as nodes and blocks as edges.
                Finally, the combined view presents both blocks and channels as nodes.
            </span>
        </p>
    """,
    evaluation="[R HSM+13/mcphillips2015a], [Matlab Bie12/mcphillips2015a]",
)

