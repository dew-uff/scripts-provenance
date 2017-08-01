# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2002 import foster2002a
from ..work.y2004 import deelman2004b
from ..work.y2004 import oinn2004a
from ..work.y2006 import callahan2006b
from ..work.y2006 import muniswamy2006a
from ..work.y2007 import taylor2007b
from ..work.y2008 import kuehn2008a
from ..work.y2008 import missier2008a
from ..work.y2009 import berthold2009a
from ..work.y2009 import clifford2009a
from ..work.y2009 import mcphillips2009a
from ..work.y2010 import guo2010a
from ..work.y2010 import angelino2010a
from ..work.y2010 import elkabany2010a
from ..work.y2010 import ikeda2010a
from ..work.y2010 import pan2010a
from ..work.y2010 import riley2010a
from ..work.y2010 import riley2010a
from ..work.y2010 import tapp2010a
from ..work.y2011 import macko2011a
from ..work.y2012 import boyd2012a
from ..work.y2013 import huq2013c
from ..work.y2016 import carvalho2016a
from ..work.y2016 import scaffidi2016a


DB(Citation(
    angelino2010a, tapp2010a, ref="[1]",
    contexts=[
        "In TaPP ’10 [1].",
        
    ],
))

DB(Citation(
    angelino2010a,
    Site("Epa frs facilities state combined csv filesdownload", "http://epa.gov/enviro/html/frsdemo/geospatialdata/geodatastatecombined.html"),
    ref="[2]",
    contexts=[
        "Suppose the user wants to download data from the U.S. Environmental Protection Agency about facilities or sites subject to environmental regulation [2].",
        
    ],
))

DB(Citation(
    angelino2010a, berthold2009a, ref="[3]",
    contexts=[
        "Workﬂow management systems also ask users to explicitly describe both information and control ﬂow; there are many in the scientiﬁc (e.g. Galaxy[26], GenePattern[16], Kepler[18], Knime[3], Pegasus[9], Taverna[22], Vistrails[4]) and business (e.g. clario[5],PentahoDataIntegration[8])communities.",
        
    ],
))

DB(Citation(
    angelino2010a, callahan2006b, ref="[4]",
    contexts=[
        "Workﬂow management systems also ask users to explicitly describe both information and control ﬂow; there are many in the scientiﬁc (e.g. Galaxy[26], GenePattern[16], Kepler[18], Knime[3], Pegasus[9], Taverna[22], Vistrails[4]) and business (e.g. clario[5],PentahoDataIntegration[8])communities.",
        
    ],
))

DB(Citation(
    angelino2010a,
    Site("clario Analytics", "http://clarioanalytics.com"),
    ref="[5]",
    contexts=[
        "Workﬂow management systems also ask users to explicitly describe both information and control ﬂow; there are many in the scientiﬁc (e.g. Galaxy[26], GenePattern[16], Kepler[18], Knime[3], Pegasus[9], Taverna[22], Vistrails[4]) and business (e.g. clario[5],PentahoDataIntegration[8])communities.",
        
    ],
))

DB(Citation(
    angelino2010a, clifford2009a, ref="[6]",
    contexts=[
        "The LinkList is stored on-disk in a serialized format. The LinkList can trivially be represented in a tabular format (CSV) or XML or RDF consistent with the Open Provenance Model (OPM) [6].",
        
    ],
))

DB(Citation(
    angelino2010a,
    Site("Azkaban", "http://sna-projects.com/azkaban/"),
    ref="[7]",
    contexts=[
        "Other workﬂow management solutions are speciﬁcally for distributed systems, such as Azkaban and Oozie for Apache Hadoop by LinkedIn and Yahoo!, respectively [7,15].",
        
    ],
))

DB(Citation(
    angelino2010a,
    Site("Kettle: Pentaho data integration", "http://kettle.pentaho.org"),
    ref="[8]",
    contexts=[
        "Workﬂow management systems also ask users to explicitly describe both information and control ﬂow; there are many in the scientiﬁc (e.g. Galaxy[26], GenePattern[16], Kepler[18], Knime[3], Pegasus[9], Taverna[22], Vistrails[4]) and business (e.g. clario[5],PentahoDataIntegration[8])communities.",
        
    ],
))

DB(Citation(
    angelino2010a, deelman2004b, ref="[9]",
    contexts=[
        "Workﬂow management systems also ask users to explicitly describe both information and control ﬂow; there are many in the scientiﬁc (e.g. Galaxy[26], GenePattern[16], Kepler[18], Knime[3], Pegasus[9], Taverna[22], Vistrails[4]) and business (e.g. clario[5],PentahoDataIntegration[8])communities.",
        
    ],
))


DB(Citation(
    angelino2010a, elkabany2010a, ref="[10]",
    contexts=[
        "Some tools, including PiCloud and pomsets, specialize in workﬂow management for cloud services, e.g., Amazon’s EC2 [10,23].",
        
    ],
))

DB(Citation(
    angelino2010a, foster2002a, ref="[11]",
    contexts=[
        "While the Chimera virtual data system is script-based, it requires use of a virtual data language (VDL) [11].",
        
    ],
))

DB(Citation(
    angelino2010a,
    Site("Eclipse c/c++ development tooling project", "http://www.eclipse.org/cdt"),
    ref="[12]",
    contexts=[
        "Eclipse’s C/C++ Development Tooling (CDT) IDE includes standard make build, plus a GUI for writing Makefiles and invoking make [12]",
        
    ],
))

