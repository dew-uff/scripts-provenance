# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1990 import katz1990a
from ..work.y2001 import buneman2001a
from ..work.y2002 import foster2002a
from ..work.y2005 import bavoil2005a
from ..work.y2005 import deelman2005a
from ..work.y2005 import giardine2005a
from ..work.y2005 import ives2005a
from ..work.y2005 import simmhan2005b
from ..work.y2005 import widom2005a
from ..work.y2005 import buyya2005a
from ..work.y2006 import altintas2006a
from ..work.y2006 import buneman2006a
from ..work.y2006 import freire2006a
from ..work.y2006 import ludascher2006a
from ..work.y2006 import oinn2006a
from ..work.y2006 import simmhan2006a
from ..work.y2006 import zhao2006a
from ..work.y2007 import green2007a
from ..work.y2008 import davidson2008a
from ..work.y2008 import freire2008a
from ..work.y2009 import cheney2009a
from ..work.y2009 import khoussainova2009a
from ..work.y2010 import moreau2010a
from ..work.y2011 import goff2011a
from ..work.y2011 import howe2011a
from ..work.y2012 import halperin2012a
from ..work.y2012 import madhavan2012a
from ..work.y2013 import halperin2013a
from ..work.y2014 import murta2014a
from ..work.y2014 import sankaranarayanan2014a
from ..work.y2015 import bhardwaj2015a
from ..work.y2015 import bhattacherjee2015a
from ..work.y2015 import chavan2015a
from ..work.y2015 import crankshaw2015a
from ..work.y2015 import interlandi2015a
from ..work.y2015 import kandogan2015a
from ..work.y2015 import kumar2015a
from ..work.y2015 import kumar2015b
from ..work.y2016 import miao2016a
from ..work.y2016 import halevy2016a
from ..work.y2016 import vartak2016a
from ..work.y2016 import zhang2016a
from ..work.y2016 import schubert2016a
from ..work.y2017 import hellerstein2017a


DB(Citation(
    miao2016a, altintas2006a, ref="[1]",
    contexts=[
        "There has also been much work onprovenance, with increasing interestintherecentyears. Provenancecanbecapturedatdifferent granularities,andatdifferentlevelsofdetail. Inscientiﬁcworkﬂowsystems [1,2,12,13,13,14,29,33,35,36,54] where the operations are typically treated as black boxes, the provenance can usually be captured only at the level of datasets.",

    ],
))

DB(Citation(
    miao2016a, bavoil2005a, ref="[2]",
    contexts=[
        "There has been much work on scientiﬁc workﬂow systems over the years, with some of the prominent systems being Kepler [29], Taverna[33],Galaxy[15],iPlant[16],VisTrails[2],Chimera[12], Pegasus [11], to name a few These systems often center around creating, automating, and monitoring a well-deﬁned workﬂow or data analysis pipeline.",
        "There has also been much work onprovenance, with increasing interestintherecentyears. Provenancecanbecapturedatdifferent granularities,andatdifferentlevelsofdetail. Inscientiﬁcworkﬂowsystems [1,2,12,13,13,14,29,33,35,36,54] where the operations are typically treated as black boxes, the provenance can usually be captured only at the level of datasets.",
    ],
))

DB(Citation(
    miao2016a, bhardwaj2015a, ref="[3]",
    contexts=[
        "PROVDB is being developed in conjunction with DataHub [3], a dataset-centric platform for enabling collaborative data analytics that supports managing a large number of datasets, their versions overtime,andderiveddataproducts.",
    ],
))

DB(Citation(
    miao2016a, bhattacherjee2015a, ref="[4]",
    contexts=[
        "A repository consists of a set of versions. A version, identiﬁed by an ID, is immutable and any update to a version conceptually results in a new version with a different version ID (physical data structures are typically not immutable and the underlying DVCS uses various strategies for compact storage [4]).",
    ],
))

