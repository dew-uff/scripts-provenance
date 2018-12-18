from snowballing.approaches import Group

from ..constants import *
from ...work.y2010 import angelino2010a
from ...work.y2011 import angelino2011a

approach = Group(
    angelino2010a, angelino2011a,
    display="Star  Flow",
    approach_name="StarFlow",
    emails="elaine@eecs.harvard.edu; mseltzer@cs.ubc.ca",
    # Invalid: yamins@fas.harvard.edu;

    to="Angelino, Elaine and Seltzer, Margo",
    _cite=False,

    _meta=[dict(
        reply=True,
        binary=NO,
        languages=[PYTHON],
        goal=MANAGEMENT,
        supports=[MANAGEMENT, COMPREHENSION, CACHE, REPRODUCIBILITY],
        categories=[CACHE, COLLECTION, QUERY, STORAGE, VISUALIZATION, PARALLEL],

        mode=USER_LEVEL,

        tools=["AST"],

        annotations=[PARSEABLE, EXECUTABLE, INTERNAL, INCLUSIVE, OPTIONAL, DEFINITION],
        execution=[PASSIVE_MONITORING, OVERRIDING, INSTRUMENTATION],
        deployment=[BEFORE_EXECUTION],
        definition=[PARSING, STATIC, DYNAMIC],

        execution_granularity=[
            INPUT_FILES,
            OUTPUT_FILES,
            FUNC_LINEAGE,
            STACK,
        ],
        deployment_granularity=[
            MODULES,
        ],
        definition_granularity=[
            FUNC_LINEAGE,
        ],

        cache=YES,
        replay=NO,
        evolution=NO,
        pipeline=YES.star("*optional"),
        summarization=[],

        distribution=[
            INTEROPERABLE.such_as([OPM]),
            PROPRIETARY.such_as([XML, "CSV"]),
        ],
        storage=[
            INTEROPERABLE.such_as([OPM]),
            PROPRIETARY.such_as([XML, "CSV"]),
        ],
        visualization=[],
        visplace=[EXTERNAL],
        query=[
            FUNCTIONS.such_as(["Navigation", "Cache"]),
            INTEROPERABLE.such_as([OPM])
        ],
        integration=["PASS through layering system"],

        granularity=[FUNCTIONS, FILES],
        granularity_text="Functions, Modules, Files (I/O), Stack Trace",
        management_text="OPM, Proprietary (CSV)",
        generic_query_text="",
        specific_query_text="Functions, OPM",
        thread=YES,
        diff=[PROVENANCE, DATA.star("cache")],

        limitations=[],
        extra=dict(
            applications="distribute"
        ),
    )],
    _about="""
        <p>
            StarFlow (<a href="#angelino2011a" class="reference">angelino2011a</a>; <a href="#angelino2010a" class="reference">angelino2011a</a>) collects provenance of Python scripts for <span class="goal">understanding file dependencies, abstracting workflows and running functions in parallel</span>. 
            It assumes that users may want to understand experiments even before running them.
            <span class="collection">
                For understanding, it considers that dynamic analysis is helpful but not fundamental. 
                Thus, it combines dynamic runtime analysis, static analysis, and annotations to collect provenance propagation.
            </span>
        </p>
        <p>
            <span class="collection">
                StarFlow allows users to annotate functions to represent function inputs as dependencies of function outputs. 
                It supports specifying dependencies statically through named arguments or dynamically through decorators that specify which argument represents each dependency. 
            </span>
        </p>
        <p>
            <span class="collection">
                During static analysis, StarFlow uses the Python last module to extract most control flow, functional dependency, and annotations as definition provenance.
                In addition to control flow and functional dependency, StarFlow also observes all <em>import</em> statements to collect module dependencies as deployment provenance. 
                StarFlow considers the dependency provenance self-contained in the scripts.
                Thus, sharing the code also shares dependencies.
            </span>
        </p>
        <p>
            <span class="collection">
                During dynamic analysis, StarFlow applies the passive monitoring strategy by setting a <span title="sys.settrace">Python tracing function</span> that walks the function stack to collect execution provenance.
                The tracing function extract function calls with their stack and identifies which files each function access. 
                StarFlow supports logging the execution provenance, comparing to results of static analysis to check for consistency, or creating dependencies not captured by annotations.
            </span>
            <span class="collection">
                StarFlow also applies the overriding strategy for execution provenance collection by overriding the open function into an enriched version that collects the provenance.
            </span>
        </p>
        <p>
            <span class="collection">
                StarFlow uses the static dependency information to produce a pipeline graph.
                StarFlow produces this pipeline graph by collating functions according to their annotations.
                For instance, suppose there are three annotated functions: <em>step1</em>, <em>step2</em>, and <em>step3</em>.
                The function <em>step1</em> has an annotation that specifies that it reads <em>input1.dat</em> and writes <em>intermediate.dat</em>.
                The function <em>step2</em> reads <em>intermediate.dat</em> and writes <em>output.dat</em>.
                Finally, <em>step3</em> reads <em>intermediate.dat</em> and <em>input2.dat</em> and writes <em>graph.png</em>.
                With this information, StarFlow produces an executable pipeline where <em>step1</em> executes before <em>step2</em> and <em>step3</em>; and these two steps execute in parallel.
                After creating this pipeline graph, StarFlow can distribute function executions to a cluster and coordinate the dependency transference.
                Additionally, StarFlow can use the dependency information to determine which functions should be re-executed. For instance, by changing <em>input2.dat</em>, StarFlow just need to re-execute <em>step3</em>.
            </span>
        </p>
        <p>
            <span class="sweeping">
                Since StarFlow runs over Python scripts and enables parallelization through static analysis, it supports defining abstract workflows as scripts that create other scripts with static annotations.
                Then, it provides some special functions for coordinating the execution of these generated scripts.
                Users can use abstract workflows for parameter sweeping.
            </span>
        </p>
        <p>
            <span class="collection">
                Executing the StarFlow pipeline in parallel is optional. 
                Since it uses Python scripts, users can determine themselves the execution order through common function calls. 
                In this case, users can use the collected provenance for understanding. 
                When using provenance for understanding, using function annotations is optional as well, since the dynamic analysis is able to collect all executed functions as dependencies.
            </span>
        </p>
        <p>
            <span class="storage">
                StarFlow stores provenance on the disk in a serializable format. 
                It supports storing CSV, XML and RDF consistent with the OPM format. 
            </span>
            <span class="analysis">
                For analysis, StarFlow provides a set of Python command-line tools for navigating dependencies <span title="DownstreamLinks()">downstream</span> and <span title="UpstreamLinks()">upstream</span>, <span title="ShowUpdates(): Describes what Python funtions to execute, and in what order, to update dependency targets relative to the source">determining the script pipeline</span>.
            </span>
        </p>
        <p>
            <span class="integration">
                Angelino et al. (<a href="#angelino2011a" class="reference">2011</a>) integrate StarFlow to PASS through the DBAPI provided by the second version of PASS.
                This integration combines system provenance (i.e. files and processes) with script specific provenance (i.e. function calls, annotation).
                Additionally, it allows StarFlow provenance to be stored in PASS database.
            </span>
        </p>
    """,
)

