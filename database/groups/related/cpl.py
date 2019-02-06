from snowballing.approaches import Group

from ..constants import *
from ...work.y2012 import macko2012a

approach = Group(
    macko2012a,
    display="CPL",
    approach_name="Core Provenance Library",
    emails="pmacko@eecs.harvard.edu; mseltzer@cs.ubc.ca",
    _cite=False,

    _meta=[dict(
        reply=True,
        binary=NO,
        languages=[PYTHON, C, CPP, JAVA, R],
        goal=FRAMEWORK,
        supports=[FRAMEWORK],
        categories=[QUERY, STORAGE],

        mode=USER_LEVEL,

        tools=[],

        annotations=[NA],
        execution=[NA],
        deployment=[NA],
        definition=[NA],

        execution_granularity=[],
        deployment_granularity=[],
        definition_granularity=[],

        cache=NO,
        replay=NO,
        evolution=TRIAL_ID,
        pipeline=NO,
        summarization=[],

        distribution=[PROPRIETARY.such_as(["JSON"])],
        storage=[
            RELATIONAL_DB.such_as(["MySQL", "PostgreSQL"]),
            GRAPH_DB.such_as(["4store"])
        ],
        visualization=[],
        visplace=[],
        query=[QUERY.such_as([SPARQL, SQL, WEB]), FUNCTIONS],
        integration=[INSTRUMENTATION],

        granularity=[],
        granularity_text="N/A",
        management_text="MySQL, PostgreSQL, 4store",
        generic_query_text="SPARQL, SQL",
        specific_query_text="Functions",
        thread=YES.star("*user"),
        diff=[],

        limitations=[],
    )],
    _about="""
        <p>
            Core Provenance Library (CPL) (<a href="#macko2012a" class="reference">macko2012a</a>) is a <span title="multi-lingual library that programmers can incorporate into a variaty of tools to integrate provenance">library</span> with implementations for C, C++, Perl, Java, Python, and R that programmers and scientists can <span class="goal">use to integrate provenance in their tools and experiments</span>.
        </p>
        <p>
            <span class="collection">
                CPL provides functions for 
                <span title="cpl_attach initializes the library and attaches the process to the appropriate storage backend">
                    initializing the library; connecting to the provenance storage backend
                </span>;
                <span title="cpl_create_object creates new objects">
                    creating provenance objects
                </span>;
                <span title="cpl_lookup_object access existing object. If there are multiple objects with the same namespace, name and type, lookup returns the most recent">accessing existing objects</span>;
                <span title="cpl_data_flow creates dataflow when an object uses data from another object">
                    creating dataflow for objects that use data from others
                </span>; 
                <span title="cpl_control indicates that an object influences the execution of another without passing data">
                    creating control flow for objects that influence others without passing data
                </span>;
                <span title="cpl_add_property attaches key/value pairs to objects">
                    attaching properties to the object
                </span>; 
                <span title="cpl_detach should be called before the application exits">
                    finishing the execution to store provenance.
                </span>
                <span title="There are special namespaces and functions for shared objects, such as files: cpl_lookup_file">
                    It also provides similar functions to deal with shared objects such as files and functions to collect deployment provenance.
                </span>
            </span>
        </p>
        <p>
            <span class="collection">
                When CPL creates a provenance object, it assigns two identifiers to it: an object ID for identification in the machine, and the MAC address of the machine to enable <span title="Externally, it uses a combination of 3 fields: namespace of application, name of object, type of object">sharing objects with provenance over the network</span>.
            </span>
            <span class="evolution">
                Additional to these identifiers, CPL annotates all provenance records with a trial identifier to track provenance evolution.
            </span>
        </p>
        <p>
            <span class="storage">
                CPL can store provenance on either on relational databases or on a graph database. It supports MySQL and PostgreSQL as relational databases and 4store as a graph database. 
            </span>
            <span class="analysis">
                For analysis, it provides functions for accessing the provenance and supports provenance queries in SPARQL and SQL.
            </span>
        </p>
    """,
)

