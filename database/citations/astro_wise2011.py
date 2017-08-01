# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1994 import jackson1994a
from ..work.y1995 import roddick1995a
from ..work.y2002 import wang2002a
from ..work.y2004 import apiwattanapong2004a
from ..work.y2005 import oliveira2005a
from ..work.y2005 import robbes2005a
from ..work.y2007 import valentijn2007a
from ..work.y2007 import jorgensen2007a
from ..work.y2008 import freire2008a
from ..work.y2009 import mwebaze2009a
from ..work.y2009 import ogasawara2009a
from ..work.y2010 import begeman2010a
from ..work.y2010 import moreau2010a
from ..work.y2011 import mwebaze2011a

DB(Citation(
    mwebaze2011a, apiwattanapong2004a, ref="[1]",
    contexts=[
        "To compare method nodes, we do not build an enhanced controlﬂow graph as work done in [1], we instead compare Python bytecodes.",
        "JDIFF [1], uses the OOP approach when comparing classes",
        
    ],
))

DB(Citation(
    mwebaze2011a, begeman2010a, ref="[2]",
    contexts=[
        "For example, Astro-WISE (AWE) [2], [12] provides scientists with an AWE environment and allows users to have their own code.",

    ],
))

DB(Citation(
    mwebaze2011a, freire2008a, ref="[3]",
    contexts=[
        "A scientist faces two principal obstacles when working with data: ﬁrstly, understanding the origins of data (i.e., data provenance [3], and secondly, understanding the differences between two data items (i.e., object versioning).",
        "Provenance systems [3] [6] do trace provenance by capturing and storing a complete trace of a data ﬂow.",
        
    ],
))

DB(Citation(
    mwebaze2011a, jackson1994a, ref="[4]",
    contexts=[
        "Semantic diff [4], compares two versions of a program procedure-by-procedure.",

    ],
))

DB(Citation(
    mwebaze2011a, jorgensen2007a, ref="[5]",
    contexts=[
        "Schema evolution and versioning [5] are other related concepts that deal with changes to classes.",

    ],
))

DB(Citation(
    mwebaze2011a, moreau2010a, ref="[6]",
    contexts=[
        "Provenance systems [3] [6] do trace provenance by capturing and storing a complete trace of a data ﬂow.",

    ],
))

DB(Citation(
    mwebaze2011a, mwebaze2009a, ref="[7]",
    contexts=[
        "Through COVA, the speciﬁc class (and/or source code) is known to the object, likewise the processing parameters which are maintained by data lineage can also be retrieved from work described in [7].",

    ],
))

DB(Citation(
    mwebaze2011a, ogasawara2009a, ref="[8]",
    contexts=[
        "At a coarse level, provenance systems refer to a ’a procedure x’ was run on ’data y’ [8] but at the lowest, scientists are also interested in knowing what changes in ’procedure x’ made data to appear the way it is.",

    ],
))

DB(Citation(
    mwebaze2011a, oliveira2005a, ref="[9]",
    contexts=[
        "However, these tools are limited in their ability to detect differences in programs because they provide purely textual differences [9].",
        "There is also considerable work related to Version Control Systems (VCSs) [9] [10], however their focus is dedicated on modeling software artifacts and therefore version numbers created by VCSs are opaque identiﬁers and as such can not be used for object versioning.",
        
    ],
))

DB(Citation(
    mwebaze2011a, robbes2005a, ref="[10]",
    contexts=[
        "There is also considerable work related to Version Control Systems (VCSs) [9] [10], however their focus is dedicated on modeling software artifacts and therefore version numbers created by VCSs are opaque identiﬁers and as such can not be used for object versioning.",

    ],
))

DB(Citation(
    mwebaze2011a, roddick1995a, ref="[11]",
    contexts=[
        "In order to let applications work on multiple schemata, schema versioning [11] is used.",

    ],
))

DB(Citation(
    mwebaze2011a, valentijn2007a, ref="[12]",
    contexts=[
        "For example, Astro-WISE (AWE) [2], [12] provides scientists with an AWE environment and allows users to have their own code.",

    ],
))

DB(Citation(
    mwebaze2011a, wang2002a, ref="[13]",
    contexts=[
        "BMAT [13] performs matching on both code and data blocks between two versions of a program in binary format, however it does not provide information about differences between matched entities.",

    ],
))