DB(Citation(
    miao2016a, buneman2006a, ref="[5]",
    contexts=[
        "On the other hand, in dataﬂow systems where the operators are written in a declarative language (e.g., SQL, Pig Latin, Spark), data provenance at record levelcanbecapturedifneeded[5,6,8,10,17,22,31,53].",
    ],
))

DB(Citation(
    miao2016a, buneman2001a, ref="[6]",
    contexts=[
        "On the other hand, in dataﬂow systems where the operators are written in a declarative language (e.g., SQL, Pig Latin, Spark), data provenance at record levelcanbecapturedifneeded[5,6,8,10,17,22,31,53].",
    ],
))

DB(Citation(
    miao2016a, chavan2015a, ref="[7]",
    contexts=[
        "The speciﬁc data model we use generalizes and reﬁnes a data model proposed in our prior work [7], and allows ﬂexibly capturing a variety of different types of information including versioning and provenance information, parameters used during experiments or modeling, statistics gathered to make decision, analysis scripts, notes or tags, etc.",
        "Apriorpaper[7]describedan initial proposal for a query language for uniﬁed querying of provenanceandversioninginformation,butdidnothaveanimplementation, and did not discuss the issues of how provenance information may be captured and the rich introspective analysis that may be performedonsuchinformation.",
        "Developing a higher-level query language also remains a major challenge; although we proposed an initial design of a query language in our prior work [7], it does not support querying over workﬂow derivations or analysis artifacts.",
    ],
))

DB(Citation(
    miao2016a, cheney2009a, ref="[8]",
    contexts=[
        "On the other hand, in dataﬂow systems where the operators are written in a declarative language (e.g., SQL, Pig Latin, Spark), data provenance at record levelcanbecapturedifneeded[5,6,8,10,17,22,31,53].",
    ],
))

DB(Citation(
    miao2016a, crankshaw2015a, ref="[9]",
    contexts=[
        "Several recent systems have attemptedtoaddressend-to-endissues,includingmodelserving(e.g., TensorFlow Serving, Velox [9], MSMS [27], ModelDB [52]).",
    ],
))

DB(Citation(
    miao2016a, davidson2008a, ref="[10]",
    contexts=[
        "On the other hand, in dataﬂow systems where the operators are written in a declarative language (e.g., SQL, Pig Latin, Spark), data provenance at record levelcanbecapturedifneeded[5,6,8,10,17,22,31,53].",
    ],
))

DB(Citation(
    miao2016a, deelman2005a, ref="[11]",
    contexts=[
        "There has been much work on scientiﬁc workﬂow systems over the years, with some of the prominent systems being Kepler [29], Taverna[33],Galaxy[15],iPlant[16],VisTrails[2],Chimera[12], Pegasus [11], to name a few These systems often center around creating, automating, and monitoring a well-deﬁned workﬂow or data analysis pipeline.",
    ],
))

DB(Citation(
    miao2016a, foster2002a, ref="[12]",
    contexts=[
        "There has been much work on scientiﬁc workﬂow systems over the years, with some of the prominent systems being Kepler [29], Taverna[33],Galaxy[15],iPlant[16],VisTrails[2],Chimera[12], Pegasus [11], to name a few These systems often center around creating, automating, and monitoring a well-deﬁned workﬂow or data analysis pipeline.",
        "There has also been much work onprovenance, with increasing interestintherecentyears. Provenancecanbecapturedatdifferent granularities,andatdifferentlevelsofdetail. Inscientiﬁcworkﬂowsystems [1,2,12,13,13,14,29,33,35,36,54] where the operations are typically treated as black boxes, the provenance can usually be captured only at the level of datasets.",
    ],
))

DB(Citation(
    miao2016a, freire2008a, ref="[13]",
    contexts=[
        "There has also been much work onprovenance, with increasing interestintherecentyears. Provenancecanbecapturedatdifferent granularities,andatdifferentlevelsofdetail. Inscientiﬁcworkﬂowsystems [1,2,12,13,13,14,29,33,35,36,54] where the operations are typically treated as black boxes, the provenance can usually be captured only at the level of datasets.",
    ],
))

