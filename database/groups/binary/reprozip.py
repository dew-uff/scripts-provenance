from snowballing.approaches import Group

from ..constants import *
from ...work.y2013 import chirigati2013a, chirigati2013b
from ...work.y2016 import chirigati2016a
    
approach = Group(
    chirigati2013a, chirigati2013b, chirigati2016a,
    display="Repro  Zip",
    approach_name="ReproZip",
    _cite=False,

    _meta=[dict(
        binary=YES,
        languages=[AGNOSTIC],
        goal=REPRODUCIBILITY,
        supports=[REPRODUCIBILITY, COMPREHENSION],
        categories=[COLLECTION, FILTER, PORTABILITY, REPRODUCIBILITY],

        mode=USER_LEVEL,

        tools=["SystemTap (beta)", "ptrace (1.x)"],
        
        annotations=[PARSEABLE, EXTERNAL, EXCLUSIVE, OPTIONAL],
        execution=[PASSIVE_MONITORING, INSTRUMENTATION],
        deployment=[BEFORE_EXECUTION, DURING_EXECUTION],
        definition=[EXECUTION],

        execution_granularity=[
            PROC_NAME,
            PROC_PARANTAGE,
            PROC_LINEAGE,
            PROC_ARGUMENTS,
            PROC_PIPE,
            INPUT_FILES,
            OUTPUT_FILES,
        ],
        deployment_granularity=[
            ENV_VAR,
            MODULES,
        ],
        definition_granularity=[
            CONTENT
        ],

        cache=NO,
        replay=YES,
        evolution=NO,
        pipeline=NO,
        summarization=[],

        distribution=[
            PACKAGE.such_as(["Extractable"]),
            PROPRIETARY.such_as(["VisTrails"]),
        ],
        storage=[
            PACKAGE.such_as(["Extractable"]),
            NOSQL.such_as(["MongoDB (beta)"]),
            RELATIONAL_DB.such_as(["SQLite (1.x)"])
        ],
        visualization=[
            PROCESS_VIEW.such_as(["VisTrails"])
        ],
        visplace=[INTERNAL],
        query=[
            QUERY.such_as(["MongoDB (beta)", "SQL (1.x)"])
        ],
        integration=[],
        
        granularity=[PROCESSES, FILES, ENV_VAR],
        granularity_text="Files (I/O), Processes, Env. Variables",
        management_text="Package (extractable), MongoDB (beta), SQLite (1.x), Proprietary (VisTrails)",
        generic_query_text="MongoDB (beta), SQL (1.x)",
        specific_query_text="",
        thread=YES,
        diff=[],
                    
        limitations=[],
    )],
    _about="""
        <p>
            ReproZip (<a href="#chirigati2016a" class="reference">chirigati2016a</a>; <a href="#chirigati2013a" class="reference">chirigati2013a</a>, <a href="#chirigati2013b" class="reference">chirigati2013b</a>) uses provenance for <span class="goal">reproducibility</span>.
            <span class="collection">
                It applies the <span class="strategy">passive monitoring</span> strategy by tracing <span title="execve, open, read, write, close and pipe">system calls</span> and capturing data dependencies, used libraries, arguments, environment variables, read files and written files.
            </span>
            <span class="storage reproducibility">
                ReproZip uses this information to create reproducible packages that contain all files involved in a computation and to derive a workflow specification.
            </span>
            <span class="collection">
                In its beta version (<a href="#chirigati2013a" class="reference">chirigati2013a</a>, <a href="#chirigati2013b" class="reference">chirigati2013b</a>), ReproZip used SystemTap for tracing system calls, but it moved to ptrace due to performance reasons (<a href="#chirigati2013b" class="reference">chirigati2013b</a>).
            </span>
            <span class="storage">
                Similarly, it used MongoDB for provenance storage during beta, but it moved to SQLite, as it is lighter.
            </span>
        </p>
        <p>
            <span class="collection">
                During collection, ReproZip creates a provenance tree. Each node represents a spawned process with command line arguments, working directory, read files, and written  files.
            </span>
            <span class="storage filter">
                After collection, ReproZip creates the reproducible package by traversing the tree and copying the directories. Users can control the size of packages by defining exclusion sets of files
            </span>
        </p>
        <p>
            <span class="storage analysis">
                ReproZip creates a workflow specification in a format compatible with VisTrails by traversing the tree.
                This way, users can use VisTrails for provenance visualization.
                To create the workflow specification, ReproZip transforms processes into workflow modules (i.e. activities) and files into module ports.
                Since processes access files that are not necessarily inputs of processes, ReproZip uses heuristics to identify input and output files of experiments:
                read files that do not belong to any software package are input files; written files are output files;
                and files that were read and written are stateful files (i.e. log files or database files). 
            </span>
        </p>
        <p>
            <span class="reproducibility">
                For reproducibility, ReproZip provides unpackers that support unpacking packages for different environments. Currently, it supports four unpackers: directory, chroot, Vagrant, and Docker.
                While the former two works only on Linux machines, the latter two are more portable due their virtual machine support.
                ReproZip supports the implementation of new unpackers for other environments and systems.
                In addition to unpackers, ReproZip supports installing all dependencies natively.
            </span>
        </p>
        <p>
            <span class="reproducibility">
                The directory unpacker just adjusts paths during unpacking and configures environment variables for the workflow execution.
                Since it adjusts paths during unpacking, it fails for hardcoded absolute paths.
                The chroot unpacker is similar to the directory unpacker, but it creates a full system environment that mimics the original paths with chroot, supporting hard-coded paths. 
                The vagrant unpacker unpacks the environment to a minimal virtual machine created through Vagrant.
                Finally, the docker unpacker creates a Docker container with the environment. 
            </span>
        </p>
    """,
)