DB(Citation(
    angelino2010a, guo2010a, ref="[13]",
    contexts=[
        "For example, provenance-aware storage systems (PASS) automatically track provenance at the level of ﬁles and processes dynamically at runtime [21], while IncPy is a modiﬁed Python interpreter that dynamically tracks ﬁle I/O and computational results at the level of function calls [13].",
        
    ],
))

DB(Citation(
    angelino2010a, ikeda2010a, ref="[14]",
    contexts=[
        "The Panda project is developing a formalism and algorithms for provenance-based refresh in data-oriented workﬂows [14].",
        
    ],
))

DB(Citation(
    angelino2010a,
    Site("Oozie", "http://yahoo.github.com/oozie/"),
    ref="[15]",
    contexts=[
        "Other workﬂow management solutions are speciﬁcally for distributed systems, such as Azkaban and Oozie for Apache Hadoop by LinkedIn and Yahoo!, respectively [7,15].",
        
    ],
))

DB(Citation(
    angelino2010a, kuehn2008a, ref="[16]",
    contexts=[
        "Workﬂow management systems also ask users to explicitly describe both information and control ﬂow; there are many in the scientiﬁc (e.g. Galaxy[26], GenePattern[16], Kepler[18], Knime[3], Pegasus[9], Taverna[22], Vistrails[4]) and business (e.g. clario[5],PentahoDataIntegration[8])communities.",
        
    ],
))

DB(Citation(
    angelino2010a,
    Site("Amazon elastic compute cloud (ec2)", "http://aws.amazon.com/ec2"),
    ref="[17]",
    contexts=[
        "We then use a grid scheduler to dispatch the parallel jobs on available machines. The next section shows how we have integrated StarFlow with Amazon’s Elastic Compute Cloud (EC2) [17] to perform automatically, parallelized web download and analysis.",
        
    ],
))

DB(Citation(
    angelino2010a, mcphillips2009a, ref="[18]",
    contexts=[
        "Workﬂow management systems also ask users to explicitly describe both information and control ﬂow; there are many in the scientiﬁc (e.g. Galaxy[26], GenePattern[16], Kepler[18], Knime[3], Pegasus[9], Taverna[22], Vistrails[4]) and business (e.g. clario[5],PentahoDataIntegration[8])communities.",
        "It is often a design goal of workﬂow management systems to support novices who do not want to write programs [18].",
        
    ],
))

DB(Citation(
    angelino2010a,
    Site("Mercurial", "Mercurial. http://mercurial.selenic.com"),
    ref="[19]",
    contexts=[
        "We will integrate StarFlow’s dependency tracking infrastructure with a version control system such as Mercurial [19].",
        
    ],
))

DB(Citation(
    angelino2010a, missier2008a, ref="[20]",
    contexts=[
        "For example, Taverna replaces a regular programming environment with a GUI for manipulating an XML-based ﬂow language, Scuﬂ [20]; users can also directly write in Scuﬂ to annotate dependencies",
        
    ],
))

DB(Citation(
    angelino2010a, muniswamy2006a, ref="[21]",
    contexts=[
        "For example, provenance-aware storage systems (PASS) automatically track provenance at the level of ﬁles and processes dynamically at runtime [21], while IncPy is a modiﬁed Python interpreter that dynamically tracks ﬁle I/O and computational results at the level of function calls [13].",
        
    ],
))

DB(Citation(
    angelino2010a, oinn2004a, ref="[22]",
    contexts=[
        "Workﬂow management systems also ask users to explicitly describe both information and control ﬂow; there are many in the scientiﬁc (e.g. Galaxy[26], GenePattern[16], Kepler[18], Knime[3], Pegasus[9], Taverna[22], Vistrails[4]) and business (e.g. clario[5],PentahoDataIntegration[8])communities.",
        
    ],
))

DB(Citation(
    angelino2010a, pan2010a, ref="[23]",
    contexts=[
        "Some tools, including PiCloud and pomsets, specialize in workﬂow management for cloud services, e.g., Amazon’s EC2 [10,23].",
        
    ],
))

DB(Citation(
    angelino2010a,
    Site("Gnu automake", "http://www.gnu.org/software/automake"),
    ref="[24]",
    contexts=[
        "Automake is another dynamic analysis tool that automates the construction of Makefiles [24].",
        
    ],
))

DB(Citation(
    angelino2010a, riley2010a, ref="[25]",
    contexts=[
        "Applying parallelization to abstract workﬂows. We combine StarFlow with StarCluster [25] to enable automatic parallelization of workﬂows in a high performance cloud setting",
        
    ],
))

DB(Citation(
    angelino2010a, taylor2007b, ref="[26]",
    contexts=[
        "Workﬂow management systems also ask users to explicitly describe both information and control ﬂow; there are many in the scientiﬁc (e.g. Galaxy[26], GenePattern[16], Kepler[18], Knime[3], Pegasus[9], Taverna[22], Vistrails[4]) and business (e.g. clario[5],PentahoDataIntegration[8])communities.",
        
    ],
))

DB(Citation(
    carvalho2016a, angelino2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    macko2011a, angelino2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    scaffidi2016a, angelino2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    boyd2012a, angelino2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    huq2013c, angelino2010a, ref="",
    contexts=[

    ],
))