DB(Citation(
    miao2016a, freire2006a, ref="[14]",
    contexts=[
        "There has also been much work onprovenance, with increasing interestintherecentyears. Provenancecanbecapturedatdifferent granularities,andatdifferentlevelsofdetail. Inscientiﬁcworkﬂowsystems [1,2,12,13,13,14,29,33,35,36,54] where the operations are typically treated as black boxes, the provenance can usually be captured only at the level of datasets.",
    ],
))

DB(Citation(
    miao2016a, giardine2005a, ref="[15]",
    contexts=[
        "There has been much work on scientiﬁc workﬂow systems over the years, with some of the prominent systems being Kepler [29], Taverna[33],Galaxy[15],iPlant[16],VisTrails[2],Chimera[12], Pegasus [11], to name a few These systems often center around creating, automating, and monitoring a well-deﬁned workﬂow or data analysis pipeline.",
    ],
))

DB(Citation(
    miao2016a, goff2011a, ref="[16]",
    contexts=[
        "There has been much work on scientiﬁc workﬂow systems over the years, with some of the prominent systems being Kepler [29], Taverna[33],Galaxy[15],iPlant[16],VisTrails[2],Chimera[12], Pegasus [11], to name a few These systems often center around creating, automating, and monitoring a well-deﬁned workﬂow or data analysis pipeline.",
    ],
))

DB(Citation(
    miao2016a, green2007a, ref="[17]",
    contexts=[
        "On the other hand, in dataﬂow systems where the operators are written in a declarative language (e.g., SQL, Pig Latin, Spark), data provenance at record levelcanbecapturedifneeded[5,6,8,10,17,22,31,53].",
    ],
))

DB(Citation(
    miao2016a, halevy2016a, ref="[18]",
    contexts=[
        "GOODS [18] is a dataset management system, that passively extracts metadata information from a large number of datasets within an enterprise, and allows users to ﬁnd, monitor, and analyze datasets.",
    ],
))

DB(Citation(
    miao2016a, halperin2013a, ref="[19]",
    contexts=[
        "Several systems have been designed that focus on speciﬁc aspects of the proposed work, including collaborative data management(e.g.,Fusiontables[30],Orchestra[23],CQMS[20,26],LabBook[24]),datasharing(e.g.,SQLShare[19,20,21],SMILE[34]), hosted data repositories accessible to applications (CKAN [37], Domo [46]), hosted data science (Domino [45]), as well as data publishingtools(Quandl[49],Factual[47],DataMarket[44]). None of them, however, aim to capture a broad range of metadata and provenance information in a uniﬁed fashion, to support high-level analysis and reasoning over data science pipelines.",
    ],
))

DB(Citation(
    miao2016a, howe2011a, ref="[20]",
    contexts=[
        "Several systems have been designed that focus on speciﬁc aspects of the proposed work, including collaborative data management(e.g.,Fusiontables[30],Orchestra[23],CQMS[20,26],LabBook[24]),datasharing(e.g.,SQLShare[19,20,21],SMILE[34]), hosted data repositories accessible to applications (CKAN [37], Domo [46]), hosted data science (Domino [45]), as well as data publishingtools(Quandl[49],Factual[47],DataMarket[44]). None of them, however, aim to capture a broad range of metadata and provenance information in a uniﬁed fashion, to support high-level analysis and reasoning over data science pipelines.",
        "Several systems have been designed that focus on speciﬁc aspects of the proposed work, including collaborative data management(e.g.,Fusiontables[30],Orchestra[23],CQMS[20,26],LabBook[24]),datasharing(e.g.,SQLShare[19,20,21],SMILE[34]), hosted data repositories accessible to applications (CKAN [37], Domo [46]), hosted data science (Domino [45]), as well as data publishingtools(Quandl[49],Factual[47],DataMarket[44]). None of them, however, aim to capture a broad range of metadata and provenance information in a uniﬁed fashion, to support high-level analysis and reasoning over data science pipelines.",
    ],
))

