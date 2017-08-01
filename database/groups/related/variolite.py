from snowballing.approaches import Group

from ..constants import *
from ...work.y2017 import kery2017a

approach = Group(
    kery2017a,
    display="Variolite",
    approach_name="Variolite",
    _cite=False,

    _meta=[dict(
        binary=NO,
        languages=[AGNOSTIC],

        goal=MANAGEMENT,
        supports=[MANAGEMENT, REPRODUCIBILITY, COMPREHENSION],
        categories=[MANAGEMENT, EVOLUTION, DIFF, REPRODUCIBILITY],

        mode=USER_LEVEL,

        tools=[], # AST, kernel, systemtap, vcs, and others that assist the collection
        
        annotations=[PARSEABLE, EXTERNAL, INCLUSIVE, PROVENANCE, OPTIONAL],
        execution=[POST_MORTEM],
        deployment=[],
        definition=[READING, STATIC],

        execution_granularity=[OUTPUT_DATA, ARGUMENTS],
        deployment_granularity=[],
        definition_granularity=[CONTENT, SOURCE, ARGUMENTS],

        cache=NO,
        replay=YES,
        evolution=INTENTION,
        pipeline=NO,
        summarization=[],

        distribution=[PROPRIETARY.such_as(["JSON"])],
        storage=[PROPRIETARY.such_as(["JSON"])],
        visualization=[LOG_VIEW],
        visplace=[INTERNAL],
        query=[COMMAND],
        integration=[],
        
        granularity=[OUTPUT_DATA, ARGUMENTS,CONTENT, SOURCE],
        granularity_text="Arguments, Output, Source",
        management_text="Proprietary (JSON)",
        generic_query_text="",
        specific_query_text="Command",
        thread=UNKNOWN,
        diff=[DATA.star("VCS")],
                    
        limitations=[],
    )],
    _about="""
        <p>
            Variolite (<a href="#kery2017a" class="reference">kery2017a</a>) is a Atom plugin that allows scientists to <span class="goal">manage</span> their scripts' variants by selecting parts they want to change.
            It applies the <span class="collection strategy">post-mortem</span> strategy to collect the output of variant execution and associate it to the variant version.
        </p> 
        <p class="collection">
            Variolite wraps the execution of the scripts to record parameters used, and inputs/outputs from the run.
            <span class="storage">
                It saves this data in JSON files separate from the code.
                Variolite lets the user decide whether they want to store copies of the results or just pointers.
            </span>
            When the user runs the code, Variolite creates a commit with the variant and the provenance.
            Users can also tag versions to tell what their execution where about.
        </p>
        <p class="reproducibility evolution">
            Variolite allows users to navigate on previous versions by checking their outputs and restoring their versions.
            It keeps tracks on all branchs of variants in the code.
            Variolite keeps revision trees for both the files and variant boxes. File variants use references to varint boxes.
        </p>
    """,
)