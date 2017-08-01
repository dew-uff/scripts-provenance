from snowballing.approaches import Group

from ..constants import *
from ...work.y2008 import bochner2008a

approach = Group(
    bochner2008a,
    display="Bochner, Gude, and Schreiber",
    approach_name="-",
    _cite=True,

    _meta=[dict(
        binary=NO,
        languages=[PYTHON],

        goal=COMPREHENSION,
        supports=[COMPREHENSION, FRAMEWORK],
        categories=[COLLECTION, QUERY, STORAGE],

        mode=USER_LEVEL,

        tools=[],
        
        annotations=[EXECUTABLE, INTERNAL, INCLUSIVE],
        execution=[INSTRUMENTATION],
        deployment=[],
        definition=[],

        execution_granularity=[
            INPUT_FILES.star("*user"),
            OUTPUT_FILES.star("*user"),
            FUNC_ARGUMENTS.star("*user"),
            FUNC_LINEAGE.star("*user"),
            VARIABLE_LINEAGE.star("*user"),
            COMMAND_LINEAGE.star("*user"),
            STACK.star("*user"),
            USER_DEFINED
        ],
        deployment_granularity=[],
        definition_granularity=[],

        cache=NO,
        replay=NO,
        evolution=NO,
        pipeline=NO,
        summarization=[],

        meta_distribution=[],
        distribution=[],
        storage=[NOSQL.such_as([XML_SERVER])],
        visualization=[],
        visplace=[],
        query=[
            QUERY.such_as([XQUERY, XPATH]),
            WEB.such_as(["SOAP messages"])
        ],
        integration=[],
        
        granularity=[USER_DEFINED],
        granularity_text="User defined",
        management_text="XML Server",
        generic_query_text="XQuery, XPath",
        specific_query_text="Web",
        thread=YES.star("*user"),
        diff=[],
                    
        limitations=[],
    )],
    _about="""
        <p>
            Bochner, Gude, and Scheireber (<a href="#bochner2008a" class="reference">bochner2008a</a>) propose a library to collect provenance in Python scripts to <span class="goal">check for compliance with applicable regulations</span>.
            <span class="collection">
                This library requires users to <span title="Defines a recording protocol to record the process documentation">annotate</span> what and how they want to capture.
                Thus, it applies the instrumentation strategy for gathering execution provenance.
            </span>
        </p>
        <p>
            <span class="storage">
                During user-defined provenance collection, the library connects to remote storage services for storing provenance as XML documents.
            </span>
            <span class="analysis" title="Defines protocols to query using XQuery and XPath">
                Hence, it supports provenance querying with XQuery and XPath
            </span>.
        </p>
    """,
)
