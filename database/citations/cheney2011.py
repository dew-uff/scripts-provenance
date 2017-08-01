# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1977 import cousot1977a
from ..work.y1981 import weiser1981a
from ..work.y1990 import wang1990a
from ..work.y1992 import wadler1992a
from ..work.y1994 import buneman1994a
from ..work.y1995 import abiteboul1995a
from ..work.y1995 import buneman1995a
from ..work.y1996 import abadi1996a
from ..work.y1996 import volpano1996a
from ..work.y1996 import wong1996a
from ..work.y1997 import biswas1997a
from ..work.y1997 import woodruff1997a
from ..work.y1998 import field1998a
from ..work.y1999 import abadi1999a
from ..work.y1999 import myers1999a
from ..work.y2000 import cui2000a
from ..work.y2000 import lynch2000a
from ..work.y2001 import buneman2001a
from ..work.y2001 import palsberg2001a
from ..work.y2002 import buneman2002a
from ..work.y2003 import acar2003a
from ..work.y2003 import sabelfeld2003a
from ..work.y2005 import simmhan2005b
from ..work.y2005 import bhagwat2005a
from ..work.y2005 import bose2005a
from ..work.y2005 import nielson2005a
from ..work.y2006 import muniswamy2006a
from ..work.y2006 import benjelloun2006a
from ..work.y2006 import buneman2006a
from ..work.y2006 import foster2006a
from ..work.y2006 import geerts2006a
from ..work.y2007 import cheney2007a
from ..work.y2007 import cheney2007b
from ..work.y2007 import green2007a
from ..work.y2007 import hidders2007a
from ..work.y2008 import buneman2008a
from ..work.y2008 import buneman2008b
from ..work.y2008 import moreau2008b
from ..work.y2008 import acar2008a
from ..work.y2008 import foster2008a
from ..work.y2008 import jia2008a
from ..work.y2008 import shroff2008a
from ..work.y2008 import swamy2008a
from ..work.y2009 import acar2009a
from ..work.y2009 import cheney2009a
from ..work.y2009 import swamy2009a
from ..work.y2011 import cheney2011a


DB(Citation(
    cheney2011a, abadi1996a, ref="[Abadi et al., 1996]",
    contexts=[
        "However, these intuitions {contribution, influence and relevance} have also motivated rigorous approaches to seemingly quite different problems, such as ... supporting efficient memoization and caching [Abadi et al., 1996, Acar et al., 2003]]",
        "Dependency tracking is also important in memoization and caching techniques [Abadi et al., 1996, Acar et al., 2003]. For example, Abadi et al. [1996] study an approach to caching the results of function calls in a software configuration management system, based on a label-propagating operational semantics. Acar et al. [2003] develop a language-based approach to memoizing and caching the results of functional programs.",
    ],
))

DB(Citation(
    cheney2011a, abadi1999a, ref="[Abadi et al., 1999]",
    contexts=[
        "As Abadi et al. [1999] have argued, slicing, information flow, and several other program analysis techniques can all be understood in terms of dependence",
        "Abadi et al. [1999] argue that techniques such as slicing, information-flow security, and other program analyses such as binding-time analysis can be given a uniform treatment by translating to a common Dependency Core Calculus. We believe provenance may also fit into this picture, but in this article, we consideredbothdynamicandstatic labeling,whereas the Dependency Core Calculus only allows for static labels.",
    ],
))

DB(Citation(
    cheney2011a, abiteboul1995a, ref="[Abiteboul et al., 1995]",
    contexts=[
        "By analogy with generic queries in relational databases [Abiteboul et al.,1995], such a-functions ought to behave in a way that is insensitive to the particular choice of colors",
    ],
))

DB(Citation(
    cheney2011a, acar2009a, ref="[Acar et al., 2009]",
    contexts=[
        "In self-adjusting computation[Acar et al., 2008, Acar, 2009], supportfor efficient incremental recomputation is provided at a language level",
    ],
))

