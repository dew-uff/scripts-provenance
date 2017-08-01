# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1997 import hines1997a
from ..work.y2007 import gewaltig2007a
from ..work.y2007 import perez2007a
from ..work.y2008 import curcin2008a
from ..work.y2008 import goodman2008a
from ..work.y2009 import bednar2009a
from ..work.y2009 import drummond2009a
from ..work.y2009 import nordlie2009a
from ..work.y2011 import freire2011a
from ..work.y2012 import davison2012a
from ..work.y2013 import stevens2013a
from ..work.y2013 import stevens2013b
from ..work.y2013 import antolik2013a
from ..work.y2013 import crook2013a
from ..work.y2014 import freire2014a
from ..work.y2014 import kubilius2014a
from ..work.y2014 import eglen2014a
from ..work.y2015 import stockton2015a
from ..work.y2015 import muller2015a
from ..work.y2015 import hjorth2015a
from ..work.y2016 import bezaire2016a
from ..work.y2016 import eglen2016a
from ..work.y2016 import mcdougal2016a


DB(Citation(
    stevens2013a, antolik2013a, ref="[Antolík and Davison, 2013]",
    contexts=[
        "The Mozaik framework (Antolík and Davison, 2013) is designed to encapsulate the workflows relevant to researchers who use spiking neural models",
        
    ],
))

DB(Citation(
    stevens2013a, bednar2009a, ref="(Bednar, 2009)",
    contexts=[
        "For instance, the Topographica project (Bednar, 2009) offers a sophisticated Command subclass in a file named lancext.py",
        
    ],
))

DB(Citation(
    stevens2013a, crook2013a, ref="(Crook et al., 2013)",
    contexts=[
        "The difficulties include problems replicating results between simulators (Crook et al., 2013) and insufficiently constrained model parameters in publications (Nordlie et al., 2009), along with an important debate about the distinction between replicability and reproducibility (Drummond, 2009; Freire et al., 2011).",
        
    ],
))


DB(Citation(
    stevens2013a, curcin2008a, ref="(Curcin and Ghanem, 2008)",
    contexts=[
        "This approach is in sharp contrast to more heavyweight automated scientific workflow systems (Curcin and Ghanem, 2008; Freire et al., 2014) that can be effective for mature research areas but would be constraining for this young and ever-changing field.",
        
    ],
)) 

DB(Citation(
    stevens2013a, davison2012a, ref="(Davison, 2012)",
    contexts=[
        "Lancet works well together with distributed version control systems like Git and Mercurial, or with management and tracking tools tailored towards scientific use, such as Sumatra (Davison, 2012).",
        "Projects like Sumatra (Davison 2012) take a far more general approach for achieving reproducibility, tailoring functionality offered by version controls to the needs of the scientist",
        
    ],
))

DB(Citation(
    stevens2013a, drummond2009a, ref="(Drummond, 2009)",
    contexts=[
        "The difficulties include problems replicating results between simulators (Crook et al., 2013) and insufficiently constrained model parameters in publications (Nordlie et al., 2009), along with an important debate about the distinction between replicability and reproducibility (Drummond, 2009; Freire et al., 2011).",
        
    ],
))

DB(Citation(
    stevens2013a, freire2011a, ref="(Freire et al., 2011)",
    contexts=[
        "The difficulties include problems replicating results between simulators (Crook et al., 2013) and insufficiently constrained model parameters in publications (Nordlie et al., 2009), along with an important debate about the distinction between replicability and reproducibility (Drummond, 2009; Freire et al., 2011).",
        "These more ambitious workflow engines are in regular use by large commercial organizations and research groups in some fields (Freire et al., 2011), but are not currently common in computational neuroscience.",
        
    ],
))

DB(Citation(
    stevens2013a, freire2014a, ref="(Freire et al., 2014)",
    contexts=[
        "This approach is in sharp contrast to more heavyweight automated scientific workflow systems (Curcin and Ghanem, 2008; Freire et al., 2014) that can be effective for mature research areas but would be constraining for this young and ever-changing field.",
        "VisTrails (Freire et al., 2014) is a scientific workflow and provenance system that integrates well with Python projects, taking a GUI-centric approach",
        
    ],
))

