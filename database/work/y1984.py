# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *


becker1984a = DB(WorkNoFile(
    1984, "S: An Interactive Environment for Data Analysis and Graphics",
    display="becker",
    authors="Becker, Richard A and Chambers, John M",
    place=Book,
    publisher="CRC Press",
    local="Pacific Grove, CA",
    request="wont",
    entrytype="book",
    cluster_id="12792729195115579186",
    scholar="http://scholar.google.com/scholar?cites=12792729195115579186&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

becker1984b = DB(WorkUnrelated(
    1984, "Design of the S system for data analysis",
    due="Unrelated to provenance",
    display="becker",
    authors="Becker, Richard A and Chambers, John M",
    place=CACM,
    file="Becker1984b.pdf",
    volume="27",
    pp="486--495",
    entrytype="article",
    cluster_id="17118236888755655723",
    publisher="ACM",
    number="5",
    scholar="http://scholar.google.com/scholar?cites=17118236888755655723&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

carr1984a = DB(WorkUnrelated(
    1984, "Organizational tools for data analysis environments",
    due="Unrelated to provenance",
    display="carr",
    authors="Carr, Daniel B and Cowley, Paula J and Whiting, MA and Nicholson, Wesley L",
    place=ASA,
    link="https://www.osti.gov/scitech/biblio/6347383",
    pp="214--218",
    entrytype="techreport",
    cluster_id="15172657669891124665",
    institution="Pacific Northwest Lab., Richland, WA (USA)",
    scholar="http://scholar.google.com/scholar?cites=15172657669891124665&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

gilman1984a = DB(WorkUnrelated(
    1984, "APL: an interactive approach",
    due="Unrelated to provenance",
    display="gilman",
    authors="Gilman, Leonard and Rose, Allen J",
    place=Book,
    file="Gilman1984a.pdf",
    publisher="John Wiley",
    local="New York",
    entrytype="book",
    cluster_id="16799603748709596038",
    scholar="http://scholar.google.com/scholar?cites=16799603748709596038&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok="aprox",
))

knuth1984a = DB(WorkUnrelated(
    1984, "Literate programming",
    due="Unrelated to scripts. Unrelated to provenance",
    display="knuth",
    authors="Knuth, Donald E",
    place=Computer,
    file="Knuth1984a.pdf",
    volume="1",
    number="2",
    pp="97--111",
    entrytype="article",
    cluster_id="11589890021075421637",
    scholar="http://scholar.google.com/scholar?cites=11589890021075421637&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

leblang1984a = DB(WorkUnrelated(
    1984, "Computer-aided software engineering in a distributed workstation environment",
    due="Unrelated to provenance. Unrelated to scripts",
    display="leblang",
    authors="Leblang, David B and Chase Jr, Robert P",
    place=SDE,
    file="Leblang1984a.pdf",
    pp="104--112",
    entrytype="inproceedings",
    cluster_id="15560897127633460210",
    volume="19",
    number="5",
    scholar="http://scholar.google.com/scholar?cites=15560897127633460210&as_sdt=2005&sciodt=0,5&hl=en",
    organization="ACM",
    scholar_ok=True,
))

nicholson1984a = DB(WorkNoFile(
    1984, "The role of environments in managing data analysis",
    display="nicholson",
    authors="Nicholson, WL and Carr, DB and Cowley, PJ and Whiting, MA",
    place=ASA,
    pp="80--84",
    request="researchgate",
    entrytype="inproceedings",
    cluster_id="1686747782178352467",
    institution="Pacific Northwest Lab., Richland, WA (USA)",
    scholar="http://scholar.google.com/scholar?cites=1686747782178352467&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

weiser1984a = DB(WorkUnrelated(
    1984, "Program slicing",
    due="Unrelated to scripts. Unrelated to provenance",
    display="weiser",
    authors="Weiser, Mark",
    place=TBME,
    file="Weiser1984a.pdf",
    pp="352--357",
    entrytype="article",
    cluster_id="17111831253132928479",
    scholar="http://scholar.google.com/scholar?cites=17111831253132928479&as_sdt=2005&sciodt=0,5&hl=en",
    organization="IEEE Press",
    scholar_ok="aprox",
))