DB(Citation(
    cheney2011a, acar2003a, ref="[Acar et al., 2003]",
    contexts=[
        "However, these intuitions {contribution, influence and relevance} have also motivated rigorous approaches to seemingly quite different problems, such as ... supporting efficient memoization and caching [Abadi et al., 1996, Acar et al., 2003]]",
        "Dependency tracking is also important in memoization and caching techniques [Abadi et al., 1996, Acar et al., 2003]. For example, Abadi et al. [1996] study an approach to caching the results of function calls in a software configuration management system, based on a label-propagating operational semantics. Acar et al. [2003] develop a language-based approach to memoizing and caching the results of functional programs.",
    ],
))

DB(Citation(
    cheney2011a, acar2008a, ref="[Acar et al., 2008]",
    contexts=[
        "In self-adjusting computation[Acar et al., 2008, Acar, 2009], supportfor efficient incremental recomputation is provided at a language level",
    ],
))

DB(Citation(
    cheney2011a, benjelloun2006a, ref="[Benjelloun et al., 2006]",
    contexts=[
        "Recent research on annotations, uncertainty, and incomplete information [Benjelloun et al.,2006, Bhagwat et al., 2005, Geerts et al., 2006] has also drawn on these approaches to provenance; in particular, definitions of provenance have been used to justify annotation-propagationbehaviors in these systems",
    ],
))

DB(Citation(
    cheney2011a, bhagwat2005a, ref="[Bhagwat et al., 2005]",
    contexts=[
        "Recent research on annotations, uncertainty, and incomplete information [Benjelloun et al.,2006, Bhagwat et al., 2005, Geerts et al., 2006] has also drawn on these approaches to provenance; in particular, definitions of provenance have been used to justify annotation-propagationbehaviors in these systems",
        "Simple SQL queries can easily be translated to equivalent SQL queries that automatically aggregate annotations in this way, using techniques similar to those used in the DBNotes system [Bhagwat et al., 2005]."
    ],
))

DB(Citation(
    cheney2011a, biswas1997a, ref="[Biswas et al., 1997]",
    contexts=[
        "However, these intuitions {contribution, influence and relevance} have also motivated rigorous approaches to seemingly quite different problems, such as aiding debugging via program slicing [Biswas, 1997, Field and Tip, 1998, Weiser, 1981]",
        "In program slicing [Biswas, 1997, Field and Tip, 1998, Weiser, 1981], the goal is to identify a (small) set of program points whose execution contributes to the value of an output variable (or other observable behavior)",
    ],
))

DB(Citation(
    cheney2011a, bose2005a, ref="[Bose and Frew, 2005]",
    contexts=[
        "Provenance is information about the origin, ownership, influences upon, or other historical or contextual information about an object. Such information has many applications, including evaluating integrity or authenticity claims, detecting and repairing errors, and memoizing and caching the results of computations such as scientific workflows [Lynch, 2000, Bose and Frew, 2005, Simmhan et al.,2005]",
        "Richer provenance tracking techniques have been studied in a variety of settings, including ...  scientific workflows [Bose and Frew, 2005, Simmhan et al., 2005]",
        "Provenance has also been studied in geospatial and scientific computation [Bose and Frew, 2005, Foster and Moreau, 2006, Simmhan et al., 2005], particularly forworkflows (visual programs written by scientists).",
    ],
))

DB(Citation(
    cheney2011a, buneman1994a, ref="[Buneman et al., 1994]",
    contexts=[
        "In this article, we arguethat data dependenceprovidesa solid semantic foundationfora provenance technique that highlights parts of the input on which each part of the output depend. We work in the setting of the nested relational calculus (NRC) [Buneman et al., 1994, 1995, Wong, 1996], a core language for database queries that is closely related to monad algebra [Wadler, 1992]",
    ],
))

DB(Citation(
    cheney2011a, buneman1995a, ref="[Buneman et al., 1995]",
    contexts=[
        "In this article, we arguethat data dependenceprovidesa solid semantic foundationfora provenance technique that highlights parts of the input on which each part of the output depend. We work in the setting of the nested relational calculus (NRC) [Buneman et al., 1994, 1995, Wong, 1996], a core language for database queries that is closely related to monad algebra [Wadler, 1992]",
        "We will provide a brief review of the nested relational calculus (NRC) [Buneman et al., 1995], a core database query language which is closely related to monad algebra [Wadler, 1992].",
        "As discussed in previous work [Buneman et al., 1995], the NRC can express a wide variety of queries including ordinary relational queries, nested subqueries, and grouping and aggregation queries.",
    ],
))

