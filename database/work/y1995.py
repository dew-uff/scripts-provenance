# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *


abiteboul1995a = DB(WorkUnrelated(
    1995, "Foundations of databases: the logical level",
    due="Unrelated to provenance and scripts",
    display="abiteboul",
    authors="Abiteboul, Serge and Hull, Richard and Vianu, Victor",
    summary="Book about DB",
    place=Book,
    file="Abiteboul1995a.pdf",
    publisher="Addison-Wesley Longman Publishing Co., Inc.",
    isbn="0-201-53771-0",
    entrytype="book",
    scholar="http://scholar.google.com/scholar?cites=3658632990711000694&as_sdt=2005&sciodt=0,5&hl=en",
    cluster_id="3658632990711000694",
    scholar_ok=True,
))

badsberg1995a = DB(WorkUnrelated(
    1995, "An environment for graphical models",
    due="Unrelated to Provenance. Uses becker1988a",
    display="badsberg",
    authors="Badsberg, Jens Henrik",
    place=Thesis,
    file="Badsberg1995a.pdf",
    cluster_id="5475808195143614917",
    ID="badsberg1995environment",
    entrytype="phdthesis",
    scholar="http://scholar.google.com/scholar?cites=5475808195143614917&as_sdt=2005&sciodt=0,5&hl=en",
    local="Aalborg University, Institute of Electronic Systems, Department of Mathematics and Computer Science",
    school="Aalborg University",
    scholar_ok=True,
))

brown1995a = DB(WorkUnrelated(
    1995, "BigSur: a system for the management of earth science data",
    due="Unrelated to provenance. Unrelated to scripts",
    display="brown",
    authors="Brown, Paul and Stonebraker, Michael",
    place=VLDB,
    file="Brown1995a.pdf",
    local="Zurich, Switzerland",
    entrytype="inproceedings",
    scholar="http://scholar.google.com/scholar?cites=17013157920113739084&as_sdt=2005&sciodt=0,5&hl=en",
    pp="720--728",
    cluster_id="17013157920113739084",
    organization="Morgan Kaufmann Publishers Inc.",
    scholar_ok=True,
))

buckheit1995a = DB(WorkUnrelated(
    1995, "Wavelab and reproducible research",
    due="It is just a paper about the actual collected 'provenance'",
    star="[repro][x] Presents many situations that motivates the need for reproducibility",
    may_be_related_to=["reproducibility"],
    display="buckheit",
    authors="Buckheit, Jonathan B and Donoho, David L",
    summary="Publishes a package that comprises all parameters and tools to reproduce wavelet articles",
    place=Book,
    file="Buckheit1995a.pdf",
    publisher="Springer",
    link="http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.53.6201",
    local="Berlin",
    entrytype="book",
    scholar="http://scholar.google.com/scholar?cites=474757613635044587&as_sdt=2005&sciodt=0,5&hl=en",
    cluster_id="474757613635044587",
    scholar_ok=True,
))

buneman1995a = DB(WorkUnrelated(
    1995, "Principles of programming with complex objects and collection types",
    due="Unrelated to provenance, unrelated to scripts",
    display="buneman",
    authors="Buneman, Peter and Naqvi, Shamim and Tannen, Val and Wong, Limsson",
    summary="Proposes the use of complex objects and collection types nested relational queries. Describes the querying mechanism",
    place=TCS,
    file="Buneman1995a.pdf",
    volume="149",
    number="1",
    pp="3--48",
    entrytype="article",
    scholar="http://scholar.google.com/scholar?cites=10333878644507640169&as_sdt=2005&sciodt=0,5&hl=en",
    publisher="Elsevier",
    cluster_id="10333878644507640169",
    scholar_ok=True,
))

davis1995a = DB(WorkUnrelated(
    1995, "EOSDIS alternative architecture",
    due="Excluding TechReport",
    display="davis",
    authors="Davis, Frank and Farrell, William and Gray, Jim and Mechoso, Roberto and Moore, Reagan and Sides, Stephanie and Stonebraker, Michael",
    place=TechReport,
    link="http://research.microsoft.com/~gray/EOS_DIS/default.htm",
    number="S2K-95-61",
    local="U.C. Berkeley, Department of Computer Science",
    ref="Figure 10a. Using a Notebook tool to view science object lineage",
    entrytype="article",
    scholar="http://scholar.google.com/scholar?cites=4566968736627704056&as_sdt=2005&sciodt=0,5&hl=en",
    volume="6",
    cluster_id="4566968736627704056",
    scholar_ok=True,
))

dopplick1995a = DB(WorkUnrelated(
    1995, "A Science User's Guide to the EOSDIS Core System (ECS) Development Process",
    due="Excluding TechReport",
    display="dopplick",
    authors="Dopplick, Thomas",
    place=TechReport,
    link="http://edhs1.gsfc.nasa.gov/waisdata/docsw/pdf/tp1600301.pdf",
    number="160-TP-003-001",
    local="Science Office, EOS Core System Project",
    entrytype="article",
    scholar="http://scholar.google.com/scholar?cites=15270912057599426324&as_sdt=2005&sciodt=0,5&hl=en",
    cluster_id="15270912057599426324",
    scholar_ok=True,
))

