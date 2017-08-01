# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *


moore1981a = DB(WorkUnrelated(
    1981, "The TXDT Package-Interlisp Text Editing Primitives",
    due="Unrelated to provenance. It was cited as an exampleof multiple granularities (e.g., bytes, lines, directories or whole volumes)",
    display="moore",
    authors="Moore, J Strother",
    place=TechReport,
    summary="Describes a package for INTERLISP to support the construction of text editors",
    file="Moore1981a.pdf",
    number="CSL-81-2",
    local="XEROX PARC",
    entrytype="book",
    publisher="Xerox. Palo Alto Research Center",
    cluster_id="16759844729700258385",
    scholar="http://scholar.google.com/scholar?cites=16759844729700258385&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

weiser1981a = DB(WorkUnrelated(
    1981, "Program slicing",
    due="Unrelated to provenance, It may be used as a technique to capture provenance from scripts, but it is not an approach about it",
    may_be_related_to=["program slicing"], #definetely will
    display="weiser",
    authors="Weiser, Mark",
    summary="Coined the term 'program slicing' and arguments that programmers use it for abstracting programs during debugging",
    place=ICSE,
    file="Weiser1981a.pdf",
    pp="439--449",
    local="Piscataway, NJ, USA",
    entrytype="inproceedings",
    organization="IEEE Press",
    scholar="http://scholar.google.com/scholar?cites=17111831253132928479&as_sdt=2005&sciodt=0,5&hl=en",
    cluster_id="17111831253132928479",
    scholar_ok=True,
))
