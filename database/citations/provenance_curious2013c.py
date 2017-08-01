# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1987 import ferrante1987a
from ..work.y1989 import cytron1989a
from ..work.y1991 import lanter1991a
from ..work.y1992 import horwitz1992a
from ..work.y1996 import lynch1996a
from ..work.y2001 import buneman2001a
from ..work.y2002 import aalst2002a
from ..work.y2002 import babcock2002a
from ..work.y2003 import newman2003a
from ..work.y2003 import abadi2003a
from ..work.y2004 import oinn2004a
from ..work.y2005 import simmhan2005a
from ..work.y2005 import abadi2005a
from ..work.y2006 import ludascher2006a
from ..work.y2006 import callahan2006b
from ..work.y2006 import bishop2006a
from ..work.y2007 import buneman2007a
from ..work.y2007 import shields2007a
from ..work.y2007 import rohwer2007a
from ..work.y2008 import simmhan2008a
from ..work.y2008 import park2008a
from ..work.y2008 import bowers2008a
from ..work.y2008 import barga2008a
from ..work.y2009 import yue2009a
from ..work.y2009 import dozier2009a
from ..work.y2010 import angelino2010a
from ..work.y2010 import sarma2010a
from ..work.y2010 import huq2010a
from ..work.y2010 import portmann2010a
from ..work.y2010 import siebert2010a
from ..work.y2010 import wombacher2010a
from ..work.y2010 import yue2010a
from ..work.y2010 import silles2010a
from ..work.y2010 import miles2010a
from ..work.y2011 import huq2011a
from ..work.y2011 import wada2011a
from ..work.y2011 import beek2011a
from ..work.y2011 import yue2011b
from ..work.y2011 import yue2011a
from ..work.y2011 import miles2011a
from ..work.y2012 import huq2012b
from ..work.y2012 import huq2012a
from ..work.y2012 import groth2012a
from ..work.y2013 import huq2013c
from ..work.y2013 import hemalatha2013a
from ..work.y2014 import kannan2014a
from ..work.y2014 import fat2014a
from ..work.y2014 import kannan2014b
from ..work.y2014 import rangwala2014a
from ..work.y2014 import hashem2014a
from ..work.y2016 import hashem2016a

DB(Citation(
    huq2013c, newman2003a, ref="[1]",
    contexts=[
        "Scientists from many domains, such as physical, geological, environmental, biological etc. facilitate data-intensive e-Science applications to study and better understand these complex systems [1].",

    ],
))

DB(Citation(
    huq2013c, yue2009a, ref="[2]",
    contexts=[
        "A new generation of information infrastructure, known as cyberinfrastructure, is being developed to support the geoscientiﬁc research [2].",

    ],
))

DB(Citation(
    huq2013c, lanter1991a, ref="[3]",
    contexts=[
        ". In GIS, data provenance is known as lineage, which explicates the relationship among events and source data in constructing the data product [3].",

    ],
))

DB(Citation(
    huq2013c, buneman2001a, ref="[4]",
    contexts=[
        "In the context of database systems, data provenance provides the description of how a data product is achieved through the transformation activities from its input data [4].",

    ],
))

DB(Citation(
    huq2013c, simmhan2005a, ref="[5]",
    contexts=[
        "In a scientiﬁc workﬂow, data provenance refers to the derivation history of a data product starting from its origin [5]",

    ],
))

DB(Citation(
    huq2013c, buneman2007a, ref="[6]",
    contexts=[
        "In all contexts, provenance can be deﬁned at different levels of granularity [6].",
        "The relationship between data and processing elements during the execution phase explicates the ﬁne-grained data provenanceof a scientiﬁc model [6].",
        
    ],
))

DB(Citation(
    huq2013c, shields2007a, ref="[7]",
    contexts=[
        "The biggest challenges to make the framework generic in nature is to address different types of developing approach, i.e., with or without facilitating any speciﬁc tools, as well as to address different types of representation of model’s structure (e.g., data-ﬂow or control-ﬂow) [7].",

    ],
))

DB(Citation(
    huq2013c, aalst2002a, ref="[8]",
    contexts=[
        "1) Design Phase Characteristics: During the design phase, scientists deﬁne the model which is based on different activities, i.e., atomic units of work performed as a whole [8].",

    ],
))

DB(Citation(
    huq2013c, ludascher2006a, ref="[9]",
    contexts=[
        "Examples of platforms, where provenanceawareness has been considered, are e-Science workﬂow engines, such as Kepler [9], Karma2 [10], Taverna [11], VisTrails [12], stream processing and complex event processing engines, such as SensorDataWeb,1 STREAM [13], Aurora [14], Borealis [15], or Esper.2 ",
        "A provenance model described in [34] can collect provenance automatically during run time. This model is an extension of the Kepler [9] workﬂow engine. A layered model to represent workﬂow provenance is introduced in [35], which facilitates windows workﬂow foundation19 as the workﬂow engine. These techniques are used in a provenanceaware platformbut they do not offer anyfunctionalities to infer workﬂow provenance without any human intervention.",
    ],
))