gupta1995a = DB(WorkUnrelated(
    1995, "Maintenance of materialized views: Problems, techniques, and applications",
    due="Unrelated to provenance. Unrelated to scripts",
    display="gupta",
    authors="Gupta, Ashish and Mumick, Inderpal Singh and others",
    place=IEEE_Bulletin,
    file="Gupta1995a.pdf",
    entrytype="article",
    cluster_id="4773358865513272505",
    volume="18",
    number="2",
    scholar="http://scholar.google.com/scholar?cites=4773358865513272505&as_sdt=2005&sciodt=0,5&hl=en",
    pp="3--18",
    scholar_ok=True,
))

krishnamurthy1995a = DB(WorkUnrelated(
    1995, "Practical reusable UNIX software",
    due="Unrelated to provenance. Unrelated to scripts",
    display="krishnamurthy",
    authors="Krishnamurthy, Balachander",
    place=Book,
    file="Krishnamurthy1995a.pdf",
    publisher="John Wiley & Sons, Inc.",
    entrytype="book",
    scholar="http://scholar.google.com/scholar?cites=9078531798100042238&as_sdt=2005&sciodt=0,5&hl=en",
    cluster_id="9078531798100042238",
    scholar_ok=True,
))

lee1995a = DB(WorkUnrelated(
    1995, "Dataflow process networks",
    due="Unrelated to scripts",
    display="lee",
    authors="Lee, Edward A and Parks, Thomas M",
    place=IEEE,
    file="Lee1995a.pdf",
    pp="773--801",
    volume="83",
    number="5",
    entrytype="article",
    cluster_id="17447589918179606665",
    publisher="IEEE",
    scholar="http://scholar.google.com/scholar?cites=17447589918179606665&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

plank1995a = DB(WorkUnrelated(
    1995, "Libckpt: Transparent checkpointing under unix",
    due="Unrelated to provenance",
    display="plank",
    authors="Plank, James S and Beck, Micah and Kingsley, Gerry and Li, Kai",
    place=Winter,
    file="Plank1995a.pdf",
    pp="213--223",
    entrytype="book",
    scholar="http://scholar.google.com/scholar?cites=3214198437863435243&as_sdt=2005&sciodt=0,5&hl=en",
    publisher="Computer Science Department",
    cluster_id="3214198437863435243",
    scholar_ok=True,
))


ramakrishnan1995a = DB(WorkUnrelated(
    1995, "A survey of deductive database systems",
    due="Unrelated to scripts",
    display="ramakrishnan",
    authors="Ramakrishnan, Raghu and Ullman, Jeffrey D",
    place=JLP,
    file="Ramakrishnan1995a.pdf",
    issn="0743-1066",
    number="2",
    pp="125--149",
    volume="23",
    entrytype="article",
    doi="10.1016/0743-1066(94)00039-9",
    cluster_id="12361815165782271420",
    publisher="Elsevier",
    scholar="http://scholar.google.com/scholar?cites=12361815165782271420&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))


roddick1995a = DB(WorkUnrelated(
    1995, "A survey of schema versioning issues for database systems",
    due="Unrelated to scripts. Unrelated to provenance",
    display="roddick",
    authors="Roddick, John F",
    place=IST,
    volume="37",
    pp="383--393",
    file="Roddick1995a.pdf",
    entrytype="article",
    cluster_id="475763651855435905",
    publisher="Elsevier",
    number="7",
    scholar="http://scholar.google.com/scholar?cites=475763651855435905&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

schroeder1995a = DB(WorkUnrelated(
    1995, "Reproducible researchdocuments using GNU-make",
    due="Excluding TechReport",
    may_be_related_to=["reproducibility"],
    display="schroeder",
    authors="Schwab, Matthias and Schroeder, Joel",
    local="Stanford Exploration Project",
    place=TechReport,
    file="Schroeder1995a.pdf",
    pp="217--226",
    entrytype="article",
    cluster_id="13479351177848245547",
    scholar="http://scholar.google.com/scholar?cites=13479351177848245547&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

seltzer1995a = DB(WorkUnrelated(
    1995, "File system logging versus clustering: A performance comparison",
    due="Unrelated to provenance, unrelated to script. Its file microbenchmarks were cited by PASS2006",
    display="seltzer",
    authors="Seltzer, Margo and Smith, Keith A and Balakrishnan, Hari and Chang, Jacqueline and McMains, Sara and Padmanabhan, Venkata",
    summary="Evaluates File Systems",
    place=ATC,
    file="Seltzer1995a.pdf",
    local="New Orleans, LA",
    entrytype="inproceedings",
    scholar="http://scholar.google.com/scholar?cites=13037688505816244986&as_sdt=2005&sciodt=0,5&hl=en",
    pp="21--21",
    cluster_id="13037688505816244986",
    organization="USENIX Association",
    scholar_ok=True,
))
