# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2003 import kementsietsidis2003a
from ..work.y2006 import braun2006c
from ..work.y2006 import muniswamy2006a
from ..work.y2007 import bowers2007a
from ..work.y2007 import jayapandian2007a
from ..work.y2008 import blaustein2008a
from ..work.y2008 import cohen2008a
from ..work.y2008 import moreau2008b
from ..work.y2008 import scheidegger2008a
from ..work.y2008 import moreau2008c
from ..work.y2009 import moreau2009a
from ..work.y2009 import smith2009a
from ..work.y2010 import braun2010a


DB(Citation(
    braun2010a,
    Site("LAIKA", "http://laika.sourceforge.net/"),
    ref="[1]",
    contexts=[
        "NIST’s Schematron [2] and Laika [1] perform XML veriﬁcation of valid C32 documents before they are exchanged between medical institutions",
        
    ],
))

DB(Citation(
    braun2010a,
    Site("NIST Schematron", "http://xreg2.nist.gov/cda-validation/archives.html/"),
    ref="[2]",
    contexts=[
        "NIST’s Schematron [2] and Laika [1] perform XML veriﬁcation of valid C32 documents before they are exchanged between medical institutions",
        
    ],
))

DB(Citation(
    braun2010a,
    Site("Open Provenance Model XML Schema", "http://openprovenance.org/model/opmx"),
    ref="[3]",
    contexts=[
        "For example, it is unclearwhetheractivitiesarewidelyacceptedastheydo not appear in the XML schema [3, 15].",
        "Schema veriﬁcation can go a step further, restricting values across attributes based on the values of other attributes [3].",
        
    ],
))

DB(Citation(
    braun2010a,
    Site("Schematron", "http://www.schematron.com"),
    ref="[4]",
    contexts=[
        "Finally, we introduce theSchematron[4]tovalidatethatadocumentconforms to both the OPM and our constraints.",
        "The Schematron [4] is a post-Schema “rule-based veriﬁcation for making assertions about the presence or absence of patterns in XML trees,” [5].",
        "Additionally, the idea of having constraints over an XML schema is not new; nor is the use of a Schematron [4]",
        
    ],
))

DB(Citation(
    braun2010a,
    Site("Schematron", "http://en.wikipedia.org/wiki/Schematron"),
    ref="[5]",
    contexts=[
        "The Schematron [4] is a post-Schema “rule-based veriﬁcation for making assertions about the presence or absence of patterns in XML trees,” [5].",
        
    ],
))

DB(Citation(
    braun2010a,
    Site("Tupelo", "http://tupeloproject.ncsa.uiuc.edu/"),
    ref="[6]",
    contexts=[
        "Very diverse groups participated in the challenge, each with their own ideology on what provenance information to capture, from the grid [17], to workﬂow executions [8] to higher-level workﬂow modiﬁcations [21]; and unique storage mechanisms, from relational[10],toRDFtriples[6].",
        
    ],
))

DB(Citation(
    braun2010a, blaustein2008a, ref="[7]",
    contexts=[
        "WedescribeourexperiencesimportingPASS[16]provenance into PLUS [7].",
        "We investigate the challenges involved in integrating two systems that both export and import OPM graphs. Our goal was to import data from the Harvard Provenance Aware Storage System (PASS) [16] system into MITRE’sPLUSsystem[7].",
        "In this work, we utilize the OPM model [14] and schematoexchangeprovenanceinformationbetweenthe PASS [16] and PLUS [7] provenance systems",
        
    ],
))

DB(Citation(
    braun2010a, bowers2007a, ref="[8]",
    contexts=[
        "Very diverse groups participated in the challenge, each with their own ideology on what provenance information to capture, from the grid [17], to workﬂow executions [8] to higher-level workﬂow modiﬁcations [21]; and unique storage mechanisms, from relational[10],toRDFtriples[6].",
        
    ],
))

DB(Citation(
    braun2010a, braun2006c, ref="[9]",
    contexts=[
        "introducing cycles [9]",
        
    ],
))

DB(Citation(
    braun2010a, cohen2008a, ref="[10]",
    contexts=[
        "Very diverse groups participated in the challenge, each with their own ideology on what provenance information to capture, from the grid [17], to workﬂow executions [8] to higher-level workﬂow modiﬁcations [21]; and unique storage mechanisms, from relational[10],toRDFtriples[6].",
        
    ],
))

DB(Citation(
    braun2010a, jayapandian2007a, ref="[11]",
    contexts=[
        "MiMI [11] utilizes a set of dictionaries provided by the National Center for Biotechnolog",
        
    ],
))

DB(Citation(
    braun2010a, kementsietsidis2003a, ref="[12]",
    contexts=[
        "Existingliteraturesdescribesapproachesthatprovidethe capabilities for such dictionaries [12].",
        
    ],
))

DB(Citation(
    braun2010a, moreau2008b, ref="[13]",
    contexts=[
        "The standardization process used a series of community challenges [13,18,19,20]toidentifyprovenanceconceptscommon across disparate systems",
        
    ],
))

