# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2000 import gansner2000a
from ..work.y2002 import brandes2002a
from ..work.y2008 import frew2008b
from ..work.y2008 import frew2008a
from ..work.y2008 import moreau2008b
from ..work.y2009 import simmhan2009a
from ..work.y2009 import simmhan2009b
from ..work.y2009 import reilly2009a
from ..work.y2009 import cruz2009a
from ..work.y2010 import graves2010a
from ..work.y2010 import miles2010a
from ..work.y2010 import glavic2010a
from ..work.y2010 import lyle2010a
from ..work.y2010 import moreau2010a
from ..work.y2011 import margo2011a
from ..work.y2012 import zhou2012a
from ..work.y2012 import janee2012a
from ..work.y2013 import conover2013a
from ..work.y2014 import zhou2014a

DB(Citation(
    frew2008b, frew2008a, ref="[1]",
    contexts=[
        "The Earth System Science Server (ES3) is a software environment for dataintensive Earth science. ES3 has unique capabilities for automatically and transparently capturing, managing, and reconstructing the provenance of arbitrary, unmodiﬁed computational sequences [1].",

    ],
))

DB(Citation(
    frew2008b, Site("The IDL Computing Environment for Data Visualization & Analysis from ITT", "http://www.ittvis.com/idl/"), ref="[2]",
    contexts=[
        "Relationshipsbetweenﬁlesandprocessesarededucedbymonitoringreadand write accesses. This monitoring can take place at the levels of system calls (using strace), library calls (using instrumented versions of application libraries), and arbitrarycheckpointswithinsourcecode(usingautomaticallyinvokedsource-tosourcepreprocessorsforspeciﬁcenvironmentssuchasIDL[2].)",

    ],
))

DB(Citation(
    frew2008b, brandes2002a, ref="[3]",
    contexts=[
        "The graphs are returned serialized in various XML formats (ES3 native, GraphML [3], etc.), and can be rendered visually by tools such as Graphviz [4] and yEd [5].",

    ],
))

DB(Citation(
    frew2008b, gansner2000a, ref="[4]",
    contexts=[
        "The graphs are returned serialized in various XML formats (ES3 native, GraphML [3], etc.), and can be rendered visually by tools such as Graphviz [4] and yEd [5].",

    ],
))

DB(Citation(
    frew2008b, Site("yEd - Java Graph Editor", "http://www.yworks.com/products/yed/"), ref="[5]",
    contexts=[
        "The graphs are returned serialized in various XML formats (ES3 native, GraphML [3], etc.), and can be rendered visually by tools such as Graphviz [4] and yEd [5].",

    ],
))

DB(Citation(
    frew2008b, moreau2008b, ref="[6]",
    contexts=[
        "TheﬁnalstepintheFirstProvenanceChallenge[6]workﬂowinvokesaprocedure convert that converts images from one format to another (Figure 2.)",

    ],
))

DB(Citation(
    frew2008b, Site("ImageMagick: Convert, Edit, and Compose Images", "http://www.imagemagick.org"), ref="[7]",
    contexts=[
        "These processes, correctly depicted as nested workﬂows, invoke the otherwise hidden command convertb with an otherwise hidden input ﬁle delegates.mgk (a conﬁguration ﬁle for the ImageMagick [7] software package.)",

    ],
))

DB(Citation(
    graves2010a, frew2008b, ref="",
    contexts=[

    ],
))



DB(Citation(
    zhou2014a, frew2008b, ref="",
    contexts=[

    ],
))

DB(Citation(
    zhou2012a, frew2008b, ref="",
    contexts=[

    ],
))

DB(Citation(
    janee2012a, frew2008b, ref="",
    contexts=[

    ],
))

DB(Citation(
    simmhan2009a, frew2008b, ref="",
    contexts=[

    ],
))

DB(Citation(
    margo2011a, frew2008b, ref="",
    contexts=[

    ],
))

DB(Citation(
    conover2013a, frew2008b, ref="",
    contexts=[

    ],
))

DB(Citation(
    miles2010a, frew2008b, ref="",
    contexts=[

    ],
))

DB(Citation(
    simmhan2009b, frew2008b, ref="",
    contexts=[

    ],
))

DB(Citation(
    glavic2010a, frew2008b, ref="",
    contexts=[

    ],
))

DB(Citation(
    reilly2009a, frew2008b, ref="",
    contexts=[

    ],
))

DB(Citation(
    lyle2010a, frew2008b, ref="",
    contexts=[

    ],
))

DB(Citation(
    cruz2009a, frew2008b, ref="",
    contexts=[

    ],
))

DB(Citation(
    moreau2010a, frew2008b, ref="",
    contexts=[

    ],
))