DB(Citation(
    huq2013c, simmhan2008a, ref="[10]",
    contexts=[
        "Examples of platforms, where provenanceawareness has been considered, are e-Science workﬂow engines, such as Kepler [9], Karma2 [10], Taverna [11], VisTrails [12], stream processing and complex event processing engines, such as SensorDataWeb,1 STREAM [13], Aurora [14], Borealis [15], or Esper.2 ",
        "This set of properties are quite similar to the process provenance reported in [10].",
        
    ],
))

DB(Citation(
    huq2013c, oinn2004a, ref="[11]",
    contexts=[
        "Examples of platforms, where provenanceawareness has been considered, are e-Science workﬂow engines, such as Kepler [9], Karma2 [10], Taverna [11], VisTrails [12], stream processing and complex event processing engines, such as SensorDataWeb,1 STREAM [13], Aurora [14], Borealis [15], or Esper.2 ",

    ],
))

DB(Citation(
    huq2013c, callahan2006b, ref="[12]",
    contexts=[
        "Examples of platforms, where provenanceawareness has been considered, are e-Science workﬂow engines, such as Kepler [9], Karma2 [10], Taverna [11], VisTrails [12], stream processing and complex event processing engines, such as SensorDataWeb,1 STREAM [13], Aurora [14], Borealis [15], or Esper.2 ",

    ],
))

DB(Citation(
    huq2013c, babcock2002a, ref="[13]",
    contexts=[
        "Examples of platforms, where provenanceawareness has been considered, are e-Science workﬂow engines, such as Kepler [9], Karma2 [10], Taverna [11], VisTrails [12], stream processing and complex event processing engines, such as SensorDataWeb,1 STREAM [13], Aurora [14], Borealis [15], or Esper.2 ",

    ],
))

DB(Citation(
    huq2013c, abadi2003a, ref="[14]",
    contexts=[
        "Examples of platforms, where provenanceawareness has been considered, are e-Science workﬂow engines, such as Kepler [9], Karma2 [10], Taverna [11], VisTrails [12], stream processing and complex event processing engines, such as SensorDataWeb,1 STREAM [13], Aurora [14], Borealis [15], or Esper.2 ",

    ],
))

DB(Citation(
    huq2013c, abadi2005a, ref="[15]",
    contexts=[
        "Examples of platforms, where provenanceawareness has been considered, are e-Science workﬂow engines, such as Kepler [9], Karma2 [10], Taverna [11], VisTrails [12], stream processing and complex event processing engines, such as SensorDataWeb,1 STREAM [13], Aurora [14], Borealis [15], or Esper.2 ",

    ],
))

DB(Citation(
    huq2013c, lynch1996a, ref="[16]",
    contexts=[
        "This paradigm is used in stream processing and complex event processing environments as well as in the models used in distributed systems research, such as I/O automata [16].",

    ],
))

DB(Citation(
    huq2013c, huq2011a, ref="[17]",
    contexts=[
        "The input–output ratio [17] refers to the ratio between the number of contributing input data products to the number of produced output data products.",
        "Our proposed framework is also capable of managing ﬁnegrained data provenance in a storage-efﬁcient way. We discuss the applicability of several existing provenance inference methods [17], [22], [23] in this paper, which can infer provenance based on the given workﬂow provenance of the model and the timestamps associated with data products.",
        "Basic provenance inference method [17] infers ﬁne-grained data provenance in two phases: 1) backward computation and 2) forward computation.",
        "To manage ﬁne-grained data provenance in a storage-efﬁcient manner, we proposed several methods to infer ﬁne-grained provenance data [17], [22], [23].",
        "Basic provenance inference method [17] infers ﬁne-grained data provenance in two phases: 1) backward computation and 2) forward computation.",
        "Having this input from users, we apply the basic provenance inference method [17]",
        
    ],
))

DB(Citation(
    huq2013c, angelino2010a, ref="[18]",
    contexts=[
        "However, there is a high demand in the scientiﬁc community to capture workﬂow provenance automatically in a provenance-unaware platform like a scripting environment [18]",
        "In StarFlow, Angelo et al. [18] proposed a method which can build provenance trace at functional level for a Python script.",
    ],
))

DB(Citation(
    huq2013c, sarma2010a, ref="[19]",
    contexts=[
        "Existing work documents ﬁne-graineddata provenanceexplicitlyin a database[19],[20].",
        "LIVE [19] is a complete DBMS, which preserves explicitly the lineage of derived data items in form of boolean algebra. In sensornet republishing, Park and Heidemann[20] used an annotation-basedapproachto representdata provenance explicitly, which is expensive in terms of storage.",
        
    ],
))

