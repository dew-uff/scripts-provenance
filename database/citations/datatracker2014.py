# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1977 import denning1977a
from ..work.y1994 import srivastava1994a
from ..work.y1998 import vahdat1998a
from ..work.y2004 import bruening2004a
from ..work.y2004 import crandall2004a
from ..work.y2004 import lattner2004a
from ..work.y2005 import simmhan2005b
from ..work.y2005 import luk2005a
from ..work.y2006 import freire2006a
from ..work.y2006 import mccamant2006a
from ..work.y2006 import oinn2006a
from ..work.y2007 import nethercote2007a
from ..work.y2007 import clause2007a
from ..work.y2008 import bowers2008a
from ..work.y2008 import simmhan2008a
from ..work.y2008 import cavallaro2008a
from ..work.y2008 import costa2008a
from ..work.y2008 import davidson2008a
from ..work.y2008 import frew2008a
from ..work.y2008 import kim2008a
from ..work.y2008 import holland2008b
from ..work.y2009 import cheney2009a
from ..work.y2009 import miles2009a
from ..work.y2009 import slowinska2009a
from ..work.y2009 import widom2009a
from ..work.y2010 import moreau2010a
from ..work.y2011 import bosman2011a
from ..work.y2011 import kang2011a
from ..work.y2012 import gessiou2012a
from ..work.y2012 import kemerlis2012a
from ..work.y2012 import macko2012a
from ..work.y2012 import magliacane2012a
from ..work.y2012 import nies2012a
from ..work.y2013 import moreau2013a
from ..work.y2013 import moreau2013b
from ..work.y2014 import stamatogiannakis2014a


