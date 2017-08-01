from snowballing.approaches import Group

from ..constants import *
from ...work.y2015 import dietrich2015a
    
approach = Group(
    dietrich2015a,
    display="versuchung",
    approach_name="versuchung",
    _cite=False,

    _meta=[dict(
        binary=NO,
        languages=[PYTHON],

        goal=REPRODUCIBILITY,
        supports=[COMPREHENSION, REPRODUCIBILITY, FRAMEWORK],
        categories=[COLLECTION, STORAGE, FRAMEWORK, REPRODUCIBILITY, QUERY],

        mode=USER_LEVEL,

        tools=[],
        
        annotations=[EXECUTABLE, INTERNAL, INCLUSIVE],
        execution=[INSTRUMENTATION],
        deployment=[],
        definition=[READING, STATIC, DYNAMIC],

        execution_granularity=[
            INPUT_FILES.star("*user"),
            OUTPUT_FILES.star("*user"),
            USER_DEFINED,
        ],
        deployment_granularity=[],
        definition_granularity=[
            VCS.star("*user")
        ],

        cache=NO,
        replay=NO,
        evolution=INTENTION.star("*opt. VCS"),
        pipeline=NO,
        summarization=[],

        distribution=[CONTENT_DATABASE, PROPRIETARY.such_as(["Dict"])],
        storage=[CONTENT_DATABASE, PROPRIETARY.such_as(["Dict"])],
        visualization=[], 
        visplace=[],
        query=[FUNCTIONS],
        integration=['dataref'],
        
        granularity=[FILES, USER_DEFINED],
        granularity_text="User defined, Files (I/O), Source",
        management_text="Content DB, Proprietary (Dict)",
        generic_query_text="",
        specific_query_text="Functions",
        thread=UNKNOWN,
        diff=[DATA.star("VCS")],
                    
        limitations=[],
    )],
    _about="""

         <p>
            versuchung (<a href="#dietrich2015a" class="reference">dietrich2015a</a> is a framework that allows users to orchestrate executable Python experiments and collect provenance from the dependencies and aggregate data and metadata.
            The goal of provenance tracking is to <span class="goal">support the replicability</span> of the experiment by <span class="strategy">instrumenting</span> it to collect input sources, output targets, and actual data.
        </p>
        <p class="collection">
            For collecting provenance, users need to specify their experiments using the versuchung embeded DSL (inheriting classes, calling special functions).
            This allows them to specify input sources (i.e., git repository, parameters), output targets (i.e., files, databases), and resulting data.
            Versuchung also collects the start and end time of the experiment.
            Versuchung provides functions for monitoring shell commands and the machine environment, such as the network activity, and the processor utilization.
        </p>
        <p class="storage">
            Versuchung calculates a hash based on the input parameters and creates a metadata file named after this hash in a artifact directory. This metadata file contains a plain-text representation of a Python data structure with all the collected information.
        </p>
        <p class="analysis">
            The framework itself can be used to load the metadata file for analysis. Thus, its execution creates a chained Experiment.
        </p>
        <p>
            versuchung in bundled with dataref, a latex package that allows users to describe data points and annotate them with metadata to describe experiments in the document. Dataref also allows users to validate data points through assertions.
        </p>

    """,
)