DB(Citation(
    braun2010a, moreau2008c, ref="[14]",
    contexts=[
        "Although both systems import and exportprovenancethatconformstotheOpenProvenance Model (OPM) [14], the two systems vary greatly with respect to the granularity of provenance captured, how much semantic knowledge the system contributes, and the completeness of provenance capture.",
        "The Provenance Challenges [18, 19, 20] were a set of community exercises designed to help reﬁne and shape the Open Provenance Model [14].",
        "The Open Provenance Model (OPM) is a proposed standard for describing provenance data [14].",
        "In this work, we utilize the OPM model [14] and schematoexchangeprovenanceinformationbetweenthe PASS [16] and PLUS [7] provenance systems",
        
    ],
))

DB(Citation(
    braun2010a, moreau2009a, ref="[15]",
    contexts=[
        "For example, it is unclearwhetheractivitiesarewidelyacceptedastheydo not appear in the XML schema [3, 15].",
        "Everyone now agrees that provenanceformsadirectedacyclicgraph(DAG).There is also agreement that objects can be artifacts or processes. Somealsodistinguishactivities,whereprocesses are instances of activities[15].",
        
    ],
))

DB(Citation(
    braun2010a, muniswamy2006a, ref="[16]",
    contexts=[
        "WedescribeourexperiencesimportingPASS[16]provenance into PLUS [7].",
        "We investigate the challenges involved in integrating two systems that both export and import OPM graphs. Our goal was to import data from the Harvard Provenance Aware Storage System (PASS) [16] system into MITRE’sPLUSsystem[7].",
        "In this work, we utilize the OPM model [14] and schematoexchangeprovenanceinformationbetweenthe PASS [16] and PLUS [7] provenance systems",
        
    ],
))

DB(Citation(
    braun2010a,
    Site("Provenance aware service oriented architecture", "http://twiki.pasoa.ecs.soton.ac.uk/bin/view/PASOA/WebHome"),
    ref="[17]",
    contexts=[
        "Very diverse groups participated in the challenge, each with their own ideology on what provenance information to capture, from the grid [17], to workﬂow executions [8] to higher-level workﬂow modiﬁcations [21]; and unique storage mechanisms, from relational[10],toRDFtriples[6].",
        
    ],
))

DB(Citation(
    braun2010a,
    Site("The First Provenance Challenge", "http://twiki.ipaw.info/bin/view/Challenge/FirstProvenanceChallenge."),
    ref="[18]",
    contexts=[
        "The Provenance Challenges [18, 19, 20] were a set of community exercises designed to help reﬁne and shape the Open Provenance Model [14].",
        "The First Provenance Challenge [18] focused on collection and querying of provenance information within individual provenance systems",
        "The standardization process used a series of community challenges [13,18,19,20]toidentifyprovenanceconceptscommon across disparate systems",
        "TheFirstProvenanceChallenge[18]comparedqueryresults on a common workload, whereas the second and third challenges sought to test interoperability by forcing groups to import and query data from other groups.",
        
    ],
))

DB(Citation(
    braun2010a,
    Site("The Second Provenance Challenge", "http://twiki.ipaw.info/bin/view/Challenge/SecondProvenanceChallenge."),
    ref="[19]",
    contexts=[
        "The Provenance Challenges [18, 19, 20] were a set of community exercises designed to help reﬁne and shape the Open Provenance Model [14].",
        "The Second Provenance Challenge [19] began looking at interoperability",
        "The standardization process used a series of community challenges [13,18,19,20]toidentifyprovenanceconceptscommon across disparate systems",
        "While we might be able to impose constraints to create a consistent naming system among different systems, for example, we can require that all artifacts begin with “Artifact”, the same object on two different systems may still be referenced using different names [19], which creates problems",
        
    ],
))

DB(Citation(
    braun2010a,
    Site("The Third Provenance Challenge", "http://twiki.ipaw.info/bin/view/Challenge/ThirdProvenanceChallenge"),
    ref="[20]",
    contexts=[
        "The Provenance Challenges [18, 19, 20] were a set of community exercises designed to help reﬁne and shape the Open Provenance Model [14].",
        "The Third Provenance Challenge [20] again focused on interoperability.",
        "The standardization process used a series of community challenges [13,18,19,20]toidentifyprovenanceconceptscommon across disparate systems",
        "Over the course of the ﬁrst two challenges the workloadandqueriesremainedthesame,whilethethirdchallenge introduced a more complex workﬂow and set of queries [20]",
        
    ],
))

DB(Citation(
    braun2010a, scheidegger2008a, ref="[21]",
    contexts=[
        "Very diverse groups participated in the challenge, each with their own ideology on what provenance information to capture, from the grid [17], to workﬂow executions [8] to higher-level workﬂow modiﬁcations [21]; and unique storage mechanisms, from relational[10],toRDFtriples[6].",
        
    ],
))

DB(Citation(
    braun2010a, smith2009a, ref="[22]",
    contexts=[
        "This deeper semantic understanding is similar to schemaintegration,itgoesbeyondthat. Schemaintegration is focused on ﬁnding the overlaps and commonalities between two schemas[22].",
        
    ],
))