DB(Citation(
    miao2016a, halperin2012a, ref="[21]",
    contexts=[
        "Several systems have been designed that focus on speciﬁc aspects of the proposed work, including collaborative data management(e.g.,Fusiontables[30],Orchestra[23],CQMS[20,26],LabBook[24]),datasharing(e.g.,SQLShare[19,20,21],SMILE[34]), hosted data repositories accessible to applications (CKAN [37], Domo [46]), hosted data science (Domino [45]), as well as data publishingtools(Quandl[49],Factual[47],DataMarket[44]). None of them, however, aim to capture a broad range of metadata and provenance information in a uniﬁed fashion, to support high-level analysis and reasoning over data science pipelines.",
    ],
))

DB(Citation(
    miao2016a, interlandi2015a, ref="[22]",
    contexts=[
        "On the other hand, in dataﬂow systems where the operators are written in a declarative language (e.g., SQL, Pig Latin, Spark), data provenance at record levelcanbecapturedifneeded[5,6,8,10,17,22,31,53].",
    ],
))

DB(Citation(
    miao2016a, ives2005a, ref="[23]",
    contexts=[
        "Several systems have been designed that focus on speciﬁc aspects of the proposed work, including collaborative data management(e.g.,Fusiontables[30],Orchestra[23],CQMS[20,26],LabBook[24]),datasharing(e.g.,SQLShare[19,20,21],SMILE[34]), hosted data repositories accessible to applications (CKAN [37], Domo [46]), hosted data science (Domino [45]), as well as data publishingtools(Quandl[49],Factual[47],DataMarket[44]). None of them, however, aim to capture a broad range of metadata and provenance information in a uniﬁed fashion, to support high-level analysis and reasoning over data science pipelines.",
    ],
))

DB(Citation(
    miao2016a, kandogan2015a, ref="[24]",
    contexts=[
       "Several systems have been designed that focus on speciﬁc aspects of the proposed work, including collaborative data management(e.g.,Fusiontables[30],Orchestra[23],CQMS[20,26],LabBook[24]),datasharing(e.g.,SQLShare[19,20,21],SMILE[34]), hosted data repositories accessible to applications (CKAN [37], Domo [46]), hosted data science (Domino [45]), as well as data publishingtools(Quandl[49],Factual[47],DataMarket[44]). None of them, however, aim to capture a broad range of metadata and provenance information in a uniﬁed fashion, to support high-level analysis and reasoning over data science pipelines.",
        "LabBook[24]hassomewhatsimilargoals, andalsousesaproperty graph to manage metadata captured during collaborative analytics and features web-based apps architecture for analyzing the metadata.",
        "Our model differs from the other similar models proposed in the past work [24,56] primarily in the explicit modeling of versions.",
    ],
))

DB(Citation(
    miao2016a, katz1990a, ref="[25]",
    contexts=[
        "For example, a grid search of a template derivation on a start snapshot can be conﬁgured directly in the UI. Maintaining suchuserannotations(andﬁleviewsdiscussednext)asthedatasets evolve is a complicated issue in itself [25].",

    ],
))

DB(Citation(
    miao2016a, khoussainova2009a, ref="[26]",
    contexts=[
        "Several systems have been designed that focus on speciﬁc aspects of the proposed work, including collaborative data management(e.g.,Fusiontables[30],Orchestra[23],CQMS[20,26],LabBook[24]),datasharing(e.g.,SQLShare[19,20,21],SMILE[34]), hosted data repositories accessible to applications (CKAN [37], Domo [46]), hosted data science (Domino [45]), as well as data publishingtools(Quandl[49],Factual[47],DataMarket[44]). None of them, however, aim to capture a broad range of metadata and provenance information in a uniﬁed fashion, to support high-level analysis and reasoning over data science pipelines.",
        "Our model differs from the other similar models proposed in the past work [24,56] primarily in the explicit modeling of versions.",

    ],
))

