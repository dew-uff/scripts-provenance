from snowballing.approaches import Group

from ..constants import *
from ...work.y2015 import acuna2015a, acuna2015b, acuna2015c
from ...work.y2016 import acuna2016a

approach = Group(
    acuna2015a, acuna2015b, acuna2015c, acuna2016a,
    display="WISE",
    approach_name="Workflow Instrumentation for Structure Extraction (WISE)",
    _cite=False,

    _meta=[dict(
        binary=NO,
        languages=[PYTHON],
        goal=COMPREHENSION,
        supports=[COMPREHENSION],
        categories=[COLLECTION, STORAGE, SUMMARIZATION, VISUALIZATION],

        mode=USER_LEVEL,

        tools=["AST"],
        
        annotations=[PARSEABLE, EXTERNAL, INCLUSIVE, OPTIONAL],
        execution=[OVERRIDING, POST_MORTEM.star("every activity")],
        deployment=[BEFORE_EXECUTION],
        definition=[READING, STATIC],

        execution_granularity=[
            PROC_NAME,
            PROC_LINEAGE.star("*only if it receives a file as parameter"),
            PROC_ARGUMENTS,
            PROC_PIPE,
            INPUT_FILES.star("*user"),
            OUTPUT_FILES,

        ],
        deployment_granularity=[
            MODULES,
        ],
        definition_granularity=[
            CONTENT.star("*instrumentation backup")
        ],

        cache=NO,
        replay=NO,
        evolution=NO,
        pipeline=YES,
        summarization=[CLUSTERING.such_as(["Combine processes"])],

        distribution=[GRAPH_FILE.such_as([GRAPHML])],
        storage=[GRAPH_FILE.such_as([GRAPHML])],
        visualization=[
            PROCESS_VIEW.such_as([GRAPHML, GRAPHVIZ, "ProtocolDB"])
        ],
        visplace=[INTERNAL],
        query=[],
        integration=[],
        
        granularity=[PROCESSES.star("Tools"), FILES, MODULES],
        granularity_text="Processes, Modules, Files (I/O - metadata)",
        management_text="Graphviz, GraphML",
        generic_query_text="",
        specific_query_text="",
        thread=NO,
        diff=[],
                    
        limitations=[],
    )],
    _about="""
        <p>
            Workflow Instrumentation for Structure Extraction (WISE) (<a href="#acuna2015b" class="reference">acuna2015b</a>; <a href="#acuna2015c" class="reference">acuna2015c</a>; <a href="#acuna2015a" class="reference">acuna2015a</a>; <a href="#acuna2016a" class="reference">acuna2016a</a>) captures execution provenance from Python scripts to support dataflow <span class="goal">comprehension</span>, allowing users to recreate experiments with workflow systems.
            <span class="collection analysis">
                WISE produces provenance graphs in two steps: automatic instrumentation and <span title="The trace is used to created a provenance graph, which is examined for equivalent regions (collected into a single unit).">provenance summarization</span>.
            </span>
        </p>
        <p>
            <span class="collection">
                The automatic <span class="strategy">instrumentation</span> step applies the overriding strategy by modifying the original script source code to include overridden versions of built-in methods.
                These overridden methods log events to produce a trace with interactions between the script and the file system.
                As it modifies source codes, WISE backups all scripts before instrumenting them.
                WISE instruments not only the main script, but it also follows imports recursively.
            </span>
        </p>
        <p>
            <span class="collection">
                WISE uses the overridden methods to record internal and external events. 
                Internal events represent the script accessing a file. External events represent system calls or data operations (e.g. copying a file). 
                External events allow identifying which tools the script use. 
                During the collection of these events, WISE also performs the post-mortem strategy, by comparing files that existed before the events to files found after. 
                Thus, it is possible to define the outputs of these tools for the provenance graph. WISE requires users to define input files for each tool manually, should the tool do not use the filename in its arguments.
            </span>
        </p>
        <p>
            <span class="analysis">
                After collecting the provenance, WISE produces a graph and summarizes it.
                The graph presents events as nodes and files as edges.
                In addition to the event nodes, the graph contains three special nodes: source, library, and sink.
                The source node produces the initial input to the program.
                The library nodes produce all files that existed in the directory before the script execution.
                Finally, the sink nodes depend on every file that exists at the end of the execution.
                WISE represents two types of file dependencies: direct and indirect.
                Direct dependencies occur when the event use the exact filename in the invocation.
                Indirect dependencies occur when the event uses a substring to refer to the file.
                WISE combines all events that correspond to the execution of the same programs for situations in which the user uses pipes or parallel.
            </span>
        </p>
        <p>
            <span class="summarization">
                For summarization, WISE identifies nodes with the same character (invocation or dataflow) and combines them into regions to remove repetitions from the dataflow.
                WISE includes collectors and dispensers as extra nodes in the graph to keep the execution and dataflow structure equivalent to the previous one.
                For better comprehension, WISE optionally applies skeletonization as an extra step to remove details.
                Skeletonizations break the workflow equivalence.
            </span>
            <span class="storage" title="Use GraphML to store graph and graphviz for visualization in hierarchical layout mode; Stores tools and associated usage profiles (parameters that are give) in a resource library; Filesystem is recorded as a snapshot of MD5 hashes for each fie in the workflow's folder">
                WISE produces a GraphML file with the final graph.
            </span>
        </p>
    """,
    website="http://bioinformatics.engineering.asu.edu/WISE/",
    evaluation="""
        From acuna2015c: [51], [57], [66], [68], [73], [85]
        From acuna2015a: [27], [28], [29], [30]
        From acuna2015b: [41], [42], [43], [44]
    """,
    export="(manual?) Maps the workflows to a conceptual workflow representation expressed in terms of a domain ontology (Acuna2015b)",
)
