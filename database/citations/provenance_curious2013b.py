# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1974 import kahn1974a
from ..work.y1984 import weiser1984a
from ..work.y1987 import ferrante1987a
from ..work.y1988 import gelfond1988a
from ..work.y1989 import cytron1989a
from ..work.y1991 import lanter1991a
from ..work.y1992 import horwitz1992a
from ..work.y1995 import lee1995a
from ..work.y1996 import lynch1996a
from ..work.y1997 import woodruff1997a
from ..work.y1999 import baeza1999a
from ..work.y2000 import cui2000a
from ..work.y2001 import buneman2001a
from ..work.y2001 import frew2001a
from ..work.y2002 import aalst2002a
from ..work.y2002 import babcock2002a
from ..work.y2002 import buneman2002a
from ..work.y2002 import lifschitz2002a
from ..work.y2003 import abadi2003a
from ..work.y2003 import baral2003a
from ..work.y2003 import chandrasekaran2003a
from ..work.y2003 import cui2003a
from ..work.y2003 import golab2003a
from ..work.y2003 import koncilia2003a
from ..work.y2003 import newman2003a
from ..work.y2003 import szomszor2003a
from ..work.y2004 import arasu2004a
from ..work.y2004 import klein2004a
from ..work.y2004 import oinn2004a
from ..work.y2004 import widom2004a
from ..work.y2005 import abadi2005a
from ..work.y2005 import bhagwat2005a
from ..work.y2005 import bose2005a
from ..work.y2005 import chiticariu2005a
from ..work.y2005 import deelman2005a
from ..work.y2005 import groth2005a
from ..work.y2005 import groth2005d
from ..work.y2005 import ledlie2005a
from ..work.y2005 import simmhan2005b
from ..work.y2005 import dongen2005a
from ..work.y2005 import dongen2005b
from ..work.y2006 import agrawal2006a
from ..work.y2006 import barga2006a
from ..work.y2006 import benjelloun2006a
from ..work.y2006 import bishop2006a
from ..work.y2006 import callahan2006b
from ..work.y2006 import freire2006a
from ..work.y2006 import futrelle2006a
from ..work.y2006 import hull2006a
from ..work.y2006 import ludascher2006a
from ..work.y2006 import mcphillips2006a
from ..work.y2006 import muniswamy2006a
from ..work.y2006 import simmhan2006b
from ..work.y2006 import vijayakumar2006a
from ..work.y2007 import buneman2007a
from ..work.y2007 import davidson2007a
from ..work.y2007 import gil2007b
from ..work.y2007 import green2007b
from ..work.y2007 import green2007a
from ..work.y2007 import groth2007a
from ..work.y2007 import miles2007a
from ..work.y2007 import pothier2007a
from ..work.y2007 import reddy2007a
from ..work.y2007 import rohwer2007a
from ..work.y2007 import shields2007a
from ..work.y2007 import tan2007a
from ..work.y2007 import vijayakumar2007a
from ..work.y2007 import vijayakumar2007b
from ..work.y2007 import wang2007a
from ..work.y2008 import barga2008a
from ..work.y2008 import bowers2008a
from ..work.y2008 import chapman2008a
from ..work.y2008 import frew2008a
from ..work.y2008 import frew2008b
from ..work.y2008 import gebali2008a
from ..work.y2008 import gedik2008a
from ..work.y2008 import kim2008a
from ..work.y2008 import misra2008a
from ..work.y2008 import moreau2008c
from ..work.y2008 import park2008a
from ..work.y2008 import simmhan2008a
from ..work.y2009 import anand2009a
from ..work.y2009 import cheney2009a
from ..work.y2009 import valle2009a
from ..work.y2009 import valle2009b
from ..work.y2009 import dozier2009a
from ..work.y2009 import glavic2009a
from ..work.y2009 import groth2009a
from ..work.y2009 import jararweh2009a
from ..work.y2009 import ludascher2009a
from ..work.y2009 import yue2009a
from ..work.y2010 import angelino2010a
from ..work.y2010 import barseghian2010a
from ..work.y2010 import huq2010a
from ..work.y2010 import miles2010a
from ..work.y2010 import moreau2010a
from ..work.y2010 import portmann2010a
from ..work.y2010 import sarma2010a
from ..work.y2010 import siebert2010a
from ..work.y2010 import silles2010a
from ..work.y2010 import stuckenschmidt2010a
from ..work.y2010 import wombacher2010a
from ..work.y2010 import yue2010a
from ..work.y2011 import do2011a
from ..work.y2011 import erdem2011a
from ..work.y2011 import esmaili2011a
from ..work.y2011 import gebser2011a
from ..work.y2011 import gebser2011b
from ..work.y2011 import glavic2011a
from ..work.y2011 import huq2011b
from ..work.y2011 import mileo2011a
from ..work.y2011 import mileo2011b
from ..work.y2011 import miles2011a
from ..work.y2011 import moreau2011b
from ..work.y2011 import schneider2011a
from ..work.y2011 import beek2011a
from ..work.y2011 import wada2011b
from ..work.y2011 import wada2011a
from ..work.y2011 import yue2011b
from ..work.y2011 import yue2011a
from ..work.y2012 import buneman2012a
from ..work.y2012 import gebser2012a
from ..work.y2012 import gebser2012b
from ..work.y2012 import gebser2012c
from ..work.y2012 import glavic2012a
from ..work.y2012 import groth2012a
from ..work.y2012 import huq2012b
from ..work.y2012 import huq2012a
from ..work.y2012 import ikeda2012a
from ..work.y2012 import novelli2012a
from ..work.y2012 import sansrimahachai2012a
from ..work.y2012 import wada2012a
from ..work.y2013 import huq2013b
from ..work.y2013 import buneman2013a
from ..work.y2013 import vlieg2013a
from ..work.y2013 import huq2013a
from ..work.y2013 import moreau2013a
from ..work.y2013 import yin2013a

DB(Citation(
    huq2013b, aalst2002a, ref="[1]",
    contexts=[
        "During the design phase, scientists deﬁne the model which is based on different activities, i.e., atomic units of work performed as a whole [1].",

    ],
))

DB(Citation(
    huq2013b, abadi2003a, ref="[2]",
    contexts=[
        "Examples of the platforms where provenance awareness has been considered are scientiﬁc workﬂowenginessuchasTaverna[102],VisTrails[24],Kepler[84],Karma2 [116], Wings/Pegasus [77], stream data processing or complex event processing engines like SensorDataWeb 2, STREAM [8], Aurora [2], Borealis [3], or Esper3",
        "The Aurora [2] system manages data streams for monitoring applications.",
        "Theworkﬂowprovenanceofascientiﬁcmodelcaneitherbecreatedand stored by using provenance-aware workﬂow engines, stream processing engines, complex event processing engines [84, 116, 102, 24, 8, 2, 3] or be captured automatically as discussed in Chapter 3 in case the model is developed using a general purpose programming tool such as Python.",
        
    ],
))

DB(Citation(
    huq2013b, abadi2005a, ref="[3]",
    contexts=[
        "Examples of the platforms where provenance awareness has been considered are scientiﬁc workﬂowenginessuchasTaverna[102],VisTrails[24],Kepler[84],Karma2 [116], Wings/Pegasus [77], stream data processing or complex event processing engines like SensorDataWeb 2, STREAM [8], Aurora [2], Borealis [3], or Esper3",
        "The Borealis [3] is an extended version of Aurora and also includes distributed functionality.",
        "Ariadne has been implemented on the top of Borealis stream processing engine [3].",
        "Theworkﬂowprovenanceofascientiﬁcmodelcaneitherbecreatedand stored by using provenance-aware workﬂow engines, stream processing engines, complex event processing engines [84, 116, 102, 24, 8, 2, 3] or be captured automatically as discussed in Chapter 3 in case the model is developed using a general purpose programming tool such as Python.",
        
    ],
))

DB(Citation(
    huq2013b, agrawal2006a, ref="[4]",
    contexts=[
        "Based on the work mentioned in [30, 29], Trio, a database system managing not only data but also the accuracy and the lineage of data is proposed in [131, 4].",

    ],
))

DB(Citation(
    huq2013b, anand2009a, ref="[5]",
    contexts=[
        "In the area of scientiﬁc data management, authors proposed annotationbased provenance framework [87, 5].",

    ],
))

DB(Citation(
    huq2013b, angelino2010a, ref="[6]",
    contexts=[
        "capture workﬂow provenance automatically in a provenance-unaware platform such as a programming/scripting language [6].",
        "Angelino et al. have proposed StarFlow [6] which can build a provenance trace at functional level for a Python program",
        "Angelinoetal.[6]reportedthatthesescientistsusedtowriteprograms/scripts in a general purpose programming/scripting language.",
    ],
))

DB(Citation(
    huq2013b, arasu2004a, ref="[7]",
    contexts=[
        "The Stanford InfoLab has undertaken a data stream processing project called STREAM (STanford stREam datA Manager) [8, 7].",

    ],
))