DB(Citation(
    miao2016a, kumar2015a, ref="[27]",
    contexts=[
        "Several recent systems have attemptedtoaddressend-to-endissues,includingmodelserving(e.g., TensorFlow Serving, Velox [9], MSMS [27], ModelDB [52]).",

    ],
))

DB(Citation(
    miao2016a, kumar2015b, ref="[28]",
    contexts=[

    ],
))

DB(Citation(
    miao2016a, ludascher2006a, ref="[29]",
    contexts=[
        "There has been much work on scientiﬁc workﬂow systems over the years, with some of the prominent systems being Kepler [29], Taverna[33],Galaxy[15],iPlant[16],VisTrails[2],Chimera[12], Pegasus [11], to name a few These systems often center around creating, automating, and monitoring a well-deﬁned workﬂow or data analysis pipeline.",
        "There has also been much work onprovenance, with increasing interestintherecentyears. Provenancecanbecapturedatdifferent granularities,andatdifferentlevelsofdetail. Inscientiﬁcworkﬂowsystems [1,2,12,13,13,14,29,33,35,36,54] where the operations are typically treated as black boxes, the provenance can usually be captured only at the level of datasets.",

    ],
))

DB(Citation(
    miao2016a, madhavan2012a, ref="[30]",
    contexts=[
        "Several systems have been designed that focus on speciﬁc aspects of the proposed work, including collaborative data management(e.g.,Fusiontables[30],Orchestra[23],CQMS[20,26],LabBook[24]),datasharing(e.g.,SQLShare[19,20,21],SMILE[34]), hosted data repositories accessible to applications (CKAN [37], Domo [46]), hosted data science (Domino [45]), as well as data publishingtools(Quandl[49],Factual[47],DataMarket[44]). None of them, however, aim to capture a broad range of metadata and provenance information in a uniﬁed fashion, to support high-level analysis and reasoning over data science pipelines.",

    ],
))

DB(Citation(
    miao2016a, moreau2010a, ref="[31]",
    contexts=[
        "On the other hand, in dataﬂow systems where the operators are written in a declarative language (e.g., SQL, Pig Latin, Spark), data provenance at record levelcanbecapturedifneeded[5,6,8,10,17,22,31,53].",

    ],
))

DB(Citation(
    miao2016a, murta2014a, ref="[32]",
    contexts=[
        "We are currently working on incorporating parsers for scripts written in popular data science tools such as Jupyter, scikit-learn and pandas, by building upon prior work [32].",

    ],
))

DB(Citation(
    miao2016a, oinn2006a, ref="[33]",
    contexts=[
        "There has been much work on scientiﬁc workﬂow systems over the years, with some of the prominent systems being Kepler [29], Taverna[33],Galaxy[15],iPlant[16],VisTrails[2],Chimera[12], Pegasus [11], to name a few These systems often center around creating, automating, and monitoring a well-deﬁned workﬂow or data analysis pipeline.",
        "There has also been much work onprovenance, with increasing interestintherecentyears. Provenancecanbecapturedatdifferent granularities,andatdifferentlevelsofdetail. Inscientiﬁcworkﬂowsystems [1,2,12,13,13,14,29,33,35,36,54] where the operations are typically treated as black boxes, the provenance can usually be captured only at the level of datasets.",
    ],
))

DB(Citation(
    miao2016a, sankaranarayanan2014a, ref="[34]",
    contexts=[
        "Several systems have been designed that focus on speciﬁc aspects of the proposed work, including collaborative data management(e.g.,Fusiontables[30],Orchestra[23],CQMS[20,26],LabBook[24]),datasharing(e.g.,SQLShare[19,20,21],SMILE[34]), hosted data repositories accessible to applications (CKAN [37], Domo [46]), hosted data science (Domino [45]), as well as data publishingtools(Quandl[49],Factual[47],DataMarket[44]). None of them, however, aim to capture a broad range of metadata and provenance information in a uniﬁed fashion, to support high-level analysis and reasoning over data science pipelines.",

    ],
))

