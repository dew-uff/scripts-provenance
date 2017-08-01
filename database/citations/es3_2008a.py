# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2001 import frew2001a
from ..work.y2001 import brandes2001a
from ..work.y2004 import dozier2004a
from ..work.y2005 import maritorena2005a
from ..work.y2005 import valeur2005a
from ..work.y2006 import malhotra2006a
from ..work.y2007 import groth2007a
from ..work.y2007 import simmhan2007a
from ..work.y2008 import simmhan2008b
from ..work.y2008 import scheidegger2008a
from ..work.y2008 import moreau2008b
from ..work.y2008 import barga2008a
from ..work.y2008 import clifford2008a
from ..work.y2008 import cohen2008a
from ..work.y2008 import frew2008a
from ..work.y2008 import futrelle2008a
from ..work.y2008 import kim2008a
from ..work.y2008 import krenek2008a
from ..work.y2008 import ludascher2008a
from ..work.y2008 import schuchardt2008a
from ..work.y2008 import zhao2008a
from ..work.y2008 import holland2008b
from ..work.y2008 import miles2008a
from ..work.y2008 import davidson2008a
from ..work.y2008 import chapman2008b
from ..work.y2009 import zhang2009b
from ..work.y2009 import dozier2009a
from ..work.y2009 import shen2009a
from ..work.y2009 import mwebaze2009a
from ..work.y2009 import reilly2009a
from ..work.y2009 import rosenthal2009a
from ..work.y2009 import moreau2009a
from ..work.y2009 import yue2009a
from ..work.y2009 import wootten2009a
from ..work.y2009 import nyasulu2009a
from ..work.y2009 import chen2009a
from ..work.y2010 import yue2010a
from ..work.y2010 import chebotko2010a
from ..work.y2010 import muniswamy2010a
from ..work.y2010 import moreau2010a
from ..work.y2010 import allen2010a
from ..work.y2010 import glavic2010a
from ..work.y2010 import malik2010a
from ..work.y2010 import barkstrom2010a
from ..work.y2010 import chapman2010a
from ..work.y2010 import gehani2010b
from ..work.y2010 import peng2010a
from ..work.y2010 import schreiber2010a
from ..work.y2010 import chapman2010b
from ..work.y2010 import deelman2010a
from ..work.y2011 import benabdelkader2011a
from ..work.y2011 import wang2011a
from ..work.y2011 import cheah2011a
from ..work.y2011 import chapman2011a
from ..work.y2011 import allen2011a
from ..work.y2011 import zhao2011c
from ..work.y2011 import turuncoglu2011a
from ..work.y2011 import allen2011b
from ..work.y2011 import kwasnikowska2011a
from ..work.y2011 import eek2011a
from ..work.y2011 import chapman2011b
from ..work.y2012 import freire2012a
from ..work.y2012 import gehani2012a
from ..work.y2012 import groth2012a
from ..work.y2012 import magliacane2012a
from ..work.y2012 import koop2012a
from ..work.y2012 import sultana2012a
from ..work.y2012 import shu2012a
from ..work.y2012 import frew2012a
from ..work.y2012 import thorpe2012a
from ..work.y2012 import janee2012a
from ..work.y2012 import turuncoglu2012a
from ..work.y2012 import sansrimahachai2012a
from ..work.y2012 import allen2012a
from ..work.y2013 import malik2013a
from ..work.y2013 import turuncoglu2013a
from ..work.y2013 import li2013a
from ..work.y2013 import carata2013a
from ..work.y2013 import di2013a
from ..work.y2013 import garcia2013a
from ..work.y2013 import neves2013a
from ..work.y2013 import patel2013a
from ..work.y2013 import soares2013a
from ..work.y2013 import nies2013b
from ..work.y2013 import magliacane2013a
from ..work.y2014 import li2014a
from ..work.y2014 import coe2014a
from ..work.y2014 import stamatogiannakis2014b
from ..work.y2014 import allen2014a
from ..work.y2014 import coe2014b
from ..work.y2014 import douglas2014a
from ..work.y2014 import bonet2014a
from ..work.y2014 import oliveira2014a
from ..work.y2014 import garcia2014b
from ..work.y2014 import sultana2014a
from ..work.y2014 import saake2014a
from ..work.y2014 import neves2014a
from ..work.y2015 import liu2015a
from ..work.y2015 import stamatogiannakis2015a
from ..work.y2015 import sultana2015a
from ..work.y2015 import sarikhani2015a
from ..work.y2015 import michaelis2015a
from ..work.y2015 import meera2015a
from ..work.y2016 import packer2016a
from ..work.y2016 import pimentel2016e
from ..work.y2016 import stamatogiannakis2016a
from ..work.y2016 import appelbaum2016a
from ..work.y2016 import sun2016a


