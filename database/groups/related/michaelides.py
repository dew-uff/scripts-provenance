from snowballing.approaches import Group

from ..constants import *
from ...work.y2016 import michaelides2016a

approach = Group(
    michaelides2016a,
    display="Michaelides et al.",
    approach_name="Intermediate Notation for Provenance and Workflow Reproducibility (INPWR)",
    emails="dtm@ecs.soton.ac.uk; Richard.Parker@bristol.ac.uk; C.Charlton@bristol.ac.uk; William.Browne@bristol.ac.uk; luc.moreau@kcl.ac.uk",
    _cite=True,

    _meta=[dict(
        reply=None,
        binary=NO,
        languages=[BLOCKLY],
        goal=REPRODUCIBILITY,
        supports=[REPRODUCIBILITY, COMPREHENSION],
        categories=[COLLECTION, REPRODUCIBILITY, STORAGE],

        mode=USER_LEVEL,

        tools=[],

        annotations=[],
        execution=[OVERRIDING],
        deployment=[],
        definition=[DYNAMIC],

        execution_granularity=[
            FUNC_ARGUMENTS,
            FUNC_LINEAGE,
            FUNC_DURATION,
            VARIABLE_LINEAGE,
            RANDOM_SEED,
            USER_INPUT,
        ],
        deployment_granularity=[],
        definition_granularity=[EXECUTION],

        cache=NO,
        replay=YES,
        evolution=NO,
        pipeline=NO,
        summarization=[],

        distribution=[
            PROPRIETARY.such_as(["INPWR"]),
            INTEROPERABLE.such_as([PROV]), 
            SOURCE.such_as([BLOCKLY])
        ],
        storage=[
            PROPRIETARY.such_as(["INPWR"]),
        ],
        visualization=[INTEROPERABLE.such_as([PROV])],
        visplace=[EXTERNAL],
        query=[INTEROPERABLE.such_as([PROV])],
        integration=[],

        granularity=["Blocks", FUNCTION_CALLS],
        granularity_text="Blocks, Calls, Random Seed, User Input",
        management_text="Proprietary (INPWR), PROV, Source",
        generic_query_text="",
        specific_query_text="PROV",
        thread=NO,
        diff=[],

        limitations=[],
    )],
    _about="""
        <p>
            Michaelides et al. (<a href="#michaelides2016a" class="reference">michaelides2016a</a>) capture provenance from scripts expressed visually using Blockly for <span class="goal">reproducibility</span>.
            <span class="storage reproducibility">
                They store the provenance in Intermediate Notation for Provenance and Workflow Reproducibility (INPWR) format. INPWR is a format based on PROV that can turn back into Blockly visual scripts for re-execution.
            </span>
        </p>
        <p>
            <span class="collection">
                They apply the <span class="strategy">overriding</span> strategy by augmenting functions that execute blocks in the <em>StarJR</em> interpreter.
                During the collection, they collect executed blocks in Blockly as tasks with their start and end time, type (e.g. sequence and if expression), value, and value type.
                Since executed blocks produce provenance tasks, this approach unwinds loop structures.
                With the reproducibility goal, Michaelides et al. (<a href="#michaelides2016a" class="reference">2016</a>) replace user input blocks with literal values that represent the input made.
            </span>
        </p>
        <p>
            <span class="storage">
                In addition to transforming INPWR into executable and editable Blockly, Michaelides et al. (<a href="#michaelides2016a" class="reference">2016</a>) also use the PROV-Template system to convert INPWR into PROV.
            </span>
        </p>
    """,
    evaluation="measures overhead of execution",
)