DB(Citation(
    stevens2013a, gewaltig2007a, ref="(Gewaltig and Diesmann, 2007)",
    contexts=[
        "There are many different simulators and analysis tools used in computational neuroscience, each constantly being developed and updated. Some popular neural simulators include Brian (Goodman and Brette, 2008), Neuron (Hines and Carnevale, 1997), and NEST (Gewaltig and Diesmann, 2007), each of which uses different custom command-line interfaces.",
        
    ],
))

DB(Citation(
    stevens2013a, goodman2008a, ref="(Goodman and Brette, 2008)",
    contexts=[
        "There are many different simulators and analysis tools used in computational neuroscience, each constantly being developed and updated. Some popular neural simulators include Brian (Goodman and Brette, 2008), Neuron (Hines and Carnevale, 1997), and NEST (Gewaltig and Diesmann, 2007), each of which uses different custom command-line interfaces.",
        
    ],
))

DB(Citation(
    stevens2013a, hines1997a, ref="(Hines and Carnevale, 1997)",
    contexts=[
        "There are many different simulators and analysis tools used in computational neuroscience, each constantly being developed and updated. Some popular neural simulators include Brian (Goodman and Brette, 2008), Neuron (Hines and Carnevale, 1997), and NEST (Gewaltig and Diesmann, 2007), each of which uses different custom command-line interfaces.",
        
    ],
))

DB(Citation(
    stevens2013a, nordlie2009a, ref="(Nordlie et al., 2009)",
    contexts=[
        "The difficulties include problems replicating results between simulators (Crook et al., 2013) and insufficiently constrained model parameters in publications (Nordlie et al., 2009), along with an important debate about the distinction between replicability and reproducibility (Drummond, 2009; Freire et al., 2011).",
        
    ],
))

DB(Citation(
    stevens2013a, perez2007a, ref="(Perez, 2007)",
    contexts=[
        "Since version 0.12 of IPython (Pérez and Granger, 2007), a notebook feature has been provided which allows code, data, and figures to be interactively explored while maintaining a complete record of the source code.",
        
    ],
))

DB(Citation(
    stevens2013a, stevens2013b, ref="(Stevens, 2013)",
    contexts=[
        "To demonstrate that this workflow is both practical and relevant to a real research project, we then briefly describe how it was used to generate all the results in Stevens et al. (2013), recently published in the Journal of Neuroscience",
        "The lancext.py code is sufficiently flexible to support day-to-day exploratory work using the simulator, and was used throughout the development of the results in Stevens et al. (2013).",
        "For this reason, to generate the final Figures in Stevens et al. (2013), a different approach was used—a small utility was written that allows SVG templates to be quickly authored in the Inkscape graphics editor.",
        "This utility then can then embed vector assets dynamically generated by Matplotlib to create the final, publication quality figure. At this stage, the notebook should embody a completely automated and reproducible workflow for published work, as illustrated by the final column of Figure 4 and demonstrated for Stevens et al. (2013).",
        "Figure 5 shows the full specification for a batch of Topographica simulations used in Stevens et al. (2013) in the form of a launcher repr.",
        "Figures 5 and 6 from Stevens et al. (2013).",
        "Calling this object without supplying any arguments in a cluster environment would relaunch the 21 Topographica simulations necessary to regenerate Figure 5 from Stevens et al. (2013).",
        "Note that the code listing in Figure 5 is only one of the launchers needed to reproduce all the Figures in Stevens et al. (2013).",
        "The IPython notebooks that fully and automatically reproduce Stevens et al. (2013) are publicly available from the GitHub repository of the Topographica project (www.topographica.org) in the models/stevens.jn13 directory (https://github.com/ioam/topographica/tree/master/models/stevens.jn13).",
        
    ],
))

DB(Citation(
    bezaire2016a, stevens2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    eglen2016a, stevens2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stockton2015a, stevens2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kubilius2014a, stevens2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mcdougal2016a, stevens2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    muller2015a, stevens2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hjorth2015a, stevens2013a, ref="",
    contexts=[

    ],
))

DB(Citation(
    eglen2014a, stevens2013a, ref="",
    contexts=[

    ],
))
