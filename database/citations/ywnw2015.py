# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2006 import zhao2006a
from ..work.y2007 import perez2007a
from ..work.y2008 import freire2008a
from ..work.y2008 import biton2008a
from ..work.y2008 import bochner2008a
from ..work.y2008 import davidson2008a
from ..work.y2010 import lim2010a
from ..work.y2012 import davison2012a
from ..work.y2012 import dey2012a
from ..work.y2012 import tariq2012a
from ..work.y2013 import missier2013b
from ..work.y2013 import moreau2013a
from ..work.y2013 import alper2013a
from ..work.y2013 import huq2013a
from ..work.y2013 import xie2013a
from ..work.y2014 import alper2014a
from ..work.y2014 import cuevas2014a
from ..work.y2014 import dey2014a
from ..work.y2014 import ipaw2014a
from ..work.y2014 import murta2014a
from ..work.y2015 import mcphillips2015a
from ..work.y2015 import mcphillips2015b
from ..work.y2015 import dey2015a
from ..work.y2016 import ludascher2016a
from ..work.y2016 import carvalho2016a


DB(Citation(
    dey2015a, alper2013a, ref="[1]",
    contexts=[
        "Given a workflowspecification, they define reduction rules that exploit user-definedtags annotating the activities of the workflows and the input andoutput ports thereof, to produce a concise workflow specificationcontaining only the steps necessary for understanding the in silicoexperiment implemented by the initial workflow [1, 2].",
        
    ],
))

DB(Citation(
    dey2015a, alper2014a, ref="[2]",
    contexts=[
        "Given a workflowspecification, they define reduction rules that exploit user-definedtags annotating the activities of the workflows and the input andoutput ports thereof, to produce a concise workflow specificationcontaining only the steps necessary for understanding the in silicoexperiment implemented by the initial workflow [1, 2].",
        
    ],
)) 

DB(Citation(
    dey2015a, biton2008a, ref="[3]",
    contexts=[
        "Our work is related to the Zoom system proposed by Biton etal. which utilizes user views as abstractions for focusing the userattention on a subset of the provenance traces of a possibly largeworkflow by composing together subsets of the activities that constitutethe workflow [3].",
        
    ],
))

DB(Citation(
    dey2015a, bochner2008a, ref="[4]",
    contexts=[
        "To this end, several mechanisms have been recently proposed to capture the provenance traces of script execution[4,7,11,18].",
        "s. [4] relieson client libraries to capture traces of executions of scripts, whereas[20] make use of compilers that insert provenance capture withinthe script before and after function calls",
        
    ],
))


DB(Citation(
    dey2015a, cuevas2014a, ref="[5]",
    contexts=[
        "For workflows, the ProvONE model extendsthe PROV model to allow detail about the processes, ports, and datalinks [5].",
        
    ],
))

DB(Citation(
    dey2015a, davidson2008a, ref="[6]",
    contexts=[
        "Previous work describes how causality can be inferred usingboth prospective and retrospective provenance and discuss the benefitsof user-defined information, which is user annotation capturedat different level of granularities [6, 10].",
        
    ],
))

DB(Citation(
    dey2015a, davison2012a, ref="[7]",
    contexts=[
        "To this end, several mechanisms have been recently proposed to capture the provenance traces of script execution[4,7,11,18].",
        
    ],
))

DB(Citation(
    dey2015a, dey2014a, ref="[8]",
    contexts=[
        "In [8], we showed that prospective provenance can improvethe precision of retrospective provenance by reducing thenumber of “false” dependencies and conversely, fine-grained executionprovenance can be used to improve the precision of input output dependencies of workflow actors.",
        
    ],
))

DB(Citation(
    dey2015a, dey2012a, ref="[9]",
    contexts=[
        ". Inour earlier work [9], we showed that prospective and retrospectiveprovenance can be combined to provide unambigious lineagequerying.",
        
    ],
)) 

DB(Citation(
    dey2015a, freire2008a, ref="[10]",
    contexts=[
        "The importance of provenance in computational science is wellrecognized[10] and has led to provenance standards including theW3C PROV data model [17].",
        "Previous work describes how causality can be inferred usingboth prospective and retrospective provenance and discuss the benefitsof user-defined information, which is user annotation capturedat different level of granularities [6, 10].",
        
    ],
))

