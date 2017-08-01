from snowballing.approaches import Group

from ..constants import *
from ...work.y2007 import zhang2007a

approach = Group(
    zhang2007a,
    display="Zhang et al.",
    approach_name="-",
    _cite=True,

    _meta=[dict(
        binary=YES,
        languages=[AGNOSTIC],
        # operating system related; comprehension; reproducibility; cache
        goal=COMPREHENSION,
        supports=[COMPREHENSION],
        categories=[COLLECTION, STORAGE],

        mode=USER_LEVEL,

        tools=["Valgrind"],
        
        annotations=[],
        execution=[OVERRIDING],
        deployment=[],
        definition=[],

        execution_granularity=[
            BYTE_LINEAGE,
            PROGRAM_SLICING,
        ],
        deployment_granularity=[],
        definition_granularity=[],

        cache=NO,
        replay=NO,
        evolution=NO,
        pipeline=NO,
        summarization=[],

        distribution=[],
        storage=[RELATIONAL_DB],
        visualization=[],
        visplace=[],
        query=[QUERY.such_as([SQL])],
        integration=[],
        
        granularity=[BYTES, VAR_DEPENDENCIES],
        granularity_text="Bytes, Dependencies",
        management_text="Relational DB",
        generic_query_text="SQL",
        specific_query_text="",
        thread=YES,
        diff=[],
                    
        limitations=[],
        extra=dict(
            applications=["Understand which input influence each output"],
        ),
    )],
    _about="""
        <p>
            Zhang et al. (<a href="#zhang2007a" class="reference">zhang2007a</a>) apply program slicing to collect execution provenance from programs binaries and understand how function output is derived from the input.
            <span class="collection">
                They use Valgrind for lineage tracing. 
                Valgrind is a dynamic instrumentation engine that adds user code into the original binary when it is about to execute.
                Thus, Zhang et al. (<a href="#zhang2007a" class="reference">zhang2007a</a>) use the <span class="strategy">overriding</span> strategy for execution provenance gathering.
            </span>
        </p>
        <p>
            <span class="collection">
                Zhang et al. (<a href="#zhang2007a" class="reference">zhang2007a</a>) collect provenance at the byte level and traces byte dependencies with the goal of the obtaining function arguments, returns and database attributes.
                <span title="Each unique lineage set is represented by a unique integer, which can be considere as an index to the universal roBDD which stores all lineage sets">
                    During the collection, they use a reduced ordered binary decision diagram to store provenance efficiently. 
                    They also implement shadow space and shadow registers to keep provenance of each memory and register byte during execution. 
                </span>
            </span>
            <span class="storage" title="While the paper does not specify a generic way to store fine-grained provenance, it proposes identifying data items in the file by the offset in the file and their data length; using a scheme proposed by Buneman et al. [zhang2007a\12] to store semi-structured data; or store at the attribute level">
                After the execution, they suggest storing provenance in a relational database for further analysis.
            </span>
        </p>
    """,
)