DB(Citation(
    huq2013c, park2008a, ref="[20]",
    contexts=[
        "Existing work documents ﬁne-graineddata provenanceexplicitlyin a database[19],[20].",
        "LIVE [19] is a complete DBMS, which preserves explicitly the lineage of derived data items in form of boolean algebra. In sensornet republishing, Park and Heidemann[20] used an annotation-basedapproachto representdata provenance explicitly, which is expensive in terms of storage.",
    ],
))

DB(Citation(
    huq2013c, huq2010a, ref="[21]",
    contexts=[
        "Since provenance data are just metadata and less often used by the end users, the explicit documentation of ﬁne-grained provenance seems to be infeasible and too expensive [21].",

    ],
))

DB(Citation(
    huq2013c, huq2012b, ref="[22]",
    contexts=[
        "Our proposed framework is also capable of managing ﬁnegrained data provenance in a storage-efﬁcient way. We discuss the applicability of several existing provenance inference methods [17], [22], [23] in this paper, which can infer provenance based on the given workﬂow provenance of the model and the timestamps associated with data products.",
        "To manage ﬁne-grained data provenance in a storage-efﬁcient manner, we proposed several methods to infer ﬁne-grained provenance data [17], [22], [23].",
        "Probabilistic provenance inference [22] is a variant of the basic provenance inference method.",
    ],
))

DB(Citation(
    huq2013c, huq2012a, ref="[23]",
    contexts=[
        "Our proposed framework is also capable of managing ﬁnegrained data provenance in a storage-efﬁcient way. We discuss the applicability of several existing provenance inference methods [17], [22], [23] in this paper, which can infer provenance based on the given workﬂow provenance of the model and the timestamps associated with data products.",
        "To manage ﬁne-grained data provenance in a storage-efﬁcient manner, we proposed several methods to infer ﬁne-grained provenance data [17], [22], [23].",
        "Multistep probabilistic provenance inference [23] is an extension of the probabilistic provenance inference method.",
        "The detailed probability calculation is discussed in [23].",
        
    ],
))

DB(Citation(
    huq2013c, wada2011a, ref="[24]",
    contexts=[
        "We have also evaluated the proposed framework based on a case-study, involving a model for estimating the global water demand [24].",
        "To illustrate the problem description in Section I-D, the use case for estimating the global water demand based on the scientiﬁc model reported in [24] is introduced",
        "The authors would like to thank Y. Wada and L. P. H. van Beek from Utrecht University, Utrecht, The Netherlands, for providing the Python script used in [24] as well as related input data to showcase a complete demonstration.",
        
    ],
))

DB(Citation(
    huq2013c, portmann2010a, ref="[25]",
    contexts=[
        "Source data are collected from different existing datasets. Irrigated areas are prescribed by the MIRCA2000 dataset [25] and the FAOSTAT database.8 Crop factors, growing season lengths, and rootingdepth are obtainedfrom GCWM [26].",
        
    ],
))

DB(Citation(
    huq2013c, siebert2010a, ref="[26]",
    contexts=[
        "Source data are collected from different existing datasets. Irrigated areas are prescribed by the MIRCA2000 dataset [25] and the FAOSTAT database.8 Crop factors, growing season lengths, and rootingdepth are obtainedfrom GCWM [26].",
        
    ],
))

DB(Citation(
    huq2013c, rohwer2007a, ref="[27]",
    contexts=[
        "A map of countryspeciﬁc irrigation efﬁciency factors is also obtained from [27].",
        
    ],
))

DB(Citation(
    huq2013c, beek2011a, ref="[28]",
    contexts=[
        "In addition, daily potential and actual bare soil evaporation and transpiration are prescribed from the simulation results from the global hydrological and water resources model PCRGLOBWB [28].",
        
    ],
))

DB(Citation(
    huq2013c, wombacher2010a, ref="[29]",
    contexts=[
        "After collecting the workﬂow provenance automatically, the workﬂow is executed based on the execution model described in [29].",
    ],
))

DB(Citation(
    huq2013c, Site("P. M. Luc Moreau. The PROV Data Model and Abstract Syntax Notation", "http://www.w3.org/TR/prov-dm/"), ref="[30]",
    contexts=[
        "It is important to choose an appropriate provenance representation model to enable interoperability for sharing provenance data. To achieve interoperability, the PROV data model, known as PROV-DM, could be facilitated to represent provenance information [30].",
        
    ],
))

DB(Citation(
    huq2013c, horwitz1992a, ref="[31]",
    contexts=[
        "To transform the control dependencesinto data dependences in a conditional branch statement, we use the concept introduced in a program representation graph [31].",
        "A system dependence graph extends the deﬁnition of a PDG and it is capable of providing data and control dependences for multiprocedure programs [31].",
    ],
))

