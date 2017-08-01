# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *


mccabe1976a = DB(WorkUnrelated(
    1976, "A complexity measure",
    due="Unrelated to scripts. Unrelated to provenance",
    display="mccabe",
    authors="McCabe, Thomas J",
    place=TBME,
    pp="308--320",
    doi="10.1109/TSE.1976.233837.",
    month="December",
    volume="2",
    file="Mccabe1976a.pdf",
    number="4",
    entrytype="article",
    cluster_id="14917182179273582081",
    publisher="IEEE",
    scholar="http://scholar.google.com/scholar?cites=14917182179273582081&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

stonebraker1976a = DB(WorkUnrelated(
    1976, "The design and implementation of INGRES",
    due="Unrelated to provenance, unrelated to scripts",
    display="stonebraker",
    authors="Stonebraker, Michael and Held, Gerald and Wong, Eugene and Kreps, Peter",
    place=TODS,
    file="Stonebraker1976a.pdf",
    number="3",
    pp="189--222",
    volume="1",
    link="http://dl.acm.org/citation.cfm?id=320476",
    entrytype="article",
    cluster_id="4436012605119588041",
    publisher="ACM",
    scholar="http://scholar.google.com/scholar?cites=4436012605119588041&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))
