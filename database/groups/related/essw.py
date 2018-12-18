from snowballing.approaches import Group

from ..constants import *
from ...work.y2001 import frew2001a

approach = Group(
    frew2001a,
    display="ESSW",
    approach_name="Earth System Science Workbench (ESSW)",
    emails="frew@bren.ucsb.edu; rbose@columbia.edu",
    _cite=False,

    _meta=[dict(
        reply=None,
        binary=NO,
        languages=[PERL],
        goal=MANAGEMENT,
        supports=[MANAGEMENT, COMPREHENSION],
        categories=[COLLECTION, QUERY, STORAGE, VISUALIZATION],

        mode=USER_LEVEL,

        tools=[],

        annotations=[EXECUTABLE, INTERNAL, INCLUSIVE, MANDATORY, DEFINITION],
        execution=[INSTRUMENTATION],
        deployment=[],
        definition=[READING, DYNAMIC],

        execution_granularity=[
            INPUT_FILES.star("*user"),
            OUTPUT_FILES.star("*user"),
            PROC_LINEAGE.star("*user"),
            USER_DEFINED
        ],
        deployment_granularity=[],
        definition_granularity=[CONTENT],

        cache=NO,
        replay=NO,
        evolution=TRIAL_ID.star("*ID"),
        pipeline=NO,
        summarization=[],

        distribution=[GRAPH_FILE.such_as([GRAPHVIZ])],
        storage=[RELATIONAL_DB.such_as(["MySQL"]), CONTENT_DATABASE],
        visualization=[COMBINED_VIEW.such_as([GRAPHVIZ])],
        visplace=[INTERNAL],
        query=[WEB, QUERY.such_as([SQL])],
        integration=[],

        granularity=[FILES, PROCESSES],
        granularity_text="User defined, Processes, Files (I/O)",
        management_text="MySQL, Content DB, Graphviz",
        generic_query_text="SQL",
        specific_query_text="Web",
        thread=NO,
        diff=[],

        limitations=[],
    )],
    _about="""
        <p>
            Earth System Science Workbench (ESSW) (<a href="#frew2001a" class="reference">frew2001a</a>) uses provenance for describing scientific experiments and providing a better <span class="goal">comprehension and data management for them</span>.
            <span class="collection">
                It proposes wrapping experiments in instrumented Perl scripts for provenance collection.
                Thus, it uses the <span class="strategy">instrumentation</span> strategy to collect provenance.
            </span>
        </p>
        <p>
            <span class="collection">
                ESSW provides a set of wrapper functions in Perl. 
                These wrappers manipulate science objects log metadata.
                ESSW provides functions to create science objects based on files, functions to link them to others, and functions to store them in an XML document during execution.
                ESSW transforms the links between these objects into lineage graphs. Hence, users are required to annotate their code specifying what and how to collect provenance.
            </span>
        </p>
        <p>
            <span class="storage">
                ESSW parses the XML document created by a trial and store <span title="Adds a new record to the Experiment table for each run (trial). Input, steps and outputs are collected and stored at the ScienceObject table. A metadata field in the ScienceObject table contains the full XML document with its metadata. Relationships are stored in a ScienceObjectLink table.">science objects and relationships in a relational database (MySQL)</span>.
                For file objects, ESSW stores their MD5 hashes in the relational database and their content in a <span title="ND-WORM">separate content database</span>.
            </span>
        </p>
        <p>
            <span class="analysis">
                After storing the science objects in the database, it is possible to perform SQL queries over them for analysis.
                Additionally, ESSW provides a web interface for querying metadata of science objects and visualizing their lineage graph.
                It uses GraphViz to produce a static combined view that presents both data files and experiment processes as nodes. 
            </span>
        </p>
    """,
)