DB(Citation(
    frew2008a, frew2001a, ref="[1]",
    contexts=[
        "Scientists are increasingly being called upon to publish data as well as conclusions[1].",
    ],
))

DB(Citation(
    frew2008a, dozier2004a, ref="[2]",
    contexts=[
        "Decades of experience with developers of data products based on satellite remote sensing of snow cover[2]and ocean color[3]have convinced us that most practicing scientists are extremely reluctant to assume the burdens of operational data publication.",
    ],
))

DB(Citation(
    frew2008a, maritorena2005a, ref="[3]",
    contexts=[
        "Decades of experience with developers of data products based on satellite remote sensing of snow cover[2]and ocean color[3]have convinced us that most practicing scientists are extremely reluctant to assume the burdens of operational data publication.",
    ],
))

DB(Citation(
    frew2008a, valeur2005a, ref="[4]",
    contexts=[
        "Broadly speaking, there are three strategies available for capturing provenance at execution time[4]: 1. Passive monitoring; 2. Overriding; 3. Instrumentation",
    ],
))

DB(Citation(
    frew2008a, 
    DB(Site("IDL Data Visualization & Analysis Platform", "http://www.ittvis.com/idl")),
    ref="[5]",
    contexts=[
        "A plugin for the IDL[5]analysis environment preprocesses IDL scripts to insert ES3-speciﬁc logging information, and to replace calls to certain IDL built-in functions with calls to instrumented ES3 equivalents."
    ],
    access="27 November 2006"
))

DB(Citation(
    frew2008a, moreau2008b, ref="[6]",
    contexts=[
        "Most approaches represented in the Provenance Challenge [6] were based on workﬂow systems [7–17].",
    ],
))

DB(Citation(
    frew2008a, krenek2008a, ref="[7]",
    contexts=[
        "Most approaches represented in the Provenance Challenge [6] were based on workﬂow systems [7–17].",
    ],
))

DB(Citation(
    frew2008a, simmhan2008b, ref="[8]",
    contexts=[
        "Most approaches represented in the Provenance Challenge [6] were based on workﬂow systems [7–17].",
    ],
))

DB(Citation(
    frew2008a, zhao2008a, ref="[9]",
    contexts=[
        "Most approaches represented in the Provenance Challenge [6] were based on workﬂow systems [7–17].",
    ],
))

DB(Citation(
    frew2008a, futrelle2008a, ref="[10]",
    contexts=[
        "Most approaches represented in the Provenance Challenge [6] were based on workﬂow systems [7–17].",
    ],
))

DB(Citation(
    frew2008a, barga2008a, ref="[11]",
    contexts=[
        "Most approaches represented in the Provenance Challenge [6] were based on workﬂow systems [7–17].",
    ],
))

DB(Citation(
    frew2008a, ludascher2008a, ref="[12]",
    contexts=[
        "Most approaches represented in the Provenance Challenge [6] were based on workﬂow systems [7–17].",
    ],
))

DB(Citation(
    frew2008a, schuchardt2008a, ref="[13]",
    contexts=[
        "Most approaches represented in the Provenance Challenge [6] were based on workﬂow systems [7–17].",
    ],
))

DB(Citation(
    frew2008a, clifford2008a, ref="[14]",
    contexts=[
        "Most approaches represented in the Provenance Challenge [6] were based on workﬂow systems [7–17].",
    ],
))

DB(Citation(
    frew2008a, scheidegger2008a, ref="[15]",
    contexts=[
        "Most approaches represented in the Provenance Challenge [6] were based on workﬂow systems [7–17].",
    ],
))

