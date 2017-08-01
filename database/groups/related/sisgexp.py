from snowballing.approaches import Group

from ..constants import *
from ...work.y2016 import cruz2016a
    
approach = Group(
    cruz2016a,
    display="SisGExp",
    approach_name="SisGExp",
    _cite=False,

    _meta=[dict(
        binary=NO,
        languages=[R],

        goal=MANAGEMENT,
        supports=[MANAGEMENT, COMPREHENSION, REPRODUCIBILITY],
        categories=[COLLECTION, QUERY, REPRODUCIBILITY],

        mode=USER_LEVEL,

        tools=["Kepler"],

        annotations=[PARSEABLE, EXTERNAL, INCLUSIVE, PROVENANCE],
        execution=[INSTRUMENTATION],
        deployment=[],
        definition=[READING, STATIC],

        execution_granularity=[INPUT_FILES, OUTPUT_FILES],
        deployment_granularity=[],
        definition_granularity=[SOURCE],

        cache=NO,
        replay=NO,
        evolution=NO,
        pipeline=NO,
        summarization=[],

        distribution=[REPOSITORY],
        storage=[CONTENT_DATABASE, RELATIONAL_DB.such_as(["PostgreSQL"])],
        visualization=[LOG_VIEW],
        visplace=[INTERNAL],
        query=[QUERY.such_as(["SQL"]), WEB],
        integration=["Kepler"],
        
        granularity=[INPUT_FILES, OUTPUT_FILES, SOURCE],
        granularity_text="User defined, Files (I/O), Source",
        management_text="PostgreSQL, Repository",
        generic_query_text="SQL",
        specific_query_text="Web",
        thread=UNKNOWN, # Does Kepler support threads?
        diff=[],
                    
        limitations=[],
    )],
    _about="""
        <p>
            SisGExp (<a href="#cruz2016a" class="reference">cruz2016a</a>) is a web application that allows scientists to <span class="goal"> manage </span> experiments by registering R scripts with input data. It applies the <span class="strategy"> instrumentation </span> strategy for provenance collection.
        </p>
        <p class="collection">
            For collecting provenance with SisGExp, users need to register R scripts, specifying input data and output targets, and other settings. The system also collects who registered the experiment.
            After registering the experiments, users can set the scripts to run with Kepler to collect execution time and output data. It uses a generic Meta-Workflow for the script execution.
        </p>
        <p>
            <span class="storage">SisGExp stores the provenance data in a PostgreSQL database</span> <span class="analysis"> and allows users to run SQL queries or to visualize logs in the web application. </span>
        </p>
    """,
)

