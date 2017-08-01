from snowballing.approaches import Group

from ..constants import *
from ...work.y2015 import greff2015a

approach = Group(
    greff2015a,
    display="Sacred",
    approach_name="Sacred",
    _cite=False,

    _meta=[dict(
        binary=NO,
        languages=[PYTHON],

        goal=REPRODUCIBILITY,
        supports=[REPRODUCIBILITY, MANAGEMENT, COMPREHENSION],
        categories=[COLLECTION, EVOLUTION, REPRODUCIBILITY, MANAGEMENT, FRAMEWORK],

        mode=USER_LEVEL,

        tools=[],
        
        annotations=[INTERNAL, EXECUTABLE, INCLUSIVE],
        execution=[INSTRUMENTATION],
        deployment=[BEFORE_EXECUTION],
        definition=[READING, STATIC, DYNAMIC],

        execution_granularity=[VALUES, OUTPUT_DATA, INPUT_FILES, OUTPUT_FILES],
        deployment_granularity=[MODULES, OS_VERSION],
        definition_granularity=[CONTENT, SOURCE],

        cache=NO,
        replay=NO,
        evolution=TRIAL_ID.star("Individual versions"),
        pipeline=NO,
        summarization=[],

        distribution=[],
        storage=[NOSQL.such_as(["MongoDB"])],
        visualization=[LOG_VIEW],
        visplace=[INTERNAL],
        query=[WEB],
        integration=[],
        
        granularity=[VALUES, OUTPUT_DATA, INPUT_FILES, OUTPUT_FILES, MODULES, OS_VERSION],
        granularity_text="User defined, Output, Modules, Host, Source, Files (I/O)",
        management_text="MongoDB",
        generic_query_text="",
        specific_query_text="Web",
        thread=UNKNOWN,
        diff=[],
                    
        limitations=[],
    )],
    _about="""
        <p>
            Sacred (<a href="#greff2015a" class="reference">greff2015a</a>) is a Python library for <span class="goal">configuring, organizing, logging and reproducing experiments</span>.
            Sacred requires users to <span class="strategy collection">instrument</span> the code specifying config parameters and main functions.
        </p>
        <p>
            <span class="collection">
                Sacred provides decorators for instrumenting config, main and other functions.
                The main function decorator also servers as a command line argument parser that allows users to variate configurations.
                Before the execution, Sacred collects the source code, the configured parameters, the module dependencies, resources and artifacts (files) and information about the host.
                To support randomness reproducibility, it also defines and captures random seeds for random and numpy modules.
                After the execution, it collects the stdout, status code, start and stop times, the main function result and fail-traces.
            </span>
        </p>
        <p>
            <span class="storage evolution">
                Sacred stores the provenance in MongoDB.
                It has a simple integrated version control system that stores all file contents and keeps references to them through MD5 hashes and name in collections of MongoDB.
            </span>
            <span class="analysis">
                For analysis, Sacred provides a Web and a desktop tool that presents a log of executions with their configurations and results.
            </span>
        </p>
    """,
)