DB(Citation(
    cheney2011a, buneman2001a, ref="[Buneman et al., 2001]",
    contexts=[
        "Richer provenance tracking techniques have been studied in a variety of settings, including databases [Cui et al., 2000, Buneman et al., 2001, 2008b, Foster et al., 2008, Green et al., 2007]",
        "Provenance for database queries has been studied by a number of researchers, beginning in the early 1990s [Buneman et al., 2001, 2002, 2008b, Cui et al., 2000, Green et al., 2007, Wang and Madnick, 1990, Woodruff and Stonebraker, 1997].",
        "In why- and where-provenance, introduced by Buneman et al. [2001], provenance is studied in a deterministic tree data model, in which each part of the database can be addressed by a uniquepath. Buneman et al. [2001]considered two forms of provenance: why-provenance, which consists of a set of witnesses, or subtrees of the input that suffice to explain a part of the output, and where-provenance, which consists of a single part of the input from which a given part of the output was copied. Both forms of provenance are sensitive to query rewriting in general, but Buneman et al. [2001] discussed normal forms for queries that avoid this problem.",
        "Accordingly, the provenance information provided by these approaches {[Buneman et al.,2006, 2008b]} only connects data to exact copies in other locations, and does not track provenance through other operations. In this sense, it is similar to the where-provenance approach considered by Buneman et al. [2001] for database queries.",
    ],
))

DB(Citation(
    cheney2011a, buneman2002a, ref="[Buneman et al., 2002]",
    contexts=[
        "Provenance for database queries has been studied by a number of researchers, beginning in the early 1990s [Buneman et al., 2001, 2002, 2008b, Cui et al., 2000, Green et al., 2007, Wang and Madnick, 1990, Woodruff and Stonebraker, 1997].",
    ],
))

DB(Citation(
    cheney2011a, buneman2006a, ref="[Buneman et al., 2006]",
    contexts=[
        "Some recent work has generalized where-provenance to database updates [Buneman et al.,2006, 2008b], motivated by curated scientific databases that are updated frequently, often by (manual) copying from other sources",
    ],
))

DB(Citation(
    cheney2011a, buneman2008a, ref="[Buneman et al., 2008a]",
    contexts=[
        "Provenanceis particularly important in scientific computation and record-keeping, since it is considered essential for ensuring the repeatabilityof experimentsand judging the scientific value of their results [Buneman et al., 2008a]",
        "please see Buneman et al. [2008a] and Cheney et al. [2009] for more complete discussion of research on provenance in databases",
    ],
))

DB(Citation(
    cheney2011a, buneman2008b, ref="[Buneman et al., 2008b]",
    contexts=[
        "Richer provenance tracking techniques have been studied in a variety of settings, including databases [Cui et al., 2000, Buneman et al., 2001, 2008b, Foster et al., 2008, Green et al., 2007]",
        "Provenance for database queries has been studied by a number of researchers, beginning in the early 1990s [Buneman et al., 2001, 2002, 2008b, Cui et al., 2000, Green et al., 2007, Wang and Madnick, 1990, Woodruff and Stonebraker, 1997].",
        "Buneman et al. [2008b] introduced a model of where-provenancefor the nested relational calculus. In their approach each part of the database is tagged with an optional annotation, or color; colors are propagated to the output so as to indicate where parts of the output have been copied from in the input.",
        "Some recent work has generalized where-provenance to database updates [Buneman et al.,2006, 2008b], motivated by curated scientific databases that are updated frequently, often by (manual) copying from other sources",
        "Although our definition of dependency correctness could also be used for updates, it is not clear whether this yields a useful form of provenance, and we plan to investigate alternative dependency conditions that are more suitable for updates, usingthe update language employed in [Buneman et al., 2008b].",
        "One technique (familiar from many program analyses [Nielson et al., 2005] as well as other work on provenance [Buneman et al., 2008b, Wang and Madnick, 1990]) is to enrich the data model with annotationsthat can be used to refer to parts of the value.",
        "The model we investigate in this article is similar to that of Buneman et al. [2008b] in many respects. There are two salient differences. The first difference is that Buneman et al. [2008b] propagates annotations comprising single (optional) input locations, whereas our approach propagates annotations consisting of sets of input locations. The second difference is that our approach provides a strong semantic guarantee formulated in terms of dependence, whereas in contrast the semantics of where-provenance in Buneman et al. [2008b] is an ad hoc syntactic definition justified by a database-theoretic expressiveness result, not a dependency property.",
        "Buneman et al.[2008b] discuss implementing provenance tracking as a source-to-source translation from NRC queries to NRC extended with a new base type color.",
    ],
))

