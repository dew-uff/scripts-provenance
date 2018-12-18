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


cambronero2017a = DB(WorkUnrelated(
    2017, "Generating Component-based Supervised Learning Programs From Crowdsourced Examples",
    surveyhide="1",
    due="Unrelated to scripts. Unrelated to provenance",
    display="cambronero",
    authors="Cambronero, Jose and Rinard, Martin",
    place=TechReport,
    entrytype="article",
    ID="cambronero2017generating",
    file="cambronero2017a.pdf",
))

correndo2017a = DB(WorkUnrelated(
    2017, "EO4Wildlife: D3. 2 Knowledge Base Service Architecture Specification v2: WP3--Advanced Analytics and Knowledge Base",
    surveyhide="1",
    due="Unrelated to scripts",
    display="correndo",
    authors="Correndo, Gianluca",
    place=Thesis,
    entrytype="article",
    ID="correndo2017eo4wildlife",
    file="correndo2017a.pdf",
))

cruz2017a = DB(WorkNoFile(
    2017, "Enriching Agronomic Experiments with Data Provenance",
    surveyhide="1",
    display="cruz",
    authors="da Cruz, Sergio Manuel Serra and do Nascimento, Jose Antonio Pires",
    place=IJAEIS,
    pp="21--38",
    entrytype="article",
    request="done",
    volume="8",
    number="3",
    publisher="IGI Global",
    ID="da2017enriching",
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
    cluster_id="17995470844046725135",
    scholar="http://scholar.google.com/scholar?cites=17995470844046725135&as_sdt=2005&sciodt=0,5&hl=en",
    tracking="alert",
    entrytype="inproceedings",
    scholar_ok=True,
    citation_file="variolite2017",
))

kery2017b = DB(WorkUnrelated(
    2017, "Exploring exploratory programming",
    surveyhide="1",
    due="Unrelated to scripts. Unrelated to provenance",
    display="kery b",
    authors="Kery, Mary Beth and Myers, Brad A",
    place=VLHCC,
    pp="25--29",
    entrytype="inproceedings",
    organization="IEEE",
    ID="kery2017exploring",
    file="kery2017b.pdf",
))

kery2017c = DB(WorkOk(
    2017, "Tools to support exploratory programming with data",
    surveyhide="1",
    display="Variolite",
    authors="Kery, Mary Beth",
    place=VLHCC,
    pp="321--322",
    entrytype="inproceedings",
    organization="IEEE",
    ID="kery2017tools",
    file="kery2017c.pdf",
))

lee2017a = DB(WorkUnrelated(
    2017, "Accelerating Scientific Data Exploration via Visual Query Systems",
    surveyhide="1",
    due="Unrelated to scripts. Unrelated to provenance",
    display="lee",
    authors="Lee, Doris Jung-Lin and Lee, John and Siddiqui, Tarique and Kim, Jaewoo and Karahalios, Karrie and Parameswaran, Aditya",
    place=arXiv,
    entrytype="article",
    ID="lee2017accelerating",
    file="lee2017a.pdf",
))

meyer2017a = DB(WorkUnrelated(
    2017, "The Influence of Mexican Hat Recurrent Connectivity on Noise Correlations and Stimulus Encoding",
    surveyhide="1",
    due="Unrelated to scripts. Unrelated to provenance",
    display="meyer",
    authors="Meyer, Robert and Ladenbauer, Josef and Obermayer, Klaus",
    place=FNCom,
    pp="34",
    entrytype="article",
    volume="11",
    publisher="Frontiers",
    ID="meyer2017influence",
    file="meyer2017a.pdf",
))

myers2017a = DB(WorkUnrelated(
    2017, "Making End User Development More Natural",
    surveyhide="1",
    due="Unrelated to scripts. Unrelated to provenance",
    display="myers",
    authors="Myers, Brad A and Ko, Andrew J and Scaffidi, Chris and Oney, Stephen and Yoon, YoungSeok and Chang, Kerry and Kery, Mary Beth and Li, Toby Jia-Jun",
    place=Book,
    booktitle="New Perspectives in End-User Development",
    pp="1--22",
    entrytype="incollection",
    publisher="Springer",
    ID="myers2017making",
    file="myers2017a.pdf",
))

nelson2017a = DB(WorkUnrelated(
    2017, "Problem-Solving Applications in Developer Environments",
    surveyhide="1",
    alias=(0, "Problem-Solving Applications in Developer Environments",),
    due="Unrelated to scripts. Unrelated to provenance",
    display="nelson",
    authors="Nelson, Nicholas",
    place=PPIG,
    entrytype="article",
    ID="nelsonproblem",
    file="nelson2017a.pdf",
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

pimentel2017a = DB(WorkOk(
    2017, "noWorkflow: a tool for collecting, analyzing, and managing provenance from python scripts",
    surveyhide="1",
    display="pimentel",
    authors="Pimentel, Joao Felipe and Murta, Leonardo and Braganholo, Vanessa and Freire, Juliana",
    place=VLDB,
    pp="1841--1844",
    entrytype="article",
    volume="10",
    number="12",
    publisher="VLDB Endowment",
    ID="pimentel2017noworkflow",
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

romano2017a = DB(WorkUnrelated(
    2017, "The joint NETTAB/Integrative Bioinformatics 2015 Meeting: aims, topics and outcomes",
    surveyhide="1",
    due="Unrelated to scripts. Unrelated to provenance",
    display="romano",
    authors="Romano, Paolo and Hofestädt, Ralf and Lange, Matthias and D’Elia, Domenica",
    place=bioinformatics,
    entrytype="misc",
    publisher="BioMed Central",
    ID="romano2017joint",
    file="Romano2017a.pdf",
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

zhang2017a = DB(WorkUnrelated(
    2017, "DS. js: Turn Any Webpage into an Example-Centric Live Programming Environment for Learning Data Science",
    surveyhide="1",
    due="Unrelated to scripts. Unrelated to provenance",
    display="zhang",
    authors="Zhang, Xiong and Guo, Philip J",
    place=UIST,
    pp="691--702",
    entrytype="inproceedings",
    organization="ACM",
    ID="zhang2017ds",
    cluster_id="6129900332389804285",
    scholar="http://scholar.google.com/scholar?cites=6129900332389804285&as_sdt=2005&sciodt=0,5&hl=en",
    file="zhang2017a.pdf",
))
