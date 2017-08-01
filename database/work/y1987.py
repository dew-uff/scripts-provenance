# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *


carroll1987a = DB(WorkUnrelated(
    1987, "Paradox of the active user",
    due="Unrelated to provenance",
    display="carroll",
    authors="Carroll, John M and Rosson, Mary Beth",
    place=Book,
    file="Carroll1987a.pdf",
    publisher="The MIT Press",
    entrytype="book",
    cluster_id="10234619659952062621",
    scholar="http://scholar.google.com/scholar?cites=10234619659952062621&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

ferrante1987a = DB(WorkUnrelated(
    1987, "The program dependence graph and its use in optimization",
    due="Unrelated to provenance. The representation may be useful for representing provenance with data dependences and control dependences, but this work describes the technique itself and does not apply it to provenance. In addition, it may not handle dynamic features of scripts",
    may_be_related_to=["program slicing"],
    display="ferrante",
    authors="Ferrante, Jeanne and Ottenstein, Karl J and Warren, Joe D",
    place=TOPLAS,
    summary="Presents an intermediate program representation, program dependence graph (PDG), that allows efficient and powerful program transformations for optimizing compilers",
    file="Ferrante1987a.pdf",
    pp="319--349",
    volume="9",
    number="3",
    entrytype="article",
    publisher="ACM",
    cluster_id="15168492501402143427",
    scholar="http://scholar.google.com/scholar?cites=15168492501402143427&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

gale1987a = DB(WorkUnrelated(
    1987, "Statistical applications of artificial intelligence and knowledge engineering",
    due="Unrelated to provenance",
    display="gale",
    authors="Gale, William A",
    pp="227--247",
    place=KER,
    file="Gale1987a.pdf",
    volume="2",
    cluster_id="11314804144053109960",
    ID="gale1987statistical",
    number="04",
    entrytype="article",
    scholar="http://scholar.google.com/scholar?cites=11314804144053109960&as_sdt=2005&sciodt=0,5&hl=en",
    publisher="Cambridge Univ Press",
    scholar_ok=True,
))

hawley1987a = DB(WorkUnrelated(
    1987, "Artificial intelligence programming environments",
    due="Unrelated to provenance",
    display="hawley",
    authors="Hawley, Robert",
    place=Book,
    publisher="Intellect Books",
    link="https://books.google.com.br/books/about/Artificial_Intelligence_Programming_Envi.html?id=43hQAAAAMAAJ&redir_esc=y",
    entrytype="book",
    cluster_id="2774070154322015039",
    scholar="http://scholar.google.com/scholar?cites=2774070154322015039&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok=True,
))

hinterberger1987a = DB(WorkLang(
    1987, "Data density: a Powerful Abstraction to Manage and Analyze Multivariate Data",
    display="hinterberger",
    authors="Hinterberger, Hans",
    place=Thesis,
    file="Hinterberger1987a.pdf",
    cluster_id="17108029648257510807",
    ID="hinterberger1987and",
    entrytype="phdthesis",
    scholar="http://scholar.google.com/scholar?cites=17108029648257510807&as_sdt=2005&sciodt=0,5&hl=en",
    local="Swiss Federal Institute of Technology Zurich",
    school="Swiss Federal Institute of Technology Zurich",
    scholar_ok=True,
))

oldford1987a = DB(WorkUnrelated(
    1987, "Abstract Statistical Computing",
    alias=(0, "Department of Statistics and Actuarial Science University of Waterloo"),
    due="Unrelated to provenance",
    display="oldford",
    authors="Oldford, RVV",
    place=WSC,
    file="Oldford1987a.pdf",
    ID="oldforddepartment",
    entrytype="article",
    local="Department of Statistics and Actuarial Science University of Waterloo",
    cluster_id="17808968599356459824",
    scholar="https://scholar.google.com/scholar?cites=17808968599356459824&as_sdt=2005&sciodt=0,5&hl=en",
    scholar_ok="impossible/citation",
))

oldford1987b = DB(WorkUnrelated(
    1987, "Statistically sophisticated software and DINDE",
    due="Unrelated to provenance. Unrelated to scripts",
    display="oldford",
    authors="Oldford, RW and Peters, SC",
    place=Interface,
    file="Oldford1987b.pdf",
    cluster_id="5187644533756120129",
    scholar="http://scholar.google.com/scholar?cites=5187644533756120129&as_sdt=2005&sciodt=0,5&hl=en",
    ID="oldford1987statistically",
    entrytype="inproceedings",
    scholar_ok=True,
))
