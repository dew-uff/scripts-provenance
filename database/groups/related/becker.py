from snowballing.approaches import Group

from ..constants import *
from ...work.y1988 import becker1988a

approach = Group(
    becker1988a,
    display="Becker and Chambers",
    approach_name="-",
    _cite=True,

    _meta=[dict(
        binary=NO,
        languages=[S],

        goal=COMPREHENSION,
        supports=[COMPREHENSION, REPRODUCIBILITY],
        categories=[COLLECTION, QUERY, STORAGE],

        mode=USER_LEVEL,

        tools=[],
        
        annotations=[],
        execution=[OVERRIDING],
        deployment=[],
        definition=[DYNAMIC],

        execution_granularity=[RANDOM_SEED, COMMANDS, VARIABLES],
        deployment_granularity=[],
        definition_granularity=[EXECUTION],

        cache=NO,
        replay=YES,
        evolution=NO,
        pipeline=NO,
        summarization=[],

        distribution=[PROPRIETARY, SOURCE],
        storage=[PROPRIETARY],
        visualization=[PROCESS_VIEW.such_as(["Statements"])], #VIEW
        visplace=[INTERNAL],
        query=[FUNCTIONS.such_as(["Command Provenance", "Data Provenance"])],
        integration=[],
        
        granularity=[COMMANDS, VARIABLES],
        granularity_text="Commands, Variables, Random Seed",
        management_text="Proprietary, Source",
        generic_query_text="",
        specific_query_text="Functions",
        thread=UNKNOWN,
        diff=[],
                    
        limitations=[],
    )],
    _about="""
        <p>
            Becker and Chambers (<a href="#becker1988a" class="reference">becker1988a</a>) propose a facility for S that captures provenance for <span class="goal">comprehension and validating reported results</span>.
            <span class="collection">
                They modified S interpreter for supporting execution provenance collection. Thus, it applies the <span class="strategy">overriding</span> strategy.
                <span class="storage">
                    During provenance collection, they produce an audit file that contains all of the statements evaluated with a list of objects that were referred to or were assigned a value in the statements.
                </span>
            </span>
        </p>
        <p>
            <span class="analysis">
                For analysis, they read the audit file and produce a data structure that allows users to run lineage queries interactively for understanding what happened during the data analysis section.
                Becker and Chambers (<a href="#becker1988a" class="reference">1988</a>) support functions for running these queries.
                They also support plotting relationships between statements as a process-centric graph.
            </span>.
        </p>
        <p>
            <span class="reproducibility">
                The provenance can also be used to generate an executable script that incorporates statements needed to produce a specied list of statements.
                Becker and Chambers (<a href="#becker1988a" class="reference">1988</a>) collect random number generators by including artificial statements in the audit file that specifies the seed.
            </span>.
        </p>
    """,
)