DB(Citation(
    cheney2011a, cheney2007a, ref="[Cheney, 2007]",
    contexts=[
        "Cheney [2007] discusses the relationship between program slicing and dependency analysis at a high level, complementing the technical details presented in this article",
    ],
))

DB(Citation(
    cheney2011a, cheney2007b, ref="[Cheney et al., 2007]",
    contexts=[
        "This paper is a revised and extended version of [Cheney et al., 2007].",
    ],
))

DB(Citation(
    cheney2011a, cheney2009a, ref="[Cheney et al., 2009]",
    contexts=[
        "please see Buneman et al. [2008a] and Cheney et al. [2009] for more complete discussion of research on provenance in databases",
    ],
))

DB(Citation(
    cheney2011a, cousot1977a, ref="[Cousot et al., 1977]",
    contexts=[
        "Moreover, it appears possible to cast our results in the abstract interpretation framework [Cousot and Cousot, 1977] that is widely used in static analysis (see e.g. Nielson et al. [2005, ch. 4] for an introduction).",
    ],
))

DB(Citation(
    cheney2011a, cui2000a, ref="[Cui et al., 2000]",
    contexts=[
        "Richer provenance tracking techniques have been studied in a variety of settings, including databases [Cui et al., 2000, Buneman et al., 2001, 2008b, Foster et al., 2008, Green et al., 2007]",
        "Provenance for database queries has been studied by a number of researchers, beginning in the early 1990s [Buneman et al., 2001, 2002, 2008b, Cui et al., 2000, Green et al., 2007, Wang and Madnick, 1990, Woodruff and Stonebraker, 1997].",
    ],
))

DB(Citation(
    cheney2011a, field1998a, ref="[Field and Tip, 1998]",
    contexts=[
        "However, these intuitions {contribution, influence and relevance} have also motivated rigorous approaches to seemingly quite different problems, such as aiding debugging via program slicing [Biswas, 1997, Field and Tip, 1998, Weiser, 1981]",
        "In program slicing [Biswas, 1997, Field and Tip, 1998, Weiser, 1981], the goal is to identify a (small) set of program points whose execution contributes to the value of an output variable (or other observable behavior)",
    ],
))

DB(Citation(
    cheney2011a, foster2006a, ref="[Foster and Moreau, 2006]",
    contexts=[
        "Provenance has also been studied in geospatial and scientific computation [Bose and Frew, 2005, Foster and Moreau, 2006, Simmhan et al., 2005], particularly forworkflows (visual programs written by scientists).",
    ],
))

DB(Citation(
    cheney2011a, foster2008a, ref="[Foster et al., 2008]",
    contexts=[
        "Richer provenance tracking techniques have been studied in a variety of settings, including databases [Cui et al., 2000, Buneman et al., 2001, 2008b, Foster et al., 2008, Green et al., 2007]",
        "Foster et al. [2008] extendedthis approachto handle NRC queries and an unordered variant of XML",
    ],
))

