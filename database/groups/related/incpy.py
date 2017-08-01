from snowballing.approaches import Group

from ..constants import *
from ...work.y2010 import guo2010a
from ...work.y2011 import guo2011b
from ...work.y2012 import guo2012c

approach = Group(
    guo2010a, guo2011b,
    display="IncPy",
    approach_name="Incremental Python",
    _cite=False,
    dont_cite=[guo2012c],

    _meta=[dict(
        binary=NO,
        languages=[PYTHON],
        goal=CACHE,
        supports=[CACHE],
        categories=[COLLECTION, CACHE],

        mode=USER_LEVEL,

        tools=[],
        
        annotations=[EXECUTABLE, INTERNAL, INCLUSIVE, EXCLUSIVE, OPTIONAL],
        execution=[OVERRIDING, INSTRUMENTATION],
        deployment=[],
        definition=[PARSING, READING, STATIC, DYNAMIC],

        execution_granularity=[
            INPUT_FILES,
            OUTPUT_FILES,
            FUNC_ARGUMENTS,
            FUNC_LINEAGE,
            FUNC_DURATION,
            VARIABLE_LINEAGE.star("*global"),
            TERMINAL,
            STACK,
        ],
        deployment_granularity=[],
        definition_granularity=[BYTECODE, CONTENT],

        cache=YES,
        replay=NO,
        evolution=NO,
        pipeline=NO,
        summarization=[],

        distribution=[CONTENT_DATABASE],
        storage=[CONTENT_DATABASE],
        visualization=[],
        visplace=[],
        query=[],
        integration=[],
        
        granularity=[FILES, FUNCTION_CALLS, VARIABLE_LINEAGE.star("*global")],
        granularity_text="Functions, Globals, Stack, Output, Files (I/O)",
        management_text="Content DB",
        generic_query_text="",
        specific_query_text="",
        thread=YES,
        diff=[PROVENANCE, DATA.star("cache")],

        limitations=["determinism", "impure functions"],
    )],
    _about="""
        <p>
            IncPy (<a href="#guo2010a" class="reference">guo2010a</a>, <a href="#guo2011b" class="reference">guo2011b</a>) collects provenance to <span class="goal">support cache invalidation</span>. 
            <span class="collection">
                It modifies the Python interpreter to enhance Python with automatic provenance collection and memoization of long running function executions.
            </span>
            <span class="cache">
                When the modified interpreter invokes a function that has a memoized result, it observes the function provenance to check whether the function has the same arguments and dependencies of the memoized results.
                The interpreter uses the memoized results only when it safe to do so.
            </span>
            <span class="collection">
                Since IncPy modifies how the interpreter handles functions for memoization, it collects provenance through the <span class="strategy">overriding</span> strategy.
            </span>
        </p>
        <p>
            <span class="collection" title="Is not designed to track fine-grained changes in code or data. If even one line in a function or dataset changes, IncPy deletes cache entries that depend on that code or data">
                For each function execution, IncPy collects the function name, function definition, passed arguments, global variables, input files, code dependencies (e.g. functions executed inside the cached one), output files, return values, terminal output and function duration.
                As function definition, it collects the function bytecode to avoid spacing, commentaries, and other cosmetic changes to break memoization.
                It uses <span class="tool">cPickle</span> to serialize entire arguments, global variables, and return values recursively.
            </span>
        </p>
        <p>
            <span class="cache">
                It uses the function name, function definition, passed arguments, global variables, input files, and code dependencies to identify the memoized value.
                Thus, if an argument, global variable or input file changes, IncPy will not use the memoized results.
                If the user changes the memoized function definition or the definition of any function that has the memoized function in their stack (e.g. a function called by the memoized one), IncPy automatically deletes previous cache entries.
                When IncPy uses memoized values for a function, it makes the function just copy output files, print terminal output cache and return cached return values.
            </span>
        </p>
        <p>
            <span class="cache collection" title="Does not mark function as impure if it just writes text to terminal or just write to the filesystem, unless the script opens the file for appending or opens the file before the function execution">
                IncPy only memoizes deterministic pure functions (i.e. functions that do not change global states and always produce the same results for the same input).
                It determines whether a function is pure or not by tracking where variables were defined and collecting dependencies of global variables, and arguments.
                Note that a call can be considered pure for some arguments and impure by others.
                IncPy considers calls that access random number generators and system clock as non-deterministic.
            </span>
        </p>
        <p>
            <span class="collection">
                Since it captures provenance with the Python interpreter, IncPy cannot track impurity, dependencies or non-determinism in C/C++ extensions and external executables.
                Additionally, it does not handle non-determinism from network accesses.
                Thus, it allows users to annotate which functions they always or never want to memoize.
            </span>
        </p>
        <p>
            <span class="storage">
                IncPy stores the memoization when the function is about to exit.
                It allows users to continue interrupted executions. At the function exit moment, it collects the function duration and checks if it took more than one second to run.
                IncPy only caches functions that take more than one seconds to run.
                Additionally, it tracks the time it takes to store the cache on the disk.
                If it is longer than the call duration, it assumes that it is faster to compute the function again than to use the cached results, and it removes the cache. 
            </span>
        </p>
    """,

    evaluation="Evaluates times for 6 approaches (guo2011b): [9],[15],[16],[22],[13]",
)