DB(Citation(
    huq2013c, cytron1989a, ref="[32]",
    contexts=[
        "In a program representation graph, after every conditional branch one extra node is added to represent the output variable to follow static single assignment forms [32].",

    ],
))

DB(Citation(
    huq2013c, bishop2006a, ref="[33]",
    contexts=[
        "First, a probabilistic model is built, which represents data products arrival pattern with respect to the start of a processing window by facilitating Markov Chain modeling [33].",

    ],
))

DB(Citation(
    huq2013c, bowers2008a, ref="[34]",
    contexts=[
        "A provenance model described in [34] can collect provenance automatically during run time. This model is an extension of the Kepler [9] workﬂow engine. A layered model to represent workﬂow provenance is introduced in [35], which facilitates windows workﬂow foundation19 as the workﬂow engine. These techniques are used in a provenanceaware platformbut they do not offer anyfunctionalities to infer workﬂow provenance without any human intervention.",

    ],
))

DB(Citation(
    huq2013c, barga2008a, ref="[35]",
    contexts=[
        "A provenance model described in [34] can collect provenance automatically during run time. This model is an extension of the Kepler [9] workﬂow engine. A layered model to represent workﬂow provenance is introduced in [35], which facilitates windows workﬂow foundation19 as the workﬂow engine. These techniques are used in a provenanceaware platformbut they do not offer anyfunctionalities to infer workﬂow provenance without any human intervention.",

    ],
))

DB(Citation(
    huq2013c, ferrante1987a, ref="[36]",
    contexts=[
        "A PDG makes explicit both the data and control dependences for each statement in a program [36].",

    ],
))

DB(Citation(
    huq2013c, yue2010a, ref="[37]",
    contexts=[
        "Yue et al. [37] proposed an approach to capture provenance data automatically using semantic web technologies.",

    ],
))

DB(Citation(
    huq2013c, yue2011b, ref="[38]",
    contexts=[
        "Furthermore, a provenance framework has also been proposedin [38]forgeoprocessingworkﬂows",

    ],
))

DB(Citation(
    huq2013c, yue2011a, ref="[39]",
    contexts=[
        "Yue et al. [39] proposed to facilitate XML encoding to represent provenance data for better interoperability. In our proposed framework, since provenance data are represented as a graph, we facilitate GraphML11 which is a XML-based ﬁle format for exchanging graph structure data. GraphML is supported by most of the graph editing tools such as yEd,12 Gephi13 etc.",
        "Yue et al. [39] reported an approach that enables interoperability for the collected provenance information in a service-oriented GIS architecture",
        
    ],
))

DB(Citation(
    huq2013c, dozier2009a, ref="[40]",
    contexts=[
        "Another method of capturing provenance has been discussed in [40].",

    ],
))

DB(Citation(
    huq2013c, miles2011a, ref="[41]",
    contexts=[
        "Miles et al. [41] proposed a methodology, known as PrIMe, that can adapt applications to make them provenance-aware by exposing application information documentedthrougha series of steps and by modifying the application design",

    ],
))

DB(Citation(
    huq2013c, groth2012a, ref="[42]",
    contexts=[
        ". Groth et al. [42] proposed a technique that can reconstructprovenanceofthe manipulationsdoneover the data in a provenance-unaware system like excel sheet or a programming tool like R",

    ],
))

DB(Citation(
    huq2013c, silles2010a, ref="[43]",
    contexts=[
        "Silles and Runnalls [43] proposed a variant of R interpreter, CXXR, which can maintain and represent collected provenance information. Miles [44] proposed to document provenance by modifying the source code of a program automatically.",

    ],
))

DB(Citation(
    huq2013c, miles2010a, ref="[44]",
    contexts=[
        "Silles and Runnalls [43] proposed a variant of R interpreter, CXXR, which can maintain and represent collected provenance information. Miles [44] proposed to document provenance by modifying the source code of a program automatically.",

    ],
))

DB(Citation(
    hashem2016a, huq2013c, ref="",
    contexts=[

    ],
))

DB(Citation(
    hemalatha2013a, huq2013c, ref="",
    contexts=[

    ],
))

DB(Citation(
    kannan2014a, huq2013c, ref="",
    contexts=[

    ],
))

DB(Citation(
    fat2014a, huq2013c, ref="",
    contexts=[

    ],
))

DB(Citation(
    kannan2014b, huq2013c, ref="",
    contexts=[

    ],
))

DB(Citation(
    rangwala2014a, huq2013c, ref="",
    contexts=[

    ],
))

DB(Citation(
    hashem2014a, huq2013c, ref="",
    contexts=[

    ],
))
