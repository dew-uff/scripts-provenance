# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1977 import tukey1977a
from ..work.y1983 import sheil1983a
from ..work.y1987 import carroll1987a
from ..work.y1987 import hawley1987a
from ..work.y1997 import beyer1997a
from ..work.y2001 import clements2001a
from ..work.y2003 import bar2003a
from ..work.y2004 import terry2004a
from ..work.y2004 import toomim2004a
from ..work.y2005 import ko2005a
from ..work.y2005 import resnick2005a
from ..work.y2007 import perez2007a
from ..work.y2007 import segal2007a
from ..work.y2008 import lunzer2008a
from ..work.y2008 import hartmann2008a
from ..work.y2008 import patel2008a
from ..work.y2010 import nguyen2010a
from ..work.y2010 import merali2010a
from ..work.y2011 import ko2011a
from ..work.y2011 import kuttal2011a
from ..work.y2012 import guo2012c
from ..work.y2012 import guo2012a
from ..work.y2012 import davenport2012a
from ..work.y2012 import yoon2012a
from ..work.y2013 import patel2013a
from ..work.y2014 import shen2014a
from ..work.y2014 import yoon2014a
from ..work.y2015 import deline2015a
from ..work.y2015 import yoon2015a
from ..work.y2016 import hill2016a
from ..work.y2016 import ragavan2016a
from ..work.y2017 import kery2017a
from ..work.y2017 import zhang2017a
from ..work.y2017 import cambronero2017a
from ..work.y2017 import myers2017a
from ..work.y2017 import kery2017b
from ..work.y2017 import nelson2017a
from ..work.y2017 import lee2017a
from ..work.y2018 import wang2018a
from ..work.y2018 import abdul2018a
from ..work.y2018 import fast2018a
from ..work.y2018 import kery2018a
from ..work.y2018 import rule2018a

DB(Citation(
    kery2017a, Site("Atom Editor", "https://atom.io/"), ref="1",
    contexts=[
        "Variolite is built on top of the Atom editor [1], and allows users to directly version code in their editor simply by drawing a box around a section of code and invoking a command.",
        "Based on this feedback, we iteratively designed and implemented a prototype tool called Variolite. Variolite is implemented in CoffeeScript and CSS, using the Atom editor’s package framework [1].",
        
    ],
))

DB(Citation(
    kery2017a, ko2005a, ref="2",
    contexts=[
        "Ko et al. [2], when studying experienced programmers, found that 60% of edits using comments were for temporarily commenting code during maintenance tasks.",

    ],
))

DB(Citation(
    kery2017a, ko2011a, ref="3",
    contexts=[
        "This sentiment is common to how end-user developers prioritize goals [3].",
        "Ko et al. distinguish end-user developers as having goals where a program is a means to an end, rather than professional developers, whose goals are the code itself as a product [3",
        
    ],
))

DB(Citation(
    kery2017a, lunzer2008a, ref="4",
    contexts=[
        "Juxtapose also built off of prior work such as Set Based Interactions [17] and Subjunctive Interfaces [4], which explored general techniques for exploring multiple alternatives in parallel.",

    ],
))

DB(Citation(
    kery2017a, sheil1983a, ref="5",
    contexts=[
        "We call this process exploratory programming [32][5], which we define as a programming task in which a specific goal or a means to that goal must be discovered by iteratively writing code for multiple ideas",

    ],
))

DB(Citation(
    kery2017a, hartmann2008a, ref="6",
    contexts=[
        "When programmers write code to design, discover, or explore ideas, there may be no clear requirements for that code at the onset, and there may be a broad space of possible solutions [6][16].",
        "Juxtapose [6] is a research tool that provided interaction designers with different alternatives of their code, in order to compare between different parameters of the look and feel of their interface designs.",
        "Using comments to store code has been observed in prior studies [6][31].",
        "This is similar to the tab-based versioning shown in Juxtapose [6].",
        "This is similar to the tab-based versioning shown in Juxtapose [6].",
        "In a simple use case, similar to Juxtapose [6], the user does not have to think about versioning more than switching between tabs.",
        
    ],
))

DB(Citation(
    kery2017a, hill2016a, ref="7",
    contexts=[
        "Another example is working with data to develop machine learning models or other intelligent systems, which is often a painstaking process of experimenting with different manipulations, parameters, and algorithms [7][14].",
        "Others who have studied data science and machine learning developers, such as Hill [7] and Guo [22] have described difficulties even for experts, struggling to create understandable and reproducible models during a process where they attempt many different things.",
        "Both Hill et al. [7] and Patel [15] reported that machine learning programmers struggled to reproduce or understand earlier experiments.",
        
    ],
))

