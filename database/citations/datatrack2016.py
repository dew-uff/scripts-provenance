# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2004 import altintas2004a
from ..work.y2006 import callahan2006b
from ..work.y2007 import miles2007a
from ..work.y2009 import deelman2009a
from ..work.y2011 import moreau2011b
from ..work.y2011 import bostock2011a
from ..work.y2013 import missier2013c
from ..work.y2014 import murta2014a
from ..work.y2015 import ocana2015a
from ..work.y2015 import mcphillips2015a
from ..work.y2016 import eichinski2016a

DB(Citation(
    eichinski2016a, moreau2011b, ref="[1]",
    contexts=[
        "Standard models for how this information should be structured have emerged, such as the Open Provenance Model (OPM) developed following the International Provenance and Annotation Workshop in 2006 [1] and PROV-DM a more recent standard, endorsed by the W3C in 2012 [7].",
        "The Open Provenance Model and PROV-DM specifications define a number of ‘objects’ that do not show up as nodes on the Datatrack dependency graph, namely the “who” (which users) and the “how” (which processes), leaving only the dependencies between the “what” (the generated data). This difference can be seen by comparing the toy example given in the OPM specification (Fig. 6) [1].",
        "Example of a workflow graph that adheres to the OPM specification [1]",
    ],
))

DB(Citation(
    eichinski2016a, miles2007a, ref="[2]",
    contexts=[
        "In computational workflows, recording the data provenance - the dependencies, processes, parameters and people responsible for the creation of the data - is important, as it helps interpretation, verification, or tracing the origin of results [2].",

    ],
))

DB(Citation(
    eichinski2016a, callahan2006b, ref="[3]",
    contexts=[
        "Existing solutions to workflow data provenance tracking normally involve scientific workflow management systems (SWfMS) such as Vistrails [3] or Kepler [4]",

    ],
))

DB(Citation(
    eichinski2016a, altintas2004a, ref="[4]",
    contexts=[
        "Existing solutions to workflow data provenance tracking normally involve scientific workflow management systems (SWfMS) such as Vistrails [3] or Kepler [4]",

    ],
))

DB(Citation(
    eichinski2016a, deelman2009a, ref="[5]",
    contexts=[
        "These systems are well suited to distributed systems, collaborative research and batch processing across a wide range of parameters, and are hugely advantageous for automating the cycle of moving data to a supercomputer for analysis or simulation, launching the computational processes and managing the storage of the output [5].",
        "There is a huge variety of these SWfMS, but generally they have the following functionality: workflow composition, mapping the workflow onto resources or services, executing the workflow and recording the provenance metadata to allow the final output to be reproduced in the future [5].",
    ],
))

DB(Citation(
    eichinski2016a, Site("Datatrack 1.0.0-beta.1", "https://github.com/peichins/datatrack http://dx.doi.org/10.5281/zenodo.60582"), ref="[6]",
    contexts=[
        "This paper introduces Datatrack, a prototype R package  that [6] manages the dependencies and versioning of data generated in R.",

    ],
))

DB(Citation(
    eichinski2016a, missier2013c, ref="[7]",
    contexts=[
        "Standard models for how this information should be structured have emerged, such as the Open Provenance Model (OPM) developed following the International Provenance and Annotation Workshop in 2006 [1] and PROV-DM a more recent standard, endorsed by the W3C in 2012 [7].",

    ],
))

DB(Citation(
    eichinski2016a, ocana2015a, ref="[8]",
    contexts=[
        "Most research into the issues of data provenance has been focussed on Scientific Workflow Management Systems (SWfMS) [8].",

    ],
))

DB(Citation(
    eichinski2016a, murta2014a, ref="[9]",
    contexts=[
        "NoWorkflow [9] is a command line tool for recording detailed provenance metadata from python scripts. Its authors note that outside of a SWfMS, provenance capture is challenging due to the fact that the workflow sequence is encoded by the scripts themselves. NoWorkflow works by using software engineering techniques such as abstract syntax tree analysis, to determine this workflow from the scripts themselves and record provenance information during their execution.",

    ],
))

DB(Citation(
    eichinski2016a, mcphillips2015a, ref="[10]",
    contexts=[
        "The YesWorkflow [10] toolkit is another tool that offers some of the provenance recording functionality of a SWfMS to users of scripting languages such as R and Python. YesWorkflow allows the scientist to insert annotations as codecomments in the scripts that they write. The toolkit can then parse the codebase and interpret and convert these comments into a form that can be queried to answer questions about data objects created.",

    ],
))

DB(Citation(
    eichinski2016a, Site("RStudio: Integrated Development for R", "http://www.rstudio.com/."), ref="[11]",
    contexts=[
        "This graph is interactive and is displayed within the viewer of R-Studio (Fig. 5), a popular integrated development for R [11].",

    ],
))

DB(Citation(
    eichinski2016a, bostock2011a, ref="[12]",
    contexts=[
        "The visualization of the dependency graph is written in Javascript, html and css using the D3 Javascript library [12]. The “HTML widgets” R package [13] was used to display this graph within the RStudio console. For maintainability reasons, the visualization tasks were abstracted to a separate R package, on which Datatrack depends",

    ],
))

DB(Citation(
    eichinski2016a, Site("htmlwidgets: HTML Widgets for R. R package version 0.6", "https://cran.r-project.org/package=htmlwidgets"), ref="[13]",
    contexts=[
        "The visualization of the dependency graph is written in Javascript, html and css using the D3 Javascript library [12]. The “HTML widgets” R package [13] was used to display this graph within the RStudio console. For maintainability reasons, the visualization tasks were abstracted to a separate R package, on which Datatrack depends",

    ],
))
