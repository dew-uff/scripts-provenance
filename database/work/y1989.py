# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *


bubenik1989a = DB(WorkUnrelated(
    1989, "Performance of optimistic make",
    due="Unrelated to provenance. Unrelated to scripts",
    display="bubenik",
    authors="Bubenik, Rick and Zwaenepoel, Willy",
    place=SIGMETRICS,
    file="Bubenik1989a.pdf",
    pp="39–48",
    entrytype="book",
    publisher="ACM",
    cluster_id="12815876953889816496",
    volume="17",
    number="1",
    scholar="http://scholar.google.com/scholar?cites=12815876953889816496&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

cytron1989a = DB(WorkUnrelated(
    1989, "An efficient method of computing static single assignment form",
    due="Unrelated to scripts. Unrelated to provenance",
    display="cytron",
    authors="Cytron, Ron and Ferrante, Jeanne and Rosen, Barry K and Wegman, Mark N and Zadeck, F Kenneth",
    place=POPL,
    pp="25--35",
    publisher="ACM",
    file="Cytron1989a.pdf",
    entrytype="inproceedings",
    cluster_id="4155281534660803428",
    scholar="http://scholar.google.com/scholar?cites=4155281534660803428&as_sdt=2005&sciodt=0,5&hl=en",
    organization="ACM",
    scholar_ok=True,
))

harner1989a = DB(WorkNoFile(
    1989, "Interactively developing models based on the exponential family",
    display="harner",
    authors="Harner, E James",
    pp="110--115",
    place=Interface,
    cluster_id="11240947501212794963",
    scholar="http://scholar.google.com/scholar?cites=11240947501212794963&as_sdt=2005&sciodt=0,5&hl=en",
    ID="harner1989interactively",
    entrytype="inproceedings",
    request="wont", # too-old
    scholar_ok=True,
))

mccarthy1989a = DB(WorkUnrelated(
    1989, "The architecture of an active database management system",
    due="Unrelated to provenance. Unrelated to scripts",
    display="mccarthy",
    authors="McCarthy, Dennis and Dayal, Umeshwar",
    place=SIGMOD,
    file="Mccarthy1989a.pdf",
    entrytype="inproceedings",
    cluster_id="13248795934521172911",
    number="2",
    scholar="http://scholar.google.com/scholar?cites=13248795934521172911&as_sdt=2005&sciodt=0,5&hl=en",
    pp="215--224",
    volume="18",
    organization="ACM",
    scholar_ok=True,
))
