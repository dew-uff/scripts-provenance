from snowballing.approaches import Group

from ..constants import *
from ...work.y2004 import frew2004a
from ...work.y2005 import valeur2005a
from ...work.y2008 import frew2008a, frew2008b
from ...work.y2010 import frew2010a
from ...work.y2011 import frew2011a

approach = Group(
    frew2008a,
    display="ES3",
    approach_name="Earth System Science Server (ES3)",
    emails="frew@bren.ucsb.edu; peter@eri.ucsb.edu; gjanee@ucop.edu",
    to="Frew, James and Slaughter, Peter and Janée, Greg",
    _cite=False,
    dont_cite=[frew2004a, frew2008b, valeur2005a, frew2010a, frew2011a],
    # janee2012a

    _meta=[dict(
        reply=None,
        repr="default",
        binary=YES,
        languages=[AGNOSTIC],
        goal=COMPREHENSION,
        supports=[COMPREHENSION],
        categories=[COLLECTION, QUERY, STORAGE, VISUALIZATION],

        mode=USER_LEVEL,

        tools=["strace"],

        annotations=[PARSEABLE, EXTERNAL, EXCLUSIVE, OPTIONAL, DEFINITION],
        execution=[PASSIVE_MONITORING, INSTRUMENTATION],
        deployment=[],
        definition=[],

        execution_granularity=[
            PROC_NAME,
            PROC_DURATION,
            PROC_PARANTAGE,
            PROC_LINEAGE,
            PROC_ARGUMENTS,
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

        distribution=[GRAPH_FILE.such_as([GRAPHML, GRAPHVIZ])],
        storage=[NOSQL.such_as([XML_SERVER])],
        visualization=[COMBINED_VIEW.such_as([GRAPHML, GRAPHVIZ])],
        visplace=[INTERNAL],
        query=[QUERY.such_as([XQUERY])],
        integration=["Logger Pluggins"],

        granularity=[FILES, PROCESSES, ARGUMENTS],
        granularity_text="Files (I/O - metadata), Processes",
        management_text="XML Server, GraphML, Graphviz",
        generic_query_text="XQuery",
        specific_query_text="",
        thread=YES,
        diff=[],

        limitations=[],
    ),dict(
        repr="script",
        binary=NO,
        languages=[IDL],
        goal=COMPREHENSION,
        supports=[COMPREHENSION],
        categories=[COLLECTION, QUERY, STORAGE, VISUALIZATION],

        mode=USER_LEVEL,

        tools=[],
        
        annotations=[],
        execution=[OVERRIDING],
        deployment=[],
        definition=[],

        execution_granularity=[
            INPUT_FILES,
            OUTPUT_FILES,
            UNKNOWN
        ],
        deployment_granularity=[],
        definition_granularity=[],

        cache=NO,
        replay=NO,
        evolution=NO,
        pipeline=NO,
        summarization=[],

        distribution=[GRAPH_FILE.such_as([GRAPHML, GRAPHVIZ])],
        storage=[NOSQL.such_as([XML_SERVER])],
        visualization=[COMBINED_VIEW.such_as([GRAPHML, GRAPHVIZ])],
        visplace=[INTERNAL],
        query=[QUERY.such_as([XQUERY])],
        integration=["Logger Pluggins"],
        
        granularity=[UNKNOWN],
        granularity_text="Files (I/O - metadata)",
        management_text="XML Server, GraphML, Graphviz",
        generic_query_text="XQuery",
        specific_query_text="",
        thread=UNKNOWN,
        diff=[],

        limitations=[],
    )],
    _about="""
        <p>
            Earth System Science Server (ES3) (<a href="#frew2008a" class="reference">frew2008a</a>; <a href="#valeur2005a" class="reference">valeur2005a</a>) captures provenance for <span class="goal">comprehending</span> Earth science data products.
            <span class="collection">
                It collects execution provenance from binary files through diverse strategies.
                For scripts, it supports either monitoring the interpreter binary or capturing directly from scripts through alternative plugins that support instrumentations.
                ES3 applies three strategies for execution provenance collection: <span class="strategy">passive monitoring, overriding and instrumentation</span>.
            </span>
        </p>
        <p>
            <span class="collection">
                ES3 uses a probulator to monitor transparently the execution. The probulator comprises two applications: 
                a logger that instruments, monitors and logs the execution;
                and a transmitter that transmits the collected provenance for storage.
            </span>
        </p>
        <p>
            <span class="collection">
                The logger uses plugins for capturing provenance.
                Frew et al. (<a href="#frew2008a" class="reference">2008</a>) propose two plugins for ES3.
                The default one uses <span class="tool">strace</span> to trace system calls in a process and capture the process name, its arguments, the sequence of children processes, accessed files, and standard input, output, and errors.
                Since system call traces can be overwhelming, users can configure filter files with patterns that can be safely ignored during the collection, such as shared library accesses.
                Hence, the default plugin uses both the <span class="strategy">passive monitoring and the instrumentation strategy</span>.
                The second plugin is specific to IDL.
                It preprocesses IDL scripts, replacing certain calls to IDL built-in functions and inserts calls to ES3 for logging.
                Thus, the second plugin uses the <span class="strategy">overriding</span> strategy for provenance collection. Both loggers produce files with provenance as results.
            </span>
        </p>
        <p>
            <span class="storage">
                After logging the provenance, the transmitter parses the files produced by the loggers;
                assigns universally unique identifier to every provenance object; converts these provenance objects into standard ES3 execution reports in XML 
                and transfer these XML documents to a <span title="ES3 core">web server</span> that stores them in an XML database.
            </span>
        </p>
        <p>
            <span class="analysis">
                For analysis, ES3 supports querying ancestors and descendants of provenance objects with XQuery.
                Additionally, it supports producing provenance graphs in GraphML format.
                The visualizations produce by ES3 combine both data files, arguments, and transformations as nodes.
            </span>
        </p>
    """,
)

