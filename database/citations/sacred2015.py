# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1994 import gamma1994a
from ..work.y2012 import davison2012a
from ..work.y2012 import guo2012b
from ..work.y2012 import snoek2012a
from ..work.y2012 import vanschoren2012a
from ..work.y2013 import bergstra2013a
from ..work.y2014 import hutter2014a
from ..work.y2014 import smith2014a
from ..work.y2014 import vanschoren2014a
from ..work.y2015 import greff2015a
from ..work.y2015 import greff2015b

DB(Citation(
    greff2015a, bergstra2013a, ref="(Bergstra et al., 2013)",
    contexts=[
        "So with the next release (0.7) of Sacred we plan to ease integration of tools like spearmint (Snoek et al., 2012) and hyperopt (Bergstra et al., 2013) into the workﬂow.",

    ],
))

DB(Citation(
    greff2015a, davison2012a, ref="(Davison, 2012)",
    contexts=[
        "There are only a few projects that we are aware of that have a focus similar to Sacred with the closest one being Sumatra (Davison, 2012).",

    ],
))

DB(Citation(
    greff2015a, gamma1994a, ref="(Gamma et al., 1994)",
    contexts=[
        "Experiments implement the observer pattern (Gamma et al., 1994) by publishing all kinds of information in the form of events and allowing observers to subscribe to them",

    ],
))

DB(Citation(
    greff2015a, Site("Github. Sacred 0.6.3", "https://github.com/IDSIA/sacred/releases/tag/0.6.3"), ref="(Github, 2015)",
    contexts=[
        "The sourcecode was released under the MIT licence on Github (2015)",

    ],
))

DB(Citation(
    greff2015a, greff2015b, ref="(Greff et al., 2015)",
    contexts=[
        "In particular this feature has been very useful to perform large scale studies like the one in Gre↵ et al. (2015).",

    ],
))

DB(Citation(
    greff2015a, guo2012b, ref="(Guo, 2012)",
    contexts=[
        "The CDE project (Guo, 2012) takes a completely di↵erent and much more general approach to facilitate reproducible research.",

    ],
))

DB(Citation(
    greff2015a, hutter2014a, ref="(Hutter et al., 2014)",
    contexts=[
        "In the same vein it is necessary to include tools for analysing the importance of hyperparameters like the FANOVA framework of Hutter et al. (2014).",

    ],
))

DB(Citation(
    greff2015a, Site("Jobman. Welcome  jobman 0.1 documentation", "http://deeplearning.net/ software/jobman/"), ref="(Jobman, 2012)",
    contexts=[
        "Jobman (2012) is a python library that grew out of the need for scheduling lots of machine learning experiments.",

    ],
))

DB(Citation(
    greff2015a, Site("MongoDB. Mongodb, 2015", "https://www.mongodb.org/"), ref="(MongoDB, 2015)",
    contexts=[
        "MongoDB (2015) is a noSQL database, or more precisely a Document Database: It allows the storage of arbitrary JSON documents without the need for a schema like in a SQL database",

    ],
))

DB(Citation(
    greff2015a, smith2014a, ref="(Smith et al., 2014)",
    contexts=[
        "Experiment databases (Vanschoren et al., 2012; Smith et al., 2014) make an e↵ort to unify the storage of machine learning problems and experiments by expressing them in a common language",

    ],
))

DB(Citation(
    greff2015a, snoek2012a, ref="(Snoek et al., 2012)",
    contexts=[
        "So with the next release (0.7) of Sacred we plan to ease integration of tools like spearmint (Snoek et al., 2012) and hyperopt (Bergstra et al., 2013) into the workﬂow.",

    ],
))

DB(Citation(
    greff2015a, vanschoren2012a, ref="(Vanschoren et al., 2012)",
    contexts=[
        "Experiment databases (Vanschoren et al., 2012; Smith et al., 2014) make an e↵ort to unify the storage of machine learning problems and experiments by expressing them in a common language",

    ],
))

DB(Citation(
    greff2015a, vanschoren2014a, ref="(Vanschoren et al., 2014)",
    contexts=[
        "By standardizing that language they improve comparability and communicability of the results. The most wellknown example of might be the OpenML project Vanschoren et al. (2014)",

    ],
))
