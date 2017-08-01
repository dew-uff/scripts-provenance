from snowballing.approaches import Group

from ..constants import *
from ...work.y2009 import demsky2009a

approach = Group(
    demsky2009a,
    display="Garm",
    approach_name="Garm",
    _cite=False,

    _meta=[dict(
        binary=YES,
        languages=[AGNOSTIC],
        goal=SECURITY,
        supports=[SECURITY, COMPREHENSION],
        categories=[COLLECTION, QUERY, SECURITY, STORAGE],

        mode=USER_LEVEL,

        tools=["Valgrind"],
        
        annotations=[PARSEABLE, EXTERNAL, INCLUSIVE, OPTIONAL, PROVENANCE],
        execution=[OVERRIDING],
        deployment=[],
        definition=[],

        execution_granularity=[
            INPUT_FILES,
            OUTPUT_FILES,
            BYTE_LINEAGE,
            POLICIES,
        ],
        deployment_granularity=[],
        definition_granularity=[],

        cache=NO,
        replay=NO,
        evolution=SEQUENCE.star("*previous"),
        pipeline=NO,
        summarization=[],

        distribution=[SHADOW_FILES],
        storage=[SHADOW_FILES],
        visualization=[],
        visplace=[],
        query=[COMMAND],
        integration=[],
        
        granularity=[BYTES, FILES],
        granularity_text="Bytes, Files (I/O - shadow)",
        management_text="Shadow Files",
        generic_query_text="",
        specific_query_text="Command",
        thread=YES,
        diff=[],

        limitations=[],
    )],
    _about="""
        <p>
            Garm (<a href="#demsky2009a" class="reference">demsky2009a</a>) collects provenance from binary applications to <span class="goal">enforce security policies</span>.
            <span class="collection">
                It combines static analysis with dynamic analysis to trace the application provenance.
                It uses <span class="tool">Valgrind</span> to instrument binaries before their execution.
                The static analysis removes redundant provenance computations and reduces the instrumentation impact. 
            </span>
        </p>
        <p>
            <span class="collection">
                <span title="When the alogirthm processes a register load statement, it checks to see if the register offset should be instrumented and has not already been loaded. If the register load meets both criteria, the instrumentation algorithm generates a shadow register load that loads the register's shadow provenance into a temporary">
                    During instrumentation, Garm finds <em>load</em> statements and replaces them by shadow load statements that load the corresponding provenance from the shadow memory.
                </span>
                Thus, it applies the <span class="strategy">overriding</span> strategy to capture execution provenance.
                Garm keeps track of a shadow memory state that stores 32-bit provenance values for each byte in the actual memory.
                These provenance values reference provenance composition tables that include the full lineage of each byte.
            </span>
            <span class="storage">
                When a monitored application writes data to a file, Garm creates a shadow file with the corresponding data provenance for every byte in the file.
                This shadow file also lists provenance values that contributes to each byte and provenance compositions.
            </span>
        </p>
        <p>
            <span class="collection">
                When a monitored application reads data from a file, Garm first looks for existing shadow file.
                If there is no shadow file, Garm creates a provenance record with the file name and the current execution number.
                Otherwise (i.e. a previous application wrote the file under Garm), it obtains the execution identifier that wrote the file, the file name, and a reference to the 32-bit provenance value that represents the existing byte provenance.
                This way, it can keep provenance across different executions.
            </span>
        </p>
        <p>
            <span class="security">
                Since the main goal of Garm is to enforce security policies, it allows users to attach data policies to provenance data. 
                With the data policies, users can 
                (i) prohibit outputting monitored data in any form; 
                (ii) allow outputting encrypted data as long as it ships the corresponding provenance information to keep the policy enforcement; 
                (iii) allow outputting unrestricted data. 
                These policies can be associated with other contexts, such as dates and data access counts. 
                Thus, it is possible to prohibit data to be read more than once, even if this data is copied to somewhere else. 
                The data provenance guarantees that the data policies can be traced to their creation moment.
            </span>
        </p>
        <p>
            <span class="security">
                In order to prevent data from leaking protected applications, 
                <span title="Uses fine-grained encryption based on stream ciphers to enable users to seamlessly share arbitrary files that contain policy protected data between applications while ensuring that programs cannot use policy-protected data in ways that violate the access policy">
                    Garm encrypts all data and provenance, 
                </span>
                and monitors interactions of the application with the underlying operating system to transfer encrypted data between different applications. 
                <span title="Uses a policy server for authenticating Garm instances, determining whether hey have permission to obtain keys and transferring keys">
                    Additionally, Garm requires that policy servers authenticate their instances to increase the security.
                </span>
            </span>
        </p>
        <p>
            <span class="analysis">
                Besides security enforcing, Demsky (<a href="#demsky2009a" class="reference">2009</a>) indicates that Garm has a provenance querying tool that allows users to navigate on the provenance graph, but does not say how does it work.
            </span>
        </p>
    """,

    categories=["collection", "security", "storage", "query"],


    _deployment=False,
    _definition=False,
    _execution=True,
    _annotations=True,

    _intrusion=True,
    _passive_monitoring=False,
    _overriding=False,
    _instrumentation=True,

    _storage="provenance shadow files",
    _visualization=False,
    _summarization=False,
    _diff=False,
    _query=True,
    _export=False,

    _reuse=False,
    _history=False,
    _goal="security", # operating system related; comprehension; reproducibility; cache
    _language="Agnostic", 
)