DB(Citation(
    kery2017a, perez2007a, ref="8",
    contexts=[
        "Other literate programming tools, such as Knitr [30] or Jupyter notebooks [8] have become popular in recent years for clearly communicating data analysis code, rationale, and output.",
        "Burrito is also intended as a lab notebook approach, like literate programming tools such as Jupyter notebooks [8].",
        
    ],
))

DB(Citation(
    kery2017a, shen2014a, ref="9",
    contexts=[
        "Tools like Jupyter notebooks have become immensely popular for data science work [9], however the focus of literate programming tools is to clearly communicate analysis work, so that it can be shared with others and replicated.",
        
    ],
))

DB(Citation(
    kery2017a, beyer1997a, ref="10",
    contexts=[
        "Due to the timespan of significant projects, we chose a retrospective interview methodology rather that direct observation of their work [10].",

    ],
))

DB(Citation(
    kery2017a, carroll1987a, ref="11",
    contexts=[
        
    ],
))

DB(Citation(
    kery2017a, tukey1977a, ref="12",
    contexts=[
        "One example of when data scientists engage in exploratory programming is “exploratory data analysis,” which is a common approach to visualizing and asking questions of data, rather than more straightforward hypothesis testing [12]",
    ],
))

DB(Citation(
    kery2017a, segal2007a, ref="13",
    contexts=[
        "Similar arguments have been made in the scientific computing community, where problems of understandability and reproducibility during experimentation with code are often mentioned [13][16][34].",

    ],
))

DB(Citation(
    kery2017a, patel2008a, ref="14",
    contexts=[
        "Another example is working with data to develop machine learning models or other intelligent systems, which is often a painstaking process of experimenting with different manipulations, parameters, and algorithms [7][14].",
        "Patel et al. [14] observed that many difficulties in applying machine learning techniques arose from the “iterative and exploratory process” of using statistics as a software development tool.",
        "Patel’s interviews with machine learning developers emphasized the non-linear progression of this work where “an apparent dead end for a project was overcome by revisiting an earlier point in their process” [14].",
        
    ],
))

DB(Citation(
    kery2017a, patel2013a, ref="15",
    contexts=[
        "Both Hill et al. [7] and Patel [15] reported that machine learning programmers struggled to reproduce or understand earlier experiments.",

    ],
))

DB(Citation(
    kery2017a, nguyen2010a, ref="16",
    contexts=[
        "When programmers write code to design, discover, or explore ideas, there may be no clear requirements for that code at the onset, and there may be a broad space of possible solutions [6][16].",
        "Similar arguments have been made in the scientific computing community, where problems of understandability and reproducibility during experimentation with code are often mentioned [13][16][34].",
        "Prior work has shown that many scientists are unaware of good software development practices [16].",
        "A benefit of over-sampling from individuals with computer science background in the interview study is that this provides a more nuanced picture than previous work, which has studied version control usage by scientists who lack training in computer science [16]",
        ". Nguyen-Hoan et al., in a survey of scientists, found that 30% of their sample used VCS [16].",
        
    ],
))

DB(Citation(
    kery2017a, terry2004a, ref="17",
    contexts=[
        "Juxtapose also built off of prior work such as Set Based Interactions [17] and Subjunctive Interfaces [4], which explored general techniques for exploring multiple alternatives in parallel.",

    ],
))

DB(Citation(
    kery2017a, toomim2004a, ref="18",
    contexts=[
        "This tool used Linked Editing, a technique for editing two alternative pieces of code simultaneously, previously developed by Toomim et al. [18].",

    ],
))

DB(Citation(
    kery2017a, resnick2005a, ref="19",
    contexts=[
        "This is in line with the “low-floor, high-ceiling” principle proposed for creativity support tools [19]",

    ],
))

DB(Citation(
    kery2017a, clements2001a, ref="20",
    contexts=[
        "On the side of professional software engineering, software product lines are a method used in industry to adapt one piece of software to be customizable for different clients or devices [20].",
        "These are known for their complexity [20].",
        
    ],
))

DB(Citation(
    kery2017a, Site("Pete Warden. Why the term data science is flawed but useful: Counterpoints to four common data science criticisms., OReilly Radar Data Newsletter", "http://radar.oreilly.com/2011/05/data-scienceterminology.html"), ref="21",
    contexts=[
        "The term “data scientist” has a broad [29] and sometimes contested definition [21] but here we use “data scientist” in the simple sense of people who manipulate data to gain insights from it.",

    ],
))

