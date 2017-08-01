from snowballing.approaches import Group

from ..constants import *
from ...work.y2006 import muniswamy2006a
from ...work.y2008 import holland2008b
from ...work.y2009 import muniswamy2009a
from ...work.y2010 import muniswamy2010b
    
approach = Group(
    muniswamy2006a, holland2008b, muniswamy2009a, muniswamy2010b,
    display="PASS",
    approach_name="Provenance-aware storage systems (PASS)",
    _cite=False,

    _meta=[dict(
        binary=YES,
        languages=[AGNOSTIC],
        goal=COMPREHENSION,
        supports=[COMPREHENSION, SECURITY, FRAMEWORK],
        categories=[COLLECTION, EVOLUTION, MANAGEMENT, STORAGE, VISUALIZATION],

        mode=SYSTEM_WIDE,

        tools=["Kernel"],
        
        annotations=[PARSEABLE, EXTERNAL, INCLUSIVE, OPTIONAL],
        execution=[OVERRIDING, PASSIVE_MONITORING],
        deployment=[DURING_EXECUTION],
        definition=[EXECUTION],

        execution_granularity=[
            PROC_NAME,
            PROC_PARANTAGE,
            PROC_ARGUMENTS,
            PROC_PIPE,
            RANDOM_SEED,
            INPUT_FILES,
            OUTPUT_FILES,

        ],
        deployment_granularity=[
            ENV_VAR,
        ],
        definition_granularity=[
            CONTENT,
        ],

        cache=NO,
        replay=NO,
        evolution=SEQUENCE.star("*previous"),
        pipeline=NO,
        summarization=[],

        distribution=[INTEROPERABLE.such_as([OPM])],
        storage=[
            KEY_VALUE_DB.such_as(["BerkeleyDB (v1)"]),
            FILE_SYSTEM.such_as(["Layering system (v2)"]),
            LOG.such_as(["Log format (v2)"]),
        ],
        visualization=[COMBINED_VIEW, INTEROPERABLE.such_as([OPM])],
        visplace=[EXTERNAL],
        query=[QUERY.such_as(["PQL"]), INTEROPERABLE.such_as([OPM])],
        integration=["Layering System", "DBAPI"],
        
        granularity=[PROCESSES, FILES],
        granularity_text="Files (I/O - metadata), Processes, Env. Variables",
        management_text="BerkeleyDB (v1), Layering System (v2), Log (v2), OPM",
        generic_query_text="",
        specific_query_text="OPM, PQL",
        thread=YES,
        diff=[PROVENANCE],
                    
        limitations=[],
        extra=dict(
            diff="Supports comparing the provenance of two pieces of derived data, which can reveal changes between two program invocations",
            query="""
                Supports conventional attribute lookup (such as ownership) and transitive closure of ancestry information. Users can access it as a conventional Berkeley DB
                Provides a query tool, new query (nq) with a query model that represents a trade-off between generality and implementation time.
                    Treats provenance as a single relational table
                    Each provenanced entity appears as a row
                    Each provenance attributed appears as a column
                    Each nq query consists of first a recursive search, which collects a subset of the tble based on ancestry relationships, followed by flat filtering, sorting, and projection operations.
                        Allowsa choice of several reporting formats for its output
                        Does not support joins
                    SQL-like syntax with elementes to find ancestors, descendents, filter results, report results in different formats, sort results, and others
            """,
            management="""
                provenance can only be accessed by users with the right priviledges (according to the generated provenance)
            """,
            visualization="""
                Visually represent and query provenance in PLUS [7/braun2010]
            """,
            applications="""
                Understand system dependencies; intrusion detection; detecting system changes; script generation; build dbugging
            """,
        ),
    )],
    _about="""
        <p>
            The Provenance-aware Storage System (PASS) (<a href="#holland2008b" class="reference">holland2008b</a>; <a href="#muniswamy2006a" class="reference">muniswamy2006a</a>, <a href="#muniswamy2009a" class="reference">muniswamy2009a</a>) transparent collects provenance in the storage system. 
            <span class="collection">
                It performs a <span class="mode" title="System-level provenance produces more metadata">system-wide</span> gathering that collects both deployment and execution provenance. 
                Because of system-wide execution provenance collection, it also collects definition provenance in the case of scripts and <span class="evolution" title="Data evolves and it is important to track versions of both processes and objects;Versions are created by explicit operations that act upon one version and produce a new one">provenance evolution</span>. 
                Additionally, PASS deduces provenance from opaque data, such as create time, creator, source system, and it supports annotating files that come from other systems to add some more information.
            </span>
        </p>
        <p>
            <span class="collection">
                The PASS implementation modifies the Linux kernel to include an interceptor that monitors all system calls events (e.g. execve, fork, open, read, write and others). 
                Thus, PASS uses the <span class="strategy">overriding strategy to allow the passive monitoring strategy</span> for provenance collection.
                After monitoring system calls, the interceptor sends them to the observer, which translates system calls to provenance records and stream them to an analyzer.
                Provenance records may contain environment variables, libraries, complete description of hardware and operation systems, executed processes, pipes, input files, output files, and other data, such as the random number generator seed.
            </span>
        </p>
        <p>
            <span class="collection">
                The analyzer eliminates duplicate records and ensures that cycles do not arise by creating a new version of objects in situations that could create cycles (e.g. multiple processes concurrently reading and writing the same files).
                The first version of PASS used a global graph of objects dependencies to check for cycles (<a href="#muniswamy2006a" class="reference">muniswamy2006a</a>).
                Having the whole provenance graph in memory was inefficient. Thus, the second version of PASS (<a href="#muniswamy2009a" class="reference">muniswamy2009a</a>) adopted a cycle avoidance algorithm that considers only local dependencies (<a href="#muniswamy2009b" class="reference">muniswamy2009b</a>).
            </span>
        </p>
        <p>
            <span class="storage">
                After the analyzer removes cycles, it sends the provenance records to a distributor that caches non-persistent objects, such as pipes, processes, and application-specific objects.
                PASS only materializes these provenance records to disk when they influence actual files.
                Thus, when the system writes files to disk, PASS incorporates the process provenance to file provenance and tightly couples to the file data in the storage system to avoid provenance loss.
                <span class="File System layer called PASTA (PASSv1)">
                    The first PASS version stored provenance in an in-kernel port of Berkeley DB.
                </span>
                <span class="Lasagna stores provenance records along with the data; "
                    The second PASS version store provenance in layered file systems
                </span>
                that use a <span title="The log format ensures consistency between the provenance and data appearing on disk">log format</span>
                <span title="Waldo is a a user-level daemon  tbat reads provenance records from the log and stores them in a database. Responsible for accessing the database on behalf of the query engine">
                    to keep provenance consistency.
                </span>

            </span>
        </p>
        <p>
            <span class="integration">
                Additionally to the new cycle avoidance algorithm and the logging system for storage, the second version of PASS also defined a layering system to facilitate the integration of multiple levels of abstractions.
                <span title="Provides Python provenance tracking wrapper; Layer thers components atop provenance-aware network storage (NFS) that builds upon a Provenance-Aware Storage System; libpass is a library that exports DPAAPI to user-level with functions: pass_read, pass_write, pass_freeze, pass_mkobj, pass_reviveobj, pass_sync">
                    This layering system proposes a disclosed provenance API, DBAPI, which external tools can use to send provenance to PASS.
                </span>
                <span title="Bundles data and provenance together to achieve consistency">
                    This layering system assumes that objects at any given layer have obvious mappings to one object in the layer beneath it.
                </span>
            </span>
        </p>
        <p>
            <span class="analysis">
                For provenance analysis, PASS supports PQL queries and provides a graphical provenance browser for visualization that presents both files and processes as nodes (<a href="#holland2008b" class="reference">holland2008b</a>).
                PQL (Path Query Language) (<a href="#holland2009a" class="reference">holland2009a</a>) derived from Lorel (<a href="#abiteboul1997a" class="reference">abiteboul1997a</a>), a query language for semistructured data organized as a directed graph, which supports navigating paths in the database without a predefined schema.
                PQL has the goal of making provenance and ancestry queries.
            </span>
        </p>
    """,
)