DB(Citation(
    huq2013b, babcock2002a, ref="[8]",
    contexts=[
        "Examples of the platforms where provenance awareness has been considered are scientiﬁc workﬂowenginessuchasTaverna[102],VisTrails[24],Kepler[84],Karma2 [116], Wings/Pegasus [77], stream data processing or complex event processing engines like SensorDataWeb 2, STREAM [8], Aurora [2], Borealis [3], or Esper3",
        "The Stanford InfoLab has undertaken a data stream processing project called STREAM (STanford stREam datA Manager) [8, 7].",
        "As discussed in [8, 59], each data product in a stream is associated with a timestamp.",
        "Theworkﬂowprovenanceofascientiﬁcmodelcaneitherbecreatedand stored by using provenance-aware workﬂow engines, stream processing engines, complex event processing engines [84, 116, 102, 24, 8, 2, 3] or be captured automatically as discussed in Chapter 3 in case the model is developed using a general purpose programming tool such as Python.",
    ],
))

DB(Citation(
    huq2013b, baeza1999a, ref="[9]",
    contexts=[
        "Precision and recall are widely chosen measures for evaluating the performance of information retrieval systems [9].",

    ],
))

DB(Citation(
    huq2013b, baral2003a, ref="[10]",
    contexts=[
        "AnswerSetProgramming(ASP)[10,83,52]isapurelydeclarativeandnonmonotonic logic programming paradigm.",

    ],
))

DB(Citation(
    huq2013b, barga2006a, ref="[11]",
    contexts=[
        "Barga et al. have proposed a mechanism for capturing provenance information in scientiﬁc workﬂows [11]",
        "VisTrails [24, 42] builds on a similar idea of multi-layered provenance representationpresentedin[11,12].",
        "Some of them proposed multi-layered provenance representation to allow users to deal with the complexity and large size of provenance information [115, 11, 24, 77].",
        "Scientiﬁc workﬂow engines collect provenance at different levels of granularity-bothworkﬂowandﬁne-grainedprovenance[84,115,11,24,77,63].",
    ],
))

DB(Citation(
    huq2013b, barga2008a, ref="[12]",
    contexts=[
        "Therefore,authorsintroduced a provenance model supporting multiple levels of provenance representation [12].",
        "VisTrails [24, 42] builds on a similar idea of multi-layered provenance representationpresentedin[11,12].",
    ],
))

DB(Citation(
    huq2013b, barseghian2010a, ref="[13]",
    contexts=[
        "Several extensions of Kepler have been proposed and implemented to support provenance in different domains [75, 13]",
        ".In[13],authorshavepresentedanextension to Kepler system to support streaming data, originating from environmental sensors.",
    ],
))

DB(Citation(
    huq2013b, benjelloun2006a, ref="[14]",
    contexts=[
        "Trio introduces a new query language TriQL [14], an extension of SQL, to deal with uncertainty and lineage information.",

    ],
))

DB(Citation(
    huq2013b, bhagwat2005a, ref="[15]",
    contexts=[
        "DBNotes [28, 15] is an annotation management system for relational database systems.",
        "Studies reported in [21, 28, 15, 61, 56] are annotation-based provenance capturing techniques",
        "Recent studies in this area provide extended solutions that can address where-provenance [21, 28, 15].",
        "Eager or annotation-based approaches [21, 131, 109, 28, 15, 60, 56, 46] documents provenance information explicitly which incurs a considerable amount of storage overhead for maintaining provenance data.",
        "Studies reported in [21, 131, 109, 28, 15, 60, 56, 46] are annotation-based approaches to collect provenance in the light of database systems.",
        "Existing annotation-based ﬁne-grained provenancecollectionsystems[21,131,109,28,15,60,56]documentsprovenance information explicitly which incurs a considerable amount of storage overhead for maintaining provenance data.",
        
    ],
))

DB(Citation(
    huq2013b, bishop2006a, ref="[16]",
    contexts=[
        "We propose a novel tuple-state graph, that has to be constructed by facilitating Markov chain model [16], to compute both P(αik) and P(βik) distributions which help us to infer ﬁne-grained data provenance.",
        "A Markov chain is amathematicalsystemthatrepresentstheundergoingtransitionsfromone state to another in a chain-like manner [16].",
        "over view Vi and the arrival of the ﬁrst tuple within that window. Computation of P(αik) distribution is accomplished by constructing a tuple-state graph, Gα, by facilitating Markov chain model [16].",
    ],
))

DB(Citation(
    huq2013b, bose2005a, ref="[17]",
    contexts=[
        "There also exists provenance-aware platforms, developed speciﬁcally for a particular applicationdomainorlanguage.Acomprehensiveoverviewofprovenance systems primarily focusing on the e-science domain is presented in [17].",
    ],
))

DB(Citation(
    huq2013b, bowers2008a, ref="[18]",
    contexts=[
        "An extension of this framework described in [18] has introduced a solution to minimize size of documented provenance information by allowing annotations on collections to cascade to all descendant elements.",

    ],
))

DB(Citation(
    huq2013b, buneman2007a, ref="[19]",
    contexts=[
        "In all contexts, provenance can be deﬁned at different levels of granularity [19].",
        "The relationships between data and processing elements during the execution phase are essentials to derive the ﬁne-grained data provenance of a scientiﬁc model [19]",
        "Provenance systems targeting a speciﬁc programming language or data processing tools has also been built. In these aforesaid platforms, provenance has been collected at different levels of granularity depending on its target application and user [19].",
        
    ],
))

DB(Citation(
    huq2013b, buneman2001a, ref="[20]",
    contexts=[
        "Maintaining data provenance [20, 114], also known as lineage [80], allows scientists to achieve these requirements and thus, leading towards the development of the provenance-aware cyberinfrastructure.",
        "In the context of database systems, data provenance provides the description of how a data product is achieved through the transformation activities from its input data [20].",
        "In the context of database systems, data provenance provides the description of how an output data product is achieved through the transformation activities from its input data [20]. In [20], Buneman et al. have also described a data model to compute provenance on both relations (coarse-grained) and tuples (ﬁne-grained) level. In this data model, the location of any piece of data can be uniquely described by a path. Furthermore, in this study, authors have also drawn a distinction between why-provenance and where-provenance.",
        
    ],
))

DB(Citation(
    huq2013b, buneman2002a, ref="[21]",
    contexts=[
        "Existing work documents ﬁne-grained data provenance explicitly in a database, also known as the annotation-based approach [21, 131, 109, 58, 108].",
        "An annotation-based approach has been proposed to address where-provenance [21].",
        "On the other hand,in the eager approach, provenance information is propagated from one activities to another during execution of a scientiﬁc experiment [21, 15, 28, 60, 61, 56].",
        "Buneman et al. have proposed propagation rules [21] which are deﬁnedforeachrelationaloperatortodeterminehowannotationsarecarried from source to output database.",
        "Studies reported in [21, 28, 15, 61, 56] are annotation-based provenance capturing techniques",
        "Recent studies in this area provide extended solutions that can address where-provenance [21, 28, 15].",
        "Eager or annotation-based approaches [21, 131, 109, 28, 15, 60, 56, 46] documents provenance information explicitly which incurs a considerable amount of storage overhead for maintaining provenance data.",
        "Some of them also propagate provenance from one activity to the next one [21, 131, 60, 56, 58].",
        "Studies reported in [21, 131, 109, 28, 15, 60, 56, 46] are annotation-based approaches to collect provenance in the light of database systems.",
        "Existing annotation-based ﬁne-grained provenancecollectionsystems[21,131,109,28,15,60,56]documentsprovenance information explicitly which incurs a considerable amount of storage overhead for maintaining provenance data.",
        
    ],
))

DB(Citation(
    huq2013b, buneman2012a, ref="[22]",
    contexts=[
        "Buneman et al. have proposed a hierarchical model on provenance information and have also demonstrated how this hierarchical structure can be derived from the execution of programs in ProvL programming language that describes the workﬂows [22].",

    ],
))

DB(Citation(
    huq2013b, buneman2013a, ref="[23]",
    contexts=[
        "A recent study conducted by Buneman et al. [23] has shown that annotations may itself be annotated",
        "In studies reported in [61, 23], authors have demonstrated their proposed provenance collection mechanisms in context of Datalog programs.",
    ],
))