DB(Citation(
    dey2015a, huq2013a, ref="[11]",
    contexts=[
        "To this end, several mechanisms have been recently proposed to capture the provenance traces of script execution[4,7,11,18].",
        
    ],
))

DB(Citation(
    dey2015a, lim2010a, ref="[12]",
    contexts=[
        ". [12] extends the OpenProvenance Model (OPM) to model both prospective and retrospectiveprovenance.",
        
    ],
))

DB(Citation(
    dey2015a, ipaw2014a, ref="[13]",
    contexts=[
        "Labelflow:Exploiting workflow provenance to surface scientific data provenance.In Ludascher and Plale [ ¨ 13], pages 84–96",
    ],
))

DB(Citation(
    dey2015a, mcphillips2015b, ref="[14]",
    contexts=[
        "We also note that the work reported in this paperis related to another ongoing (and complementary) work [14] thataims to capture the provenance of data artifacts used and generatedwithin scripts and stored on the file system using YesWorkflow.",
        
    ],
))

DB(Citation(
    dey2015a, mcphillips2015a, ref="[15]",
    contexts=[
        "YesWorkflow [15] uses an annotation language, which is similarto Javadoc∗and Doxygen†, to generate workflow graphs thathelp users understand the building blocks (modules) that composethe script and their dataflow dependencies, a.k.a. prospective provenance.YesWorkflow is also related to the area of literate programming(e.g., Knitr [21] and IPython [19]).",
        
    ],
))

DB(Citation(
    dey2015a, missier2013b, ref="[16]",
    contexts=[
        "t. [16] extends W3CPROV to model both prospective and retrospective provenance",
        
    ],
)) 

DB(Citation(
    dey2015a, moreau2013a, ref="[17]",
    contexts=[
        "The importance of provenance in computational science is wellrecognized[10] and has led to provenance standards including theW3C PROV data model [17].",
        
    ],
))

DB(Citation(
    dey2015a, murta2014a, ref="[18]",
    contexts=[
        "To this end, several mechanisms have been recently proposed to capture the provenance traces of script execution[4,7,11,18].",
        "o capture provenance information for Python scripts [18].",
        "noWorkflow adopts a non-intrusive approach to capturing retrospectiveprovenance of scripts [18].",
        
    ],
))

DB(Citation(
    dey2015a, perez2007a, ref="[19]",
    contexts=[
        "YesWorkflow [15] uses an annotation language, which is similarto Javadoc∗and Doxygen†, to generate workflow graphs thathelp users understand the building blocks (modules) that composethe script and their dataflow dependencies, a.k.a. prospective provenance.YesWorkflow is also related to the area of literate programming(e.g., Knitr [21] and IPython [19]).",
        
    ],
))

DB(Citation(
    dey2015a, tariq2012a, ref="[20]",
    contexts=[
        "s. [4] relieson client libraries to capture traces of executions of scripts, whereas[20] make use of compilers that insert provenance capture withinthe script before and after function calls",
        
    ],
))

DB(Citation(
    dey2015a, xie2013a, ref="[21]",
    contexts=[
        "YesWorkflow [15] uses an annotation language, which is similarto Javadoc∗and Doxygen†, to generate workflow graphs thathelp users understand the building blocks (modules) that composethe script and their dataflow dependencies, a.k.a. prospective provenance.YesWorkflow is also related to the area of literate programming(e.g., Knitr [21] and IPython [19]).",
        
    ],
)) 

DB(Citation(
    dey2015a, zhao2006a, ref="[22]",
    contexts=[
        "Both prospective provenance (i.e.,the specification of the computation) and retrospective provenance(i.e., the exact steps followed during execution) contribute importantinformation [22].",
        "e. [22] argues that prospective and retrospectiveprovenance together provide a complete understanding of the data,illustrates a virtual data approach to integrating prospective andretrospective provenance with semantic annotations, describes thepowerful queries that can be performed on such an integrated base,and introduces an implementation that provides these benefits ina large-scale scientific computing environment. [",
        
    ],
))

DB(Citation(
    ludascher2016a, dey2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    carvalho2016a, dey2015a, ref="",
    contexts=[

    ],
))