DB(Citation(
    frew2008a, kim2008a, ref="[16]",
    contexts=[
        "Most approaches represented in the Provenance Challenge [6] were based on workﬂow systems [7–17].",
    ],
))

DB(Citation(
    frew2008a, cohen2008a, ref="[17]",
    contexts=[
        "Most approaches represented in the Provenance Challenge [6] were based on workﬂow systems [7–17].",
    ],
))

DB(Citation(
    frew2008a, holland2008b, ref="[18]",
    contexts=[
        "By contrast, both ES3 and PASS[18]employ a descriptive approach to provenance: existing processes’ interactions with each other and with the underlying computing environment (filesystem, operating system, etc.) are transparently monitored, collected, and assembled post hoc into a provenance graph.",
    ],
))

DB(Citation(
    frew2008a, brandes2001a, ref="[19]",
    contexts=[
        "The workﬂow representation of the challenge script (Figure 2) was assembled post hoc by ES3, and retrieved from ES3 as a GraphML [19] document."
    ],
))

DB(Citation(
    frew2008a, 
    DB(Site("yEd—JavaTM Graph Editor", "http://www.yworks.com/en/products_yed_about.htm")),
    ref="[20]",
    contexts=[
        "The workﬂow diagrams are generated by yWorks’ yEd [20] graph editor, using reformatted ES3 GraphML documents as input."
    ],
    access="27 November 2006"
))


DB(Citation(
    frew2008a, malhotra2006a, ref="[21]",
    contexts=[
        "Note that ES3 only partially succeeds for Query 4, since the XQuery language [21] lacks a day-of-week comparison operator."
    ],
))

# Snowballing

DB(Citation(
    clifford2008a, frew2008a, ref="4",
    contexts=[
        "Other systems, such as PASS [10] and ES3 [11], capture provenance information at the operating system level—PASS in the kernel, at the ﬁle system interface, and ES3 via the user-level strace interface.",
    ],
))




DB(Citation(
    zhang2009b, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    dozier2009a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    shen2009a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    yue2010a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    freire2012a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    miles2008a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    chebotko2010a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    simmhan2008b, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    cohen2008a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gehani2012a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    scheidegger2008a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    muniswamy2010a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    moreau2010a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    moreau2008b, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    davidson2008a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    allen2010a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    groth2012a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    malik2013a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mwebaze2009a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    turuncoglu2013a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    benabdelkader2011a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    wang2011a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    glavic2010a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    reilly2009a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    li2014a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    magliacane2012a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    cheah2011a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    malik2010a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    groth2007a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    chapman2011a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    li2013a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    rosenthal2009a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    koop2012a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    carata2013a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    barkstrom2010a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sultana2012a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    liu2015a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    shu2012a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    chapman2010a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    moreau2009a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    allen2011a, frew2008a, ref="16",
    contexts=[
        "For  instance, in ES3 [16], the applications used by scientists for data analysis are modified to capture provenance.", 
    ],
))

DB(Citation(
    zhao2011c, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    turuncoglu2011a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    schuchardt2008a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    frew2012a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    yue2009a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    allen2011b, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    di2013a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gehani2010b, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    coe2014a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    thorpe2012a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    garcia2013a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    peng2010a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    chapman2008b, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    janee2012a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stamatogiannakis2014b, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    allen2014a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    neves2013a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stamatogiannakis2015a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    patel2013a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sultana2015a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    schreiber2010a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    coe2014b, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    chapman2010b, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    douglas2014a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    deelman2010a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bonet2014a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    simmhan2007a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    wootten2009a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sarikhani2015a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    packer2016a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    pimentel2016e, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    nyasulu2009a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stamatogiannakis2016a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    appelbaum2016a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    soares2013a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    oliveira2014a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    nies2013b, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    turuncoglu2012a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sansrimahachai2012a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    michaelis2015a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    magliacane2013a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    allen2012a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sun2016a, frew2008a, ref="",
    contexts=[

    ],
))



DB(Citation(
    garcia2014b, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sultana2014a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    saake2014a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kwasnikowska2011a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    meera2015a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    eek2011a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    chen2009a, frew2008a, ref="",
    contexts=[

    ],
))



DB(Citation(
    neves2014a, frew2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    chapman2011b, frew2008a, ref="",
    contexts=[

    ],
))
