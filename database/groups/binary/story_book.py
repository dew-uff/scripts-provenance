from snowballing.approaches import Group

from ..constants import *
from ...work.y2009 import spillane2009a
    
approach = Group(
    spillane2009a,
    display="Story Book",
    approach_name="Story Book",
    categories=["collection", "storage", "query"],
    _cite=False,

    _meta=[dict(
        binary=YES,
        languages=[AGNOSTIC],
        goal=FRAMEWORK,
        supports=[FRAMEWORK, COMPREHENSION],
        categories=[COLLECTION],

        mode=USER_LEVEL,

        tools=["FUSE"],
        
        annotations=[EXECUTABLE, EXTERNAL, INCLUSIVE, OPTIONAL],
        execution=[PASSIVE_MONITORING, INSTRUMENTATION],
        deployment=[],
        definition=[],

        execution_granularity=[
            PROC_NAME,
            PROC_LINEAGE.star("as long it accesses files"),
            INPUT_FILES,
            OUTPUT_FILES,
        ],
        deployment_granularity=[],
        definition_granularity=[],

        cache=NO,
        replay=NO,
        evolution=NO,
        pipeline=NO,
        summarization=[],

        distribution=[],
        storage=[
            LOG.such_as(["Stasis"]),
            KEY_VALUE_DB.such_as(["BerkeleyDB"])
        ],
        visualization=[],
        visplace=[],
        query=[COMMAND.such_as(["Custom query API"])],
        integration=["extensions"],
        
        granularity=[PROCESSES, FILES],
        granularity_text="Files (I/O - metadata), Processes",
        management_text="Stasis Log, BerkeleyDB",
        generic_query_text="",
        specific_query_text="Command",
        thread=YES,
        diff=[],
                    
        limitations=[],
        extra=dict(
            storage="""
                Implementation is independent of the format of extended records. Allows applications to use metadata such as RDF, of Dublin Core

                Three kinds of records:
                    Basic records: open, close, read and write
                    Process records: caller-callee relationship
                    Extendend records: application-specific procenance information

                Supports record compression
                    Ignores multiple calls to read and write from the same process to the same file
            """,
        ),
    )],
    _about="""
        <p>
            Story Book (<a href="#spillane2009a" class="reference">spillane2009a</a>) intends to <span class="goal">decouple application-specific aspects of provenance tracking from dependency tracking, queries, and other mechanisms</span>. 
            <span class="integration collection">
                Thus, it provides a database to store provenance and supports extensions to capture execution provenance from different sources.
                Both its file system extension and its MySQL extension intercepts respectively operating system and database events to capture execution provenance. 
                Hence, the proposed extensions apply the passive monitoring strategy.
            </span>

        </p>
        <p>
            <span class="collection">
                Story Book runs in <span class="mode">user-space</span>. Its file system extension uses the <span class="tool">FUSE file system instrumentation layer</span> to intercept system calls.
                This extension uses file access events (e.g. open, close, read and write) instead of process events (e.g. fork and exit) to monitor process parentage.
                This way, it only considers the processes that direct influence files, and it avoids logging processes that do not modify files.
                As a consequence, it avoids maintaining provenance graphs in ram during the collection.
                While not having the graphs in ram reduces the complexity of file provenance gathering, it is not sufficient to reflect process reparenting (<a href="#spillane2009a" class="reference">spillane2009a</a>).
            </span>
        </p>
        <p>
            <span class="collection extension">
                The file system extension can also be extended through provenance inspectors. 
                Provenance inspectors define sets of files as a target and intercept events related to these sets of files to extract specific provenance data from them. 
                For instance, Spillane et al. (<a href="#spillane2009a" class="reference">spillane2009a</a>) propose an interceptor to detect changes made applications in <em>.txt</em> files and an interceptor to detect changes in the metadata of <em>.docx</em> files.
            </span>
        </p>
        <p>
            <span class="storage extension">
                Since Story Book supports multiple extensions for provenance collection, each extension can define different granularities for their provenance records.
                Additionally, some applications can focus on data provenance, others can focus on process provenance, and others can focus on both data and process provenance. 
                Thus, Story Book only requires extensions and interceptors to specify the type of each provenance record and its content for storage.
            </span>
        </p>
        <p>
            <span class="storage">
                <span title="Stasis [12] and Berkeley-DB [15] (or Fable); Stasis stores provenance data using database-style no-Force/Steal recovery for its hashtables and compressed log structured merge (LSM) trees for its Rose indexes; Uses Valor to maintain write-ordering between its logs and the kernel page cache">
                    Story Book stores provenance in a physically separate location on disk.
                </span>
                This way, it can preserve the locality of provenance graph nodes and support efficient provenance queries. 
                Additionally, it uses a write-ahead log file to keep writing consistency and avoid cycles.
            </span>
            <span class="analysis">
                For analysis, Story Book provides a querying API that performs <span title="Performes a BFS in the basic and process record tables starting by the inode">breadth-first searches</span> in <span title="Lookup files inode in the (file name, ino) hash table">files and processes</span> and follows the <span title="Performs transitiv closures over sets of processes that wrote to the given file (or other files encoutered during the search), over sets of files read by these processes and over the parents of these processes; Search in order of decreasing LSN and return results in reverse chronological order">transitive closures to obtain all dependencies</span>.
            </span>
        </p>
    """,
)

