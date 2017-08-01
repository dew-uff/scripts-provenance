# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *


aho1985a = DB(WorkUnrelated(
    1985, "Compilers: Principles, Techniques, and Tools",
    due="Unrelated to provenance",
    display="aho",
    authors="Aho, Alfred V and Sethi, Ravi and Ullman, Jeffrey D",
    place=Book,
    file="Aho1985a.pdf",
    publisher="Addison wesley Boston",
    local="Reading, MA",
    entrytype="book",
    cluster_id="14589105653825902392",
    scholar="http://scholar.google.com/scholar?cites=14589105653825902392&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

gale1985a = DB(WorkUnrelated(
    1985, "Artificial Intelligence and Statistics",
    due="Unrelated to provenance. Unrelated to scripts",
    display="gale",
    authors="Gale, William A",
    place=Book,
    file="Gale1985a.pdf",
    publisher="Addison-Wesley Pub. Co. Inc.",
    local="Reading, MA",
    entrytype="article",
    cluster_id="15923031966306380290",
    scholar="http://scholar.google.com/scholar?cites=15923031966306380290&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

leblang1985a = DB(WorkNoFile(
    1985, "Configuration management for large-scale software development efforts",
    display="leblang",
    authors="Leblang, David B and McLean Jr, Gordon D",
    place=GTE,
    pp="122–127",
    cluster_id="1230603814485892455",
    scholar="http://scholar.google.com/scholar?cites=1230603814485892455&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
    request="wont",
))

mcdonald1985a = DB(WorkUnrelated(
    1985, "Computing environments for data analysis, Parts I and II",
    due="Unrelated to provenance",
    display="mcdonald",
    authors="McDonald, John A and Pedersen, Jan",
    place=SIAMJSciStatComput,
    file="Mcdonald1985a.pdf",
    volume="6",
    pp="1004--1021",
    entrytype="article",
    cluster_id="7671536574754452540",
    scholar="http://scholar.google.com/scholar?cites=7671536574754452540&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok="aprox",
))

tichy1985a = DB(WorkUnrelated(
    1985, "RCS -- a system for version control",
    due="Unrelated to provenance",
    display="tichy",
    authors="Tichy, Walter F",
    place=SPE,
    month="July",
    file="Tichy1985a.pdf",
    pp="637--654",
    number="7",
    volume="15",
    entrytype="article",
    cluster_id="16131406944534290732",
    publisher="Wiley Online Library",
    scholar="http://scholar.google.com/scholar?cites=16131406944534290732&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))