DB(Citation(
    cheney2011a, geerts2006a, ref="[Geerts et al., 2006]",
    contexts=[
        "Recent research on annotations, uncertainty, and incomplete information [Benjelloun et al.,2006, Bhagwat et al., 2005, Geerts et al., 2006] has also drawn on these approaches to provenance; in particular, definitions of provenance have been used to justify annotation-propagationbehaviors in these systems",
    ],
))

DB(Citation(
    cheney2011a, green2007a, ref="[Green et al., 2007]",
    contexts=[
        "Richer provenance tracking techniques have been studied in a variety of settings, including databases [Cui et al., 2000, Buneman et al., 2001, 2008b, Foster et al., 2008, Green et al., 2007]",
        "Provenance for database queries has been studied by a number of researchers, beginning in the early 1990s [Buneman et al., 2001, 2002, 2008b, Cui et al., 2000, Green et al., 2007, Wang and Madnick, 1990, Woodruff and Stonebraker, 1997].",
        "Green et al. [2007] showed that relations with semiring-valuedannotations on rows generalize several variations of the relational model, including set, bag, probabilistic, and incomplete information models, and identified a relationship between free semiring-valued relations and why-provenance",
    ],
))

DB(Citation(
    cheney2011a, hidders2007a, ref="[Hidders et al., 2007]",
    contexts=[
        "One principled approach recently introduced by Hidders et al. [2007] defines provenance for the nested relational calculus augmented with additional function symbols that represent calls to scientific workflow components.",
    ],
))

DB(Citation(
    cheney2011a, jia2008a, ref="[Jia et al., 2008]",
    contexts=[
        "In computer security, it is often of interest to specify and enforce information-flow policies [Sabelfeld and Myers, 2003] that ensure that information marked secret can only be read by privileged users, and that privileged users cannot leak secret information by writing it to public locations. These properties are sometimes referred to as secrecy and integrity, respectively. Both can be enforced using static (e.g. [Myers, 1999, Volpano et al., 1996] or dynamic (e.g. [Shroff et al., 2008, Jia et al., 2008]) dependency tracking techniques",
        "Nevertheless there are many interesting possible connections that need to be explored, particularly in relating provenance to dynamic information flow tracking [Shroff et al., 2008] and integrating provenance security policies with other access-control, information-flow and audit policies [Swamy et al., 2008, Jia et al., 2008].",
    ],
))

DB(Citation(
    cheney2011a, lynch2000a, ref="[Lynch, 2000]",
    contexts=[
        "Provenance is information about the origin, ownership, influences upon, or other historical or contextual information about an object. Such information has many applications, including evaluating integrity or authenticity claims, detecting and repairing errors, and memoizing and caching the results of computations such as scientific workflows [Lynch, 2000, Bose and Frew, 2005, Simmhan et al., 2005]",
    ],
))

DB(Citation(
    cheney2011a, moreau2008b, ref="[Moreau et al., 2007]",
    contexts=[
        "In their simplest form (see e.g. the Provenance Challenge [Moreau et al., 2007]), workflows are essentially directed acyclic graphs (DAGs) representing a computation.",
    ],
))

DB(Citation(
    cheney2011a, muniswamy2006a, ref="[Muniswamy-Reddy et al., ]",
    contexts=[
        "Richer provenance tracking techniques have been studied in a variety of settings, including ... file systems[Muniswamy-Reddy et al., 2006]",
    ],
))

DB(Citation(
    cheney2011a, myers1999a, ref="[Myers et al., 1999]",
    contexts=[
        "In computer security, it is often of interest to specify and enforce information-flow policies [Sabelfeld and Myers, 2003] that ensure that information marked secret can only be read by privileged users, and that privileged users cannot leak secret information by writing it to public locations. These properties are sometimes referred to as secrecy and integrity, respectively. Both can be enforced using static (e.g. [Myers, 1999, Volpano et al., 1996] or dynamic (e.g. [Shroff et al., 2008, Jia et al., 2008]) dependency tracking techniques",
    ],
))

