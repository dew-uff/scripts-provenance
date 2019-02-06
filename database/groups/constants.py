""" This file has the goal of defining constants to avoid mispellings in 
approaches comparisons """
from snowballing.approaches import Item
from .models import description

with description("generic"):
    YES = Item(u"\u2713", _bool=True)
    NO = Item(u"\u2717", _bool=False)
    UNKNOWN = Item(u"?", _bool=False)
    BOTH = Item(u"\u2713\u2717", _bool=True)
    TODO = Item("?", _bool=False)
    USER_DEFINED = Item("User defined")
    NA = Item("—", _bool=False)

with description("languages"):
    AGNOSTIC = Item("*")
    PYTHON = Item("Python")
    MATLAB = Item("Matlab")
    BLOCKLY = Item("Blockly")
    SHELL = Item("Shell")
    R = Item("R")
    S = Item("S")
    C = Item("C")
    CPP = Item("C++")
    PERL = Item("Perl")
    JAVA = Item("Java")
    IDL = Item("IDL")
    PROLOG = Item("Prolog")

with description("mode"):
    SYSTEM_WIDE = Item("System Wide")
    USER_LEVEL = Item("User Level")

with description("goals"):
    CACHE = Item("Caching")
    COMPREHENSION = Item("Comprehension")
    FRAMEWORK = Item("Framework")
    REPRODUCIBILITY = Item("Reproducibility")
    SECURITY = Item("Security")
    MANAGEMENT = Item("Management")

with description("categories"):
    REPEATABILITY = Item("Repeatability")
    PARALLEL = Item("Parallel")
    REPLAY = Item("Replay")
    COLLECTION = Item("Collection")
    PORTABILITY = Item("Portability")
    PACKAGE = Item("Package")
    DIFF = Item("Diff")
    VISUALIZATION = Item("Visualization")
    SUMMARIZATION = Item("Summarization")
    QUERY = Item("Query")
    STORAGE = Item("Storage")
    FILTER = Item("Filter")
    STREAMING = Item("Streaming")
    EVOLUTION = Item("Evolution")

with description("annotations"):
    INTERNAL = Item("Internal")
    EXTERNAL = Item("External")
    INCLUSIVE = Item("Inclusive")
    EXCLUSIVE = Item("Exclusive")
    PARSEABLE = Item("Parseable")
    EXECUTABLE = Item("Executable")
    OPTIONAL = Item("Optional")
    MANDATORY = Item("Mandatory")
    PROVENANCE = Item("Provenance")
    DEFINITION = Item("Definition")

with description("diff"):
    DATA = Item("Data")
    # PROVENANCE

with description("execution"):
    PASSIVE_MONITORING = Item("Passive Monitoring")
    OVERRIDING = Item("Overriding")
    INSTRUMENTATION = Item("Instrumentation")
    POST_MORTEM = Item("Post-Mortem")

with description("deployment"):
    SNAPSHOT = Item("Snapshot")
    CONTINUOUS = Item("Continuous")
    ANNOTATIONS = Item("Annotations")

with description("definition"):
    READING = Item("Reading")
    PARSING = Item("Parsing")
    STATIC = Item("Static")
    DYNAMIC = Item("Dynamic")
    ASKS = Item("Asks Users")

