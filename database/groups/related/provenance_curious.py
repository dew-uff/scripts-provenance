from snowballing.approaches import Group

from ..constants import *
from ...work.y2013 import huq2013a, huq2013b, huq2013c
    
approach = Group(
    huq2013a, huq2013c,
    display="Prove  nance Curious",
    approach_name="Provenance Curious",
    _cite=False,
    dont_cite=[huq2013b],

    _meta=[dict(
        binary=NO,
        languages=[PYTHON],
        goal=COMPREHENSION,
        supports=[COMPREHENSION],
        categories=[COLLECTION, QUERY, STORAGE, VISUALIZATION],

        mode=USER_LEVEL,

        tools=["AST"],
        
        annotations=[PARSEABLE, EXTERNAL, INCLUSIVE],
        execution=[POST_MORTEM],
        deployment=[],
        definition=[PARSING, STATIC],

        execution_granularity=[],
        deployment_granularity=[],
        definition_granularity=[
            FUNCTION_CALLS,
            VARIABLE_LINEAGE,
        ],

        cache=NO,
        replay=YES.star("simulate"),
        evolution=NO,
        pipeline=YES,
        summarization=[CLUSTERING.such_as(["Graph compression re-write rules"])],

        distribution=[GRAPH_FILE.such_as(["GraphML"])],
        storage=[RELATIONAL_DB.such_as(["SQLite"])],
        visualization=[
            COMBINED_VIEW.such_as(["with graph compression re-write rules"]),
        ],
        visplace=[INTERNAL],
        query=[
            FUNCTIONS.such_as(["Input values and debug model"]),
            QUERY.such_as(["SQL"]),
        ],
        integration=[],
        
        granularity=[FUNCTIONS],
        granularity_text="Language Constructs, Files (I/O)",
        management_text="SQLite, GraphML",
        generic_query_text="SQL",
        specific_query_text="Functions",
        thread=NO,
        diff=[],
                    
        limitations=[],
    )],
    _about="""
        <p>
            Provenance Curious (<a href="#huq2013a" class="reference">huq2013a</a>, <a href="#huq2013b" class="reference">huq2013b</a>, <a href="#huq2013c" class="reference">huq2013c</a>) collects the definition provenance from Python scripts for <span class="goal">comprehending</span> the experiment.
            <span class="collection">
                It traverses the AST and applies graph rewriting rules to generate a summarized dataflow graph. Then, it applies the <span class="strategy">post mortem</span> strategy to infer provenance through probabilistic models.
            </span>
        </p>
        <p>
            <span class="visualuzation summarization" title="Supports customizations in the graph, such as grouping processes">
                After extracting the graph, it applies graph-rewriting rules to reduce the number of nodes and edges and supports user customizations for grouping processes. 
            </span>
            <span class="storage analysis">
                Provenance curious stores the resulting graph in an SQLite database and provides an inference engine that allows users to input values and debug the model to check if it represents the provenance.
            </span>
            <span class="distribution analysis visualuzation">
                It also generates GraphML files for visualization and distribution.
            </span> 
        </p>
    """,
)

