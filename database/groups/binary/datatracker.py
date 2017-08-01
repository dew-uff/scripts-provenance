from snowballing.approaches import Group

from ..constants import *
from ...work.y2014 import stamatogiannakis2014a

approach = Group(
    stamatogiannakis2014a,
    display="Data  Tracker",
    approach_name="DataTracker",
    _cite=False,

    _meta=[dict(
        binary=YES,
        languages=[AGNOSTIC],
        goal=COMPREHENSION,
        supports=[COMPREHENSION],
        categories=[COLLECTION, QUERY, VISUALIZATION],

        mode=USER_LEVEL,

        tools=["libdft", "Intel Pin"],
        
        annotations=[],
        execution=[OVERRIDING],
        deployment=[],
        definition=[],

        execution_granularity=[
            PROC_NAME,
            INPUT_FILES,
            OUTPUT_FILES,
            BYTE_LINEAGE,
            DTA,
        ],
        deployment_granularity=[],
        definition_granularity=[],

        cache=NO,
        replay=NO,
        evolution=NO,
        pipeline=NO,
        summarization=[],

        distribution=[
            INTEROPERABLE.such_as([PROV]),
            LOG.such_as(["Raw"])
        ],
        storage=[LOG.such_as(["Raw"])],
        visualization=[
            INTEROPERABLE.such_as([PROV]),
        ],
        visplace=[EXTERNAL],
        query=[INTEROPERABLE.such_as([PROV])],
        integration=[],
        
        granularity=[FILES, PROCESSES, BYTES],
        granularity_text="Bytes, Files (I/O - metadata), Processes",
        management_text="Log",
        generic_query_text="",
        specific_query_text="PROV",
        thread=UNKNOWN.star(YES),
        diff=[],
                    
        limitations=[],
    )],
    _about="""
        <p>
            DataTracker (<a href="#stamatogiannakis2014a" class="reference">stamatogiannakis2014a</a>) collects provenance from binaries for <span class="goal">comprehension</span>. 
            It based on <span class="tool">libdft</span>, a tool that performs Dynamic Taint Analysis (DTA).
            libdft uses <span class="tool">Intel Pin</span> framework to monitor, interact, and apply dynamic instrumentation to existing programs with a rich API.
            <span class="collection">
                With this dynamic instrumentation, applications and instrumentation code appear as a single process to the operating system and share the same address space.
                The original libdft only supports bit and byte-sized taint marks and omits support for implicit dataflow to improve its performance. 
                DataTracker abdicates these performance optimizations and includes support to arbitrary taint marks. 
                Since Intel Pin applies dynamic instrumentation, DataTracker uses the <span class="strategy">overriding</span> strategy for execution provenance collection.
            </span>
        </p>
        <p>
            <span class="collection">
                <span title="a technique widely used in the security and reverse engineering fields">DTA</span> tracks the dataflow by defining 
                <span title="b) Taint sources: locations where new taint marks are checked or logged">
                    <em>taint sources</em> as locations to check or log new taint marks;
                </span>
                <span title="c) Taint sinks: locations where the propagated taint marks are checked or logged">
                    <em>taint sinks</em> as locations to check or log propagated taint marks;
                </span> 
                <span title="a) Taint type: encapsulates the semantics tracked for each piece of data">
                    <em>taint type</em> as semantic encapsulations for each piece of data;
                </span>
                <span title="d) Propagation policies: define how that taint marks are handled during program execution">
                    and <em>propagation policies</em> as definitions of how to handle taint marks during the program execution.
                </span>
            </span>
        </p>
        <p>
            <span class="collection">
                In the case of DataTracker, it uses the system calls, <em>read</em> and <em>mmap2</em>, as <em>taint sources</em>.
                These operations read data from files to the memory.
                <span title="Queries the OS using lseek() system call to obtain the offset to create the taint marks or keeps read/write counters for systems that lseek() does not work.">
                    Thus, DataTracker sets taint marks on the memory locations where data was read into.
                </span>
                As <em>taint sinks</em>, DataTracker uses the system calls, <em>write</em> and <em>munmap</em>.
            </span>
            <span class="storage">
                These operations data from memory into the disk.
                Hence, DataTracker logs taint marks with provenance information into raw log files.
                For reducing the space overhead, DataTracker condenses logged information into two types of taint ranges: sequence ranges for consecutive taint marks that appear in both the input and the output; and repetition ranges for consecutive output bytes marked with the same taint mark.
            </span>
            <span class="collection">
                As <em>propagation policies</em>, it uses the byte propagation defined by libdft.
            </span>
        </p>
        <p>
            <span class="collection">
                DataTracker does not perform taint analysis on all files. 
                <span title="Invokes its UFD mapper sub-component">
                    It first intercepts <em>open</em> system calls to decide whether or not use their read operations as taint sources.
                </span>
                <span title="If the file descriptor should be watched, creates a new UFD mapping for it">
                    DataTracker avoids applying taint on uninteresting data and data unlikely to end up in the application output, such as UI icons and shared libraries.
                    DataTracker also avoids tainting files opened exclusively for writing.
                </span>
            </span>
        </p>
        <p>
            <span class="analysis storage">
                For analysis, DataTracker converts the raw provenance file into PROV.
                The generated PROV presents the monitored application as an activity, and the accessed files as entities, presenting the derivation of files.
            </span>
        </p>
        <p>
            <span class="collection">
                DTA has some limitations for provenance gathering in scripts.
                First, it is unable to capture implicit flows created by conditions and lookup tables as it traces only dataflows.
                Second, it presents the script files as part of the derivations.
                Finally, it imposes an extra overhead, since its instrumentation occurs on the interpreter.
            </span>
        </p>

    """,

    evaluation="""
        Evaluates high-fidelity
    """,
)

