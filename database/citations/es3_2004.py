# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2000 import barclay2000a
from ..work.y2001 import frew2001a
from ..work.y2001 import papadopoulos2001a
from ..work.y2001 import smith2001a
from ..work.y2002 import bose2002a
from ..work.y2002 import janee2002a
from ..work.y2004 import frew2004a
from ..work.y2008 import woollard2008a

DB(Citation(
    frew2004a, barclay2000a, ref="[1]",
    contexts=[
        "For these users, ES3 will support random access to selected data products through a Microsoft TerraServer interface [1].",

    ],
))

DB(Citation(
    frew2004a, bose2002a, ref="[2]",
    contexts=[
        "A unique feature of the Lab Notebook is its ability to capture and maintain lineage metadata [2], i.e. ancestordescendent relationships between processes and data streams that are absolutely critical for establishing the pedigree and credibility of investigator-generated data products.",

    ],
))

DB(Citation(
    frew2004a, frew2001a, ref="[3]",
    contexts=[
        "The metadata management component is the heart of ES3, keeping track of everything that happens in the system – external data objects imported, processes run, data objects created, and data products delivered. Metadata about all these activities are captured by the “Lab Notebook” (LN) subsystem [3] (Figure 1).",

    ],
))

DB(Citation(
    frew2004a, janee2002a, ref="[4]",
    contexts=[
        ". In addition to supporting the standard Federation FIND interfaces, ES3 includes the Alexandria Digital Earth Prototype (ADEPT) digital library middleware [4], which allows an ES3 system to function as a node in the Alexandria distributed geographic library [6].",

    ],
))

DB(Citation(
    frew2004a, papadopoulos2001a, ref="[5]",
    contexts=[
        "ES3 uses the NPACI Rocks software suite [5] to manage clusters of Linux processors. Processing environments (re-)created by the LN are submitted to the Rocks scheduler as batch jobs.",

    ],
))

DB(Citation(
    frew2004a, smith2001a, ref="[6]",
    contexts=[
        ". In addition to supporting the standard Federation FIND interfaces, ES3 includes the Alexandria Digital Earth Prototype (ADEPT) digital library middleware [4], which allows an ES3 system to function as a node in the Alexandria distributed geographic library [6].",

    ],
))

DB(Citation(
    woollard2008a, frew2004a, ref="",
    contexts=[

    ],
))
