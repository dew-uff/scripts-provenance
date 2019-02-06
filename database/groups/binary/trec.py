from snowballing.approaches import Group

from ..constants import *
from ...work.y1998 import vahdat1998a

approach = Group(
    vahdat1998a,
    display="TREC",
    approach_name="Transparent Result Caching",
    _cite=False,

    _meta=[dict(
        binary=YES,
        languages=[AGNOSTIC],
        goal=CACHE,
        supports=[CACHE, COMPREHENSION],
        categories=[CACHE, COLLECTION, QUERY],

        mode=USER_LEVEL,

        tools=["Solaris PROC"],
        
        annotations=[],
        execution=[PASSIVE_MONITORING],
        deployment=[SNAPSHOT, CONTINUOUS],
        definition=[],

        execution_granularity=[
            PROC_NAME,
            PROC_PARANTAGE,
            PROC_LINEAGE,
            PROC_ARGUMENTS,
            INPUT_FILES,
            OUTPUT_FILES.star("I/O files becomes output files"),
        ],
        deployment_granularity=[
            ENV_VAR,
            MODULES,
        ],
        definition_granularity=[
            CONTENT.star("*last")
        ],

        cache=YES,
        replay=YES.star("no guarantees"),
        evolution=NO,
        pipeline=NO,
        summarization=[],

        distribution=[],
        storage=[RELATIONAL_DB.star("Database (?)")],
        visualization=[],
        visplace=[],
        query=[COMMAND],
        integration=[],
        
        granularity=[FILES],
        granularity_text="Files (I/O - metadata), Env. Var.",
        management_text="Database",
        generic_query_text="",
        specific_query_text="Command",
        thread=YES,
        diff=[DATA.star("cache")],
                    
        limitations=["difficult to trace inputs", "non-determinism"],
        extra=dict(
            applications=["transparent make", "web-cache"],
        )
    )],
    _about="""
        <p>
            Transparent Result Caching (TREC) (<a href="#vahdat1998a" class="reference">vahdat1998a</a>) uses provenance for <span class="goal">cache invalidation</span>.
            <span class="collection"> 
                It captures deployment and execution provenance of unmodified binary programs during execution.
                Thus, it supports provenance from scripts by capturing binary provenance from script interpreters.
            </span>
        </p>
        <p>
            <span class="collection"> 
                TREC uses Solaris proc file system for gathering provenance.
                The proc file system runs at the user-level (i.e. without root) and intercepts a set of <span title="Avoid intercepting read and write due the overhead">system calls</span> (e.g. open, fork, creat, exec) of monitored processes. 
                TREC extracts necessary information from these system calls to build dependency information. 
                Thus, TREC applies the <span class="strategy">passive monitoring</span> strategy for extracting provenance.
            </span>
        </p>
        <p>
            <span class="collection"> 
                For each monitored processes, TREC captures the parent process, children processes, input files and output files.
                Process parentage describes the process lineage.
                When a monitored process invokes a new process, TREC collects environment variables and line arguments as its deployment information.
                When a process ends, TREC computes the process duration.
                For each collected output file, TREC collects file dependencies as the sequence of processes and set of input files used to create the file.
                TREC considers files that are both read and written as only output files. Thus, such files do not appear in dependencies of other files.
            </span>
            <span class="storage"> 
                While Vahdat and Anderson (<a href="#vahdat1998a" class="reference">vahdat1998a</a>) say that TREC stores the metadata in a database, they do not specify which kind of database TREC uses.
            </span>
        </p>
        <p>
            <span class="cache"> 
                As stated before, the main goal of TREC is to use provenance for cache invalidation. 
                As a possible application, it proposes replacing makefiles with dynamic shell scripts that sequentially specify all compilation steps. 
                <span title="Uses lineage to determine the exact sequence of operations used to create any system file or to keep the contents of output files synchronized as dependent input files are modified; Checks input files by date">
                    With the collected provenance, it can detect whether or not input files and environment variables have changed and just re-execute compilations steps when necessary.
                </span>
                <span title="When combined to source control system, unmake could be used to rollback to earlier versions of output files">
                    This application frees users from explicitly specifying dependency information. 
                </span>
                Another possible application is to cache dynamically generated web pages to avoid recomputations for every request when it is not necessary, improving server performance and client latency. 
            </span>
            <span class="analysis"> 
                In addition to these caching applications, TREC also provides a simple command line querying tool that obtains file lineage with the full sequence of programs that executed prior its generation.
            </span>
        </p>
        <p>
            <span class="limitations cache collection"> 
                Provenance gathering and usage for caching in TREC have a series of limitations.
                First, it does not handle difficult-to-trace input (e.g. user input and network connection) and non-determinism (e.g. random calls, time-based executions).
                For applications that use such resources, it may produce incorrect results.
                Second, files content must be static and only changed locally.
                It fails to collect changes written by external programs or changes to non-static files, such as /dev ones.
                Finally, programs must safely finish their execution while monitored.
                Interrupted programs also produce incorrect results.
                In most of these cases, TREC can still be used for comprehending file dependencies.
            </span>
        </p>
    """,
)