DB(Citation(
    stamatogiannakis2014a, bosman2011a, ref="[1]",
    contexts=[
        "The technique has remainedrelevant through the years and has been implemented on different levels,ranging from source code [22], to interpreters2, to full emulators [8,1].",
        "Its mostcommon applications are in the field of security and intrusion detection [7,1].",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, bowers2008a, ref="[2]",
    contexts=[
        "Thisapproach is popular with the scientific workflow community and includes systemssuch as Taverna [29], VisTrails [11], Kepler [2] and Wings [17].",
        
    ],
))

DB(Citation(
    stamatogiannakis2014a, bruening2004a, ref="[3]",
    contexts=[
        "We picked Pin over similar Dynamic Binary Instrumentation (DBI) platforms[27,3] because it is considered the easiest to work with while providinghigh performance without the need for much manual tinkering",
        
    ],
))

DB(Citation(
    stamatogiannakis2014a, cavallaro2008a, ref="[4]",
    contexts=[
        "This is consistent with Cavallaro’sobservations [4].",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, cheney2009a, ref="[5]",
    contexts=[
        "Provenance has been widely studied in the database [5], distributed systems [31]and e-science communities [9].",
        ". Furthermore, Cheney et al. [5] and Simmhanet al. [30] provide specialized reviews for databases and e-science respectively",
        
    ],
))

DB(Citation(
    stamatogiannakis2014a, clause2007a, ref="[6]",
    contexts=[
        "Dytan [6] uses the IntelPin [19] DBI framework and provides much flexibility for configuring taintsources and propagation policies",
        "A more recent effort (also based on Intel Pin) which emphasizes on performanceis libdft [16].",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, costa2008a, ref="[7]",
    contexts=[
        "Its mostcommon applications are in the field of security and intrusion detection [7,1].",
        
    ],
))

DB(Citation(
    stamatogiannakis2014a, crandall2004a, ref="[8]",
    contexts=[
        "The technique has remainedrelevant through the years and has been implemented on different levels,ranging from source code [22], to interpreters2, to full emulators [8,1].",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, davidson2008a, ref="[9]",
    contexts=[
        "Provenance has been widely studied in the database [5], distributed systems [31]and e-science communities [9].",
        
    ],
))

DB(Citation(
    stamatogiannakis2014a, denning1977a, ref="[10]",
    contexts=[
        "Pioneered by Denning in the 70s [10], the idea oftracking the flow of data though a program is all but new",
        ". This problem had already been noted by Denning[10] in her seminal work",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, freire2006a, ref="[11]",
    contexts=[
        "Thisapproach is popular with the scientific workflow community and includes systemssuch as Taverna [29], VisTrails [11], Kepler [2] and Wings [17].",
        
    ],
))

DB(Citation(
    stamatogiannakis2014a, frew2008a, ref="[12]",
    contexts=[
        "It has also been proposed to capture provenance by exploiting the mechanismsoffered by the operating system to trace the activities of programs. Suchsystems include TREC [34], ES3 [12] and the work of Gessiou et al. [13].",
        "This test demonstrates that DataTracker is able to produce the same provenancegraph as those of techniques like [14,12,13]",
        "We can see in Fig. 3b that DataTracker correctly identifies that the outputcontains lines (and therefore was derived) from only two out of the four inputfiles. This is an improvement over systems like [14,12,13],",
        
    ],
))

DB(Citation(
    stamatogiannakis2014a, gessiou2012a, ref="[13]",
    contexts=[
        "It has also been proposed to capture provenance by exploiting the mechanismsoffered by the operating system to trace the activities of programs. Suchsystems include TREC [34], ES3 [12] and the work of Gessiou et al. [13].",
        "This test demonstrates that DataTracker is able to produce the same provenancegraph as those of techniques like [14,12,13]",
        "We can see in Fig. 3b that DataTracker correctly identifies that the outputcontains lines (and therefore was derived) from only two out of the four inputfiles. This is an improvement over systems like [14,12,13],",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, holland2008b, ref="[14]",
    contexts=[
        "A slightly differentapproach is taken by PASS [14], which has been implemented as a Linuxkernel extension.",
        "This test demonstrates that DataTracker is able to produce the same provenancegraph as those of techniques like [14,12,13]",
        "We can see in Fig. 3b that DataTracker correctly identifies that the outputcontains lines (and therefore was derived) from only two out of the four inputfiles. This is an improvement over systems like [14,12,13],",
        
    ],
))

DB(Citation(
    stamatogiannakis2014a, kang2011a, ref="[15]",
    contexts=[
        "DTA++[15] by Kang et al. focuses on the efficienthandling of such implicit flows in benign programs.",
        "Fortracking taint through implicit flows in benign programs, Kang et al. proposeDTA++ [15].",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, kemerlis2012a, ref="[16]",
    contexts=[
        "A short andconcise definition of DTA has been given by Kemerlis et al. [16] as: “the processof accurately tracking the flow of selected data throughout the execution of a program or system”.",
        "A more recent effort (also based on Intel Pin) which emphasizes on performanceis libdft [16].",
        ". InDTA implementations like libdft [16], where taint marks propagate only throughoperations directly involving a tainted location, these cases will not result inpropagation of taint from x to y.",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, kim2008a, ref="[17]",
    contexts=[
        "Thisapproach is popular with the scientific workflow community and includes systemssuch as Taverna [29], VisTrails [11], Kepler [2] and Wings [17].",
        
    ],
))

DB(Citation(
    stamatogiannakis2014a, lattner2004a, ref="[18]",
    contexts=[
        ". Instrumentationtechniques which require modification or recompilation of the instrumentedprograms [33,18] were precluded.",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, luk2005a, ref="[19]",
    contexts=[
        ": DataTracker applies Dynamic Instrumentation onthe executing programs using the Intel Pin [19] framework",
        "Dytan [6] uses the IntelPin [19] DBI framework and provides much flexibility for configuring taintsources and propagation policies",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, macko2012a, ref="[20]",
    contexts=[
        "Frameworks for modifying programs to recordprovenance information have also been proposed [23,20].",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, magliacane2012a, ref="[21]",
    contexts=[
        "Finally, newer work [21,28] does not use a-priori instrumentation but attemptsto reconstruct provenance directly from data.",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, mccamant2006a, ref="[22]",
    contexts=[
        "The technique has remainedrelevant through the years and has been implemented on different levels,ranging from source code [22], to interpreters2, to full emulators [8,1].",
        
    ],
))

DB(Citation(
    stamatogiannakis2014a, miles2009a, ref="[23]",
    contexts=[
        "Frameworks for modifying programs to recordprovenance information have also been proposed [23,20].",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, moreau2010a, ref="[24]",
    contexts=[
        "For a comprehensive overview of the field, werefer the reader to Moreau [24].",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, moreau2013b, ref="[25]",
    contexts=[
        "This record can be analyzed to understand if data was producedaccording to regulations, understand the decision making procedure behind thegeneration of data, used in debugging complex scientific programs, or used tomake trust calculations [25].",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, moreau2013a, ref="[26]",
    contexts=[
        "Provenance is a “record that describes the people, institutions, entities, andactivities involved in producing, influencing, or delivering a piece of data or athing” [26].",
        
    ],
))

DB(Citation(
    stamatogiannakis2014a, nethercote2007a, ref="[27]",
    contexts=[
        "We picked Pin over similar Dynamic Binary Instrumentation (DBI) platforms[27,3] because it is considered the easiest to work with while providinghigh performance without the need for much manual tinkering",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, nies2012a, ref="[28]",
    contexts=[
        "Finally, newer work [21,28] does not use a-priori instrumentation but attemptsto reconstruct provenance directly from data.",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, oinn2006a, ref="[29]",
    contexts=[
        "Thisapproach is popular with the scientific workflow community and includes systemssuch as Taverna [29], VisTrails [11], Kepler [2] and Wings [17].",
        
    ],
))

DB(Citation(
    stamatogiannakis2014a, simmhan2005b, ref="[30]",
    contexts=[
        ". Furthermore, Cheney et al. [5] and Simmhanet al. [30] provide specialized reviews for databases and e-science respectively",
        
    ],
))

DB(Citation(
    stamatogiannakis2014a, simmhan2008a, ref="[31]",
    contexts=[
        "Provenance has been widely studied in the database [5], distributed systems [31]and e-science communities [9].",
        "Other middlewarebasedsystems like Karma [31] are not tied to a workflow system, but insteadtap into the communication stack to capture provenance.",
        
    ],
))

DB(Citation(
    stamatogiannakis2014a, slowinska2009a, ref="[32]",
    contexts=[
        "Attempting to track implicit flows may result in over-tainting and a highnumber of false-positive, especially when using DTA to analyze malware [32].",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, srivastava1994a, ref="[33]",
    contexts=[
        ". Instrumentationtechniques which require modification or recompilation of the instrumentedprograms [33,18] were precluded.",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, vahdat1998a, ref="[34]",
    contexts=[
        "It has also been proposed to capture provenance by exploiting the mechanismsoffered by the operating system to trace the activities of programs. Suchsystems include TREC [34], ES3 [12] and the work of Gessiou et al. [13].",
        "Capturing the user input has remainedlargely unaddressed by previous work (e.g. [34]).",
        
    ],
)) 

DB(Citation(
    stamatogiannakis2014a, widom2009a, ref="[35]",
    contexts=[
        ". Forexample, Trio DBMS [35] extends a relational database system to cope withuncertain data and provenance.",
        
    ],
))