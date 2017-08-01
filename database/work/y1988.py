# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *


aho1988a = DB(WorkUnrelated(
    1988, "The AWK programming language",
    due="Unrelated to provenance",
    display="aho",
    authors="Aho, Alfred V and Kernighan, Brian W and Weinberger, Peter J",
    place=Book,
    file="Aho1988a.pdf",
    publisher="Addison-Wesley Longman Publishing Co., Inc.",
    entrytype="book",
    cluster_id="1901067318849000714",
    scholar="http://scholar.google.com/scholar?cites=1901067318849000714&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

becker1988a = DB(WorkSnowball(
    1988, "Auditing of data analyses",
    snowball=datetime(2017, 3, 6),
    display="becker",
    authors="Becker, Richard A and Chambers, John M",
    place=SIAMJSciStatComput,
    file="Becker1988a.pdf",
    volume="9",
    pp="747--760",
    entrytype="article",
    publisher="SIAM",
    cluster_id="18309143093492440675",
    number="4",
    scholar="http://scholar.google.com/scholar?cites=18309143093492440675&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
    citation_file="becker1988",
    tracking="alert",
))

becker1988b = DB(WorkUnrelated(
    1988, "The New S Language",
    due="Unrelated to provenance",
    display="becker",
    authors="Becker, Richard A and Chambers, John M and Wilks, Allan R",
    place=Book,
    link="http://dl.acm.org/citation.cfm?id=43380",
    publisher="Wadsworth",
    local="Pacific Grove, CA",
    isbn="0-534-09192-X",
    entrytype="book",
    cluster_id="4045688070574639943",
    scholar="http://scholar.google.com/scholar?cites=4045688070574639943&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

bershad1988a = DB(WorkUnrelated(
    1988, "Watchdogs-extending the UNIX file system",
    due="Unrelated to provenance, unrelated to scripts",
    display="bershad",
    authors="Bershad, Brian N and Pinkerton, C Brian",
    place=TOCS,
    file="Bershad1988a.pdf",
    volume="1",
    number="2",
    pp="169–188",
    entrytype="inproceedings",
    cluster_id="2554892771857462056",
    organization="Citeseer",
    scholar="http://scholar.google.com/scholar?cites=2554892771857462056&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

feldman1988a = DB(WorkUnrelated(
    1988, "Igor: A system for program debugging via reversible execution",
    due="Unrelated to provenance",
    display="feldman",
    authors="Feldman, Stuart I and Brown, Channing B",
    place=PADD,
    file="Feldman1988a.pdf",
    pp="112--123",
    entrytype="inproceedings",
    number="1",
    volume="24",
    cluster_id="5192474481636552944",
    scholar="http://scholar.google.com/scholar?cites=5192474481636552944&as_sdt=2005&sciodt=0,5&hl=en",
    organization="ACM",
    scholar_ok=True,
))

gelfond1988a = DB(WorkUnrelated(
    1988, "The stable model semantics for logic programming",
    due="Unrelated to scripts. Unrelated to provenance",
    display="gelfond",
    authors="Gelfond, Michael and Lifschitz, Vladimir",
    place=ICFP,
    pp="1070--1080",
    volume="88",
    file="Gelfond1988a.pdf",
    entrytype="inproceedings",
    cluster_id="14460061977998484960",
    scholar="http://scholar.google.com/scholar?cites=14460061977998484960&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

howard1988a = DB(WorkUnrelated(
    1988, "Scale and performance in a distributed file system",
    due="Unrelated to provenance. Unrelated to scripts",
    display="howard",
    authors="Howard, John H and Kazar, Michael L and Menees, Sherri G and Nichols, David A and Satyanarayanan, Mahadev and Sidebotham, Robert N and West, Michael J",
    place=TOCS,
    file="Howard1988a.pdf",
    volume="6",
    number="1",
    pp="51--81",
    entrytype="article",
    publisher="ACM",
    cluster_id="5050314366548821417",
    scholar="http://scholar.google.com/scholar?cites=5050314366548821417&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

korel1988a = DB(WorkUnrelated(
    1988, "Dynamic program slicing",
    due="Unrelated to provenance. May be used as a technique to collect provenance though",
    may_be_related_to=["slicing"],
    display="korel",
    authors="Korel, Bogdan and Laski, Janusz",
    summary="Proposes dynamic program slicing to handle arrayas and dynamic data structures more precisely than static slices and to reduce the slice size",
    place=IPL,
    file="Korel1988a.pdf",
    volume="29",
    number="3",
    pp="155--163",
    entrytype="article",
    publisher="Elsevier",
    cluster_id="2147609536996486320",
    scholar="http://scholar.google.com/scholar?cites=2147609536996486320&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

molenaar1988a = DB(WorkUnrelated(
    1988, "Statistical consultants and statistical expert systems",
    due="Unrelated to provenance. Unrelated to scripts",
    display="molenaar",
    authors="Molenaar, IW",
    pp="187--192",
    place=COMPSTAT,
    file="Molenaar1988a.pdf",
    organization="Springer",
    cluster_id="1762811843515085226",
    ID="molenaar1988statistical",
    entrytype="inproceedings",
    scholar="http://scholar.google.com/scholar?cites=1762811843515085226&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

oldford1988a = DB(WorkUnrelated(
    1988, "DINDE: Towards more statistically sophisticated software",
    due="Unrelated to provenance",
    display="oldford",
    authors="Oldford, RW and Peters, SC",
    place=SIAMJSciStatComput,
    file="Oldford1988a.pdf",
    volume="9",
    entrytype="incollection",
    cluster_id="10981556454963316755",
    publisher="MIT Center for Computer Research in economics and Management Science Cambridge, MA",
    scholar="http://scholar.google.com/scholar?cites=10981556454963316755&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))
