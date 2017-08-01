# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1984 import knuth1984a
from ..work.y2004 import gentleman2004a
from ..work.y2004 import oinn2004a
from ..work.y2005 import bavoil2005a
from ..work.y2006 import muniswamy2006a
from ..work.y2006 import ludascher2006a
from ..work.y2007 import perez2007a
from ..work.y2008 import bochner2008a
from ..work.y2008 import clifford2008a
from ..work.y2008 import davidson2008a
from ..work.y2008 import frew2008a
from ..work.y2008 import heidorn2008a
from ..work.y2010 import goecks2010a
from ..work.y2010 import lim2010a
from ..work.y2010 import mcphillips2010a
from ..work.y2010 import zinn2010a
from ..work.y2011 import gavish2011a
from ..work.y2012 import bowers2012a
from ..work.y2012 import guo2012a
from ..work.y2012 import bieda2012a
from ..work.y2012 import davison2012a
from ..work.y2012 import dou2012a
from ..work.y2012 import pham2012a
from ..work.y2012 import stropp2012a
from ..work.y2012 import tariq2012a
from ..work.y2012 import zundert2012a
from ..work.y2013 import moreau2013a
from ..work.y2013 import huntzinger2013a
from ..work.y2013 import huq2013a
from ..work.y2013 import tsai2013a
from ..work.y2013 import wallis2013a
from ..work.y2013 import xie2013a
from ..work.y2014 import bocinsky2014a
from ..work.y2014 import hanken2014a
from ..work.y2014 import lerner2014a
from ..work.y2014 import murta2014a
from ..work.y2014 import stodden2014a
from ..work.y2015 import mcphillips2015a
from ..work.y2015 import cuevas2015a
from ..work.y2015 import padhy2015a
from ..work.y2015 import nascimento2015a
from ..work.y2016 import jones2016a
from ..work.y2016 import thanos2016a
from ..work.y2016 import cao2016a
from ..work.y2016 import gammack2016a
from ..work.y2016 import bennett2016a
from ..work.y2016 import erickson2016a
from ..work.y2016 import cao2016b
from ..work.y2016 import schreiber2016a
from ..work.y2016 import thavasimani2016a
from ..work.y2016 import carvalho2016a
from ..work.y2016 import moehrke2016a
from ..work.y2017 import samuel2017a
from ..work.y2017 import bastos2017a
from ..work.y2017 import reimann2017a

DB(Citation(
    mcphillips2015a, bavoil2005a, ref="[BCC + 05]",
    contexts=[
        "One advantage of using scientificworkflow systems (e.g., Galaxy [GNT10], Kepler [LAB+06], Taverna [OAF+04],VisTrails [BCC+05], RestFlow [MM10, TMnG+13]) is that they often include capabilitiesto track data as it is being processed.",
        
    ],
))

DB(Citation(
    mcphillips2015a, bochner2008a, ref="[BGS08]",
    contexts=[
        "Some tools [BGS08, Dav12, HAW13, MBC+14] have been developed to capture runtimeprovenance for Python scripts: while Bochner et al. [BGS08] and Davison [Dav12] proposePython libraries and APIs that need to be added to the code to capture the executionsteps, ProvenanceCurious [HAW13] and noWorkflow [MBC+14] are transparent and donot require changes to the scripts.",
        
    ],
))

DB(Citation(
    mcphillips2015a, bieda2012a, ref="[Bie12]",
    contexts=[
        "In addition, analysis of even asingle bioinformatics dataset tends to yield a large number of different output files.Hence, bioinformatics pipelines are attractive candidates for workflow systems, whichcan capture this complexity [Bie12]",
        
    ],
)) 


DB(Citation(
    mcphillips2015a, bocinsky2014a, ref="[BK14]",
    contexts=[
        "As another working example from a different field, we have used the YesWorkflow markupsyntax to analyze the paleoclimate reconstruction workflow presented by Bocinsky andKohler [BK14].",
        
    ],
)) 

DB(Citation(
    mcphillips2015a, bowers2012a, ref="[BML12]",
    contexts=[
        "We additionally foresee that combining the information extracted from a markedupscript with references to data files corresponding to a run of that script will in somecases allow the retrospective provenance of those files to be inferred (see also [BML12]and [ZL10]).",
        
    ],
))