DB(Citation(
    huq2013b, callahan2006b, ref="[24]",
    contexts=[
        "Examples of the platforms where provenance awareness has been considered are scientiﬁc workﬂowenginessuchasTaverna[102],VisTrails[24],Kepler[84],Karma2 [116], Wings/Pegasus [77], stream data processing or complex event processing engines like SensorDataWeb 2, STREAM [8], Aurora [2], Borealis [3], or Esper3",
        "A workﬂow management system (e.g. Kepler [84], Taverna [102], VisTrails [24]) deﬁnes and manages a series of activities within a scientiﬁc data intensive experiment to produce an output data product. In such systems, activities create a processing chain and each activity takes input data products from a previous activity, i.e., data-driven workﬂows.",
        "VisTrails [24, 42] builds on a similar idea of multi-layered provenance representationpresentedin[11,12].",
        "Some of them proposed multi-layered provenance representation to allow users to deal with the complexity and large size of provenance information [115, 11, 24, 77].",
        "Scientiﬁc workﬂow engines collect provenance at different levels of granularity-bothworkﬂowandﬁne-grainedprovenance[84,115,11,24,77,63].",
        "Theworkﬂowprovenanceofascientiﬁcmodelcaneitherbecreatedand stored by using provenance-aware workﬂow engines, stream processing engines, complex event processing engines [84, 116, 102, 24, 8, 2, 3] or be captured automatically as discussed in Chapter 3 in case the model is developed using a general purpose programming tool such as Python.",
        "There are existing tools and techniques that can extract workﬂow provenance of a scientiﬁc model [102, 84, 24, 116, 77]",
    ],
))

DB(Citation(
    huq2013b, chandrasekaran2003a, ref="[25]",
    contexts=[
        "Chandrasekaran et al. adopted the concept of dataﬂow process networks for stream data processing engine [25].",
        "In [25], authors deﬁned different windowing schemes to bound this inﬁnite data stream. However, provenance tracing has not been supported in TelegraphCQ.",
    ],
))

DB(Citation(
    huq2013b, chapman2008a, ref="[26]",
    contexts=[
        "Existing approaches [103, 26, 109, 108] record ﬁne-grained data provenance explicitly in varying manners.",
        "Therefore, we improve this explicit provenance collection system using the concept of basic factorization which is proposed in [26].",
    ],
))

DB(Citation(
    huq2013b, cheney2009a, ref="[27]",
    contexts=[
        "Provenance-aware platforms have been also built in the context of database systems as discussed in [119, 27].",

    ],
))

DB(Citation(
    huq2013b, chiticariu2005a, ref="[28]",
    contexts=[
        "On the other hand,in the eager approach, provenance information is propagated from one activities to another during execution of a scientiﬁc experiment [21, 15, 28, 60, 61, 56].",
        "DBNotes [28, 15] is an annotation management system for relational database systems.",
        "Studies reported in [21, 28, 15, 61, 56] are annotation-based provenance capturing techniques",
        "Recent studies in this area provide extended solutions that can address where-provenance [21, 28, 15].",
        "Studies reported in [21, 131, 109, 28, 15, 60, 56, 46] are annotation-based approaches to collect provenance in the light of database systems.",
        "Existing annotation-based ﬁne-grained provenancecollectionsystems[21,131,109,28,15,60,56]documentsprovenance information explicitly which incurs a considerable amount of storage overhead for maintaining provenance data.",
        
    ],
))

DB(Citation(
    huq2013b, cui2003a, ref="[29]",
    contexts=[
        "Why-provenance determines the input data tuples which contributed to produce an output data tuple. This type of provenance is studied in [133, 29].",
        "lazy approach and eager approach. In the lazy approach, provenance information is generated on demand based on a user request [133,29]",
        "Another work falling in the class of lazy approach of provenance generation is the study reported in [30, 29].",
        "Based on the work mentioned in [30, 29], Trio, a database system managing not only data but also the accuracy and the lineage of data is proposed in [131, 4].",
        "Severalprovenancesolutionsindatabasesystemsaddresswhy-provenance [133, 30, 29, 56, 131, 109].",
        
    ],
))

DB(Citation(
    huq2013b, cui2000a, ref="[30]",
    contexts=[
        "Another work falling in the class of lazy approach of provenance generation is the study reported in [30, 29].",
        "Based on the work mentioned in [30, 29], Trio, a database system managing not only data but also the accuracy and the lineage of data is proposed in [131, 4].",
        "Severalprovenancesolutionsindatabasesystemsaddresswhy-provenance [133, 30, 29, 56, 131, 109].",
        
    ],
))

DB(Citation(
    huq2013b, cytron1989a, ref="[31]",
    contexts=[
        "In a program representation graph, after every conditional branch one extra node is added to represent the output variable to follow static single assignment forms [31].",

    ],
))

DB(Citation(
    huq2013b, davidson2007a, ref="[32]",
    contexts=[
        "A lot of attention has been paid to design and develop provenance-aware platforms in scientiﬁc workﬂow systems as discussed in surveys conducted by Simmhan et al. [114] and Davidson et al. [32].",
        "While scientiﬁc workﬂows mainly focus on derivation of data and in these kind of systems data processing activities are treated as black boxes, hiding details of data transformations [32].",
    ],
))

DB(Citation(
    huq2013b, vlieg2013a, ref="[33]",
    contexts=[
        "Very recently, Netherlands eScience center published a white paper on ‘data stewardship’ [33], referring to the practice of preserving data to ensure reproducibility and to also stimulate more data-driven research where provenance can play an important role.",

    ],
))

DB(Citation(
    huq2013b, deelman2005a, ref="[34]",
    contexts=[
        "This approach is implemented in the Wings/Pegasus framework [ 34, 55].",

    ],
))

DB(Citation(
    huq2013b, valle2009a, ref="[35]",
    contexts=[
        "Stream processing and reasoning [36, 35, 117] are a relatively new area of research individuallyconcernedwithprocessinglargeamountsofdynamicallygenerated data.",

    ],
))

DB(Citation(
    huq2013b, valle2009b, ref="[36]",
    contexts=[
        "Stream processing and reasoning [36, 35, 117] are a relatively new area of research individuallyconcernedwithprocessinglargeamountsofdynamicallygenerated data.",

    ],
))

DB(Citation(
    huq2013b, do2011a, ref="[37]",
    contexts=[
        "While some attempts have been made to re-purpose ASP reasoners for streaming data [37], The current work by Gebser et al. [50] provides an all encompassing software solution to ASP-based stream reasoning.",

    ],
))

DB(Citation(
    huq2013b, dozier2009a, ref="[38]",
    contexts=[
        "Furthermore, in another study, Dozier et al. facilitates ES3 system to build provenance traces of a scientiﬁc experiment computing snow-covered areas [38].",

    ],
))

DB(Citation(
    huq2013b, erdem2011a, ref="[39]",
    contexts=[
        "The ability to deal with incomplete knowledge, conﬂicting and noisy input and common sense reasoning made ASP applicable to domains such as civil engineering, home healthcare, sensor networks, planning, bio-informatics, phylogenesis, system biology, industrial applications and more [101, 88, 89, 39, 49]",

    ],
))

DB(Citation(
    huq2013b, esmaili2011a, ref="[40]",
    contexts=[
        "Studies reported in [103, 129, 93, 40, 58, 108] proposed different mechanisms to manage ﬁne-grained data provenance for data streams. Next, we discuss these work in turn.",
        "Anotherworkreportedin[40,58]alsoaddressesﬁne-graineddataprovenance management for data streams.",
    ],
))

DB(Citation(
    huq2013b, ferrante1987a, ref="[41]",
    contexts=[
        "Similar work has also been done in software engineering domain by facilitating static program analysis. A program dependence graph (PDG) makes both the data and the control dependences explicit for each statement in a program [41].",

    ],
))

DB(Citation(
    huq2013b, freire2006a, ref="[42]",
    contexts=[
        "VisTrails [24, 42] builds on a similar idea of multi-layered provenance representationpresentedin[11,12].",

    ],
))

DB(Citation(
    huq2013b, frew2001a, ref="[43]",
    contexts=[
        "Another study by Frew et al. have proposed a data management infrastructure to track processing of satellite images [43].",

    ],
))

DB(Citation(
    huq2013b, frew2008a, ref="[44]",
    contexts=[
        "This technique has been used to build a prototype, called Earth System Science Server (ES3) [44].",
        "This technique has been usedintheES3projectprovidingcomputationalprovenance[44]",
    ],
))

DB(Citation(
    huq2013b, frew2008b, ref="[45]",
    contexts=[
        "Afterward, this technique has been extended by the study reported in [45].",
        "Furthermore, documenting ﬁne-grained data provenance explicitly requires operator instrumentation that explicitly adds a few lines of code into the actual model itself to capture provenance [45].",
    ],
))

DB(Citation(
    huq2013b, futrelle2006a, ref="[46]",
    contexts=[
        "Another project has been initiated for recording and querying provenance data, called Tupelo2 project1. This project is aimed at creating a metadata management system based on semantic web technologies [46].",
        "Eager or annotation-based approaches [21, 131, 109, 28, 15, 60, 56, 46] documents provenance information explicitly which incurs a considerable amount of storage overhead for maintaining provenance data.",
        "Studies reported in [21, 131, 109, 28, 15, 60, 56, 46] are annotation-based approaches to collect provenance in the light of database systems.",
        "In [103], authors propose to use transaction time on incoming stream data. Ensuring temporal ordering of data tuples is one of the main requirements in stream dataprocessing. Moreover,several studies [46, 116] have proposed to maintain process level provenance which correspond to the documentation of workﬂow provenance.",
        
    ],
))

