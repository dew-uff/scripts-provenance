from snowballing.approaches import Group

from ..constants import *
from ...work.y2014 import devecsery2014a

approach = Group(
    devecsery2014a,
    display="Arnold",
    approach_name="Arnold",
    _cite=False,
    
    _meta=[dict(
        binary=YES,
        languages=[AGNOSTIC],
        goal=COMPREHENSION,
        supports=[COMPREHENSION, CACHE, REPRODUCIBILITY, SECURITY],
        categories=[COLLECTION, QUERY, REPRODUCIBILITY, STORAGE],

        mode=SYSTEM_WIDE,

        tools=["Kernel"],
        
        annotations=[],
        execution=[OVERRIDING],
        deployment=[DURING_EXECUTION],
        definition=[EXECUTION],

        execution_granularity=[
            PROC_NAME, PROC_DURATION, PROC_PARANTAGE,
            PROC_LINEAGE.star("*during analysis"),
            INPUT_FILES, PROC_ARGUMENTS, PROC_PIPE,
            RANDOM_SEED, BYTE_LINEAGE, TERMINAL, NETWORK,
            USER_INPUT,
        ],
        deployment_granularity=[ENV_VAR, MODULES],
        definition_granularity=[SOURCE, PROGRAM, CONTENT],

        cache=YES.star("*no reuse"),
        replay=YES,
        evolution=NO,
        pipeline=NO,
        summarization=[],

        distribution=[LOG.such_as(["Compressed with GZIP"])],
        storage=[LOG.such_as(["Compressed with GZIP"])],
        visualization=[],
        visplace=[],
        query=[COMMAND.such_as(["During Replay"])],
        integration=[],
        
        granularity=[BYTES, FILES, PROCESSES],
        granularity_text="Bytes, Files (I), Processes, Env. Variables",
        management_text="Log",
        generic_query_text="",
        specific_query_text="Command",
        thread=YES,
        diff=[],
                    
        limitations=[],
    )],
    _about="""
        <p>
            Arnold (<a href="#devecsery2014a" class="reference">devecsery2014a</a>) is a Linux kernel modification that captures <span class="mode">system-wide</span> provenance for <span class="goal">comprehension</span>.
            Arnold seeks to balance provenance storage overhead and re-computation by dividing the system into <span title="that can be replayed independently">replay groups</span> and <span class="collection">storing only the interactions between these groups as a <span title="treat log of data as cache">dependency graph</span></span>.
            <span class="analysis">Thus, if a user wants to see want occurred inside a group, she can just <span class="reproducibility" title="cooperative replay supports conserving spance">replay</span> the desired group and use the recorded interactions to guarantee the group will produce the same results.</span>
            <span class="collection">This allows Arnold to move provenance overhead from the collection to the analysis phase and conserve space.</span>
        </p>
        <p>
            <span class="collection">Arnold applies the <span class="strategy">overriding</span> strategy by modifying the system for provenance collection. It records provenance within a process, between processes, and between files and processes. When a process executes the exec system call, Arnold creates a new replay group. However, it joins all threads and processes that share memory into a single replay group and seeks to replay the interleaving of events from the replay group deterministically. To do so, it records all synchronization operations, instruments races and records atomic hardware instructions. This allows Arnold to replay multiprocessor instructions. In addition to this information, Arnold also records non-deterministic data that enters a process, such as execution order, return values, memory addresses modified by a system call, timing and values of received signals, and results of querying the system time. The collected non-deterministic data allows replaying groups deterministically.</span>
        </p>
        <p>
            <span class="storage">Arnold applies a model-based compression and file deduplication for provenance storage. First, it constructs a model for predictable operations and stores only values that differs from the model. Then, it deduplicates files by storing files only at their <span title="Does not store written files">first read</span> and assuming users can obtain other versions by <span title="If the current version of the file still exists, or was stored before, use this version. Otherwise, replay another group to generate the file">replaying the provenance</span>. Arnold compresses the provenance log with a <em>gzip</em> and stores it in the file system.</span>
        </p>
        <p>
            <span class="query">For provenance analysis, Arnold replays the collected provenance and tracks lineage. Since it divides the system into replay groups, it supports <span class="reproducibility" title="Arnold instruments replays to perform retrospective binary analysis">replaying each group individually</span> and reduces the query cost by using cached results. During the analysis, Arnold uses linkage functions chosen by the users to track the dependencies between inputs and outputs. Arnold provides linkage functions that consider dependencies in dataflows, control flows, data used as index and <span title="(i) Uses fuzzy string matching to look for contextual linkages among inputs and outputs that occur at approximately the same time. This way, it captures lineage that passes through the user of the system. (ii) copy linkage: links only copied data">others.</span>
        </p>
    """,
)