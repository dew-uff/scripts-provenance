from snowballing.approaches import Group

from ..constants import *
from ...work.y2010 import silles2010a
from ...work.y2011 import runnalls2011a, runnalls2011b
from ...work.y2012 import runnalls2012a
from ...work.y2014 import silles2014a

approach = Group(
    silles2010a, runnalls2012a, silles2014a,
    display="CXXR",
    approach_name="CXXR",
    _cite=False,
    dont_cite=[runnalls2011a, runnalls2011b],

    _meta=[dict(
        binary=NO,
        languages=[R],
        goal=COMPREHENSION,
        supports=[COMPREHENSION],
        categories=[COLLECTION, QUERY],

        mode=USER_LEVEL,

        tools=[],
        
        annotations=[],
        execution=[OVERRIDING],
        deployment=[],
        definition=[],

        execution_granularity=[
            INPUT_FILES,
            RANDOM_SEED,
            VARIABLE_LINEAGE.star("global"),
            COMMAND_LINEAGE.star("global"),

        ],
        deployment_granularity=[],
        definition_granularity=[],

        cache=NO,
        replay=NO,
        evolution=NO,
        pipeline=NO,
        summarization=[],

        distribution=[],
        storage=[MEMORY], #Memory
        visualization=[],
        visplace=[],
        query=[
            FUNCTIONS.such_as(["Command Provenance", "Data Provenance"])
        ],
        integration=[],
        
        granularity=[COMMANDS, VARIABLES],
        granularity_text="Commands, Variables, Random Seed, Files (I)",
        management_text="Memory",
        generic_query_text="",
        specific_query_text="Functions",
        thread=NO,
        diff=[],
                    
        limitations=[],
    )],
    _about="""
        <p>
            CXXR (<a href="#runnalls2012a" class="reference">runnalls2012a</a> <a href="#silles2010a" class="reference">silles2010a</a>) is a project that aims to remake fundamental parts of the standard R interpreter from C into C++, and enhance it with R data objects and provenance tracking.
            The goal of provenance tracking is to <span class="goal">provide an understanding of object derivations</span> by providing functions to obtain variables ancestors (i.e. which objects it depends on), descendants (i.e. which objects depends on it), and pedigree (i.e. the sequence of commands that led to its binding).
            Since it changes the standard R interpreter, it applies the <span class="strategy">overriding</span> strategy.
        </p>
        <p>
            <span class="collection">
                For provenance tracking, it attaches read and write monitors to <span title="scrips or Read-Evaluate-Print-Loops (REPL)">R global environments</span>. 
                Reading, creating or overwriting variable bindings in these environments trigger the monitors, which collect timestamp, expressions and children bindings of variable bindings. 
                <span title="B1 is a parent of B2 (B2 is a child of B1) if B1 was read in the course of evaluating the top-level expression that gave rise to binding B2">
                    A binding is a child of another when it uses its parent value during its evaluation. 
                </span>
                CXXR adds every new variable binding into a set of variables that the interpreter saw.
                This way, it avoids repeating provenance collection in loops.
            </span>
        </p>
        <p>
            <span class="collection">
                <span title="Do not add variables created as a result of a forced evaluation of lazy expression">
                    CXXR considers that top-level commands are provenance processes, and variables bindings are provenance entities.
                </span>
                Hence, it does not consider the result of function calls as provenance entities. However, for some <span title="xenogenetic functions">functions whose behavior is not is not fully define (e.g. reading user input or file content)</span>, CXXR creates the resulting value as a binding.
                Yet, as CXXR tracks only top-level provenance in the global environment, it is possible to evade provenance through local environments in stateful function calls.
            </span>
        </p>
        <p>
            <span class="analysis">
                For provenance analysis, CXXR allows users to call functions during the program execution, as it does not store provenance.
                Silles and Runnalls (<a href="#silles2010a" class="reference">2010</a>) describe two provenance retrieval functions: <em>provenance(x)</em> returns the timestamp of the binding x, the expression responsible for its current state and a list of both ancestors and descendants; and <em>pedigree(x)</em> returns the full sequence of commands that influenced the current binding of x, with all ancestors sorted by binding creation.
            </span>
        </p>
    """,
)