with description("execution granularities"):
    POLICIES = Item("Policies")
    PROC_NAME = Item("Process Name")
    PROC_DURATION = Item("Process Duration")
    PROC_PARANTAGE = Item("Process Parantage")
    PROC_LINEAGE = Item("Process Lineage")
    PROC_ARGUMENTS = Item("Process Arguments")
    PROC_PIPE = Item("Process Pipe")
    RANDOM_SEED = Item("Random Seed")
    INPUT_FILES = Item("Input Files")
    OUTPUT_FILES = Item("Output Files")
    OUTPUT_DATA = Item("Output Data")
    BYTE_LINEAGE = Item("Byte Lineage")
    TERMINAL = Item("Terminal")
    NETWORK = Item("Network")
    FUNC_LINEAGE = Item("Function Lineage")
    FUNC_ARGUMENTS = Item("Function Arguments")
    FUNC_DURATION = Item("Function Duration")
    VARIABLE_LINEAGE = Item("Variable Lineage")
    COMMAND_LINEAGE = Item("Command Lineage")
    DTA = Item("Dynamic Taint Analysis")
    PROGRAM_SLICING = Item("Program Slicing")
    USER_INPUT = Item("User Input")
    STACK = Item("Stack")
    MEMORY_FOOTPRINT = Item("Memory Footprint")
    BYTES = Item("Bytes")
    PROCESSES = Item("Processes")
    FILES = Item("Files")
    COMMANDS = Item("Commands")
    VARIABLES = Item("Variables")
    VALUES = Item("Values")
    VAR_DEPENDENCIES = Item("Variable Dependencies")
    FUNCTION_CALLS = Item("Function Calls")
    ARGUMENTS = Item("Arguments")
    RETURNS = Item("Returns")

with description("deployment granularities"):
    MODULES = Item("Modules")
    ENV_VAR = Item("Environment Variables")
    OS_VERSION = Item("Operating System Version")
    PYTHON_VERSION = Item("Python Version")
    R_VERSION = Item("Python Version")
    SELF_VERSION = Item("Self Version")

with description("definition granularities"):
    SOURCE = Item("Source")
    SOURCE_STRUCTURE = Item("Source Structure")
    BYTECODE = Item("Bytecode")
    PROGRAM = Item("Program")
    CONTENT = Item("File Content")
    EXECUTION = Item("Execution")

with description("Summarization"):
    CLUSTERING = Item("Clustering")
    FILTERING = Item("Filtering")

with description("evolution"):
    TRIAL_ID = Item("Trial Identification")
    SEQUENCE = Item("Trial Sequence")
    INTENTION = Item("Evolution Intention")

with description("distribution"):
    XML = Item("XML")
    PROV = Item("PROV")
    OPM = Item("OPM")
    XML_SERVER = Item("XML Server")
    GRAPHML = Item("GraphML")
    GRAPHVIZ = Item("GraphViz")
    SHADOW_FILES = Item("Shadow Files")
    NOSQL = Item("NoSQL")
    INTEROPERABLE = Item("Interoperable Format")
    GRAPH_FILE = Item("Graph File")
    MEMORY = Item("Memory")
    LOG = Item("Log")
    PROPRIETARY = Item("Proprietary")
    VCS = Item("Version Control System")
    REPOSITORY = Item("Repository")
    LOGIC_FILE = Item("Logic File")
    CONTENT_DATABASE = Item("Content Database")
    FILE = Item("File")
    WEB_SERVER = Item("Web Server")

with description("storage"):
    DATABASE = Item("Database")
    FILE_SYSTEM = Item("File System")
    KEY_VALUE_DB = Item("Key-Value Database")
    RELATIONAL_DB = Item("Relational Database")
    GRAPH_DB = Item("Graph Database")
    MEMORY = Item("Memory")

with description("query"):
    GENERIC = Item("Generic")
    SPECIFIC = Item("Specific")

    FILE_LINEAGE = Item("File Lineage")
    COMMAND = Item("Command")
    QUERY = Item("Query")
    WEB = Item("Web")
    TEXTUAL = Item("Textual")
    XQUERY = Item("XQuery")
    XPATH = Item("XPath")
    SPARQL = Item("SPARQL")
    SQL = Item("SQL")
    WEB_INTERFACE = Item("Web Interface")
    SOAP_MESSAGES = Item("Soap Messages")
    FUNCTIONS = Item("Functions")

with description("visualization"):
    JUPYTER = Item("Jupyter")
    COMBINED_VIEW = Item("Combined View")
    DATA_VIEW = Item("Data View")
    PROCESS_VIEW = Item("Process View")
    LOG_VIEW = Item("Log View")

with description("visplace"):
    INTERNAL = Item("Internal")
    EXTERNAL = Item("External")
    