DB(Citation(
    cheney2011a, nielson2005a, ref="[Nielson et al., 2005]",
    contexts=[
        "One technique (familiar from many program analyses [Nielson et al., 2005] as well as other work on provenance [Buneman et al., 2008b, Wang and Madnick, 1990]) is to enrich the data model with annotationsthat can be used to refer to parts of the value.",
        "The techniques in Section 4 and Section 5 draw upon standard techniques in static analysis [Nielson et al., 2005, Palsberg, 2001]",
        "Moreover, it appears possible to cast our results in the abstract interpretation framework [Cousot and Cousot, 1977] that is widely used in static analysis (see e.g. Nielson et al. [2005, ch. 4] for an introduction).",
    ],
))


DB(Citation(
    cheney2011a, palsberg2001a, ref="[Palsberg et al., 2001]",
    contexts=[
        "We formulate the analysis as a type-based analysis[Palsberg, 2001]; annotated types (a-types) b τ and raw types (r-types) ω are defined as follows",
        "The techniques in Section 4 and Section 5 draw upon standard techniques in static analysis [Nielson et al., 2005, Palsberg, 2001]",
    ],
))

DB(Citation(
    cheney2011a, sabelfeld2003a, ref="[Sabelfeld and Myers, 2003]",
    contexts=[
        "However, these intuitions {contribution, influence and relevance} have also motivated rigorous approaches to seemingly quite different problems, such as ...  improving program security using information flow analysis [Sabelfeld and Myers, 2003]",
        "In computer security, it is often of interest to specify and enforce information-flow policies [Sabelfeld and Myers, 2003] that ensure that information marked secret can only be read by privileged users, and that privileged users cannot leak secret information by writing it to public locations. These properties are sometimes referred to as secrecy and integrity, respectively. Both can be enforced using static (e.g. [Myers, 1999, Volpano et al., 1996] or dynamic (e.g. [Shroff et al., 2008, Jia et al., 2008]) dependency tracking techniques",
    ],
))

DB(Citation(
    cheney2011a, shroff2008a, ref="[Shroff et al., 2008]",
    contexts=[
        "In computer security, it is often of interest to specify and enforce information-flow policies [Sabelfeld and Myers, 2003] that ensure that information marked secret can only be read by privileged users, and that privileged users cannot leak secret information by writing it to public locations. These properties are sometimes referred to as secrecy and integrity, respectively. Both can be enforced using static (e.g. [Myers, 1999, Volpano et al., 1996] or dynamic (e.g. [Shroff et al., 2008, Jia et al., 2008]) dependency tracking techniques",
        "Nevertheless there are many interesting possible connections that need to be explored, particularly in relating provenance to dynamic information flow tracking [Shroff et al., 2008] and integrating provenance security policies with other access-control, information-flow and audit policies [Swamy et al., 2008, Jia et al., 2008].",
    ],
))

DB(Citation(
    cheney2011a, simmhan2005b, ref="[Simmhan et al., 2005]",
    contexts=[
        "Provenance is information about the origin, ownership, influences upon, or other historical or contextual information about an object. Such information has many applications, including evaluating integrity or authenticity claims, detecting and repairing errors, and memoizing and caching the results of computations such as scientific workflows [Lynch, 2000, Bose and Frew, 2005, Simmhan et al., 2005]",
        "Provenance has also been studied in geospatial and scientific computation [Bose and Frew, 2005, Foster and Moreau, 2006, Simmhan et al., 2005], particularly forworkflows (visual programs written by scientists).",
    ],
))

DB(Citation(
    cheney2011a, swamy2008a, ref="[Swamy et al., 2008]",
    contexts=[
        "Nevertheless there are many interesting possible connections that need to be explored, particularly in relating provenance to dynamic information flow tracking [Shroff et al., 2008] and integrating provenance security policies with other access-control, information-flow and audit policies [Swamy et al., 2008, Jia et al., 2008].",
        "Our approachto provenancetrackingbased on dependencyanalysis has been used in the Fable system [Swamy et al., 2008]. In this work provenance is one of a large class of security policies that can be implemented using Fable, a dependently-typedlanguage for specifying security policies. Subsequently, Swamy et al. [2009] have explored a theory of typed coercions that can be used to implement dependency provenance.",
    ],
))