DB(Citation(
    huq2013b, gebali2008a, ref="[47]",
    contexts=[
        "The long-term behavior of a Markov chain enters a steady state, i.e., the probability of being in a state will not change with time [47].",

    ],
))

DB(Citation(
    huq2013b, gebser2011a, ref="[48]",
    contexts=[
        "It is primarily based on their previous work into incremental based ASP reasoning [48] in which external data was sequentially passed as input into the reasoner to provide continuous results.",
    ],
))

DB(Citation(
    huq2013b, gebser2011b, ref="[49]",
    contexts=[
        "The ability to deal with incomplete knowledge, conﬂicting and noisy input and common sense reasoning made ASP applicable to domains such as civil engineering, home healthcare, sensor networks, planning, bio-informatics, phylogenesis, system biology, industrial applications and more [101, 88, 89, 39, 49]",
    ],
))

DB(Citation(
    huq2013b, gebser2012a, ref="[50]",
    contexts=[
        "While some attempts have been made to re-purpose ASP reasoners for streaming data [37], The current work by Gebser et al. [50] provides an all encompassing software solution to ASP-based stream reasoning.",

    ],
))

DB(Citation(
    huq2013b, gebser2012b, ref="[51]",
    contexts=[
        "In this chapter, we focus on scientiﬁc models with complex stream reasoning capabilities based on ASP, which can offer these reasoning capabilities along with pure declarativity in the problem speciﬁcation [51].",

    ],
))

DB(Citation(
    huq2013b, gebser2012c, ref="[52]",
    contexts=[
        "We argue that the general principle of this method can be extended to address other scripting and programming languages such as MATLAB12, R13, Answer Set Programming [52] etc.",
        "languages based on the stable model semantics, namely Answer Set Programming (ASP), has been intensively applied in the last decade to solve computationally hard problems [52].",
        "AnswerSetProgramming(ASP)[10,83,52]isapurelydeclarativeandnonmonotonic logic programming paradigm.",
        
    ],
))

DB(Citation(
    huq2013b, gedik2008a, ref="[53]",
    contexts=[
        "Gedik et al. proposed a large-scale, distributed data stream processing middleware, called System S [53].",

    ],
))

DB(Citation(
    huq2013b, gelfond1988a, ref="[54]",
    contexts=[
        "It applies “generate and test” approach, based on the stable model semantics [54] where solutions are representedbysetsofatoms(answersets)forwhichallrulesintheprogram are satisﬁed",

    ],
))

DB(Citation(
    huq2013b, gil2007b, ref="[55]",
    contexts=[
        "This approach is implemented in the Wings/Pegasus framework [ 34, 55].",

    ],
))

DB(Citation(
    huq2013b, glavic2009a, ref="[56]",
    contexts=[
        "On the other hand,in the eager approach, provenance information is propagated from one activities to another during execution of a scientiﬁc experiment [21, 15, 28, 60, 61, 56].",
        "In another work, Glavic et al. have proposed the Perm system (Provenance Extension of the Relational Model) which represents provenance as a relation containing both output tuples and contributing input tuples [56].",
        "Studies reported in [21, 28, 15, 61, 56] are annotation-based provenance capturing techniques",
        "Severalprovenancesolutionsindatabasesystemsaddresswhy-provenance [133, 30, 29, 56, 131, 109].",
        "Eager or annotation-based approaches [21, 131, 109, 28, 15, 60, 56, 46] documents provenance information explicitly which incurs a considerable amount of storage overhead for maintaining provenance data.",
        "Some of them also propagate provenance from one activity to the next one [21, 131, 60, 56, 58].",
        "Studies reported in [21, 131, 109, 28, 15, 60, 56, 46] are annotation-based approaches to collect provenance in the light of database systems.",
        "Existing annotation-based ﬁne-grained provenancecollectionsystems[21,131,109,28,15,60,56]documentsprovenance information explicitly which incurs a considerable amount of storage overhead for maintaining provenance data.",
        
    ],
))

DB(Citation(
    huq2013b, glavic2011a, ref="[57]",
    contexts=[
        "Glavic et al. presented several use cases that motivates the necessity of maintaining ﬁne-grained data provenance for streams as well as the study highlighted a few challenges to achieve such a framework [57].",

    ],
))

DB(Citation(
    huq2013b, glavic2012a, ref="[58]",
    contexts=[
        "Existing work documents ﬁne-grained data provenance explicitly in a database, also known as the annotation-based approach [21, 131, 109, 58, 108].",
        "Studies reported in [103, 129, 93, 40, 58, 108] proposed different mechanisms to manage ﬁne-grained data provenance for data streams. Next, we discuss these work in turn.",
        "Anotherworkreportedin[40,58]alsoaddressesﬁne-graineddataprovenance management for data streams.",
        "However, solutions reported in [103, 129, 58, 108] have to maintain persistent provenance information to some extent.",
        "Moreover, neither of these solutions [129, 58] consider the erratic nature of stream data processing",
        "Some of them also propagate provenance from one activity to the next one [21, 131, 60, 56, 58].",
        "Moreover, there exist some other work in the context of data streams which also document provenance assertions/information explicitly [103, 129, 58, 108].",
        "Several existing research facilitate this timestamp to express data dependencies between input and output data products in streams [129, 103, 109, 58, 108]",
        "Existing systems addressing ﬁne-grained data provenance for data streams [103, 129, 58, 108] maintain persistent provenance information and thus, incur a signiﬁcant storage overhead.",
    ],
))

DB(Citation(
    huq2013b, golab2003a, ref="[59]",
    contexts=[
        "In general, stream data processing engines handle massive amount of sensor data which are transmitted in form of a data stream - a real-time, continuous, ordered sequence of data products [59].",
        "As discussed in [8, 59], each data product in a stream is associated with a timestamp.",
    ],
))

DB(Citation(
    huq2013b, green2007b, ref="[60]",
    contexts=[
        "On the other hand,in the eager approach, provenance information is propagated from one activities to another during execution of a scientiﬁc experiment [21, 15, 28, 60, 61, 56].",
        "Authors described an application that applied the technique of provenance semirings in the context of collaborative data sharing in [60].",
        "Eager or annotation-based approaches [21, 131, 109, 28, 15, 60, 56, 46] documents provenance information explicitly which incurs a considerable amount of storage overhead for maintaining provenance data.",
        "Some of them also propagate provenance from one activity to the next one [21, 131, 60, 56, 58].",
        "Studies reported in [21, 131, 109, 28, 15, 60, 56, 46] are annotation-based approaches to collect provenance in the light of database systems.",
        "Existing annotation-based ﬁne-grained provenancecollectionsystems[21,131,109,28,15,60,56]documentsprovenance information explicitly which incurs a considerable amount of storage overhead for maintaining provenance data.",
        
    ],
))

DB(Citation(
    huq2013b, green2007a, ref="[61]",
    contexts=[
        "On the other hand,in the eager approach, provenance information is propagated from one activities to another during execution of a scientiﬁc experiment [21, 15, 28, 60, 61, 56].",
        "Green et al. have proposed another technique to capture provenance in database systems called provenance semirings [61].",
        "Studies reported in [21, 28, 15, 61, 56] are annotation-based provenance capturing techniques",
        "Another study conducted by Green et al. focuses on the need to understand how-provenance [61]",
        "In studies reported in [61, 23], authors have demonstrated their proposed provenance collection mechanisms in context of Datalog programs.",
    ],
))

DB(Citation(
    huq2013b, groth2007a, ref="[62]",
    contexts=[
        "Another study in the area of provenance-aware scientiﬁc workﬂow systems is Provenance Aware Service Oriented Architecture (PASOA) [62, 63].",

    ],
))

DB(Citation(
    huq2013b, groth2009a, ref="[63]",
    contexts=[
        "Another study in the area of provenance-aware scientiﬁc workﬂow systems is Provenance Aware Service Oriented Architecture (PASOA) [62, 63].",
        "Scientiﬁc workﬂow engines collect provenance at different levels of granularity-bothworkﬂowandﬁne-grainedprovenance[84,115,11,24,77,63].",
    ],
))

DB(Citation(
    huq2013b, groth2005a, ref="[64]",
    contexts=[
        "Since provenance data is ‘just’ metadata and less often used by end users, explicit documentation of ﬁne-grained provenanceseemstobeinfeasibleandtooexpensive[64,69].",
        "Therefore, the size of provenance data becomes a multiple of the size of the actual data stream. Since provenance data is another type of metadata and not frequently accessed by users, the explicit documentation of ﬁne-grained data provenance seems to be too expensive and infeasible [64, 69].",
        
    ],
))

DB(Citation(
    huq2013b, groth2005d, ref="[65]",
    contexts=[
        "Based on this idea, the Provenance Recording for Services (PReServ) [65] software package has been developed.",

    ],
))

