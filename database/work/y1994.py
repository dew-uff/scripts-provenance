# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *


becker1994a = DB(WorkUnrelated(
    1994, "A brief history of S",
    due="Unrelated to provenance",
    display="becker",
    authors="Becker, Richard A",
    place=TechReport,
    file="Becker1994a.pdf",
    local="AT&T Bell",
    entrytype="article",
    scholar="http://scholar.google.com/scholar?cites=16898975515087469825&as_sdt=2005&sciodt=0,5&hl=en",
    cluster_id="16898975515087469825",
    scholar_ok=True,
))

braun1994a = DB(WorkUnrelated(
    1994, "Web traffic characterization: an assessment of the impact of caching documents from NCSA's web server",
    due="Unrelated to provenance. Unrelated to scripts",
    display="braun",
    authors="Braun, Hans-Werner and Claffy, Kimberly C",
    place=WWW,
    file="Braun1994a.pdf",
    entrytype="inproceedings",
    cluster_id="12510890439953893792",
    number="1",
    scholar="http://scholar.google.com/scholar?cites=12510890439953893792&as_sdt=2005&sciodt=0,5&hl=en",
    publisher="Elsevier",
    pp="37--51",
    volume="28",
    scholar_ok=True,
))

buneman1994a = DB(WorkUnrelated(
    1994, "Comprehension syntax",
    due="Unrelated to Provenance, unrelated to scripts",
    display="buneman",
    authors="Buneman, Peter and Libkin, Leonid and Suciu, Dan and Tannen, Val and Wong, Limsoon",
    summary="Define a comprehension syntax for querying the database",
    place=SIGMOD_REC,
    file="Buneman1994a.pdf",
    volume="23",
    number="1",
    pp="87--96",
    entrytype="article",
    scholar="http://scholar.google.com/scholar?cites=11465106281560286893&as_sdt=2005&sciodt=0,5&hl=en",
    publisher="ACM",
    cluster_id="11465106281560286893",
    scholar_ok=True,
))

dumville1994a = DB(WorkNoFile(
    1994, "English Square Minuscule script: the mid-century phases",
    display="dumville",
    authors="Dumville, David N",
    place=Book,
    booktitle="Anglo-Saxon England",
    volume="23",
    pp="133--164",
    entrytype="article",
    scholar="http://scholar.google.com/scholar?cites=14641210234455162053&as_sdt=5,33&sciodt=0,33&hl=en",
    cluster_id="14641210234455162053",
    publisher="Cambridge University Press",
    scholar_ok=True,
))

frew1994a = DB(WorkUnrelated(
    1994, "Bigfoot: An earth science computing environment for the Sequoia 2000 project",
    due="Unrelated to provenance, unrelated to scripts",
    display="frew",
    authors="Frew, James",
    summary="Talks about the Sequoia 2000 Project, which is a collaboration between earth scientis and computer scientists to manage a large amount of data",
    place=Book,
    file="Frew1994a.pdf",
    booktitle="Environmental Information Management and Analysis",
    bookauthors="W. Michener, J. Brunt, and S. Stafford",
    editors="Taylor and Francis",
    pp="113--125",
    local="London",
    entrytype="book",
    scholar="http://scholar.google.com/scholar?cites=18222170675883538871&as_sdt=2005&sciodt=0,5&hl=en",
    publisher="London: Taylor and Francis",
    cluster_id="18222170675883538871",
    scholar_ok=True,
))

gamma1994a = DB(WorkUnrelated(
    1994, "Design patterns: elements of reusable object-oriented software",
    due="Unrelated to provenance",
    display="gamma",
    authors="Gamma, Erich",
    place=Book,
    publisher="Pearson Education",
    file="Gamma1994a.pdf",
    entrytype="book",
    cluster_id="16758307189166775102",
    scholar="http://scholar.google.com/scholar?cites=16758307189166775102&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

jackson1994a = DB(WorkUnrelated(
    1994, "Semantic Diff: A Tool for Summarizing the Effects of Modifications",
    due="Unrelated to scripts. Unrelated to provenance",
    display="jackson",
    authors="Jackson, Daniel and Ladd, David A",
    place=ICSM,
    pp="243--252",
    publisher="IEEE Computer Society",
    file="Jackson1994a.pdf",
    local="Washington, DC, USA",
    entrytype="inproceedings",
    cluster_id="8673710600807619302",
    volume="94",
    scholar="http://scholar.google.com/scholar?cites=8673710600807619302&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

ramsey1994a = DB(WorkUnrelated(
    1994, "Literate programming simplified",
    due="Unrelated to scripts. Unrelated to provenance",
    display="ramsey",
    authors="Ramsey, Norman",
    place=Software,
    number="5",
    volume="11",
    pp="97--105",
    file="Ramsey1994a.pdf",
    entrytype="article",
    cluster_id="17713245942768296787",
    publisher="IEEE",
    scholar="http://scholar.google.com/scholar?cites=17713245942768296787&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

srivastava1994a = DB(WorkUnrelated(
    1994, "ATOM: A system for building customized program analysis tools",
    due="Unrelated to provenance. May be used as a technique, though",
    may_be_related_to=["instrumentation"],
    display="srivastava",
    authors="Srivastava, Amitabh and Eustace, Alan",
    place=PLDI,
    file="Srivastava1994a.pdf",
    local="Orlando, FL, USA",
    entrytype="book",
    scholar="http://scholar.google.com/scholar?cites=9243688666376979849&as_sdt=2005&sciodt=0,5&hl=en",
    number="6",
    volume="29",
    publisher="ACM",
    cluster_id="9243688666376979849",
    scholar_ok=True,
))