DB(Citation(
    cheney2011a, swamy2009a, ref="[Swamy et al., 2009]",
    contexts=[
        "Our approachto provenancetrackingbased on dependencyanalysis has been used in the Fable system [Swamy et al., 2008]. In this work provenance is one of a large class of security policies that can be implemented using Fable, a dependently-typedlanguage for specifying security policies. Subsequently, Swamy et al. [2009] have explored a theory of typed coercions that can be used to implement dependency provenance.",
    ],
))

DB(Citation(
    cheney2011a, volpano1996a, ref="[Volpano et al., 1996]",
    contexts=[
        "In computer security, it is often of interest to specify and enforce information-flow policies [Sabelfeld and Myers, 2003] that ensure that information marked secret can only be read by privileged users, and that privileged users cannot leak secret information by writing it to public locations. These properties are sometimes referred to as secrecy and integrity, respectively. Both can be enforced using static (e.g. [Myers, 1999, Volpano et al., 1996] or dynamic (e.g. [Shroff et al., 2008, Jia et al., 2008]) dependency tracking techniques",
    ],
))

DB(Citation(
    cheney2011a, wadler1992a, ref="[Wadler, 1992]",
    contexts=[
        "In this article, we arguethat data dependenceprovidesa solid semantic foundationfora provenance technique that highlights parts of the input on which each part of the output depend. We work in the setting of the nested relational calculus (NRC) [Buneman et al., 1994, 1995, Wong, 1996], a core language for database queries that is closely related to monad algebra [Wadler, 1992]",
        "We will provide a brief review of the nested relational calculus (NRC) [Buneman et al., 1995], a core database query language which is closely related to monad algebra [Wadler, 1992].",
    ],
))

DB(Citation(
    cheney2011a, wang1990a, ref="[Wang and Madnick, 1990]",
    contexts=[
        "Provenance for database queries has been studied by a number of researchers, beginning in the early 1990s [Buneman et al., 2001, 2002, 2008b, Cui et al., 2000, Green et al., 2007, Wang and Madnick, 1990, Woodruff and Stonebraker, 1997].",
        "One technique (familiar from many program analyses [Nielson et al., 2005] as well as other work on provenance [Buneman et al., 2008b, Wang and Madnick, 1990]) is to enrich the data model with annotationsthat can be used to refer to parts of the value.",
    ],
))

DB(Citation(
    cheney2011a, weiser1981a, ref="[Weiser et al., 1981]",
    contexts=[
        "However, these intuitions {contribution, influence and relevance} have also motivated rigorous approaches to seemingly quite different problems, such as aiding debugging via program slicing [Biswas, 1997, Field and Tip, 1998, Weiser, 1981]",
        "This is analogous to the notion of dependence underlying program slicing [Weiser, 1981], a debugging aid that identifies the parts of a program on which a program output may depend",
        "In program slicing [Biswas, 1997, Field and Tip, 1998, Weiser, 1981], the goal is to identify a (small) set of program points whose execution contributes to the value of an output variable (or other observable behavior)",
    ],
))

DB(Citation(
    cheney2011a, wong1996a, ref="[Wong et al., 1996]",
    contexts=[
        "In this article, we arguethat data dependenceprovidesa solid semantic foundationfora provenance technique that highlights parts of the input on which each part of the output depend. We work in the setting of the nested relational calculus (NRC) [Buneman et al., 1994, 1995, Wong, 1996], a core language for database queries that is closely related to monad algebra [Wadler, 1992]",
        "It is well known that flat NRC queries whose input and output types do not involve nested set types and that do not involve grouping or aggregation and map sets of records to sets of records can be translated back to SQL via a normalization process [Wong, 1996]",
    ],
))

DB(Citation(
    cheney2011a, woodruff1997a, ref="[Woodruff and Stonebraker, 1997]",
    contexts=[
        "Provenance for database queries has been studied by a number of researchers, beginning in the early 1990s [Buneman et al., 2001, 2002, 2008b, Cui et al., 2000, Green et al., 2007, Wang and Madnick, 1990, Woodruff and Stonebraker, 1997].",
    ],
))