DB(Citation(
    huq2013b, groth2012a, ref="[66]",
    contexts=[
        "In another studyconducted by Groth et al. [66], authors haveproposed a technique that can reconstruct provenance of the manipulations done over the data in a provenance-unaware platform like excel sheet or a programming tool like R.",
        "generic data processing tools, general-purpose programming languages etc.Studiesreportedin[90,66,113]captureprovenanceinformationfroma program developed in a provenance-unaware platform.",
        "Studies reported in [90, 113, 66] can extract provenance information from programs/scripts developed in different provenance-unaware environment such as Java, R, Microsoft Excel, respectively.",
    ],
))

DB(Citation(
    huq2013b, horwitz1992a, ref="[67]",
    contexts=[
        "A system dependence graph (SDG) extends the deﬁnition of a program dependence graph and it is capable of providing data and control dependences for multiprocedure programs [67].",
        "To transform the control dependencies into data dependencies in a conditional branching statement, we use the concept introduced in a program representation graph [67]. ",
    ],
))

DB(Citation(
    huq2013b, hull2006a, ref="[68]",
    contexts=[
        "In the life science domain, the Taverna project has developed a powerful, scalable tool for designing and executing bio-informatics workﬂows [102, 68]",
        "Furthermore, some of these scientiﬁc workﬂow engines are developed for a particular domain such as Taverna [102, 68] addresses bioinformatics workﬂows only.",
        "A few of them are also domainspeciﬁc [102, 68].",
        
    ],
))

DB(Citation(
    huq2013b, huq2010a, ref="[69]",
    contexts=[
        "Since provenance data is ‘just’ metadata and less often used by end users, explicit documentation of ﬁne-grained provenanceseemstobeinfeasibleandtooexpensive[64,69].",
        "We reported this storage problem of maintaining ﬁne-grained data provenance in one of our earlier [69].",
        "In one of our initial ideas [69], we have also reported the use of timestamps to establish dependencies between input and output data products, i.e., ﬁne-grained data provenance.",
        "Therefore, the size of provenance data becomes a multiple of the size of the actual data stream. Since provenance data is another type of metadata and not frequently accessed by users, the explicit documentation of ﬁne-grained data provenance seems to be too expensive and infeasible [64, 69].",
        
    ],
))

DB(Citation(
    huq2013b, huq2011b, ref="[70]",
    contexts=[
        "The input-output ratio [70] refers to the ratio between the numberofcontributinginputdataproductsproducingoutputtothenumberof produced output data products.",
        "It was decided that Yoshi (Y. Wada) would provide related source code of the scientiﬁc model alongside the input and output ﬁles (data products) of the model and Rezwan (M. R. Huq) would develop a prototype based on their work reported in [70, 71, 72] which could infer provenance information based on the given scientiﬁc model and available data products.",
        
    ],
))

DB(Citation(
    huq2013b, huq2012b, ref="[71]",
    contexts=[
        "It was decided that Yoshi (Y. Wada) would provide related source code of the scientiﬁc model alongside the input and output ﬁles (data products) of the model and Rezwan (M. R. Huq) would develop a prototype based on their work reported in [70, 71, 72] which could infer provenance information based on the given scientiﬁc model and available data products.",
        
    ],
))

DB(Citation(
    huq2013b, huq2012a, ref="[72]",
    contexts=[
        "It was decided that Yoshi (Y. Wada) would provide related source code of the scientiﬁc model alongside the input and output ﬁles (data products) of the model and Rezwan (M. R. Huq) would develop a prototype based on their work reported in [70, 71, 72] which could infer provenance information based on the given scientiﬁc model and available data products.",

    ],
))

DB(Citation(
    huq2013b, huq2013a, ref="[73]",
    contexts=[
        "We have also built a prototype that demonstrates the complete framework based on this use case [73].",
        "We have developed a prototype1 demonstrating the proposed framework [73]",
    ],
))

DB(Citation(
    huq2013b, ikeda2012a, ref="[74]",
    contexts=[
        "Another recent study [74] has shown that provenance information can be also used for debugging a scientiﬁc data processing model.",
        "Very recently, provenance information has been also used for debugging [74].",
        "Debugging is an emerging application of data provenance [74].",
        "Data provenance is often used for auditing and debugging of data intensive applications [114, 74].",
    ],
))


DB(Citation(
    huq2013b, jararweh2009a, ref="[75]",
    contexts=[
        "Several extensions of Kepler have been proposed and implemented to support provenance in different domains [75, 13]",
        "Jararweh et al. have exploited the open-source features of Kepler system and have created customized processing models in order to accelerate and automate the experimentsinecosystemsresearch[75]",
    ],
))

DB(Citation(
    huq2013b, kahn1974a, ref="[76]",
    contexts=[
        "A sequence of such ﬁrings is a particular type of a Kahn process network [76].",
        "A sequence of such ﬁrings is a particular type of Kahn processnetwork[76]",
    ],
))

DB(Citation(
    huq2013b, kim2008a, ref="[77]",
    contexts=[
        "Examples of the platforms where provenance awareness has been considered are scientiﬁc workﬂowenginessuchasTaverna[102],VisTrails[24],Kepler[84],Karma2 [116], Wings/Pegasus [77], stream data processing or complex event processing engines like SensorDataWeb 2, STREAM [8], Aurora [2], Borealis [3], or Esper3",
        "Kim et al. proposed another multi-layered provenance capturing mechanism in large-scale scientiﬁc workﬂow systems [77]",
        "Some of them proposed multi-layered provenance representation to allow users to deal with the complexity and large size of provenance information [115, 11, 24, 77].",
        "Scientiﬁc workﬂow engines collect provenance at different levels of granularity-bothworkﬂowandﬁne-grainedprovenance[84,115,11,24,77,63].",
        "There are existing tools and techniques that can extract workﬂow provenance of a scientiﬁc model [102, 84, 24, 116, 77]",
        
    ],
))

DB(Citation(
    huq2013b, klein2004a, ref="[78]",
    contexts=[
        "Most of these applications facilitate data fusion [78] which combines several sources of raw data to produce new data products.",

    ],
))

DB(Citation(
    huq2013b, koncilia2003a, ref="[79]",
    contexts=[
        "Further,wealsoassumethattherearethreesensorsmeasuring electrical conductivity in three different cells. Sensors send data tuples containing the device id, the latitude and the longitude of the device, the measured electrical conductivity, the timestamp of the measurement, also referred to as valid time [79], along with some other attributes.",
        "Therefore, a view Vi can be deﬁned as a set of tuples tji where j is the transaction time [79].",
        "Explicit System Timestamps - System timestamp, also referred to as transaction time [79], is added to every data product representing the point in time when the data product/tuple is inserted into the view.",
        "These sensors send data tuples containing the device id, the latitude and the longitude of the location, the measured electrical conductivity, the timestamp of the measurement, also referred to as valid time [79], along with some other attributes.",
        "A view Vi can be deﬁned as a set of tuples tji where j is the transaction time [79].",
        "These sensors send data tuples containing the device id, the latitude and the longitude of the location, the measured electrical conductivity, the timestamp of the measurement, also referred to as valid time [79], along with some other attributes.",
        "A view Vi can be deﬁned as a set of tuples tji where j is the transaction time [79].",
        
    ],
))

DB(Citation(
    huq2013b, lanter1991a, ref="[80]",
    contexts=[
        "Maintaining data provenance [20, 114], also known as lineage [80], allows scientists to achieve these requirements and thus, leading towards the development of the provenance-aware cyberinfrastructure.",
        "In GIS, data provenance is known aslineage which explicates the relationship among events and source data in generating the data product [80].",
        "In GIS, data provenance is known as lineage, which explicates the relationship among events and source data in constructing the data product [80]",
        
    ],
))

DB(Citation(
    huq2013b, ledlie2005a, ref="[81]",
    contexts=[
        "Another study conducted by Ledlie et al. have outlined the structure of a provenance-aware storage for sensor data [81].",
        "The work reported in [124, 125, 81] does not provide details about a provenance capturing framework that can maintain provenance at tuple level, i.e., ﬁne-grained data provenance, in a stream data processing environment.",
        
    ],
))

DB(Citation(
    huq2013b, lee1995a, ref="[82]",
    contexts=[
        "Lee et al. proposed a computational model, known as dataﬂow process networks, that can model stream based data processing approaches [82]",
        "The aforesaid semantics of the proposed workﬂow provenance model is quite similar to the computational model, known as dataﬂow process networks[82",
        
    ],
))

DB(Citation(
    huq2013b, lifschitz2002a, ref="[83]",
    contexts=[
        "AnswerSetProgramming(ASP)[10,83,52]isapurelydeclarativeandnonmonotonic logic programming paradigm.",

    ],
))

