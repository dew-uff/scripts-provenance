from snowballing.approaches import Group

from ..constants import *
from ...work.y2013 import stevens2013a

approach = Group(
    stevens2013a,
    display="Lancet",
    approach_name="Lancet",
    categories=["notebook", "collection", "reproducibility"],
    emails="jlrstevens@gmail.com; me@marcoelver.com; jbednar@inf.ed.ac.uk",
    # Invalid email: jlstevens@inf.ed.ac.uk;
    _cite=False,

    _meta=[dict(
        reply=True,
        binary=NO,
        languages=[PYTHON],
        goal=REPRODUCIBILITY,
        supports=[REPRODUCIBILITY, COMPREHENSION, MANAGEMENT],
        categories=[COLLECTION, REPRODUCIBILITY, STORAGE, EVOLUTION],

        mode=USER_LEVEL,

        tools=[],

        annotations=[EXECUTABLE, INTERNAL, INCLUSIVE, MANDATORY, DEFINITION],
        execution=[INSTRUMENTATION],
        deployment=[BEFORE_EXECUTION],
        definition=[PARSING, STATIC],

        execution_granularity=[PROC_ARGUMENTS],
        deployment_granularity=[
            OS_VERSION, PYTHON_VERSION, SELF_VERSION
        ],
        definition_granularity=[
            PROC_NAME,
            "Launcher repr"
        ],

        cache=NO,
        replay=YES,
        evolution=INTENTION.star("*opt. VCS"),
        pipeline=NO,
        summarization=[],

        distribution=[LOG],
        storage=[LOG],
        visualization=[],
        visplace=[],
        query=[],
        integration=[],

        granularity=[ARGUMENTS, COMMANDS, ENV_VAR],
        granularity_text="Arguments, Commands, Platform, Env. Var.",
        management_text="Log",
        generic_query_text="",
        specific_query_text="",
        thread=YES,
        diff=[DATA.star("VCS")],

        limitations=[],
    )],
    _about="""
        <p>
            Lancet (<a href="#stevens2013a" class="reference">stevens2013a</a>) is a Python library that supports defining <span title="allows scientists to spend less time worrying about the implementation">declarative specifications</span> for experiments and collects provenance of executions <span class="goal">for reproducing the experiments</span>.
            <span class="collection">
                Thus, users need to <span class="strategy">instrument</span> and rewrite their code to collect provenance with Lancet.
            </span>
        </p>
        <p>
            <span class="collection">
                With Lancet, users declare arguments, commands, and launchers.
                <span title="Arguments specify the parameter space to be covered by a set of runs">
                    Arguments express <em>what they aim to achieve</em>, with the platform and tool-independent specifications.
                    An argument specification can define multiple arguments sets for parameter sweeping.
                </span>
                <span title="Commands can be extended to other tools through subclasses">
                    Commands express <em>how they aim to achieve</em>, with platform-independent, but tool-dependent specifications.
                    A command specification handles the interface to an external tool and supports defining how to run the tool on multiple platforms.
                </span>
                Finally, launchers express <em>where they want to execute</em> the task with platform-dependent, but tool-independent notations.
                A launcher specification combines arguments to commands and launch jobs on the desired platform.
                Lancet provides launchers to run locally or in parallel on a Grid Engine.
            </span>
        </p>
        <p>
            <span class="collection reproducibility">
                When the <span title="Integrates with pandas to visualize results">launchers execute</span>, Lancet records the Python version, the Lancet version, operating system information and other useful metadata as deployment provenance.
                In addition, Lancet records the launcher representation along with argument data as definition provenance.
                The launcher representation is enough for recreating it for reproducibility. 
            </span>
        </p>
        <p>
            <span class="storage">
                Lancet stores the collected provenance to a file. Lancet allows users to include annotations with library versions, comments and metadata descriptions in the provenance file. 
                Lancet also offers a function to help writing version control information to this file, maintaining an explicit log of all parameters used in the experiment history. 
            </span>
            <span class="analysis" title="It is also possible to inspect and browse previously runned params">
                For provenance analysis, users can inspect the provenance file.
            </span>
        </p>
    """,
)
