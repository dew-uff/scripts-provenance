from snowballing.approaches import Group

from ..constants import *
from ...work.y2012 import tariq2012a

approach = Group(
    tariq2012a,
    display="Tariq, Ali, and Gehani",
    approach_name="-",
    _cite=True,

    _meta=[dict(
        binary=NO,
        languages=[AGNOSTIC.star("LLVM")],
        goal=COMPREHENSION,
        supports=[COMPREHENSION],
        categories=[COLLECTION, FILTER, STORAGE, VISUALIZATION],

        mode=USER_LEVEL,

        tools=["SPADE"],
        
        annotations=[PARSEABLE, EXTERNAL, EXCLUSIVE, OPTIONAL],
        execution=[OVERRIDING, INSTRUMENTATION],
        deployment=[],
        definition=[],

        execution_granularity=[
            FUNC_ARGUMENTS,
            FUNC_LINEAGE,
            STACK,
        ],
        deployment_granularity=[],
        definition_granularity=[],

        cache=NO,
        replay=NO,
        evolution=NO,
        pipeline=NO,
        summarization=[],

        distribution=[
            PROPRIETARY.such_as(["SPADE"]),
            INTEROPERABLE.such_as([OPM]),
        ],
        storage=[
            PROPRIETARY.such_as(["SPADE"]),
        ],
        visualization=[
            PROPRIETARY.such_as(["SPADE"]),
            INTEROPERABLE.such_as([OPM]),
            COMBINED_VIEW,
        ],
        visplace=[INTERNAL, EXTERNAL],
        query=[INTEROPERABLE.such_as([OPM])],
        integration=["SPADE"],
        
        granularity=[FUNCTION_CALLS, ARGUMENTS, RETURNS],
        granularity_text="Functions, Returns, Arguments, Stack Trace",
        management_text="Proprietary (SPADE), OPM",
        generic_query_text="",
        specific_query_text="OPM",
        thread=YES,
        diff=[],
                    
        limitations=["only LLVM"],
    )],
    _about="""
        <p>
            Tariq, Ali, and Gehani (<a href="#tariq2012a" class="reference">tariq2012a</a>) use the LLVM framework to add provenance instrumentation at compilation time for <span class="goal">comprehension</span>.
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
                Tariq, Ali, and Gehani (<a href="#tariq2012a" class="reference">tariq2012a</a>) produce an OPM graph that presents function calls as activities, as the result of this approach.
                They either print out the result to the standard output or launches a server and send the results to SPADE through TCP sockets.
                Since the provenance of all function calls can be overwhelming, they support using SPADE filters declared by users to filter out provenance records during collection.
            </span>
        </p>
    """,
)