DB(Citation(
    huq2013b, ludascher2006a, ref="[84]",
    contexts=[
        "Examples of the platforms where provenance awareness has been considered are scientiﬁc workﬂowenginessuchasTaverna[102],VisTrails[24],Kepler[84],Karma2 [116], Wings/Pegasus [77], stream data processing or complex event processing engines like SensorDataWeb 2, STREAM [8], Aurora [2], Borealis [3], or Esper3",
        "A workﬂow management system (e.g. Kepler [84], Taverna [102], VisTrails [24]) deﬁnes and manages a series of activities within a scientiﬁc data intensive experiment to produce an output data product. In such systems, activities create a processing chain and each activity takes input data products from a previous activity, i.e., data-driven workﬂows.",
        "Kepler is a scientiﬁc workﬂow management system for designing, executing, reusing, evolving, archiving, and sharing scientiﬁc workﬂows [84].",
        "This framework is implemented on the top of Kepler workﬂow management systems [84], representing provenance of scientiﬁc workﬂows.",
        "Scientiﬁc workﬂow engines collect provenance at different levels of granularity-bothworkﬂowandﬁne-grainedprovenance[84,115,11,24,77,63].",
        "Theworkﬂowprovenanceofascientiﬁcmodelcaneitherbecreatedand stored by using provenance-aware workﬂow engines, stream processing engines, complex event processing engines [84, 116, 102, 24, 8, 2, 3] or be captured automatically as discussed in Chapter 3 in case the model is developed using a general purpose programming tool such as Python.",
        "There are existing tools and techniques that can extract workﬂow provenance of a scientiﬁc model [102, 84, 24, 116, 77]",
        
    ],
))

DB(Citation(
    huq2013b, ludascher2009a, ref="[85]",
    contexts=[
        "Business workﬂows are different from scientiﬁc workﬂows [85].",

    ],
))

DB(Citation(
    huq2013b, lynch1996a, ref="[86]",
    contexts=[
        "This paradigm is used in stream data processing and complex event processing engines as well as in models used in distributed systems research such as I/O automata [86].",
        
    ],
))

DB(Citation(
    huq2013b, mcphillips2006a, ref="[87]",
    contexts=[
        "In the area of scientiﬁc data management, authors proposed annotationbased provenance framework [87, 5].",

    ],
))

DB(Citation(
    huq2013b, mileo2011b, ref="[88]",
    contexts=[
        "The ability to deal with incomplete knowledge, conﬂicting and noisy input and common sense reasoning made ASP applicable to domains such as civil engineering, home healthcare, sensor networks, planning, bio-informatics, phylogenesis, system biology, industrial applications and more [101, 88, 89, 39, 49]",

    ],
))

DB(Citation(
    huq2013b, mileo2011a, ref="[89]",
    contexts=[
        "The ability to deal with incomplete knowledge, conﬂicting and noisy input and common sense reasoning made ASP applicable to domains such as civil engineering, home healthcare, sensor networks, planning, bio-informatics, phylogenesis, system biology, industrial applications and more [101, 88, 89, 39, 49]",

    ],
))

DB(Citation(
    huq2013b, miles2010a, ref="[90]",
    contexts=[
        "Miles et al. [90] have proposed a provenance collection mechanism by modifying the source code of a program automatically.",
        "generic data processing tools, general-purpose programming languages etc.Studiesreportedin[90,66,113]captureprovenanceinformationfroma program developed in a provenance-unaware platform.",
        "Studies reported in [90, 113, 66] can extract provenance information from programs/scripts developed in different provenance-unaware environment such as Java, R, Microsoft Excel, respectively.",
        
    ],
))


DB(Citation(
    huq2013b, miles2007a, ref="[91]",
    contexts=[
        "It becomes also useful for validating scientiﬁc models. Furthermore, provenance information can be facilitated to trace where data come from and for other auditing purposes [91].",

    ],
))

DB(Citation(
    huq2013b, miles2011a, ref="[92]",
    contexts=[
        "During the design phase, scientists deﬁne the model which is based on different activities, i.e., atomic units of work performed as a whole [1].",
        "Miles et al. have proposed a software engineering methodology, known as Provenance Incorporating Methodology (PrIMe) [92], that can adapt applications to make them provenance-aware by exposing application information documented through a series of steps and by modifying the application design.",
        
    ],
))

DB(Citation(
    huq2013b, misra2008a, ref="[93]",
    contexts=[
        "Studies reported in [103, 129, 93, 40, 58, 108] proposed different mechanisms to manage ﬁne-grained data provenance for data streams. Next, we discuss these work in turn.",
        "Later, Misra et al. have proposed an storage optimization technique [93] over the work described in [129].",
        
    ],
))

DB(Citation(
    huq2013b, moreau2010a, ref="[94]",
    contexts=[
        "Furthermore, several studies on provenance for stream data processing have been undertaken. Recently, Moreau has investigated provenance in the context of Web [94]",

    ],
))

DB(Citation(
    huq2013b, moreau2013a, ref="[95]",
    contexts=[
        "PROV-DM is the conceptual data model that forms a basis for the PROV family of speciﬁcations [95].",
        "The workﬂowprovenancemodelcanbeeasilyextendedtoadopttheprimitives deﬁned by PROV-DM [95].",
        
    ],
))

DB(Citation(
    huq2013b, moreau2008c, ref="[96]",
    contexts=[
        "The Open Provenance Model (OPM) [96, 98] is designed for supporting interoperability between provenance systems.",

    ],
))

DB(Citation(
    huq2013b, moreau2013a, ref="[97]",
    contexts=[
        "provenance information to be exchanged between systems, by means of a compatibility layer based on a shared provenance model proposed in [97].",
        
    ],
))

DB(Citation(
    huq2013b, moreau2011b, ref="[98]",
    contexts=[
        "The Open Provenance Model (OPM) [96, 98] is designed for supporting interoperability between provenance systems.",
        "These PROV-DM types are analogous to the nodes deﬁned in OPM [98].",
        
    ],
))

DB(Citation(
    huq2013b, muniswamy2006a, ref="[99]",
    contexts=[
        "This provenance collection technique is similar to the techniques that capture provenance at operating system level [99].",

    ],
))

DB(Citation(
    huq2013b, newman2003a, ref="[100]",
    contexts=[
        "Scientists from many domains such as physical, geological, environmental, biological etc. facilitate data intensive applications to study and better understand these complex systems [100].",
        
    ],
))

DB(Citation(
    huq2013b, novelli2012a, ref="[101]",
    contexts=[
        "The ability to deal with incomplete knowledge, conﬂicting and noisy input and common sense reasoning made ASP applicable to domains such as civil engineering, home healthcare, sensor networks, planning, bio-informatics, phylogenesis, system biology, industrial applications and more [101, 88, 89, 39, 49]",
        
    ],
))

DB(Citation(
    huq2013b, oinn2004a, ref="[102]",
    contexts=[
        "Examples of the platforms where provenance awareness has been considered are scientiﬁc workﬂowenginessuchasTaverna[102],VisTrails[24],Kepler[84],Karma2 [116], Wings/Pegasus [77], stream data processing or complex event processing engines like SensorDataWeb 2, STREAM [8], Aurora [2], Borealis [3], or Esper3",
        "A workﬂow management system (e.g. Kepler [84], Taverna [102], VisTrails [24]) deﬁnes and manages a series of activities within a scientiﬁc data intensive experiment to produce an output data product. In such systems, activities create a processing chain and each activity takes input data products from a previous activity, i.e., data-driven workﬂows.",
        "In the life science domain, the Taverna project has developed a powerful, scalable tool for designing and executing bio-informatics workﬂows [102, 68]",
        "Furthermore, some of these scientiﬁc workﬂow engines are developed for a particular domain such as Taverna [102, 68] addresses bioinformatics workﬂows only.",
        "A few of them are also domainspeciﬁc [102, 68].",
        "Theworkﬂowprovenanceofascientiﬁcmodelcaneitherbecreatedand stored by using provenance-aware workﬂow engines, stream processing engines, complex event processing engines [84, 116, 102, 24, 8, 2, 3] or be captured automatically as discussed in Chapter 3 in case the model is developed using a general purpose programming tool such as Python.",
        "There are existing tools and techniques that can extract workﬂow provenance of a scientiﬁc model [102, 84, 24, 116, 77]",
        
    ],
))

DB(Citation(
    huq2013b, park2008a, ref="[103]",
    contexts=[
        "Studies reported in [103, 129, 93, 40, 58, 108] proposed different mechanisms to manage ﬁne-grained data provenance for data streams. Next, we discuss these work in turn.",
        "Park et al. proposed an annotation-based approach, called tuple-level link, to document provenance of sensor data explicitly [103].",
        "However, solutions reported in [103, 129, 58, 108] have to maintain persistent provenance information to some extent.",
        "Moreover, there exist some other work in the context of data streams which also document provenance assertions/information explicitly [103, 129, 58, 108].",
        "Several existing research facilitate this timestamp to express data dependencies between input and output data products in streams [129, 103, 109, 58, 108]",
        "Existing approaches [103, 26, 109, 108] record ﬁne-grained data provenance explicitly in varying manners.",
        "In [103], authors propose to use transaction time on incoming stream data. Ensuring temporal ordering of data tuples is one of the main requirements in stream dataprocessing. Moreover,several studies [46, 116] have proposed to maintain process level provenance which correspond to the documentation of workﬂow provenance.",
        "Existing systems addressing ﬁne-grained data provenance for data streams [103, 129, 58, 108] maintain persistent provenance information and thus, incur a signiﬁcant storage overhead.",
        
    ],
))

