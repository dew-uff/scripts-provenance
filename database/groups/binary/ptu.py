from snowballing.approaches import Group

from ..constants import *
from ...work.y2013 import pham2013a

approach = Group(
    pham2013a,
    display="PTU",
    approach_name="Provenance-To-Use",
    _cite=False,

    _meta=[dict(
        binary=YES,
        languages=[AGNOSTIC],
        goal=REPRODUCIBILITY,
        supports=[REPRODUCIBILITY, CACHE, COMPREHENSION],
        categories=[CACHE, REPRODUCIBILITY, REPEATABILITY, VISUALIZATION],

        mode=USER_LEVEL,

        tools=["strace"],
        
        annotations=[],
        execution=[PASSIVE_MONITORING],
        deployment=[SNAPSHOT, CONTINUOUS],
        definition=[EXECUTION],

        execution_granularity=[
            INPUT_FILES,
            OUTPUT_FILES,
            PROC_NAME,
            PROC_PARANTAGE,
            PROC_LINEAGE,
            PROC_ARGUMENTS,
            MEMORY_FOOTPRINT,
            NETWORK,
        ],
        deployment_granularity=[
            ENV_VAR,
            MODULES,
        ],
        definition_granularity=[
            CONTENT,
        ],

        cache=YES,
        replay=YES,
        evolution=NO,
        pipeline=NO,
        summarization=[],

        distribution=[
            INTEROPERABLE.such_as([OPM]),
            PACKAGE.such_as([FILE_SYSTEM]),
        ],
        storage=[
            PACKAGE.such_as([FILE_SYSTEM]),
            RELATIONAL_DB.such_as(["SQLite"]),
        ],
        visualization=[INTEROPERABLE.such_as([OPM])],
        visplace=[EXTERNAL],
        query=[
            INTEROPERABLE.such_as([OPM]),
            QUERY.such_as(["SQL"])
        ],
        integration=[],
        
        granularity=[FILES, PROCESSES, NETWORK],
        granularity_text="Files (I/O - metadata), Processes, Network, Env. Variables",
        management_text="Package (file system), SQLite, OPM",
        generic_query_text="SQL",
        specific_query_text="OPM",
        thread=YES,
        diff=[],
                    
        limitations=[],
    )],
    _about="""
        <p>
            Provenance-To-Use (PTU) (<a href="#pham2013a" class="reference">pham2013a</a>) enhances CDE (<a href="#guo2012b" class="reference">guo2012b</a>, <a href="#guo2011c" class="reference">guo2011c</a>; <a href="#guo2011a" class="reference">guo2011a</a>) to use provenance for repeatability testing.
            <span class="collection storage">
                Since it is based on CDE, it collects <span title="Monitors ~50 system calls: process provenance: execve, sys_fork; file provenance: read, write, sys_io; network activity: bind, connect, socket, send">systems calls</span> to produce a package with all accessed files and environment variables for supporting the re-execution of experiments.
                However, different from CDE, PTU creates a provenance graph and stores it in an SQLite database inside the reproducible package.
                This provenance graph contains intermediate files, process information, and network activity.
            </span>
            <span class="repeatability">
                PTU uses the provenance graph for partial determinist replay, which allows users to re-execute experiments with previous data, avoiding re-computing intensive parts of the replay.
                Additionally, it allows testers to verify whether replays correspond to previous executions.
            </span>
        </p>
        <p>
            <span class="collection">
                During the collection, PTU collects the process identifier and uses it to extract more information about the processes tom Linux <em>/proc</em> file system. 
                PTU extracts the process name, owner, group, parent host, creation time, command line, environment variables, file name, path, host, size and modification time.
                For every three seconds, PTU obtains memory footprint, CPU consumption and I/O activity data for each process, using a different thread.
                <span title="Audits network activity independently at each node using ptrace. CMD makes all network system blocking during auditing, making the information extracted current and accurate">
                    Additionally, PTU audits network activity by collecting network connection information.
                </span>
            </span>
        </p>
        <p>
            <span class="collection">
                PTU does not create network dumps nor audits non-deterministic functions, such as ctime and random. 
                Thus, it is not always safe to replay using the collected data, and it is necessary to conduct network communications again during the replay.
            </span>
        </p>
        <p>
            <span class="repeatability">
                For repeatability testing, PTU allows testers to request the execution of a specific package by either modifying a run configuration file in the package or specifying nodes in the provenance graph.
                With flags that specify if a process needs to run or a file needs to be regenerated, PTU automatically sets other processes in the descendant provenance sub-graph for re-running or regeneration.
            </span>
        </p>
        <p>
            <span class="analysis">
                Besides repeatability testing, PTU also supports exporting and visualizing the provenance as an OPM compliant graph.
            </span>
        </p>
    """,
)

