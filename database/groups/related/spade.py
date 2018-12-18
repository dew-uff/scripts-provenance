from snowballing.approaches import Group

from ..constants import *
from ...work.y2011 import gehani2011a
from ...work.y2012 import tariq2012a, gehani2012a
from ...work.y2013 import moore2013a
from ...work.y2014 import gehani2014a
from ...work.y2016 import gehani2016a


approach = Group(
    tariq2012a, gehani2012a, gehani2011a, moore2013a, gehani2014a, gehani2016a,
    display="SPADE",
    approach_name="SPADE",
    emails="dawood.tariq@sri.com; ashish.gehani@sri.com",
    to="Tariq, Dawood and Gehani, Ashish",
    _cite=False,

    _meta=[dict(
        reply=True,
        binary=NO,
        languages=[AGNOSTIC.star("LLVM")],
        goal=COMPREHENSION,
        supports=[COMPREHENSION, REPRODUCIBILITY],
        categories=[COLLECTION, FILTER, STORAGE, VISUALIZATION, REPRODUCIBILITY],

        mode=USER_LEVEL,

        tools=[],

        annotations=[PARSEABLE, EXTERNAL, EXCLUSIVE, OPTIONAL, DEFINITION],
        execution=[OVERRIDING],
        deployment=[BEFORE_EXECUTION],
        definition=[],

        execution_granularity=[
            FUNC_ARGUMENTS,
            FUNC_LINEAGE,
            STACK,
        ],
        deployment_granularity=[],
        definition_granularity=[],

        cache=NO,
        replay=YES,
        evolution=NO,
        pipeline=NO,
        summarization=[FILTERING, CLUSTERING],

        distribution=[
            WEB.such_as(["Apache Kafka"]),
            INTEROPERABLE.such_as([PROV]),
            PROPRIETARY.such_as(["Text"]),
            LOGIC_FILE.such_as(["Datalog"]),
            GRAPH_FILE.such_as([GRAPHVIZ])
        ],
        storage=[
            RELATIONAL_DB.such_as(["Postgres", "MySQL", "H2"]),
            GRAPH_DB.such_as(["Neo4j"]),
            INTEROPERABLE.such_as([PROV]),
            PROPRIETARY.such_as(["Text"]),
            LOGIC_FILE.such_as(["Datalog"]),
            GRAPH_FILE.such_as([GRAPHVIZ])
        ],
        visualization=[
            PROPRIETARY.such_as(["SPADE"]),
            INTEROPERABLE.such_as([PROV]),
            COMBINED_VIEW,
        ],
        visplace=[INTERNAL, EXTERNAL],
        query=[INTEROPERABLE.such_as([PROV])],
        integration=[],

        granularity=[FUNCTION_CALLS, ARGUMENTS, RETURNS],
        granularity_text="Functions, Returns, Arguments, Stack Trace, Env. Var.",
        management_text="DB, PROV",
        generic_query_text="SQL, Cypher, Datalog",
        specific_query_text="PROV, Functions",
        thread=YES,
        diff=[PROVENANCE],

        limitations=["only LLVM"],
    )],
    _about="""
        <p>
            SPADE (<a href="#tariq2012a" class="reference">tariq2012a</a>) uses the LLVM framework to add provenance instrumentation at compilation time for <span class="goal">comprehension</span>.
            <span class="collection">
                It modifies function calls in programs compiled by an LLVM compiler to insert instrumentation for provenance collection.
                Thus, it applies the overriding strategy.
                This approach collects function calls, arguments and return values as execution provenance.
            </span>
        </p>
        <p>
            <span class="collection">
                This approach can be used for scripting language that uses LLVM compilers (<a href="https://blog.pyston.org/" class="web_reference">DROPBOX, 2016</a>). 
                However, it only accesses primitive types, since the LLVM has no information about language-specific data structures.
                While this limitation does not prevent lineage collection, it may prevent the understanding in some scripting languages that use language specific data structures to wrap primitive types.
            </span>
        </p>
        <p>
            <span class="storage filter">
                SPADE (<a href="#tariq2012a" class="reference">tariq2012a</a>) produce an PROV graph that presents function calls as activities, as the result of this approach.
                They either print out the result to the standard output or launches a server and send the results to SPADE through TCP sockets.
                Since the provenance of all function calls can be overwhelming, they support using SPADE filters declared by users to filter out provenance records during collection.
            </span>
        </p>
    """,
)