DB(Citation(
    huq2013b, portmann2010a, ref="[104]",
    contexts=[
        "The scientiﬁc model combines irrigated areas, crop-related data and simulated potential and actual evaporation and transpiration, which are all processed at a 0.5◦ grid spatial resolution, i.e., 50 km by 50 km, and at a monthly temporal resolution. Irrigated areas are prescribed by the MIRCA2000 dataset [104] and the FAOSTAT database3",
        
    ],
))

DB(Citation(
    huq2013b, pothier2007a, ref="[105]",
    contexts=[
        "To overcome this drawback, Pothier et al. [105] have proposed a scalable omniscient debugger, called Trace-Oriented Debugger for Java (TOD), that makes it possible to navigate backwards in time within a program execution trace, drastically improving the task of debugging complex applications.",
        
    ],
))

DB(Citation(
    huq2013b, reddy2007a, ref="[106]",
    contexts=[
        "sensor data in sensornet systems [106] and therefore, it is difﬁcult to apply this technique for data streams in other domains.",
        
    ],
))

DB(Citation(
    huq2013b, rohwer2007a, ref="[107]",
    contexts=[
        "A map of countryspeciﬁc irrigation efﬁciency factors is also obtained from [107].",

    ],
))

DB(Citation(
    huq2013b, sansrimahachai2012a, ref="[108]",
    contexts=[
        "Existing work documents ﬁne-grained data provenance explicitly in a database, also known as the annotation-based approach [21, 131, 109, 58, 108].",
        "Studies reported in [103, 129, 93, 40, 58, 108] proposed different mechanisms to manage ﬁne-grained data provenance for data streams. Next, we discuss these work in turn.",
        "Recently, a study conducted by Sansrimahachai have proposed a solution to track ﬁne-grained data provenance for data streams [108].",
        "However, solutions reported in [103, 129, 58, 108] have to maintain persistent provenance information to some extent.",
        "The reverse mapping technique using stream ancestor functions presented in [108] explicitly documents the parameters associated with the processing (e.g. processing delay) in provenance assertions.",
        "Moreover, there exist some other work in the context of data streams which also document provenance assertions/information explicitly [103, 129, 58, 108].",
        "Several existing research facilitate this timestamp to express data dependencies between input and output data products in streams [129, 103, 109, 58, 108]",
        "In the study reported in [108], the author proposed to document processing delay explicitly as an additional attribute in output data products.",
        "Existing approaches [103, 26, 109, 108] record ﬁne-grained data provenance explicitly in varying manners.",
        "Existing systems addressing ﬁne-grained data provenance for data streams [103, 129, 58, 108] maintain persistent provenance information and thus, incur a signiﬁcant storage overhead.",
        
    ],
))

DB(Citation(
    huq2013b, sarma2010a, ref="[109]",
    contexts=[
        "Existing work documents ﬁne-grained data provenance explicitly in a database, also known as the annotation-based approach [21, 131, 109, 58, 108].",
        "To overcome the limitations of Trio project [131] addressing temporal data, Sarma et al. introduced LIVE [109], a complete DBMS, which can store relations with simple versioning capabilities.",
        "Severalprovenancesolutionsindatabasesystemsaddresswhy-provenance [133, 30, 29, 56, 131, 109].",
        "Eager or annotation-based approaches [21, 131, 109, 28, 15, 60, 56, 46] documents provenance information explicitly which incurs a considerable amount of storage overhead for maintaining provenance data.",
        "Studies reported in [21, 131, 109, 28, 15, 60, 56, 46] are annotation-based approaches to collect provenance in the light of database systems.",
        "Several existing research facilitate this timestamp to express data dependencies between input and output data products in streams [129, 103, 109, 58, 108]",
        "Existing approaches [103, 26, 109, 108] record ﬁne-grained data provenance explicitly in varying manners.",
        "Existing annotation-based ﬁne-grained provenancecollectionsystems[21,131,109,28,15,60,56]documentsprovenance information explicitly which incurs a considerable amount of storage overhead for maintaining provenance data.",
        
    ],
))

DB(Citation(
    huq2013b, schneider2011a, ref="[110]",
    contexts=[
        "One objective of the RECORD project is to study how river restoration affects water quality, both in the river itself and in the groundwater [110].",
        
    ],
))

DB(Citation(
    huq2013b, shields2007a, ref="[111]",
    contexts=[
        "The biggest challenge to make the framework generic in nature is to address different types of developing approach as, i.e., with or without facilitating any speciﬁc tools, as well as to address different types of coordination scheme within a model (e.g. data-ﬂow or control-ﬂow) [111].",
        "The second dimension of classifying scientiﬁc models is based on the underlying coordination approach of the model (e.g. data-ﬂow or controlﬂow) [111].",
        "Therefore, the coordination between different processing elements is data-ﬂow based [111] specifying that once a processing element is triggered, the processing element processes data products hold by single/multiple input views which are the output of the preceding processing elements.",
        "Someoftheseoperations/activities (e.g. assignment, arithmetic operations) exhibit data-ﬂow based coordination whereas the others exhibit control-ﬂow based coordination [111]",
        
    ],
))

DB(Citation(
    huq2013b, siebert2010a, ref="[112]",
    contexts=[
        "Crop factors, growing season lengths, and rooting depth are obtained from GCWM [112]",

    ],
))

DB(Citation(
    huq2013b, silles2010a, ref="[113]",
    contexts=[
        "In [113], authors proposed a variant of R interpreter, CXXR, which can maintain and represent collected provenance information.",
        "generic data processing tools, general-purpose programming languages etc.Studiesreportedin[90,66,113]captureprovenanceinformationfroma program developed in a provenance-unaware platform.",
        "Studies reported in [90, 113, 66] can extract provenance information from programs/scripts developed in different provenance-unaware environment such as Java, R, Microsoft Excel, respectively.",
        
    ],
))

DB(Citation(
    huq2013b, simmhan2005b, ref="[114]",
    contexts=[
        "Maintaining data provenance [20, 114], also known as lineage [80], allows scientists to achieve these requirements and thus, leading towards the development of the provenance-aware cyberinfrastructure.",
        "In a scientiﬁc workﬂow, data provenance refers to the derivation history of a data product starting from its origin [114]",
        "A lot of attention has been paid to design and develop provenance-aware platforms in scientiﬁc workﬂow systems as discussed in surveys conducted by Simmhan et al. [114] and Davidson et al. [32].",
        "Provenance information has been facilitated for a number of reasons [114].",
        "A study conducted by Simmhan et al. [114] narrated different applications of provenance information.",
        "Data provenance is often used for auditing and debugging of data intensive applications [114, 74].",
        
    ],
))

DB(Citation(
    huq2013b, simmhan2006b, ref="[115]",
    contexts=[
        "Karma2 provenance framework was developed to document provenance of data products produced by scientiﬁc workﬂows in a service-oriented architecture [115, 116].",
        "Some of them proposed multi-layered provenance representation to allow users to deal with the complexity and large size of provenance information [115, 11, 24, 77].",
        "Scientiﬁc workﬂow engines collect provenance at different levels of granularity-bothworkﬂowandﬁne-grainedprovenance[84,115,11,24,77,63].",
        
    ],
))

DB(Citation(
    huq2013b, simmhan2008a, ref="[116]",
    contexts=[
        "Examples of the platforms where provenance awareness has been considered are scientiﬁc workﬂowenginessuchasTaverna[102],VisTrails[24],Kepler[84],Karma2 [116], Wings/Pegasus [77], stream data processing or complex event processing engines like SensorDataWeb 2, STREAM [8], Aurora [2], Borealis [3], or Esper3",
        "Karma2 provenance framework was developed to document provenance of data products produced by scientiﬁc workﬂows in a service-oriented architecture [115, 116].",
        "Theworkﬂowprovenanceofascientiﬁcmodelcaneitherbecreatedand stored by using provenance-aware workﬂow engines, stream processing engines, complex event processing engines [84, 116, 102, 24, 8, 2, 3] or be captured automatically as discussed in Chapter 3 in case the model is developed using a general purpose programming tool such as Python.",
        "The explicated information of a computing processing element is quite similar to the process provenance reported in [116].",
        "In [103], authors propose to use transaction time on incoming stream data. Ensuring temporal ordering of data tuples is one of the main requirements in stream dataprocessing. Moreover,several studies [46, 116] have proposed to maintain process level provenance which correspond to the documentation of workﬂow provenance.",
        "There are existing tools and techniques that can extract workﬂow provenance of a scientiﬁc model [102, 84, 24, 116, 77]",
        
    ],
))

