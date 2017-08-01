# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *


alper2017a = DB(WorkUnrelated(
    2017, "Static analysis of Taverna workflows to predict provenance patterns",
    due="Unrelated to scripts",
    display="alper",
    authors="Alper, Pinar and Belhajjame, Khalid and Goble, Carole A",
    place=FGCS,
    file="Alper2017a.pdf",
    publisher="Elsevier",
    entrytype="article",
    ID="alper2017static",
    scholar_ok=True,
))

bastos2017a = DB(WorkUnrelated(
    2017, "WISP: A pattern-based approach to the interchange of scientific workflow specifications",
    due="Unrelated to scripts",
    display="bastos",
    authors="Bastos, Bruno F and Braga, Regina Maria M and Gomes, Antonio Tadeu A",
    summary="Captures workflow patterns and software architectures to understand the key structural semantics expressed in workflow specifications",
    place=CCPE,
    file="Bastos2017a.pdf",
    scholar="http://scholar.google.com/scholar?cites=3767105103863610318&as_sdt=2005&sciodt=0,5&hl=en",
    publisher="Wiley Online Library",
    entrytype="article",
    volume="29",
    number="2",
    cluster_id="3767105103863610318",
    scholar_ok=True,
))


hellerstein2017a = DB(WorkUnrelated(
    2017, "Ground: A Data Context Service",
    due="Unrelated to scripts. Unrelated to provenance",
    display="hellerstein",
    authors="Hellerstein, Joseph M and Sreekanti, Vikram and Gonzalez, Joseph E and Dalton, James and Dey, Akon and Nag, Sreyashi and Ramachandran, Krishna and Arora, Sudhanshu and Bhattacharyya, Arka and Das, Shirshanka and others",
    place=CIDR,
    scholar="http://scholar.google.com/scholar?cites=13852224024056316692&as_sdt=2005&sciodt=0,5&hl=en",
    ID="hellersteinground",
    cluster_id="13852224024056316692",
    file="Hellerstein2017a.pdf",
    entrytype="article",
    scholar_ok=True,
))

kery2017a = DB(WorkSnowball(
    2017, "Variolite: Supporting Exploratory Programming by Data Scientists",
    snowball=datetime(2017, 3, 6),
    due="Unrelated to provenance. It is rather a versioning approach",
    summary="Ad-hoc local versioning for scripts. Variolite is a Atom plugin that allows users to select code chunks and create variations for scripts. For each variation, it records input parameters and outputs.",
    may_be_related_to=["evolution"],
    display="kery",
    authors="Kery, Mary Beth and Horvath, Amber and Myers, Brad",
    place=CHI,
    local="Denver, USA",
    publisher="ACM",
    pp="1--12",
    file="Kery2017a.pdf",
    ID="keryvariolite",
    cluster_id="12665963803047105016",
    scholar="http://scholar.google.com/scholar?cites=12665963803047105016&as_sdt=2005&sciodt=0,5&hl=en",
    tracking="alert",
    entrytype="inproceedings",
    scholar_ok=True,
    citation_file="variolite2017",
))

oliveira2017a = DB(WorkUnrelated(
    2017, "Provenance Analytics for Workflow-based Computational Experiments: a Survey",
    due="Unrelated to scripts",
    may_be_related_to=["survey", "analysis"],
    display="oliveira",
    authors="Oliveira, Wellington and de Oliveira, Daniel and Braganholo, Vanessa",
    place=CSUR,
    file="Oliveira2017a_update.pdf",
    notes="in press",
    entrytype="article",
    publisher="ACM",
    pp="1--27",
))


oxvig2017a = DB(WorkUnrelated(
    2017, "Structure assisted compressed sensing reconstruction of undersampled AFM images",
    due="Unrelated to provenance",
    display="oxvig",
    authors="Oxvig, Christian Schou and Arildsen, Thomas and Larsen, Torben",
    place=Ultramicroscopy,
    pp="1--9",
    entrytype="article",
    ID="oxvig2017structure",
    publisher="Elsevier",
    volume="172",
    file="Oxvig2017a.pdf",
    summary="Uses Magni",
    scholar_ok=True,
))

reimann2017a = DB(WorkUnrelated(
    2017, "Data provisioning in simulation workflows",
    due="Unrelated to scripts",
    may_be_related_to=["workflow"],
    display="reimann",
    authors="Reimann, Peter",
    place=Thesis,
    entrytype="article",
    scholar="http://scholar.google.com/scholar?cites=14509334846461082775&as_sdt=2005&sciodt=0,5&hl=en",
    ID="reimann2017data",
    cluster_id="14509334846461082775",
    file="Reimann2017a.pdf",
    scholar_ok=True,
    excerpt="Computer-based simulations become more and more important, eg, to imitate real-world experiments such as crash tests, which would otherwise be too expensive or not feasible at all. Thereby, simulation workflows may be used to control the interaction with simulation ",
))

samuel2017a = DB(WorkUnrelated(
    2017, "Towards Reproducibility of Microscopy Experiments",
    due="Unrelated to scripts",
    display="samuel",
    authors="Samuel, Sheeba and Taubert, Frank and Walther, Daniel and König-Ries, Birgitta and Bücker, H Martin",
    place=DLIB,
    number="1/2",
    publisher="Corporation for National Research Initiatives",
    ID="samuel2017towards",
    entrytype="article",
    link="http://mirror.dlib.org/dlib/january17/samuel/01samuel.html",
    volume="23",
    scholar_ok=True,
))

santana2017a = DB(WorkUnrelated(
    2017, "Reproducibility of execution environments in computational science using Semantics and Clouds",
    due="Unrelated to scripts",
    may_be_related_to=["reprodutibility", "workflow"],
    display="santana",
    authors="Santana-Perez, Idafen and da Silva, Rafael Ferreira and Rynge, Mats and Deelman, Ewa and Pérez-Hernández, María S and Corcho, Oscar",
    place=FGCS,
    scholar="http://scholar.google.com/scholar?cites=10438670480182847512&as_sdt=2005&sciodt=0,5&hl=en",
    ID="santana2017reproducibility",
    pp="354--367",
    entrytype="article",
    publisher="Elsevier",
    cluster_id="10438670480182847512",
    file="Santana2017a.pdf",
    volume="67",
    scholar_ok=True,
))

wilson2017a = DB(WorkUnrelated(
    2017, "recipy",
    due="Excluding unpublished work",
    display="recipy",
    authors="Wilson, Robin and van der Zwaan, Janneke and Alegre, Raquel and Jackson, Michael and others",
    place=Unpublished,
    entrytype="misc",
    link="https://github.com/recipy/recipy",
    scholar_ok='impossible',
    tracking="impossible"
))