DB(Citation(
    mcphillips2015a, clifford2008a, ref="[CFV + 08]",
    contexts=[
        "The data provenance captured by workflow environments is sometimes called retrospectiveprovenance to distinguish it from another form called prospective provenance[CFV+08, LLCF10].",
        
    ],
))

DB(Citation(
    mcphillips2015a, cuevas2015a, ref="[CVLM + 15]",
    contexts=[
        "Similarly, to improve YW interoperabilitywithin the DataONE infrastructure, PROV [MM13] and ProvONE [CVLM+15] compatiblevocabulary extensions may be used in YesWorkflow in the future.",
        
    ],
)) 

DB(Citation(
    mcphillips2015a, davison2012a, ref="[Dav12]",
    contexts=[
        "Some tools [BGS08, Dav12, HAW13, MBC+14] have been developed to capture runtimeprovenance for Python scripts: while Bochner et al. [BGS08] and Davison [Dav12] proposePython libraries and APIs that need to be added to the code to capture the executionsteps, ProvenanceCurious [HAW13] and noWorkflow [MBC+14] are transparent and donot require changes to the scripts.",
        
    ],
))

DB(Citation(
    mcphillips2015a, dou2012a, ref="[DCM + 12]",
    contexts=[
        "In addition to the widespread use in the naturalsciences, computational automation tools are also increasingly used in other domains,e.g., for data mining workflows in the digital humanities [VZ12], or to implement datacuration workflows for natural history collections [DCM+12].",
        
    ],
)) 

DB(Citation(
    mcphillips2015a, davidson2008a, ref="[DF08]",
    contexts=[
        "The former consists of data dependencies and lineage informationrecorded at runtime, which can then be used later for retrospective exploration andanalysis (a.k.a. “querying provenance” [DF08]).",
        
    ],
))

DB(Citation(
    mcphillips2015a, frew2008a, ref="[FMS08]",
    contexts=[
        "Mechanismsthat capture provenance at the operating system level [FMS08, GS12, MRHBS06]monitor system calls to track the data dependencies between computational processes",
        
    ],
))

DB(Citation(
    mcphillips2015a, gentleman2004a, ref="[GCB + 04]",
    contexts=[
        "The Rscript employs a set of standard BioConductor [GCB+04] packages mixed with customprogramming",
        
    ],
)) 

DB(Citation(
    mcphillips2015a, gavish2011a, ref="[GD11]",
    contexts=[
        "Gavish and Donoho [GD11] present the notion of a Verifiable ComputationalResult (VCR), where every result is assigned a unique identifier, and results producedunder the exact same conditions have the same identifier to support reproducibility",
        
    ],
))

DB(Citation(
    mcphillips2015a, goecks2010a, ref="[GNT10]",
    contexts=[
        "One advantage of using scientificworkflow systems (e.g., Galaxy [GNT10], Kepler [LAB+06], Taverna [OAF+04],VisTrails [BCC+05], RestFlow [MM10, TMnG+13]) is that they often include capabilitiesto track data as it is being processed.",
        
    ],
))

DB(Citation(
    mcphillips2015a, guo2012a, ref="[GS12]",
    contexts=[
        "Mechanismsthat capture provenance at the operating system level [FMS08, GS12, MRHBS06]monitor system calls to track the data dependencies between computational processes",
        
    ],
))

DB(Citation(
    mcphillips2015a, huq2013a, ref="[HAW13]",
    contexts=[
        "Some tools [BGS08, Dav12, HAW13, MBC+14] have been developed to capture runtimeprovenance for Python scripts: while Bochner et al. [BGS08] and Davison [Dav12] proposePython libraries and APIs that need to be added to the code to capture the executionsteps, ProvenanceCurious [HAW13] and noWorkflow [MBC+14] are transparent and donot require changes to the scripts.",
        
    ],
))

DB(Citation(
    mcphillips2015a, heidorn2008a, ref="[Hei08]",
    contexts=[
        "This is true in particular forthe “long tail of science” [WRB13, Hei08], where advanced features such as provenancesupport are rarely available",
        
    ],
)) 