DB(Citation(
    huq2013b, stuckenschmidt2010a, ref="[117]",
    contexts=[
        "Stream processing and reasoning [36, 35, 117] are a relatively new area of research individuallyconcernedwithprocessinglargeamountsofdynamicallygenerated data.",
        
    ],
))

DB(Citation(
    huq2013b, szomszor2003a, ref="[118]",
    contexts=[
        "In large-scale computational systems like Grid and Web Services, Szomszor et al. have proposed a data model to provide infrastructure level support for a provenance recording capability [118].",
        
    ],
))

DB(Citation(
    huq2013b, tan2007a, ref="[119]",
    contexts=[
        "Provenance-aware platforms have been also built in the context of database systems as discussed in [119, 27].",
        
    ],
))

DB(Citation(
    huq2013b, beek2011a, ref="[120]",
    contexts=[
        "In addition, daily potential and actual bare soil evaporation and transpiration are prescribed from the simulation results from the global hydrological and water resources model PCR-GLOBWB [120].",

    ],
))

DB(Citation(
    huq2013b, dongen2005a, ref="[121]",
    contexts=[
        "These log ﬁles store detailed derivation history of processes, i.e., provenance of business processes. In this direction, van Dongen et al. proposed a meta model for event logs, represented as an XML format, called MXML [121].",

    ],
))

DB(Citation(
    huq2013b, dongen2005b, ref="[122]",
    contexts=[
        "Moreover, the same group of authors also developed the ProM framework [122], which is ﬂexible with respecttotheinputandoutputformatoflogﬁles,andisalsoopenenoughto allow for the easy reuse of code during the implementation of new process mining ideas.",

    ],
))

DB(Citation(
    huq2013b, vijayakumar2007a, ref="[123]",
    contexts=[
        "data streams by documenting the change in terms of rate and accuracy of the input streams [123]",

    ],
))

DB(Citation(
    huq2013b, vijayakumar2006a, ref="[124]",
    contexts=[
        "In this connection, a data model and architeture for capturing and collecting provenance by facilitating timestamps of change events has been proposed in [124, 125].",
        "The work reported in [124, 125, 81] does not provide details about a provenance capturing framework that can maintain provenance at tuple level, i.e., ﬁne-grained data provenance, in a stream data processing environment.",
        
    ],
))

DB(Citation(
    huq2013b, vijayakumar2007b, ref="[125]",
    contexts=[
        "In this connection, a data model and architeture for capturing and collecting provenance by facilitating timestamps of change events has been proposed in [124, 125].",
        "The work reported in [124, 125, 81] does not provide details about a provenance capturing framework that can maintain provenance at tuple level, i.e., ﬁne-grained data provenance, in a stream data processing environment.",
        
    ],
))

DB(Citation(
    huq2013b, wada2011b, ref="[126]",
    contexts=[
        "This water is vital when estimating renewable groundwater resources, which is used in subsequent studies [126].",

    ],
))

DB(Citation(
    huq2013b, wada2011a, ref="[127]",
    contexts=[
        "In this chapter, we present a case study which describes the process of applying the proposed inference-based framework over a scientiﬁc model that estimates the global water demand [127].",
        "Net irrigation water demand thus equals the sum of the differences between the potential and actual crop transpiration, and between the potential and actual bare soil evaporation which ensures maximum crop growth over the irrigated areas [127].",
        "The ﬁrst case study involves a scientiﬁc model for estimating the global water demand [127],",
        "In Chapter 8, we have presented a case study that demonstrates the viability of the proposed inference-based framework over a scientiﬁc model estimating global water demand [127], developed in Python programming language.",
        
    ],
))

DB(Citation(
    huq2013b, wada2012a, ref="[128]",
    contexts=[
        "Return ﬂow to groundwater is calculated by taking the minimum of irrigation losses, i.e., the difference between the gross and net irrigation water demand, and the unsaturated hydraulic conductivity of the bottom soil layer [128].",
        
    ],
))

DB(Citation(
    huq2013b, wang2007a, ref="[129]",
    contexts=[
        "Studies reported in [103, 129, 93, 40, 58, 108] proposed different mechanisms to manage ﬁne-grained data provenance for data streams. Next, we discuss these work in turn.",
        "Another study by Wang et al. argued that annotation-based approaches are not suitable for recording provenance in case of data streams because of the high storage overhead [129].",
        "Later, Misra et al. have proposed an storage optimization technique [93] over the work described in [129].",
        "However, solutions reported in [103, 129, 58, 108] have to maintain persistent provenance information to some extent.",
        "Moreover, neither of these solutions [129, 58] consider the erratic nature of stream data processing",
        "Moreover, there exist some other work in the context of data streams which also document provenance assertions/information explicitly [103, 129, 58, 108].",
        "Several existing research facilitate this timestamp to express data dependencies between input and output data products in streams [129, 103, 109, 58, 108]",
        "Existing systems addressing ﬁne-grained data provenance for data streams [103, 129, 58, 108] maintain persistent provenance information and thus, incur a signiﬁcant storage overhead.",
        
    ],
))

DB(Citation(
    huq2013b, weiser1984a, ref="[130]",
    contexts=[
        "code analyzer developed for C programming language. It also supports the concept of program slicing [130].",
        "It could be also possible to apply the concept of program slicing [130],",
        
    ],
))

DB(Citation(
    huq2013b, widom2004a, ref="[131]",
    contexts=[
        "Existing work documents ﬁne-grained data provenance explicitly in a database, also known as the annotation-based approach [21, 131, 109, 58, 108].",
        "Based on the work mentioned in [30, 29], Trio, a database system managing not only data but also the accuracy and the lineage of data is proposed in [131, 4].",
        "To overcome the limitations of Trio project [131] addressing temporal data, Sarma et al. introduced LIVE [109], a complete DBMS, which can store relations with simple versioning capabilities.",
        "Severalprovenancesolutionsindatabasesystemsaddresswhy-provenance [133, 30, 29, 56, 131, 109].",
        "Eager or annotation-based approaches [21, 131, 109, 28, 15, 60, 56, 46] documents provenance information explicitly which incurs a considerable amount of storage overhead for maintaining provenance data.",
        "Some of them also propagate provenance from one activity to the next one [21, 131, 60, 56, 58].",
        "Studies reported in [21, 131, 109, 28, 15, 60, 56, 46] are annotation-based approaches to collect provenance in the light of database systems.",
        "Existing annotation-based ﬁne-grained provenancecollectionsystems[21,131,109,28,15,60,56]documentsprovenance information explicitly which incurs a considerable amount of storage overhead for maintaining provenance data.",
        
    ],
))

DB(Citation(
    huq2013b, wombacher2010a, ref="[132]",
    contexts=[
        "Therefore,thefollowingproperties of a computing processing element must be documented during this phase based on the discussion in Section 3.1, Section 4.5 and a workﬂow model for continuous data [132].",
        
    ],
))

DB(Citation(
    huq2013b, woodruff1997a, ref="[133]",
    contexts=[
        "Why-provenance determines the input data tuples which contributed to produce an output data tuple. This type of provenance is studied in [133, 29].",
        "lazy approach and eager approach. In the lazy approach, provenance information is generated on demand based on a user request [133,29]",
        "Woodruff et al. [133] have proposed the notion of weak inversion and veriﬁcation to generate data lineage (provenance).",
        "Severalprovenancesolutionsindatabasesystemsaddresswhy-provenance [133, 30, 29, 56, 131, 109].",
        
    ],
))

DB(Citation(
    huq2013b, yin2013a, ref="[134]",
    contexts=[
        "A recent study [134] on debugging aspect-oriented programs has argued that some bugs in this programming paradigm could be difﬁcult to detect, since aspect-oriented source code elements and their locations could be transformed or even lost after compilation.",
        
    ],
))

DB(Citation(
    huq2013b, yue2009a, ref="[135]",
    contexts=[
        "A new generation of information infrastructure, known as cyberinfrastructure, is being developed to support these data intensive applications [135].",
        "In the context of the geoscientiﬁc domain, geospatial data provenance is deﬁned as the processing history of a geospatial data product [135].",
        
    ],
))

DB(Citation(
    huq2013b, yue2010a, ref="[136]",
    contexts=[
        "Yue et al. have proposed an approach to capture provenance data automatically using semantic web technologies [136].",
        
    ],
))

DB(Citation(
    huq2013b, yue2011b, ref="[137]",
    contexts=[
        "In another study, a provenance framework has been proposed for geoprocessing workﬂows [137].",
    ],
))

DB(Citation(
    huq2013b, yue2011a, ref="[138]",
    contexts=[
        "In [138], authors have reported an approach which enables interoperability for the collected provenance information in a service-oriented GIS architecture.",
        "In another study, Yue et al. have proposed to facilitate XML encoding to represent geospatial provenance data for better interoperability [138]",
        

    ],
))
