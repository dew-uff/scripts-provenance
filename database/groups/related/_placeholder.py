from snowballing.approaches import Group

from ..constants import *
# from ...work.y9999 import name999

approach = Group(
    #name999,
    _category = "Unrelated", # Remove
    display="default",
    approach_name="-",
    _cite=False,

    _meta=[dict(
        binary=TODO, # YES,NO
        languages=[], # AGNOSTIC, PYTHON, ...

        goal=TODO, # MANAGEMENT, COMPREHENSION, FRAMEWORK, REPRODUCIBILITY, CACHE, SECURITY
        supports=[], # ^
        categories=[], # COLLECTION, DIFF, EVOLUTION, MANAGEMENT, QUERY, FILTER, FRAMEWORK, STORAGE, STREAMING, SUMMARIZATION, REPRODUCIBILITY, PORTABILITY, PARALLEL, CACHE, PACKAGE, REPEATABILITY, VISUALIZATION, SECURITY

        mode=TODO, # SYSTEM_WIDE, USER_LEVEL

        tools=[], # AST, kernel, systemtap, vcs, and others that assist the collection
        
        annotations=[], # PARSEABLE x EXECUTABLE, INTERNAL x EXTERNAL, INCLUSIVE x EXCLUSIVE, MANDATORY x OPTIONAL, DEFINITION x PROVENANCE
        execution=[], # INSTRUMENTATION, PASSIVE_MONITORING, POST_MORTEM, OVERRIDING
        deployment=[], # BEFORE_EXECUTION, DURING_EXECUTION, OPTIONAL
        definition=[], # ASKS_USERS, READING, PARSING, STATIC, DYNAMIC

        execution_granularity=[], # COMMANDS, VARIABLES, VALUES, FUNCTIONS, INPUT_FILES, OUTPUT_FILES, ...
        deployment_granularity=[], # SELF_VERSION, MODULES, OS_VERSION, ENV_VAR, PYTHON_VERSION, ...
        definition_granularity=[], # FUNCTION_CALLS, CONTENT, BYTECODE, SOURCE, ARGUMENTS, EXECUTION, ... 

        cache=TODO, # YES, NO
        replay=TODO, # YES, NO
        evolution=TODO, # TRIAL_ID, SEQUENCE, INTENTION, NO
        pipeline=TODO, # YES, NO
        summarization=[], # CLUSTERING, FILTERING

        distribution=[], # INTEROPERABLE, LOGIC_FILE, SHADOW_FILES, GRAPH_FILE, LOG, VCS, PROPRIETARY, REPOSITORY, WEB, PACKAGE, CONTENT_DATABASE, SOURCE, NOSQL
        storage=[], # ^ + FILE_SYSTEM, GRAPH_DB, RELATIONAL_DB, KEY_VALUE_DB, REPOSITORY
        visualization=[], # COMBINED_VIEW, INTEROPERABLE, DATA_VIEW, PROCESS_VIEW, GRAPH_FILE, WEB, PROPRIETARY, LOG_VIEW 
        visplace=[], # INTERNAL, EXTERNAL
        query=[], # PROV, QUERY, FUNCTION_CALLS, WEB, PROPRIETARY, COMMAND
        integration=[], # Str: other approaches
        
        granularity=[], # see individual granularities
        granularity_text="",
        management_text="",
        generic_query_text="",
        specific_query_text="",
        thread=TODO, # UNKNOWN, YES, NO
        diff=[], # PROVENANCE, DATA
                    
        limitations=[],
    )],
    _about="""
    """,
)