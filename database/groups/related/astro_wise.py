from snowballing.approaches import Group

from ..constants import *
from ...work.y2009 import mwebaze2009a
from ...work.y2011 import mwebaze2011a

approach = Group(
    mwebaze2009a, mwebaze2011a,
    display="Astro-WISE",
    approach_name="Astro-WISE",
    emails="Jmwebaze@gmail.com; d.r.boxhoorn@astro.rug.nl; valentyn@astro.rug.nl",
    _cite=False,

    _meta=[dict(
        reply=True,
        binary=NO,
        languages=[PYTHON],

        goal=FRAMEWORK,
        supports=[COMPREHENSION, FRAMEWORK, REPRODUCIBILITY, CACHE],
        categories=[COLLECTION, DIFF, QUERY, FRAMEWORK, STORAGE, REPRODUCIBILITY, CACHE],

        mode=USER_LEVEL,

        tools=[],

        annotations=[EXECUTABLE, INTERNAL, INCLUSIVE, MANDATORY, DEFINITION],
        execution=[INSTRUMENTATION],
        deployment=[],
        definition=[READING, DYNAMIC],

        execution_granularity=[INPUT_FILES, OUTPUT_FILES, ARGUMENTS, VARIABLES],
        deployment_granularity=[],
        definition_granularity=[CONTENT, BYTECODE],

        cache=YES,
        replay=YES,
        evolution=SEQUENCE,
        pipeline=YES,
        summarization=[],

        distribution=[],
        storage=[RELATIONAL_DB.such_as(["Oracle"])],
        visualization=[DATA_VIEW.star("Tree")],
        visplace=[INTERNAL],
        query=[QUERY.such_as(["SQL"]), FUNCTIONS, WEB],
        integration=[],

        granularity=[INPUT_FILES, OUTPUT_FILES, ARGUMENTS, VARIABLES, CONTENT],
        granularity_text="User defined, Attributes, Files (I/O), Parameters, Source",
        management_text="Oracle",
        generic_query_text="SQL",
        specific_query_text="Functions, Web",
        thread=UNKNOWN,
        diff=[PROVENANCE],

        limitations=[],
    )],
    _about="""
        <p>
            Astro-WISE (<a href="#mwebaze2009a" class="reference">mwebaze2009a</a>, <a href="#mwebaze2011a" class="reference">mwebaze2011a</a>) is a python framework that astronomers can <span class="goal">use to collect and integrate provenance in their tools and experiments</span>.
            Thus, in order to capture provenance with Astro-WISE, it is necessary to <span class="strategy collection">instrument</span> the code.
        </p>
        <p>
            <span class="collection">
                Astro-WISE uses a object oriented programming approach for capturing provenance. It defines descriptors that can be used within classes to declare attributes.
                These descriptors specify that the framework should trace the lineage of the attributes.
                To do so, the descriptors must declare dependencies to other traced classes or to file accesses and paramenters.
                <span class="evolution">
                    Astro-WISE enforces the immutability of the attributes and uses a unique object identifier and version for them. Thus, it allows some basic evolution tracking.
                    Instead of comparing the source code for versioning, Astro-WISE compares the bytecode (<a href="#mwebaze2011a" class="reference">mwebaze2011a</a>).
                    Each class keeps a reference to its predecessors for versioning.
                </span>
                Each class in Astro-WISE must specify a make method that specifies file targets, their dependencies, and transformation comands that create the derived product.
            </span>
        <p class="reproducibility">
            <span class="cache">
                Astro-WISE supports the re-computation of targets by checking which dependencies have changed.
            </span>
            <span class="diff">
                It also supports comparing the dependencies of two targets as lineage trees to check what has changed.
            </span>
        </p>
        <p class="analysis">
            <span class="visualization">
                Astro-WISE presents the dependencies of a target file as a textual lineage tree in a Web visualization tool. This tree is equivalent to a data-view graph with nodes representing data.
            </span>
            <span class="query">
                In addition to the visualization tool, Astro-WISE provides python functions as an extended query language to query the database. These functions are internally transformed into SQL queries for the <span class="storage"> relational database </span>
            </span>
        </p>
    """,
)