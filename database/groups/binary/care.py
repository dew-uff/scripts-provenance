from snowballing.approaches import Group

from ..constants import *
from ...work.y2014 import janin2014a

approach = Group(
    janin2014a,
    display="CARE",
    approach_name="Comprehensive Archiver for Reproducible Execution on Linux",
    _cite=False,
    
    _meta=[dict(
        binary=YES,
        languages=[AGNOSTIC],
        goal=REPRODUCIBILITY,
        supports=[REPRODUCIBILITY],
        categories=[COLLECTION, PACKAGE, STORAGE, FILTER],

        mode=USER_LEVEL,

        tools=["PRoot", "ptrace"],
        
        annotations=[PARSEABLE, EXTERNAL, INCLUSIVE, EXCLUSIVE, OPTIONAL],
        execution=[PASSIVE_MONITORING, INSTRUMENTATION],
        deployment=[BEFORE_EXECUTION, DURING_EXECUTION],
        definition=[EXECUTION],

        execution_granularity=[INPUT_FILES, OUTPUT_FILES],
        deployment_granularity=[ENV_VAR, MODULES],
        definition_granularity=[CONTENT],

        cache=NO,
        replay=YES.star("no guarantees"),
        evolution=NO,
        pipeline=NO,

        distribution=[PACKAGE.such_as(["Self-Contained"])],
        storage=[PACKAGE.such_as(["Self-Contained"])],
        visualization=[],
        visplace=[],
        query=[],
        integration=[],
        summarization=[],
        
        granularity=[FILES, ENV_VAR],
        granularity_text="Files (I/O), Env. Variables",
        management_text="Package (self-contained)",
        generic_query_text="",
        specific_query_text="",
        thread=YES,
        diff=[],
                    
        limitations=[],
    )],
    _about="""
        <p>
            Comprehensive Archiver for Reproducible Execution (CARE) (<a href="#janin2014a" class="reference">janin2014a</a>) uses provenance for <span class="goal">reproducibility</span>.
            <span class="collection">
                Similar to CDE (<a href="#guo2012b" class="reference">guo2012b</a>, <a href="#guo2011c" class="reference">guo2011c</a>; <a href="#guo2011a" class="reference">guo2011a</a>), it monitors system calls and discovers all executables, accessed files, and environment variables that a given application uses by observing its execution.
            </span>
            <span class="storage package">
                However, differently from CDE, that produces a directory, CARE produces a self-extractable archive with all the <span title="Different from CDE, CARE preserves file attributes when inserting files in archives">files</span>
            </span>
            <span class="reproducibility" title="During the re-execution step, adjusts all dependencies to the new environment">
                and machinery required for re-executing the program without external dependencies.
            </span>
        </p>
        <p>
            <span class="collection">
                For monitoring system calls and re-executing packages, it uses <span class="tool" title="Intercepts system calls right before transmission to the kernel for execution; Applies application virtualization">PRoot</span>, which is a user-land implementation of chroot that uses ptrace for tracing system calls and rewriting paths. Thus, CARE applies the <span class="strategy">passive monitoring</span> strategy for provenance collection.
            </span>
        </p>
        <p>
            <span class="collection filter">
                CARE supports filtering the file collection by defining concealed and revealed paths. Users can use concealed paths to hide all content and subdirectories of a directory. Additionally, users can use revealed paths as exceptions to concealed paths. Thus, it is possible to include some subdirectories of concealed paths.
            </span>
        </p>
    """,
)

