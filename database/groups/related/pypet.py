from snowballing.approaches import Group

from ..constants import *
from ...work.y2015 import meyer2015a
from ...work.y2016 import meyer2016a

approach = Group(
    meyer2015a, meyer2016a,
    display="pypet",
    approach_name="pypet",
    emails="robert.meyer@ni.tu-berlin.de",
    to="Robert Meyer",
    # Invalid: oby@cs.tu-berlin.de
    categories=["collection", "parameter"],
    _cite=False,

    _meta=[dict(
        reply=True,
        binary=NO,
        languages=[PYTHON],
        goal=MANAGEMENT,
        supports=[MANAGEMENT],
        categories=[COLLECTION, STORAGE, EVOLUTION],

        mode=USER_LEVEL,

        tools=["Sumatra"],

        annotations=[
            EXECUTABLE,
            INTERNAL,
            INCLUSIVE,

            MANDATORY, DEFINITION, # Default
            PROVENANCE, OPTIONAL, # For provenance
        ],
        execution=[INSTRUMENTATION],
        deployment=[SNAPSHOT],
        definition=[READING, STATIC],

        execution_granularity=[
            OUTPUT_DATA,
        ],
        deployment_granularity=[
        ],
        definition_granularity=[
        ],

        cache=NO,
        replay=YES,
        evolution=INTENTION.star("*opt. Sumatra or VCS"),
        pipeline=NO,
        summarization=[],

        distribution=[PROPRIETARY.such_as(["HDF5"])],
        storage=[PROPRIETARY.such_as(["HDF5"])],
        visualization=[],
        visplace=[],
        query=[],
        integration=["Sumatra"],

        granularity=[ARGUMENTS, OUTPUT_DATA],
        granularity_text="Arguments, Output, Sumatra",
        management_text="Proprietary (HDF5)",
        generic_query_text="",
        specific_query_text="",
        thread=YES,
        diff=[DATA.star("VCS")],

        limitations=[],
    )],
    _about="""
        <p>
            pypet (<a href="#meyer2016a" class="reference">meyer2016a</a>) is a Python library that supports defining declarative parameter specifications for experiments and <span class="goal"> manages </span> the experiment execution for finding the best parameter combination.
            <span class="collection">
                Thus, users need to <span class="strategy">instrument</span> and rewrite their code to collect provenance with pypet.
            </span>
        </p>
        <p class="collection">
            With pypet, users declare trajectories with parameters and use a experiment environment to execute a function with such parameters.
            It collects the execution results for each input combination.
            Pypet also integrates with <a href="#davison2012a" class="reference">Sumatra</a> or standalone version control systems to track the evolution and the definition provenance of experiments.
        </p>
        <p class="storage">
            Pypet stores the collected provenance in HDF5 files.
        <p>
    """,
)

