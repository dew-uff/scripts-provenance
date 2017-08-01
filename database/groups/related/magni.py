from snowballing.approaches import Group

from ..constants import *
from ...work.y2016 import oxvig2016a

approach = Group(
    oxvig2016a,
    display="Magni",
    approach_name="Magni",
    _cite=False,

    _meta=[dict(
        binary=NO,
        languages=[PYTHON],

        goal=REPRODUCIBILITY,
        supports=[REPRODUCIBILITY, FRAMEWORK],
        categories=[COLLECTION, REPRODUCIBILITY],

        mode=USER_LEVEL,

        tools=[VCS],
        
        annotations=[EXECUTABLE, INTERNAL, INCLUSIVE], 
        execution=[INSTRUMENTATION],
        deployment=[DURING_EXECUTION],
        definition=[READING, STATIC],

        execution_granularity=[USER_DEFINED],
        deployment_granularity=[SELF_VERSION, OS_VERSION, VCS],
        definition_granularity=[SOURCE, STACK],

        cache=NO,
        replay=NO,
        evolution=INTENTION.star("*opt VCS"),
        pipeline=NO,
        summarization=[],

        distribution=[PROPRIETARY.such_as(["JSON", "HDF5"])],
        storage=[PROPRIETARY.such_as(["JSON", "HDF5"])],
        visualization=[],
        visplace=[],
        query=[],
        integration=[],
        
        granularity=[USER_DEFINED, SELF_VERSION, OS_VERSION, VCS, SOURCE, STACK],
        granularity_text="User defined, Stack Trace, Platform, Source",
        management_text="Proprietary (JSON, HDF5)",
        generic_query_text="",
        specific_query_text="",
        thread=YES,
        diff=[DATA.star("VCS")],
                    
        limitations=[],
    )],
    _about="""
        <p>
            Magni (<a href="#oxvig2016a" class="reference">oxvig2016a</a>) is a library that captures provenance from Python scripts for <span class="goal">reproducibility</span> through the <span class="strategy"> instrumentation </span> strategy.
        </p>
        <p class="collection">
            It requires users to instrument the code with functions specifying which data should it collect.
            In addition to the user-defined data, when Magni creates a database for a trial, it collects the git revision number, the datetime, the information about Conda environment (optional), information about magni itself, and about the platform. Additionally, it captures the main source code and the stack trace.
        </p>
        <p class="storage">
            Magni supports storing the provenance either in a JSON file or in a HDF5 database.
        </p>
    """,
)