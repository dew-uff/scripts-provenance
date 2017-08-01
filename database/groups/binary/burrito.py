from snowballing.approaches import Group

from ..constants import *
from ...work.y2012 import guo2012a, guo2012c

approach = Group(
    guo2012a,
    display="Burrito",
    approach_name="Burrito",
    _cite=False,
    dont_cite=[guo2012c],

    _meta=[dict(
        binary=YES,
        languages=[AGNOSTIC],
        goal=COMPREHENSION,
        supports=[COMPREHENSION, REPRODUCIBILITY, MANAGEMENT],
        categories=[COLLECTION, VISUALIZATION, DIFF, EVOLUTION],

        mode=SYSTEM_WIDE,

        tools=["SystemTap"],
        
        annotations=[PARSEABLE, EXTERNAL, INCLUSIVE, PROVENANCE, OPTIONAL],
        execution=[PASSIVE_MONITORING],
        deployment=[],
        definition=[READING],

        execution_granularity=[
            PROC_NAME, PROC_PARANTAGE, PROC_LINEAGE,
            PROC_ARGUMENTS, PROC_PIPE,
            INPUT_FILES, OUTPUT_FILES,
        ],
        deployment_granularity=[],
        definition_granularity=[SOURCE, PROGRAM, CONTENT],

        cache=NO,
        replay=YES.star("no guarantees"),
        evolution=SEQUENCE,
        pipeline=NO,
        summarization=[],

        distribution=[LOG.such_as(["Lab Notebook HTML"])],
        storage=[
            FILE_SYSTEM.such_as(["NILFS"]),
            NOSQL.such_as(["MongoDB"]),
        ],
        visualization=[LOG_VIEW.such_as(["Activity Feed"]), COMBINED_VIEW],
        visplace=[INTERNAL],
        query=[
            COMMAND.such_as(["File Lineage"]),
            QUERY.such_as(["MongoDB"])
        ],
        integration=["Plugins"],
        
        granularity=[PROCESSES, FILES, "Bash commands", "Website visits", USER_DEFINED.star("annotations")],
        granularity_text="Files (I/O), Processes, Bash Commands, Annotations",
        management_text="NILFS, MongoDB, Log",
        generic_query_text="MongoDB",
        specific_query_text="Command",
        thread=YES,
        diff=[DATA.star("*files")],
                    
        limitations=[],
    )],
    _about="""
        <p>
            Burrito (<a href="#guo2012a" class="reference">guo2012a</a>) uses <span class="mode">system-wide</span> provenance for <span class="goal">comprehending the process of developing experiments and managing them</span>.
            It uses <span class="tool">SystemTap</span> to monitor system calls and collect execution provenance using the <span class="strategy">passive monitoring</span> strategy.
            <span class="collection" title="through an OS-level provenance collection daemon">
                This monitor captures which processes were executed and which files did each process access;
            </span>
            <span class="analysis">
                allowing users to understand how each file was produced.
            </span>
            <span class="collection">
                Additionally, it uses a GUI tracer to monitor user interactions with GUI applications
            </span> 
            <span class="analysis>
                and provide context for what is happening at each time in the provenance analysis.
            </span>
            <span class="collection">
                Burrito also supports plugins to capture activities within applications.
                Thus, it is possible to use a bash plugin for recording executed bash commands or a Firefox plugin for recording the browser history.
            </span>
            <span class="collection" title="also creates checkpoint events">
                Finally, Burrito supports annotating the captured provenance to describe what is happening in the experiment.
            </span>
        </p>
        <p>
            <span class="collection">
                Burrito executes on top of an NILFS versioning file system (<a href="#konish2006a">KONISHI et al., 2006</a>), which is a file system that stores all old versions of source codes and data files without requiring external version control systems.
            </span>
            <span class="reproducibility">
                When combined to the provenance collected by Burrito, this versioning file system supports restoring old experiment versions and re-executing them.
            </span>
        </p>
        <p>
            <span class="analysis">
                For analysis, Burrito presents an activity feed that displays the stream of user’s actions, including program executions, file data productions, and annotations. Additionally, it provides a computational context viewer that supports visualizing all versions of a given file, with parameters and processes that created each one, and supports <span class="diff">comparing them side by side or by textual diffs</span>. Burrito can also export a Lab Notebook HTML with user’s activities and notes in a given period for sharing progress in experiments.
            </span>
        </p>
    """,
)