DB(Citation(
    mcphillips2015a, hanken2014a, ref="[HLM14]",
    contexts=[
        "In the Kurator project [HLM14] we plan to enable collection managers to author theirown data curation workflows using both an Akka-based workflow system and via scriptinglanguages such as Python and R. In the latter case, Kurator tool users will annotate theirscripts with YW comments to enable provenance queries to span script-based curationworkflows.",
        
    ],
))

DB(Citation(
    mcphillips2015a, huntzinger2013a, ref="[HSM + 13]",
    contexts=[
        ". MsTMIP is a large, collaborative effort, aimedat harmonizing a number of complex terrestrial biospheric models for the purposes ofcomparing these model outputs [HSM+13].",
        
    ],
)) 

DB(Citation(
    mcphillips2015a, knuth1984a, ref="[Knu84]",
    contexts=[
        "Don Knuth has argued [Knu84] that we should change our traditional attitude to programming:“Instead of imagining that our main task is to instruct a computer what to do, let us concentrate ratheron explaining human beings what we want a computer to do”",
        
    ],
)) 

DB(Citation(
    mcphillips2015a, ludascher2006a, ref="[LAB + 06]",
    contexts=[
        "One advantage of using scientificworkflow systems (e.g., Galaxy [GNT10], Kepler [LAB+06], Taverna [OAF+04],VisTrails [BCC+05], RestFlow [MM10, TMnG+13]) is that they often include capabilitiesto track data as it is being processed.",
        
    ],
))

DB(Citation(
    mcphillips2015a, lerner2014a, ref="[LB14]",
    contexts=[
        "For example, provenance libraries for R have only recentlybeen announced [LB14], while for Python, a new tool called noWorkflow has just beendeveloped [MBC+14].",
        "Similarly, RDataTracker [LB14] captures provenancefrom the execution of R scripts, and the approach taken by Tariq et al. [TAG12] supportsall programming languages allowed by the LLVM compiler framework.",
        
    ],
))

DB(Citation(
    mcphillips2015a, lim2010a, ref="[LLCF10]",
    contexts=[
        "The data provenance captured by workflow environments is sometimes called retrospectiveprovenance to distinguish it from another form called prospective provenance[CFV+08, LLCF10].",
        
    ],
))

DB(Citation(
    mcphillips2015a, murta2014a, ref="[MBC + 14]",
    contexts=[
        "For example, provenance libraries for R have only recentlybeen announced [LB14], while for Python, a new tool called noWorkflow has just beendeveloped [MBC+14].",
        "Some tools [BGS08, Dav12, HAW13, MBC+14] have been developed to capture runtimeprovenance for Python scripts: while Bochner et al. [BGS08] and Davison [Dav12] proposePython libraries and APIs that need to be added to the code to capture the executionsteps, ProvenanceCurious [HAW13] and noWorkflow [MBC+14] are transparent and donot require changes to the scripts.",
        
    ],
))

DB(Citation(
    mcphillips2015a, mcphillips2010a, ref="[MM10]",
    contexts=[
        "One advantage of using scientificworkflow systems (e.g., Galaxy [GNT10], Kepler [LAB+06], Taverna [OAF+04],VisTrails [BCC+05], RestFlow [MM10, TMnG+13]) is that they often include capabilitiesto track data as it is being processed.",
        
    ],
))

DB(Citation(
    mcphillips2015a, moreau2013a, ref="[MM13]",
    contexts=[
        "Similarly, to improve YW interoperabilitywithin the DataONE infrastructure, PROV [MM13] and ProvONE [CVLM+15] compatiblevocabulary extensions may be used in YesWorkflow in the future.",
        
    ],
))

DB(Citation(
    mcphillips2015a, muniswamy2006a, ref="[MRHBS06]",
    contexts=[
        "Mechanismsthat capture provenance at the operating system level [FMS08, GS12, MRHBS06]monitor system calls to track the data dependencies between computational processes",
        
    ],
))

DB(Citation(
    mcphillips2015a, oinn2004a, ref="[OAF + 04]",
    contexts=[
        "One advantage of using scientificworkflow systems (e.g., Galaxy [GNT10], Kepler [LAB+06], Taverna [OAF+04],VisTrails [BCC+05], RestFlow [MM10, TMnG+13]) is that they often include capabilitiesto track data as it is being processed.",
        
    ],
)) 

