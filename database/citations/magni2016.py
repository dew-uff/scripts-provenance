# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1976 import mccabe1976a
from ..work.y1996 import mccabe1996a
from ..work.y2004 import oinn2004a
from ..work.y2005 import barni2005a
from ..work.y2006 import miller2006a
from ..work.y2007 import hunter2007a
from ..work.y2007 import oliphant2007a
from ..work.y2007 import silva2007a
from ..work.y2009 import eckel2009a
from ..work.y2009 import vandewalle2009b
from ..work.y2010 import pourmal2010a
from ..work.y2010 import mckinney2010a
from ..work.y2010 import merali2010a
from ..work.y2011 import editorial2011a
from ..work.y2011 import peng2011a
from ..work.y2011 import rupp2011a
from ..work.y2011 import walt2011a
from ..work.y2012 import begley2012a
from ..work.y2012 import davison2012a
from ..work.y2012 import gibson2012a
from ..work.y2012 import leveque2012a
from ..work.y2013 import ecma2013a
from ..work.y2013 import sandve2013a
from ..work.y2014 import hinsen2014a
from ..work.y2014 import oxvig2014a
from ..work.y2014 import stodden2014a
from ..work.y2014 import miguez2014a
from ..work.y2014 import wilson2014a
from ..work.y2015 import fomel2015a
from ..work.y2015 import hinsen2015a
from ..work.y2016 import oxvig2016a
from ..work.y2017 import oxvig2017a

DB(Citation(
    oxvig2016a, begley2012a, ref="[BE12]",
    contexts=[
        "Unfortunately, retractions of papers in high-ranked journals due to erroneous computations [Mil06] as well as a general lack of reproducibility of computational results [Mer10], with some studiesshowingthatonlyaround10%ofcomputationalresultsare reproducible [BE12], [RGPN+11], have led to a so-call credibility crisis in the computational sciences",
    ],
))

DB(Citation(
    oxvig2016a, barni2005a, ref="[BPG05]",
    contexts=[
        "The lack of reproducibility of computational results is oftentimes attributed to missing information about critical computational details such as library versions, parameter values, or precise descriptions of the exact code that was run [LMS12], [BPG05], [RGPN+11], [Mer10].",
    ],
))

DB(Citation(
    oxvig2016a, gibson2012a, ref="[CG12]",
    contexts=[
        "the experiment reproducible must be included with the textual presentation [RGPN+11], [CG12], [SLP14].",
        ". As pointed out in several studies [Fom15], [CG12], [VKV09], the author of the results gains as least as much in terms increasing one’s productivity.",
    ],
))

DB(Citation(
    oxvig2016a, davison2012a, ref="[Dav12]",
    contexts=[
        "Several communities have proposed best practices, rules, andtoolstohelpinmakingresultsreproducible,seee.g.[VKV09], [SNTH13], [SM14], [Dav12], [SLP14].",
        "Several studies have given best practices for how to detail such metadata to make computational results reproducible, see e.g. [VKV09], [SNTH13], [SM14], [Dav12].",
        "Several tools for keeping track of provenance and aiding in adhering to best practices for reproducible research already exist, e.g. Sumatra [Dav12], ActivePapers [Hin15], or Madagascar [Fom15].",
        "E.g. when using Sumatra, one would replace python my_experiment.py with [Dav12]",
        "For example, Sumatra by default stores all metadata in a SQLite database [Dav12] separate from simulation results (which may be stored in any format) whereas ActivePapers stores the metadata along with the results in an HDF5 database [Hin15].",
        "We have already discussed ActivePapers [Hin15], Sumatra [Dav12], and Madagascar [Fom15] which are general reproducibility frameworks that allow for wrapping most tools - not only Python based computation",
    ],
))

DB(Citation(
    oxvig2016a, ecma2013a, ref="[ECM13]",
    contexts=[
        ".Wesuggestusing JSON [ECM13] for serializing the metadata.",
    ],
))

DB(Citation(
    oxvig2016a, editorial2011a, ref="[Edi11]",
    contexts=[
        "Consequently, reproducibility of computational results have become a requirement for submission to many high-ranked journals [Edi11], [LMS12].",
    ],
))

DB(Citation(
    oxvig2016a, fomel2015a, ref="[Fom15]",
    contexts=[
        "Several tools for keeping track of provenance and aiding in adhering to best practices for reproducible research already exist, e.g. Sumatra [Dav12], ActivePapers [Hin15], or Madagascar [Fom15].",
        ". As pointed out in several studies [Fom15], [CG12], [VKV09], the author of the results gains as least as much in terms increasing one’s productivity.",
        "We have already discussed ActivePapers [Hin15], Sumatra [Dav12], and Madagascar [Fom15] which are general reproducibility frameworks that allow for wrapping most tools - not only Python based computation",
    ],
))

