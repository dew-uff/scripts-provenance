from snowballing.approaches import Group

from ..constants import *
from ...work.y2012 import gessiou2012a

approach = Group(
    gessiou2012a,
    display="Gessiou et al.",
    approach_name="-",
    _cite=True,

    _meta=[dict(
        binary=YES,
        languages=[AGNOSTIC],
        goal=FRAMEWORK,
        supports=[FRAMEWORK],
        categories=[FRAMEWORK, COLLECTION, STORAGE],

        mode=USER_LEVEL,

        tools=["DTrace"],
        
        annotations=[EXECUTABLE, EXTERNAL, INCLUSIVE, MANDATORY, DEFINITION],
        execution=[OVERRIDING, INSTRUMENTATION],
        deployment=[],
        definition=[],

        execution_granularity=[
            PROC_NAME,
            PROC_ARGUMENTS,
            FUNCTION_CALLS,
            STACK,
            USER_DEFINED
        ],
        deployment_granularity=[],
        definition_granularity=[],

        cache=NO,
        replay=NO,
        evolution=NO,
        pipeline=NO,
        summarization=[],

        distribution=[LOG],
        storage=[LOG],
        visualization=[],
        visplace=[],
        query=[],
        integration=[],
        
        granularity=[PROCESSES, USER_DEFINED],
        granularity_text="Processes, User defined",
        management_text="Log",
        generic_query_text="",
        specific_query_text="",
        thread=YES,
        diff=[],

        limitations=[],
    )],
    _about="""
        <p>
            Gessiou et al. (<a href="#gessiou2012a" class="reference">gessiou2012a</a>) propose a universal data provenance <span class="goal">framework</span> for transparently collecting provenance from binary applications.
            <span class="collection">
                They use DTrace to perform <span title="Disadvantages:Runtime overhead">dynamic instrumentation</span> and change the executable at runtime.
                DTrace performs system call and function level instrumentation of binary programs using D, a high-level programming language.
                It supports enabling and disabling instrumentations at runtime, on demand. 
                As DTrace changes the executable at runtime, Gessiou et al. (<a href="#gessiou2012a" class="reference">gessiou2012a</a>) apply the <span class="strategy">overriding</span> strategy for execution provenance collection.
            </span>
        </p>
        <p>
            <span class="collection">
                For provenance collection, users need to specify what they what to instrument.
                However, it requires knowing all entry points where data flows inside the process.
                To support the process of finding the right point of interest for provenance instrumentation, Gessiou et al. (<a href="#gessiou2012a" class="reference">gessiou2012a</a>) propose a configurable logging component and an assisted discovery mechanism.
                The configurable logging component monitors all system calls of all running process by default.
                <span class="storage">
                    However, users can configure it to log only specific function calls from a library by specifying the library name and the function name.
                </span>
                Thus, having the source code is not necessary for instrumentation, but it helps to determine what to instrument.
                The logging component collects system call arguments, return values, user id, process name, process id, and arguments.
                The assisted discovery instruments all functions to find inputs given by the user. When it finds the given input, it <span class="storage">logs the function name and calls stack</span>.
            </span>
        </p>
        <p>
            <span class="framework">
                After discovering points of interest through configurable monitoring and assisted discovery, users can dynamically instrument programs for capturing provenance with DTrace.
            </span>
        </p>
    """,

    evaluation="""
        File system operations, database transactions, web browser HTTP requests
    """,
)

