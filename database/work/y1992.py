# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *


cate1992a = DB(WorkUnrelated(
    1992, "Alex-a global filesystem",
    due="Unrelated to provenance. Unrelated to scripts",
    display="cate",
    authors="Cate, Vincent",
    place=HotStorage,
    file="Cate1992a.pdf",
    pp="1--12",
    entrytype="inproceedings",
    cluster_id="17442267408440459488",
    number="7330",
    scholar="http://scholar.google.com/scholar?cites=17442267408440459488&as_sdt=2005&sciodt=0,5&hl=en",
    organization="Citeseer",
    scholar_ok=True,
))

claerbout1992a = DB(WorkUnrelated(
    1992, "Electronic documents give reproducible research a new meaning",
    due="Does not propose an automatic solution for supporting reproducibility",
    star="[repro][x] motivates the need for reproducibility",
    may_be_related_to=["reproducibility"],
    display="claerbout",
    authors="Claerbout, Jon and Karrenbach, Martin",
    place=SEG,
    organization="SEG",
    local="New Orleans, Louisiana, USA",
    file="Claerbout1992a.pdf",
    summary="Talks about the need for reprocibility in eletronic documents; proposes some initial ideas on how to achieved it manually",
    pp="601--604",
    doi="10.1190/1.1822162",
    link="http://link.aip.org/link/SEGEAB/v11/i1/p601/s1\&Agg=doi",
    entrytype="inproceedings",
    cluster_id="13200858648614530433",
    scholar="http://scholar.google.com/scholar?cites=13200858648614530433&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

fitzgerald1992a = DB(WorkUnrelated(
    1992, "A New Windows-Based Statistical Analysis",
    due="Unrelated to provenance. Unrelated to scripts",
    aliases=[
        (2012, "A New Windows-Based Statistical Analysis", "FitzGerald, GC and Hurley, TA"),
        (1992, "A New Windows-Based Statistical Analysis Environment", "FitzGerald, GC and Hurley, TA"),
    ],
    display="fitzgerald",
    authors="FitzGerald, GC and Hurley, TA",
    pp="133--148",
    place=COMPSTAT,
    file="Fitzgerald1992a.pdf",
    organization="Springer Science & Business Media",
    ID="fitzgerald2012new",
    entrytype="inproceedings",
    scholar_ok=True,
))

gehani1992a = DB(WorkUnrelated(
    1992, "Exceptional C or C with Exceptions",
    due="Unrelated to scripts. Unrelated to provenance",
    display="gehani",
    authors="Gehani, Narain H.",
    place=SPE,
    file="Gehani1992a.pdf",
    pp="827--848",
    number="10",
    volume="22",
    entrytype="article",
    cluster_id="1325363126854395229",
    publisher="Wiley Online Library",
    scholar="http://scholar.google.com/scholar?cites=1325363126854395229&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

horwitz1992a = DB(WorkUnrelated(
    1992, "The use of program dependence graphs in software engineering",
    due="Unrelated to provenance. The techniques described here could be used for obtaining provenance, but it is not the focus of the paper",
    may_be_related_to=["program slicing"],
    display="horwitz",
    authors="Horwitz, Susan and Reps, Thomas",
    summary="Discusses how program dependence graphs (PDG) can be used together with program slincing to address SE problems, such as understanding what existing program does and how it works, understanding differences between version, and reusing parts of old versions",
    place=ICSE,
    file="Horwitz1992a.pdf",
    pp="392--411",
    entrytype="inproceedings",
    cluster_id="5429211019947941376",
    organization="ACM",
    scholar="http://scholar.google.com/scholar?cites=5429211019947941376&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
    publisher="ACM",
))

mcintosh1992a = DB(WorkUnrelated(
    1992, "SHAW: An Auditor for S",
    may_be_related_to=["visualization"],
    due="Unrelated to script collection",
    summary="Graphical editor for becker1988a provenance",
    display="mcintosh",
    authors="McIntosh, Allen A",
    pp="451--455",
    place=Interface,
    file="Mcintosh1992a.pdf#page=462",
    ID="mcintosh1992shaw",
    entrytype="incollection",
    publisher="Springer",
    scholar_ok=True,
))

rivest1992a = DB(WorkUnrelated(
    1992, "The MD5 message-digest algorithm",
    due="Unrelated to provenance. Unrelated to scripts",
    display="rivest",
    authors="Rivest, Ronald",
    summary="Describes the MD5 Algorithm",
    place=Web,
    number="RFC 1321",
    local="MIT Laboratory for Computer Science, Cambridge, MA, April 1992",
    link="http://www.freesoft.org/CIE/RFC/1321/index.htm",
    entrytype="article",
    scholar="http://scholar.google.com/scholar?cites=1644810191891842772&as_sdt=2005&sciodt=0,5&hl=en",
    cluster_id="1644810191891842772",
    scholar_ok=True,
))

wadler1992a = DB(WorkUnrelated(
    1992, "Comprehending monads",
    due="Unrelated to provenance at all",
    display="wadler",
    authors="Wadler, Philip",
    summary="Shows how list comprehensions may be generalised to an arbitrary monad",
    place=MSCS,
    file="Wadler1992a.pdf",
    volume="2",
    pp="461--493",
    entrytype="article",
    scholar="http://scholar.google.com/scholar?cites=6992593365790220682&as_sdt=2005&sciodt=0,5&hl=en",
    number="04",
    publisher="Cambridge Univ Press",
    cluster_id="6992593365790220682",
    scholar_ok="aprox",
))