DB(Citation(
    oxvig2016a, pourmal2010a, ref="[FP10]",
    contexts=[
        "The HDF5 Hierarchical Data Format [FP10] is a great candidate for such a ﬁle format due to the availability of cross-platform viewers like HDFView3 and HDFCompass4 as well as its capabilities in terms of storing large datasets.",
    ],
))

DB(Citation(
    oxvig2016a, hinsen2014a, ref="[Hin14]",
    contexts=[
        "Most data scientists and researchers have probably asked this question at some point. For one to be able to answer the question, it is of utmost importance to track the provenance of the computational results by making the computational experiment reproducible, i.e. describing the experiment in such detail that it is possible for others to independently repeat it [LMS12], [Hin14].",
        "For our treatment of reproducibility of computational results, we adoptthemeaningofreproducibilityfrom[LMS12],[Hin14].",
        "As pointed out in [Hin14], reproducibility generally requires replicability.",
    ],
))

DB(Citation(
    oxvig2016a, hinsen2015a, ref="[Hin15]",
    contexts=[
        "Several tools for keeping track of provenance and aiding in adhering to best practices for reproducible research already exist, e.g. Sumatra [Dav12], ActivePapers [Hin15], or Madagascar [Fom15].",
        "For example, Sumatra by default stores all metadata in a SQLite database [Dav12] separate from simulation results (which may be stored in any format) whereas ActivePapers stores the metadata along with the results in an HDF5 database [Hin15].",
        "We have already discussed ActivePapers [Hin15], Sumatra [Dav12], and Madagascar [Fom15] which are general reproducibility frameworks that allow for wrapping most tools - not only Python based computation",
    ],
))

DB(Citation(
    oxvig2016a, hunter2007a, ref="[Hun07]",
    contexts=[
        "Matplotlib [Hun07] (Tested on version >= 1.3)",
    ],
))

DB(Citation(
    oxvig2016a, leveque2012a, ref="[LMS12]",
    contexts=[
        "Most data scientists and researchers have probably asked this question at some point. For one to be able to answer the question, it is of utmost importance to track the provenance of the computational results by making the computational experiment reproducible, i.e. describing the experiment in such detail that it is possible for others to independently repeat it [LMS12], [Hin14].",
        "Consequently, reproducibility of computational results have become a requirement for submission to many high-ranked journals [Edi11], [LMS12].",
        "For our treatment of reproducibility of computational results, we adoptthemeaningofreproducibilityfrom[LMS12],[Hin14].",
        "The lack of reproducibility of computational results is oftentimes attributed to missing information about critical computational details such as library versions, parameter values, or precise descriptions of the exact code that was run [LMS12], [BPG05], [RGPN+11], [Mer10].",
    ],
))

DB(Citation(
    oxvig2016a, mccabe1976a, ref="[McC76]",
    contexts=[
        "All code adheres to the PEP819 style guide and no function or class has a cyclomatic complexity [McC76], [WM96] exceeding 10.",
    ],
))

DB(Citation(
    oxvig2016a, mckinney2010a, ref="[McK10]",
    contexts=[
        "Furthermore, HDF5 is recognized in the scientiﬁc Python community5 with bindings available through e.g. PyTables6, h5py7, or Pandas [McK10]. Also, bindings for HDF5 exists in several other major programming languages.",
    ],
))

DB(Citation(
    oxvig2016a, merali2010a, ref="[Mer10]",
    contexts=[
        "Unfortunately, retractions of papers in high-ranked journals due to erroneous computations [Mil06] as well as a general lack of reproducibility of computational results [Mer10], with some studiesshowingthatonlyaround10%ofcomputationalresultsare reproducible [BE12], [RGPN+11], have led to a so-call credibility crisis in the computational sciences",
        "The lack of reproducibility of computational results is oftentimes attributed to missing information about critical computational details such as library versions, parameter values, or precise descriptions of the exact code that was run [LMS12], [BPG05], [RGPN+11], [Mer10].",
    ],
))

DB(Citation(
    oxvig2016a, miller2006a, ref="[Mil06]",
    contexts=[
        "Unfortunately, retractions of papers in high-ranked journals due to erroneous computations [Mil06] as well as a general lack of reproducibility of computational results [Mer10], with some studiesshowingthatonlyaround10%ofcomputationalresultsare reproducible [BE12], [RGPN+11], have led to a so-call credibility crisis in the computational sciences",
    ],
))

DB(Citation(
    oxvig2016a, oinn2004a, ref="[OAF+04]",
    contexts=[
        "Another category of related tools are graphical user interface (GUI) based workﬂow managing tools like Taverna [OAF+04] or Vistrail [SFC07].",
    ],
))

DB(Citation(
    oxvig2016a, oliphant2007a, ref="[Oli07]",
    contexts=[
        "SciPy [Oli07] (Tested on version >= 0.14)",
    ],
))

DB(Citation(
    oxvig2016a, oxvig2014a, ref="[OPA+14]",
    contexts=[
        "A reference implementation of the above suggested library design is available in the open source Magni Python package [OPA+14].",
        "More details about the quality assurance of magni are given in [OPA+14].",
    ],
))