DB(Citation(
    miao2016a, simmhan2005b, ref="[35]",
    contexts=[
        "There has also been much work onprovenance, with increasing interestintherecentyears. Provenancecanbecapturedatdifferent granularities,andatdifferentlevelsofdetail. Inscientiﬁcworkﬂowsystems [1,2,12,13,13,14,29,33,35,36,54] where the operations are typically treated as black boxes, the provenance can usually be captured only at the level of datasets.",

    ],
))

DB(Citation(
    miao2016a, simmhan2006a, ref="[36]",
    contexts=[
        "There has also been much work onprovenance, with increasing interestintherecentyears. Provenancecanbecapturedatdifferent granularities,andatdifferentlevelsofdetail. Inscientiﬁcworkﬂowsystems [1,2,12,13,13,14,29,33,35,36,54] where the operations are typically treated as black boxes, the provenance can usually be captured only at the level of datasets.",

    ],
))

DB(Citation(
    miao2016a, Site("CKAN: an Open-Source Data Portal", "http://ckan.org"), ref="[37]",
    contexts=[
        "Several systems have been designed that focus on speciﬁc aspects of the proposed work, including collaborative data management(e.g.,Fusiontables[30],Orchestra[23],CQMS[20,26],LabBook[24]),datasharing(e.g.,SQLShare[19,20,21],SMILE[34]), hosted data repositories accessible to applications (CKAN [37], Domo [46]), hosted data science (Domino [45]), as well as data publishingtools(Quandl[49],Factual[47],DataMarket[44]). None of them, however, aim to capture a broad range of metadata and provenance information in a uniﬁed fashion, to support high-level analysis and reasoning over data science pipelines.",

    ],
))

DB(Citation(
    miao2016a, Site("IPython", "http://ipython.org"), ref="[38]",
    contexts=[
        "A wide range of analytic packages like SAS [51], Excel [40], R [50], Matlab [48], and Mahout[39],ordatasciencetoolkitssuchasIPython[38],Scikit[42], andPandas[41], arefrequentlyusedforperforminganalysisitself; however,thoselackcomprehensivedatamanagementorcollaboration capabilities.",

    ],
))

DB(Citation(
    miao2016a, Site("Apache Mahout Machine Learning Library", "http://mahout.apache.org"), ref="[39]",
    contexts=[
        "A wide range of analytic packages like SAS [51], Excel [40], R [50], Matlab [48], and Mahout[39],ordatasciencetoolkitssuchasIPython[38],Scikit[42], andPandas[41], arefrequentlyusedforperforminganalysisitself; however,thoselackcomprehensivedatamanagementorcollaboration capabilities.",

    ],
))

DB(Citation(
    miao2016a, Site("Microsoft Excel", "http://office.microsoft.com/en-us/excel/"), ref="[40]",
    contexts=[
        "A wide range of analytic packages like SAS [51], Excel [40], R [50], Matlab [48], and Mahout[39],ordatasciencetoolkitssuchasIPython[38],Scikit[42], andPandas[41], arefrequentlyusedforperforminganalysisitself; however,thoselackcomprehensivedatamanagementorcollaboration capabilities.",

    ],
))

DB(Citation(
    miao2016a, Site("Python Data Analysis Library", "http://pandas.pydata.org"), ref="[41]",
    contexts=[
        "A wide range of analytic packages like SAS [51], Excel [40], R [50], Matlab [48], and Mahout[39],ordatasciencetoolkitssuchasIPython[38],Scikit[42], andPandas[41], arefrequentlyusedforperforminganalysisitself; however,thoselackcomprehensivedatamanagementorcollaboration capabilities.",

    ],
))

