from snowballing.approaches import Group

from ..constants import *
from ...work.y2011 import guo2011a, guo2011c
from ...work.y2012 import guo2012b, guo2012c

approach = Group(
    guo2011a, guo2011c, guo2012b,
    display="CDE",
    approach_name="Code, Data, and Environment",
    _cite=False,
    dont_cite=[guo2012c],
    # guo2011d

    _meta=[dict(
        binary=YES,
        languages=[AGNOSTIC],
        goal=REPRODUCIBILITY,
        supports=[REPRODUCIBILITY, CACHE],
        categories=[COLLECTION, PACKAGE, REPRODUCIBILITY, STORAGE, STREAMING],

        mode=USER_LEVEL,

        tools=["strace", "ptrace"],
        
        annotations=[],
        execution=[PASSIVE_MONITORING],
        deployment=[BEFORE_EXECUTION, DURING_EXECUTION],
        definition=[EXECUTION],

        execution_granularity=[INPUT_FILES, OUTPUT_FILES],
        deployment_granularity=[ENV_VAR, MODULES],
        definition_granularity=[CONTENT],

        cache=YES.star("for streaming"),
        replay=YES.star("no guarantees"),
        evolution=NO,
        pipeline=NO,
        summarization=[],

        distribution=[PACKAGE.such_as([FILE_SYSTEM])],
        storage=[PACKAGE.such_as([FILE_SYSTEM])],
        visualization=[],
        visplace=[],
        query=[],
        integration=[],
        
        granularity=[FILES, ENV_VAR],
        granularity_text="Files (I/O), Env. Variables",
        management_text="Package (file system)",
        generic_query_text="",
        specific_query_text="",
        thread=YES,
        diff=[],
                    
        limitations=[],
    )],
    _about="""
        <p>
            Code, Data, and Environment (CDE) (<a href="#guo2012b" class="reference">guo2012b</a>, <a href="#guo2011c" class="reference">guo2011c</a>; <a href="#guo2011a" class="reference">guo2011a</a>) collects provenance from binary programs for <span class="goal">reproducibility</span>. 
            It applies the <span class="strategy">passive monitoring</span> strategy by using <span class="tool"><em>strace</em></span> to monitor system calls during the execution of a program.
            <span class="collection" title="Uses system call interposition to monitor the execution of linux programas and package up code, data, and enviroment">
                CDE monitors system calls to obtain all environment variables and accessed files, including executables, scripts, modules and data files.
            </span>
            <span class="storage package">
                When it receives a system call that access these files, CDE <span tilte="Copies using OKAPI">collects</span> and stores them in a <span title="creates a new sub-directory called cde-package/cde-root/ and copies all accessed files into there, mirroing the original directory structure">directory package</span> that mirrors the original directory structure.
                <span title="Limitations: Shared libraries are "frozen" and do not receive security updates; Packages are only portable across machines with a compatible archtecture and Linux kernel version">
                    Since CDE copies files for all accesses, the resulting directory package corresponds to the state after the execution.
                </span>
            </span>
            <span class="reproducibility">
                CDE allows users to re-execute the program in the mirror directory package, avoiding the burdens of installing everything in other machines.
            </span>
        </p>
        <p>
            <span class="collection">
                For mirroring directories, CDE copies all necessary subdirectories and symbolic links.
                When it copies symbolic links, it copies both the links and their target.
                Additionally, CDE uses heuristics to complete packages. Completing packages are necessary to allow the execution of programs with different input data.
                For instance, suppose a program accepts both compressed and uncompressed files as input and it dynamically loads the library that decompresses files when necessary.
                If a user had captured only accessed files with CDE for an execution with uncompressed files, she would not be able to use the program to load compressed files on another machine.
            </span>
        </p>
        <p>
            <span class="collection">
                To cope with this situation, when CDE copies <em>ELF binaries</em>, it searches for constants strings that are filenames or contain “.so” (which are likely to be shared libraries), and it copies these files into the package should they exist.
                CDE assumes that many binaries load libraries named by constant string dynamically.
                Note that this approach fails for obtaining full modules from scripts, since scripts load them dynamically and are not binary ELF files.
            </span>
        </p>
        <p>
            <span class="reproducibility">
                For executing directory packages, CDE uses <span class="tool" title="Limitation: a process monitored by ptrace cannont itself ptrace another process">ptrace</span> to monitor system calls and rewrite path arguments to match the mirrored structure. CDE provides two execution modes: chroot-like mode and seamless execution mode.
                The <span title="Use the original dynamic linker">chroot-like</span> mode creates an isolated environment that mimics the original structure and environment variables, and it executes only programs contained within the directory package.
                On the other hand, the seamless execution mode runs on top of the system and it uses the directory programs and data when they are available, or the system ones when they are not.
                This second approach works better for scripting languages since it allows users to have full packages installed on their machines and use partial packages collected by CDE.
            </span>
        </p>
        <p>
            <span class="streaming">
                CDE also provides a streaming mode that supports mounting a remote directory and running remote programs locally. 
                In this mode, when a monitored program accesses a file in the remote directory, CDE copies it to a local CDE package for caching. 
                On subsequent runs, the local program uses only the cache.
            </span>
        </p>
    """,
)

