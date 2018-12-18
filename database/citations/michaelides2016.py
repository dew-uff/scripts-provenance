# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2006 import callahan2006b
from ..work.y2006 import ludascher2006a
from ..work.y2008 import freire2008a
from ..work.y2011 import moreau2011a
from ..work.y2011 import missier2011a
from ..work.y2011 import simmhan2011a
from ..work.y2012 import fraser2012a
from ..work.y2012 import yang2012a
from ..work.y2013 import chirigati2013a
from ..work.y2013 import missier2013b
from ..work.y2013 import moreau2013a
from ..work.y2013 import wolstencroft2013a
from ..work.y2014 import michaelides2014a
from ..work.y2014 import murta2014a
from ..work.y2014 import stodden2014a
from ..work.y2015 import mcphillips2015a
from ..work.y2016 import michaelides2016a
from ..work.y2016 import correndo2016a
from ..work.y2017 import correndo2017a
from ..work.y2018 import moreau2018a
from ..work.y2018 import lerner2018a
from ..work.y2018 import moreau2018b


DB(Citation(
    michaelides2016a, stodden2014a, ref="[1]",
    contexts=[
        "Reproducibility of scientific results is a key challenge to the modern scientist[1].",
        
    ],
))

DB(Citation(
    michaelides2016a, yang2012a, ref="[2]",
    contexts=[
        "The tool suite consists of a Web frontendto statistical processes, a command line interface and a dynamic documentsystem, whereby interactive computations can be embedded in a document[2].",
        
    ],
))

DB(Citation(
    michaelides2016a, wolstencroft2013a, ref="[3]",
    contexts=[
        "Many scientific workflow tools, such as Taverna[3], Kepler[4] and VisTrails[5],are monolithic “integrated development environments”.",
        "Taverna[3] collects retrospective provenance foruse internally with in its workbench and provides export in the form of PROVO",
        
    ],
))

DB(Citation(
    michaelides2016a, ludascher2006a, ref="[4]",
    contexts=[
        "Many scientific workflow tools, such as Taverna[3], Kepler[4] and VisTrails[5],are monolithic “integrated development environments”.",
        
    ],
))

DB(Citation(
    michaelides2016a, callahan2006b, ref="[5]",
    contexts=[
        "Many scientific workflow tools, such as Taverna[3], Kepler[4] and VisTrails[5],are monolithic “integrated development environments”.",
        "VisTrails[5] uses an SQLdatabase for storage of retrospective provenance and an XML serialization forstoring prospective provenance",
        
    ],
)) 

DB(Citation(
    michaelides2016a, mcphillips2015a, ref="[6]",
    contexts=[
        "Our approach is more akin toYesWorkflow[6] allowing multiple tools to be used in the scientific processes.",
        "YesWorkflow[6]provides script authors with an annotation mechanism to describe prospectiveprovenance.",
        
    ],
))

DB(Citation(
    michaelides2016a, chirigati2013a, ref="[7]",
    contexts=[
        "Furthermore, reproducibility is a key direction of development for many work-flow tools. For example, ReproZip[7] enables reproducible experiments by monitoringcommand-line executions and packaging required resources into a single,distributable package.",
        
    ],
))

DB(Citation(
    michaelides2016a, moreau2011a, ref="[8]",
    contexts=[
        "In that context, Moreau[8] sees provenance as a “program”, which when interpreted,can reproduce results.",
        
    ],
)) 

DB(Citation(
    michaelides2016a, fraser2012a, ref="[9]",
    contexts=[
        "StatJR uses the Blockly visual programming system[9]",
        
    ],
))

DB(Citation(
    michaelides2016a, missier2013b, ref="[10]",
    contexts=[
        ". For example, D-PROV[10]introduces extensions to PROV to express structural features in typical dataflowmodels",
        
    ],
))

DB(Citation(
    michaelides2016a, michaelides2014a, ref="[11]",
    contexts=[
        "The PROV-Template system[11] allows the generation of PROV[12] documentsby combining a template with a binding",
        
    ],
))

DB(Citation(
    michaelides2016a, moreau2013a, ref="[12]",
    contexts=[
        "The PROV-Template system[11] allows the generation of PROV[12] documentsby combining a template with a binding",
        ". In PROV-Template, attributes in the tmpl namespace map to specificelements in PROV-DM[12] where the typing does not allow a Qualified Name,for example the attribute tmpl:startTime on an Activity corresponds to the activity’sstart time.",
        
        
    ],
))

DB(Citation(
    michaelides2016a, freire2008a, ref="[13]",
    contexts=[
        "Many scientific workflow systems capture provenance[13] with a distinction madebetween prospective and retrospective provenance.",
        
    ],
))

DB(Citation(
    michaelides2016a, murta2014a, ref="[14]",
    contexts=[
        "The noWorkflow system[14] captures provenance information from scriptswithout the need to instrument them",
        
    ],
))

DB(Citation(
    michaelides2016a, simmhan2011a, ref="[15]",
    contexts=[
        "Converting workflow traces back into valid workflows was the subject of thethird Provenance Challenge[15].",
    ],
)) 

DB(Citation(
    michaelides2016a, missier2011a, ref="[16]",
    contexts=[
        "To guarantee losslessness in the conversion fromOPM back into a valid Taverna workflows additional annotations are needed[16].",
        
    ],
))

DB(Citation(
    moreau2018a, michaelides2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    correndo2017a, michaelides2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lerner2018a, michaelides2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    correndo2016a, michaelides2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    moreau2018b, michaelides2016a, ref="",
    contexts=[

    ],
))
