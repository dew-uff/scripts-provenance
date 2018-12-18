from snowballing.approaches import Group

from ..constants import *
from ...work.y2016 import eichinski2016a

approach = Group(
	eichinski2016a,
    display="Datatrack",
    approach_name="Datatrack",
    emails="philip.eichinski@qut.edu.au; p.roe@qut.edu.au",
    _cite=False,

    _meta=[dict(
        reply=True,
        binary=NO,
        languages=[R],

        goal=MANAGEMENT,
        supports=[MANAGEMENT, COMPREHENSION],
        categories=[COLLECTION, MANAGEMENT, VISUALIZATION],

        mode=USER_LEVEL,

        tools=[],

        annotations=[EXECUTABLE, INTERNAL, INCLUSIVE, MANDATORY, OPTIONAL, DEFINITION, PROVENANCE],
        execution=[INSTRUMENTATION],
        deployment=[DURING_EXECUTION],
        definition=[],

        execution_granularity=[COMMANDS, USER_DEFINED, STACK],
        deployment_granularity=[OS_VERSION, R_VERSION, MODULES],
        definition_granularity=[SOURCE],

        cache=NO,
        replay=NO,
        evolution=SEQUENCE,
        pipeline=YES,
        summarization=[CLUSTERING.such_as(["Combines all data accesses in nodes"])],

        distribution=[VCS, PROPRIETARY.such_as(["CSV"])],
        storage=[CONTENT_DATABASE.star("VCS"), PROPRIETARY.such_as(["CSV"])],
        visualization=[DATA_VIEW],
        visplace=[INTERNAL],
        query=[],
        integration=[],

        granularity=[USER_DEFINED, OS_VERSION, R_VERSION, MODULES],
        granularity_text="User defined, Parameters, Platform, Modules",
        management_text="VCS, Proprietary (CSV)",
        generic_query_text="",
        specific_query_text="",
        thread=UNKNOWN,
        diff=[DATA.star("VCS")],

        limitations=[],
    )],
    _about="""
        <p>
            Datatrack (<a href="#eichinski2016a" class="reference"> eichinski2016a </a>) is a package that collects provenance from R scripts to support their <span class="goal"> management </span>.
            It provides wrapper functions for accessing files that allows users to <span class="strategy"> instrument </span> the code, describing dependencies and annotating data objects. 
        </p>
        <p class="collection">
            Instead of using the default R functions for opening files, users need to use Datatrack ones for capturing provenance. Thus, it uses inclusive, internal, executable annotations.
            Such functions receive the file name, a list of dependencies, parameters, and optional annotations that target provenance as arguments. Users can use arbritary dependencies and annotations to describe the experiment.
            All dependencies are treated as data dependencies and connected by their names.
            These wrapper functions also collect the date that the data object were accessed, and a stack trace of function calls.
            In addition to the execution provenance, Datatrack also records the script paramenters, and deployment information, such as the operation system version, R version, and loaded packages with their versions.
        </p>
        <p class="storage">
            Datatrack stores provenance and versioning metadata in a CSV file under the project directory.
        </p>
        <p class="analysis">
            For analysis, datatrack produces a data-centric graph with all files and user-declared dependencies. This graph presents nodes representing data and edges representing dependencies. In a single data node, it presents multiple trial versions.
        </p>
    """,
)