DB(Citation(
    kery2017a, guo2012c, ref="22",
    contexts=[
        "Others who have studied data science and machine learning developers, such as Hill [7] and Guo [22] have described difficulties even for experts, struggling to create understandable and reproducible models during a process where they attempt many different things.",
        "Guo previously studied people who program to gain insights from data, whom he called “research programmers” [22].",
    ],
))

DB(Citation(
    kery2017a, guo2012a, ref="23",
    contexts=[
        "Guo et al. [23] also produced a research system called Burrito, which displays a GUI activity feed of things like outputs, save events, and notes relevant to a given project.",

    ],
))

DB(Citation(
    kery2017a, Site("R Studio", "https://www.rstudio.com/"), ref="24",
    contexts=[
        "R Studio, has focused on making it easier to quickly prototype ideas [25][24].",

    ],
))

DB(Citation(
    kery2017a, deline2015a, ref="25",
    contexts=[
        "R Studio, has focused on making it easier to quickly prototype ideas [25][24].",
        "Live programming environments, whose strength is instant feedback, tend to de-emphasize history, which DeLine et al. remarked was an issue their users cared about [25]",
        
    ],
))

DB(Citation(
    kery2017a, hawley1987a, ref="26",
    contexts=[

    ],
))

DB(Citation(
    kery2017a, kuttal2011a, ref="27",
    contexts=[
        "Other interactions for versioning have been developed for Enduser Programmers, such as for Mashups [27].",

    ],
))

DB(Citation(
    kery2017a, ragavan2016a, ref="28",
    contexts=[
        "This decision is informed by prior work by Srinivasa et al. [28] who used an information foraging theory approach to study how programmers distinguish between similar versions.",

    ],
))

DB(Citation(
    kery2017a, davenport2012a, ref="29",
    contexts=[
        "The term “data scientist” has a broad [29] and sometimes contested definition [21] but here we use “data scientist” in the simple sense of people who manipulate data to gain insights from it.",
        "We specifically target data scientists who write code, which is a large group [29] encompassing people who work with data in domains such as engineering, design, business, and research.",
        
    ],
))

DB(Citation(
    kery2017a, Site("Knitr tool", "http://yihui.name/knitr/"), ref="30",
    contexts=[
        "Other literate programming tools, such as Knitr [30] or Jupyter notebooks [8] have become popular in recent years for clearly communicating data analysis code, rationale, and output.",

    ],
))

DB(Citation(
    kery2017a, yoon2012a, ref="31",
    contexts=[
        "Using comments to store code has been observed in prior studies [6][31].",

    ],
))

DB(Citation(
    kery2017a, yoon2014a, ref="32",
    contexts=[
        "We call this process exploratory programming [32][5], which we define as a programming task in which a specific goal or a means to that goal must be discovered by iteratively writing code for multiple ideas",
        "This reflects the finding that people do not always know in advance what they will find useful [32]",
        
    ],
))

DB(Citation(
    kery2017a, yoon2015a, ref="33",
    contexts=[
        "Azurite [33] developed an interaction for selectively undoing past actions in code using a timeline visualization.",

    ],
))

DB(Citation(
    kery2017a, merali2010a, ref="34",
    contexts=[
        "Similar arguments have been made in the scientific computing community, where problems of understandability and reproducibility during experimentation with code are often mentioned [13][16][34].",

    ],
))

DB(Citation(
    kery2017a, bar2003a, ref="35",
    contexts=[
        "For example, developing a new algorithm for computational biology may take considerable trial-and-error on both the code and the concepts behind it [35].",

    ],
))

DB(Citation(
    wang2018a, kery2017a, ref="",
    contexts=[

    ],
))

DB(Citation(
    abdul2018a, kery2017a, ref="",
    contexts=[

    ],
))

DB(Citation(
    fast2018a, kery2017a, ref="",
    contexts=[

    ],
))

DB(Citation(
    zhang2017a, kery2017a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kery2018a, kery2017a, ref="",
    contexts=[

    ],
))

DB(Citation(
    cambronero2017a, kery2017a, ref="",
    contexts=[

    ],
))

DB(Citation(
    myers2017a, kery2017a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kery2017b, kery2017a, ref="",
    contexts=[

    ],
))

DB(Citation(
    rule2018a, kery2017a, ref="",
    contexts=[

    ],
))

DB(Citation(
    nelson2017a, kery2017a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lee2017a, kery2017a, ref="",
    contexts=[

    ],
))
