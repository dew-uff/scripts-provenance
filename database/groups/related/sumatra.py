from snowballing.approaches import Group

from ..constants import *
from ...work.y2012 import davison2012a
from ...work.y2014 import davison2014a

approach = Group(
    davison2012a,
    display="Sumatra",
    approach_name="Sumatra",
    emails="andrew.davison@unic.cnrs-gif.fr; mattions@gmail.com; samarkanov@gmail.com; telenczuk@unic.cnrs-gif.fr",
    _cite=False,
    dont_cite=[davison2014a,],

    _meta=[dict(
        reply=None,
        binary=NO,
        languages=[AGNOSTIC, PYTHON],
        goal=REPRODUCIBILITY,
        supports=[REPRODUCIBILITY, COMPREHENSION, MANAGEMENT],
        categories=[COLLECTION, DIFF, MANAGEMENT, QUERY, REPRODUCIBILITY, STORAGE],

        mode=USER_LEVEL,

        tools=["VCS"],

        annotations=[PARSEABLE, EXTERNAL, INCLUSIVE, PROVENANCE, OPTIONAL],
        execution=[POST_MORTEM],
        deployment=[BEFORE_EXECUTION],
        definition=[READING, STATIC],

        execution_granularity=[
            INPUT_FILES,
            OUTPUT_FILES,
            PROC_NAME,
            PROC_DURATION,
            PROC_ARGUMENTS,
            TERMINAL,
        ],
        deployment_granularity=[
            ENV_VAR,
            MODULES,
        ],
        definition_granularity=[
            CONTENT
        ],

        cache=NO,
        replay=YES.star("no guarantees"),
        evolution=INTENTION,
        pipeline=NO,
        summarization=[],

        distribution=[VCS],
        storage=[CONTENT_DATABASE.star("VCS"), RELATIONAL_DB.such_as(["SQLite"])],
        visualization=[LOG_VIEW],
        visplace=[INTERNAL],
        query=[
            COMMAND.such_as(["Annotations"]),
            QUERY.such_as([SQL]),
            WEB.such_as(["Textual listing"]),
        ],
        integration=["Plugins"],

        granularity=[FILES],
        granularity_text="Modules, Files (I/O)",
        management_text="SQLite, VCS",
        generic_query_text="SQL",
        specific_query_text="Command, Web",
        thread=YES,
        diff=[DATA.star("VCS"), PROVENANCE],

        limitations=[],
    )],
    _about="""
        <p>
            Sumatra (<a href="#davison2012a" class="reference">davison2012a</a>) uses provenance to support <span class="goal">reproducibility</span>.
            <span class="reproducibility"> 
                It provides commands for re-executing trials and comparing previous trial results. 
            </span>
            <span class="collection">
                Sumatra collects deployment, definition and execution provenance before and after each trial.
            </span> 
            <span class="evolution">
                Additionally, it keeps the evolution provenance and supports tagging trials.
            </span>
        </p>
        <p>
            <span class="collection" title="Steps: (i) Create new record; (2) Check changes in code; (3) Store diffs; (4) Find dependencies; (5) Look for environment characteristics; (6) Run simulation; (7) Store time; (8) Find new files; (9) Add tags; (10) Save record">
                When a user runs a program or script with Sumatra, it collects hardware information, operating system version, and binary executable version as deployment provenance; it collects input files as definition provenance; and it collects output files, terminal output, program arguments and execution duration as execution provenance. Sumatra applies the post-mortem strategy for execution provenance collection, as it identifies files that existed before the execution and compares to new files. For Python scripts, Sumatra also collects imported modules with their versions as deployment provenance and the script definition as definition provenance.
            </span>
        </p>
        <p>
            <span class="storage evolution">
                Sumatra uses both a version control system and a relational database (SQLite) to store provenance content.
                It stores metadata in the SQLite database and files in the version control system.
            </span>
            <span class="evolution">
                Using version control systems gives Sumatra the ability to track provenance evolution.
            </span>
        </p>
        <p>
            <span class="reproducibility analysis">
                Sumatra has the goal of supporting reproducibility. 
                Thus, it provides a web application and command line tools that list trials, summarizes them, compares them, and supports describing previous executions.
                Additionally, Sumatra provides a command line tools for repeating trials using the same arguments.
                This command checks if there are changes on the collected data before running.
            </span>
        </p>
    """,
)