DB(Citation(
    miao2016a, Site("Scikit-Learn: Machine Learning in Python", "http://scikit-learn.org"), ref="[42]",
    contexts=[
        "A wide range of analytic packages like SAS [51], Excel [40], R [50], Matlab [48], and Mahout[39],ordatasciencetoolkitssuchasIPython[38],Scikit[42], andPandas[41], arefrequentlyusedforperforminganalysisitself; however,thoselackcomprehensivedatamanagementorcollaboration capabilities.",

    ],
))

DB(Citation(
    miao2016a, Site("Google Prediction API", "https://cloud.google.com/prediction"), ref="[43]",
    contexts=[

    ],
))

DB(Citation(
    miao2016a, Site("Data Market Inc", "http://www.datamarket.com"), ref="[44]",
    contexts=[
        "Several systems have been designed that focus on speciﬁc aspects of the proposed work, including collaborative data management(e.g.,Fusiontables[30],Orchestra[23],CQMS[20,26],LabBook[24]),datasharing(e.g.,SQLShare[19,20,21],SMILE[34]), hosted data repositories accessible to applications (CKAN [37], Domo [46]), hosted data science (Domino [45]), as well as data publishingtools(Quandl[49],Factual[47],DataMarket[44]). None of them, however, aim to capture a broad range of metadata and provenance information in a uniﬁed fashion, to support high-level analysis and reasoning over data science pipelines.",

    ],
))

DB(Citation(
    miao2016a, Site("Domino Data Lab", "http://www.dominoup.com"), ref="[45]",
    contexts=[
        "Several systems have been designed that focus on speciﬁc aspects of the proposed work, including collaborative data management(e.g.,Fusiontables[30],Orchestra[23],CQMS[20,26],LabBook[24]),datasharing(e.g.,SQLShare[19,20,21],SMILE[34]), hosted data repositories accessible to applications (CKAN [37], Domo [46]), hosted data science (Domino [45]), as well as data publishingtools(Quandl[49],Factual[47],DataMarket[44]). None of them, however, aim to capture a broad range of metadata and provenance information in a uniﬁed fashion, to support high-level analysis and reasoning over data science pipelines.",

    ],
))

DB(Citation(
    miao2016a, Site("Domo Lab", "http://www.domo.org"), ref="[46]",
    contexts=[
        "Several systems have been designed that focus on speciﬁc aspects of the proposed work, including collaborative data management(e.g.,Fusiontables[30],Orchestra[23],CQMS[20,26],LabBook[24]),datasharing(e.g.,SQLShare[19,20,21],SMILE[34]), hosted data repositories accessible to applications (CKAN [37], Domo [46]), hosted data science (Domino [45]), as well as data publishingtools(Quandl[49],Factual[47],DataMarket[44]). None of them, however, aim to capture a broad range of metadata and provenance information in a uniﬁed fashion, to support high-level analysis and reasoning over data science pipelines.",

    ],
))

DB(Citation(
    miao2016a, Site("Factual Inc", "http://www.factual.com"), ref="[47]",
    contexts=[
        "Several systems have been designed that focus on speciﬁc aspects of the proposed work, including collaborative data management(e.g.,Fusiontables[30],Orchestra[23],CQMS[20,26],LabBook[24]),datasharing(e.g.,SQLShare[19,20,21],SMILE[34]), hosted data repositories accessible to applications (CKAN [37], Domo [46]), hosted data science (Domino [45]), as well as data publishingtools(Quandl[49],Factual[47],DataMarket[44]). None of them, however, aim to capture a broad range of metadata and provenance information in a uniﬁed fashion, to support high-level analysis and reasoning over data science pipelines.",

    ],
))