DB(Citation(
    mcphillips2015a, perez2007a, ref="[PG07]",
    contexts=[
        "YW is also related to ideas from literate programming6 and available in tools such asKnitr [Xie13] and IPython [PG07].",
        
    ],
))

DB(Citation(
    mcphillips2015a, pham2012a, ref="[PMF + 12]",
    contexts=[
        "For instance, the SOLE system [PMF+12]allows linking articles with science objects, which can be source code, a dataset, or aworkflow.",
        
    ],
))

DB(Citation(
    mcphillips2015a, stodden2014a, ref="[SLP14]",
    contexts=[
        "YW can also contribute to the area of reproducible computational research [SLP14],which seeks to provide scientists with sufficient information to understand and eventuallyvalidate the results claimed by their peers.",
        
    ],
)) 

DB(Citation(
    mcphillips2015a, stropp2012a, ref="[SMLB12]",
    contexts=[
        "This R script was modeled on our previous work-flows developed in the Kepler environment [SMLB12].",
        
    ],
)) 

DB(Citation(
    mcphillips2015a, tariq2012a, ref="[TAG12]",
    contexts=[
        "Similarly, RDataTracker [LB14] captures provenancefrom the execution of R scripts, and the approach taken by Tariq et al. [TAG12] supportsall programming languages allowed by the LLVM compiler framework.",
        
    ],
))

DB(Citation(
    mcphillips2015a, tsai2013a, ref="[TMnG + 13]",
    contexts=[
        "One advantage of using scientificworkflow systems (e.g., Galaxy [GNT10], Kepler [LAB+06], Taverna [OAF+04],VisTrails [BCC+05], RestFlow [MM10, TMnG+13]) is that they often include capabilitiesto track data as it is being processed.",
        
    ],
))

DB(Citation(
    mcphillips2015a, zundert2012a, ref="[VZ12]",
    contexts=[
        "In addition to the widespread use in the naturalsciences, computational automation tools are also increasingly used in other domains,e.g., for data mining workflows in the digital humanities [VZ12], or to implement datacuration workflows for natural history collections [DCM+12].",
        
    ],
)) 

DB(Citation(
    mcphillips2015a, wallis2013a, ref="[WRB13]",
    contexts=[
        "This is true in particular forthe “long tail of science” [WRB13, Hei08], where advanced features such as provenancesupport are rarely available",
        
    ],
)) 

DB(Citation(
    mcphillips2015a, xie2013a, ref="[Xie13]",
    contexts=[
        "YW is also related to ideas from literate programming6 and available in tools such asKnitr [Xie13] and IPython [PG07].",
        
    ],
))

DB(Citation(
    mcphillips2015a, 
    DB(Site("Git repositories at", "http://yesworkflow.org")),
    ref="[Yes15]",
    contexts=[
        "However, they are all availablefrom the yw-idcc-15 repository on the YW GitHub site [Yes15].",
        "Our early YW prototype [Yes15] has been used by scientists from different domains tomark up complex, real-world scientific scripts with ease.",
        
    ],
    access="2015",
))

DB(Citation(
    mcphillips2015a, zinn2010a, ref="[ZL10]",
    contexts=[
        "We additionally foresee that combining the information extracted from a markedupscript with references to data files corresponding to a run of that script will in somecases allow the retrospective provenance of those files to be inferred (see also [BML12]and [ZL10]).",
        
    ],
))

DB(Citation(
    jones2016a, mcphillips2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    thanos2016a, mcphillips2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    cao2016a, mcphillips2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gammack2016a, mcphillips2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bennett2016a, mcphillips2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    samuel2017a, mcphillips2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    erickson2016a, mcphillips2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    cao2016b, mcphillips2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    schreiber2016a, mcphillips2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    thavasimani2016a, mcphillips2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    carvalho2016a, mcphillips2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    padhy2015a, mcphillips2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bastos2017a, mcphillips2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    nascimento2015a, mcphillips2015a, ref="",
    contexts=[

    ],
))

DB(Citation(
    moehrke2016a, mcphillips2015a, ref="",
    contexts=[

    ],
))


DB(Citation(
    reimann2017a, mcphillips2015a, ref="",
    contexts=[

    ],
))
