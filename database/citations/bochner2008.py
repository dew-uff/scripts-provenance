# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1999 import dubois1999a
from ..work.y2002 import jackson2002a
from ..work.y2005 import jiang2005a
from ..work.y2006 import groth2006a
from ..work.y2006 import groth2006b
from ..work.y2006 import miles2006a
from ..work.y2006 import miles2006b
from ..work.y2006 import jiang2006a
from ..work.y2006 import munroe2006a
from ..work.y2007 import schlauch2007a
from ..work.y2008 import moreau2008a
from ..work.y2008 import bochner2008a
from ..work.y2009 import chen2009a
from ..work.y2011 import schreiber2011a
from ..work.y2012 import freire2012a
from ..work.y2015 import nascimento2015a
from ..work.y2016 import pimentel2016e


DB(Citation(
    bochner2008a, moreau2008a, ref="1",
    contexts=[
        "The recording and analysis of the provenance for data (i.e., a suitable documentation of the process that led to the data [1,2])",  
    ],
))

DB(Citation(
    bochner2008a, groth2006a, ref="2",
    contexts=[
        "The recording and analysis of the provenance for data (i.e., a suitable documentation of the process that led to the data [1,2])",
        "The recording and querying of data and the interaction between Provenance-aware applications and a provenance store rests upon the following definitions [2]",
        "As the current version of the Python CSL is a proof of concept, not all protocols and functions of the provenance architecture [2] are supported.",
    ],
))

DB(Citation(
    bochner2008a,
    DB(Site("The Python Website","http://www.python.org")),
    ref="3",
    contexts=[
        "As an example, in science and engineering the high-level programming language Python [3] is being used in more and more complex applications",
    ],
))

DB(Citation(
    bochner2008a,
    DB(Site("The AeroGrid Project Website","http://www.aero-grid.de")),
    ref="4",
    contexts=[
        "An example, where provenance-enabling Python applications is important is the German national D-Grid community project AeroGrid [4]",
    ],
))

DB(Citation(
    bochner2008a, schlauch2007a, ref="5",
    contexts=[
        "The main user interface in AeroGrid is the data management client DataFinder [5], a lightweight application software for managing technical and scientific data"
    ],
))

DB(Citation(
    bochner2008a, dubois1999a, ref="6",
    contexts=[
        "The advantages of Python for applications in science and engineering are manifold [6,7], but it is an important prerequisite that Python is a general-purpose programming language without any restrictions and available on any platform with an ANSI-C compiler",
    ],
))

DB(Citation(
    bochner2008a, jackson2002a, ref="7",
    contexts=[
        "The advantages of Python for applications in science and engineering are manifold [6,7], but it is an important prerequisite that Python is a general-purpose programming language without any restrictions and available on any platform with an ANSI-C compiler",
    ],
))

DB(Citation(
    bochner2008a,
    DB(Site("The EU Grid Provenance Website","http://www.gridprovenance.org")),
    ref="8",
    contexts=[
        "The rest of this paper presents a Python client library for recording and querying provenance information based on specifications developed in the EU Grid Provenance project [8]."
    ],
))

DB(Citation(
    bochner2008a, miles2006a, ref="9",
    contexts=[
        "After the provenance of a process is recorded and stored in a provenance store a querying actor can ask for this provenance by sending a provenance query request to a provenance query engine, which is typically implemented by the provenance store [9]",
        "Query protocol - Specifies the SOAP message communication between a querying actor and the the provenance store [9].",
    ],
))

DB(Citation(
    bochner2008a, jiang2005a, ref="10",
    contexts=[
        "A client-side library (CSL) is a collection of functions that allows applications to communicate with the services of the provenance store [10]",
    ],
))

DB(Citation(
    bochner2008a, groth2006b, ref="11",
    contexts=[
        "Process documentation recording protocol - Definies the SOAP message communication between a recording actor and the provenance store [11]).",
    ],
))

DB(Citation(
    bochner2008a, miles2006b, ref="12",
    contexts=[
        "XPath protocol - Definies the XPath-based profile of the provenance queries [12].",
    ],
))

DB(Citation(
    bochner2008a, munroe2006a, ref="13",
    contexts=[
        "Furthermore, the client-side library needs to communicate with the provenance store using a defined technology binding (like the SOAP binding defined in [13]).",
    ],
))

DB(Citation(
    bochner2008a,
    DB(Site("The PReServ Website","http://twiki.pasoa.ecs.soton.ac.uk/bin/view/PASOA/SoftWare")),
    ref="14",
    contexts=[
        "Currently prototype version 0.31 with WSDL 25 is available and used as reference store in this project [14].",
        "For querying the Provenance store currently the XQuery XML query language is supported, as defined in the PreServ XQuery interface [14].",
        "Current files enable the communication with the PReServ Provenance store [14] according to the defined WSDL files of version 0.25.",
    ],
))

DB(Citation(
    bochner2008a, jiang2006a, ref="15",
    contexts=[
        "As the PReServ comes with a Java client-side Library [15], this Java CSL was used as a first reference for the design and implementation of the Python CSL. Therefore both architectures are mainly based on a similar layered model [15].",
    ],
))

DB(Citation(
    bochner2008a,
    DB(Site("The Python Webservices Project Website (including ZSI)","http://pywebsvcs.sourceforge.net")),
    ref="16",
    contexts=[
        "The Zolera SOAP Infrastructure (ZSI) [16] is an implementation of SOAP version 1.1.",
    ],
))

DB(Citation(
    bochner2008a,
    DB(Site("The Python Enterprise Application Kit (PEAK) Website","http://peak.telecommunity.com")),
    ref="17",
    contexts=[
        "ThePythonEnterpriseApplication Toolkit (PEAK) [17] is a collection of Python modules which adds useful features for component based design to Python.",
    ],
))

DB(Citation(
    schreiber2011a, bochner2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    chen2009a, bochner2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    pimentel2016e, bochner2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    nascimento2015a, bochner2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    freire2012a, bochner2008a, ref="",
    contexts=[

    ],
))