DB(Citation(
    oxvig2016a, eckel2009a, ref="[PE09]",
    contexts=[
        "The idea of storing (or \"caching\") intermediate results and metadata along with the ﬁnal results has also been pursued in another study [PE09].",
    ],
))

DB(Citation(
    oxvig2016a, peng2011a, ref="[Pen11]",
    contexts=[
        "The answer has been a demand for requiring research to be reproducible [Pen11]",
    ],
))

DB(Citation(
    oxvig2016a, rupp2011a, ref="[RGPN+11]",
    contexts=[
        "Unfortunately, retractions of papers in high-ranked journals due to erroneous computations [Mil06] as well as a general lack of reproducibility of computational results [Mer10], with some studiesshowingthatonlyaround10%ofcomputationalresultsare reproducible [BE12], [RGPN+11], have led to a so-call credibility crisis in the computational sciences",
        "the experiment reproducible must be included with the textual presentation [RGPN+11], [CG12], [SLP14].",
        "The lack of reproducibility of computational results is oftentimes attributed to missing information about critical computational details such as library versions, parameter values, or precise descriptions of the exact code that was run [LMS12], [BPG05], [RGPN+11], [Mer10].",
    ],
))

DB(Citation(
    oxvig2016a, silva2007a, ref="[SFC07]",
    contexts=[
        "Another category of related tools are graphical user interface (GUI) based workﬂow managing tools like Taverna [OAF+04] or Vistrail [SFC07].",
    ],
))

DB(Citation(
    oxvig2016a, stodden2014a, ref="[SLP14]",
    contexts=[
        "the experiment reproducible must be included with the textual presentation [RGPN+11], [CG12], [SLP14].",
        "Several communities have proposed best practices, rules, andtoolstohelpinmakingresultsreproducible,seee.g.[VKV09], [SNTH13], [SM14], [Dav12], [SLP14].",
        "Some authors (e.g. [SLP14]) swap the meaning of reproducibility and replicability compared to the convention, we have adopted.",
    ],
))

DB(Citation(
    oxvig2016a, miguez2014a, ref="[SM14]",
    contexts=[
        "Several communities have proposed best practices, rules, andtoolstohelpinmakingresultsreproducible,seee.g.[VKV09], [SNTH13], [SM14], [Dav12], [SLP14].",
        "Several studies have given best practices for how to detail such metadata to make computational results reproducible, see e.g. [VKV09], [SNTH13], [SM14], [Dav12].",
        "We now give several smaller examples of how to use magni.reproducibility to implement the best practices for reproducibility of computational result described in [VKV09], [SNTH13], [SM14].",
    ],
))

DB(Citation(
    oxvig2016a, sandve2013a, ref="[SNTH13]",
    contexts=[
        "Several communities have proposed best practices, rules, andtoolstohelpinmakingresultsreproducible,seee.g.[VKV09], [SNTH13], [SM14], [Dav12], [SLP14].",
        "Several studies have given best practices for how to detail such metadata to make computational results reproducible, see e.g. [VKV09], [SNTH13], [SM14], [Dav12].",
        "We now give several smaller examples of how to use magni.reproducibility to implement the best practices for reproducibility of computational result described in [VKV09], [SNTH13], [SM14].",
    ],
))

DB(Citation(
    oxvig2016a, walt2011a, ref="[vdWCV11]",
    contexts=[
        "NumPy [vdWCV11] (Tested on version >= 1.8)",
    ],
))

DB(Citation(
    oxvig2016a, vandewalle2009b, ref="[VKV09]",
    contexts=[
        "Several communities have proposed best practices, rules, andtoolstohelpinmakingresultsreproducible,seee.g.[VKV09], [SNTH13], [SM14], [Dav12], [SLP14].",
        "Several studies have given best practices for how to detail such metadata to make computational results reproducible, see e.g. [VKV09], [SNTH13], [SM14], [Dav12].",
        "We now give several smaller examples of how to use magni.reproducibility to implement the best practices for reproducibility of computational result described in [VKV09], [SNTH13], [SM14].",
        ". As pointed out in several studies [Fom15], [CG12], [VKV09], the author of the results gains as least as much in terms increasing one’s productivity.",
    ],
))

DB(Citation(
    oxvig2016a, wilson2014a, ref="[WAB+14]",
    contexts=[
        "It has been developed using best practices for developing scientiﬁc software [WAB+14] and all code has been reviewed by at least one other person than its author prior to its inclusion in Magni",
    ],
))

DB(Citation(
    oxvig2016a, mccabe1996a, ref="[WM96]",
    contexts=[
        "All code adheres to the PEP819 style guide and no function or class has a cyclomatic complexity [McC76], [WM96] exceeding 10.",
    ],
))

DB(Citation(
    oxvig2017a, oxvig2016a, ref="",
    contexts=[

    ],
))
