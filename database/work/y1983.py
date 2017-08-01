# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *


becker1983a = DB(WorkNoFile(
    1983, "poster presentation",
    due="Non-paper format",
    display="becker",
    authors="R.A. BECKER",
    place=ASA,
    local="Toronto, Ontario, Canada",
    request="wont",
    scholar_ok="impossible",
))

sheil1983a = DB(WorkNoFile(
    1983, "Environments for exploratory programming",
    due="Unrelated to provenance",
    display="sheil",
    authors="Sheil, Beau",
    place=Datamation,
    number="7",
    volume="29",
    pp="131--144",
    request="wont",
    entrytype="article",
    cluster_id="14376102466336457565",
    scholar="http://scholar.google.com/scholar?cites=14376102466336457565&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

zaniolo1983a = DB(WorkUnrelated(
    1983, "The database language GEM",
    due="Unrelated to provenance, unrelated to scripts",
    display="zaniolo",
    authors="Zaniolo, Carlo",
    place=SIGMOD_REC,
    file="Zaniolo1983a.pdf",
    number="4",
    pp="207--218",
    volume="13",
    link="http://dl.acm.org/citation.cfm?id=582226",
    entrytype="article",
    cluster_id="573099096700414421",
    publisher="ACM",
    scholar="http://scholar.google.com/scholar?cites=573099096700414421&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))