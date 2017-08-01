from snowballing.approaches import Group

from ..constants import *
from ...work.y2011 import gavish2011a

approach = Group(
    gavish2011a,
    display="VCR",
    approach_name="Verifiable Computational Result (VCR)",
    _cite=False,

    _meta=[dict(
        binary=NO,
        languages=[R, PYTHON, MATLAB],
        goal=REPRODUCIBILITY,
        supports=[REPRODUCIBILITY, COMPREHENSION],
        categories=[COLLECTION, QUERY],

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

        distribution=[REPOSITORY],
        storage=[LOG],
        visualization=[LOG_VIEW],
        visplace=[INTERNAL],
        query=[WEB.such_as(["Links"])],
        integration=["Plugins"],
        
        granularity=[VARIABLES, FUNCTION_CALLS, USER_DEFINED],
        granularity_text="User defined, Variables, Calls, Stack Trace",
        management_text="Log, Repository",
        generic_query_text="",
        specific_query_text="Web",
        thread=YES,
        diff=[],
                    
        limitations=[],
    )],
    _about="""
        <p>
            Gavish and Donoho (<a href="#gavish2011a" class="reference">gavish2011a</a>) propose using provenance to create a VCR (Verifiable Computational Result) identifiable by a VRI (Verifiable Result Identifier) as a link to a repository.
            <span class="storage reproducibility">
                This repository has both the goal of storing provenance and supporting data and metadata analysis.
                Results created under the same conditions should carry the same VRI.
                Thus, users can apply provenance for <span class="goal">repeatability checking</span>.
            </span>
        </p>
        <p>
            <span class="collection">
                For capturing provenance in scripts, they propose a plugin with implementations for R, Matlab, and Python. 
                The plugin includes four commands for provenance tracking and transference to a repository: <em>verifiable</em>, <em>chronicled</em>, <em>repository</em>, and <em>loadvcr</em>.
                Users need to <span class="strategy">instrument</span> their scripts with these commands.
            </span>
        </p>
        <p>
            <span class="collection">
                The <em>verifiable</em> command assigns a VRI (Verifiable Result Identifier) to a variable, turning it into a VCR (i.e. a monitored object with a verifiable computational result).
                The <em>chronicled</em> command records the function activation tree with function durations.
                The <em>loadvcr</em> command imports a VCR generated be a previous computation.
                Finally, the <em>repository</em> command indicates the provenance repository URL.
                During the execution, the VCR plugin sends the provenance to the repository.
            </span>
        </p>
    """,
)