DB(Citation(
    miao2016a, Site("Mathworks Matlab", "http://www.mathworks.com"), ref="[48]",
    contexts=[
        "A wide range of analytic packages like SAS [51], Excel [40], R [50], Matlab [48], and Mahout[39],ordatasciencetoolkitssuchasIPython[38],Scikit[42], andPandas[41], arefrequentlyusedforperforminganalysisitself; however,thoselackcomprehensivedatamanagementorcollaboration capabilities.",

    ],
))

DB(Citation(
    miao2016a, Site("Quandl", "http://www.quandl.com"), ref="[49]",
    contexts=[
        "Several systems have been designed that focus on speciﬁc aspects of the proposed work, including collaborative data management(e.g.,Fusiontables[30],Orchestra[23],CQMS[20,26],LabBook[24]),datasharing(e.g.,SQLShare[19,20,21],SMILE[34]), hosted data repositories accessible to applications (CKAN [37], Domo [46]), hosted data science (Domino [45]), as well as data publishingtools(Quandl[49],Factual[47],DataMarket[44]). None of them, however, aim to capture a broad range of metadata and provenance information in a uniﬁed fashion, to support high-level analysis and reasoning over data science pipelines.",

    ],
))

DB(Citation(
    miao2016a, Site("The R Project", "http://www.r-project.org"), ref="[50]",
    contexts=[
        "A wide range of analytic packages like SAS [51], Excel [40], R [50], Matlab [48], and Mahout[39],ordatasciencetoolkitssuchasIPython[38],Scikit[42], andPandas[41], arefrequentlyusedforperforminganalysisitself; however,thoselackcomprehensivedatamanagementorcollaboration capabilities.",

    ],
))

DB(Citation(
    miao2016a, Site("SAS Business Analytics Software", "http://www.sas.com"), ref="[51]",
    contexts=[
        "A wide range of analytic packages like SAS [51], Excel [40], R [50], Matlab [48], and Mahout[39],ordatasciencetoolkitssuchasIPython[38],Scikit[42], andPandas[41], arefrequentlyusedforperforminganalysisitself; however,thoselackcomprehensivedatamanagementorcollaboration capabilities.",

    ],
))

DB(Citation(
    miao2016a, vartak2016a, ref="[52]",
    contexts=[
        "Several recent systems have attemptedtoaddressend-to-endissues,includingmodelserving(e.g., TensorFlow Serving, Velox [9], MSMS [27], ModelDB [52]).",

    ],
))

DB(Citation(
    miao2016a, widom2005a, ref="[53]",
    contexts=[
        "On the other hand, in dataﬂow systems where the operators are written in a declarative language (e.g., SQL, Pig Latin, Spark), data provenance at record levelcanbecapturedifneeded[5,6,8,10,17,22,31,53].",

    ],
))

DB(Citation(
    miao2016a, buyya2005a, ref="[54]",
    contexts=[
        "There has also been much work onprovenance, with increasing interestintherecentyears. Provenancecanbecapturedatdifferent granularities,andatdifferentlevelsofdetail. Inscientiﬁcworkﬂowsystems [1,2,12,13,13,14,29,33,35,36,54] where the operations are typically treated as black boxes, the provenance can usually be captured only at the level of datasets.",

    ],
))

DB(Citation(
    miao2016a, zhang2016a, ref="[55]",
    contexts=[
        "Muchofthatworkhasfocusedonthe“training” aspect; several general-purpose systems like GraphLab, TensorFlow,ParameterServer,etc.,havebeendesignedovertheyears, and there is also much work on speciﬁc aspects of ML pipeline (e.g., feature engineering [55].",

    ],
))

DB(Citation(
    miao2016a, zhao2006a, ref="[56]",
    contexts=[
        "Workﬂow provenance may include: a) prospective information about the deﬁnition of the workﬂow, b) retrospective information during the execution of the workﬂow,c)metadataaboutblocksanddatasetsinaworkﬂow,and d) input/output lineages among blocks [56].",

    ],
))

DB(Citation(
    schubert2016a, miao2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    hellerstein2017a, miao2016a, ref="",
    contexts=[

    ],
))
