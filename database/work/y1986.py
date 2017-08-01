# coding: utf-8
from datetime import datetime
from snowballing.models import *
from ..places import *


chambers1986a = DB(WorkNoFile(
    1986, "A computing environment for statisticians",
    display="chambers",
    authors="Chambers, John M",
    place=TechReport,
    institution="AT&T Bell Laboratories Statistical Research Report",
    local="Murray Hill, NJ",
    request="wont",
    entrytype="misc",
    scholar_ok="impossible",
))

ciss1986a = DB(WorkUnrelated(
    1986, "Second Catalan International Symposium on Statistics: 18th-19th September 1986, Barcelona, Spain",
    due="It is a conference",
    display="bonet",
    authors="Bonet, Eduardo",
    place=CISS,
    link="https://books.google.com.br/books/about/Second_Catalan_International_Symposium_o.html?id=AOtUAAAAYAAJ&hl=en&output=html_text&redir_esc=y",
    ID="bonet1986second",
    entrytype="book",
    publisher="Consorci d'Informacio i Documentacio de Catalunya",
    volume="1",
    scholar_ok=True,
))

cowley1986a = DB(WorkNoFile(
    1986, "Experiences with a data analysis management prototype",
    due="Excluding tech report. Unrelated to script",
    display="cowley",
    authors="Cowley, Paula J and Carr, Daniel B and Nicholson, WL",
    place=TechReport,
    institution="Pacific Northwest Lab., Richland, WA (USA)",
    ID="cowley1986experiences",
    entrytype="techreport",
    request="wont",
    scholar_ok=True,
))
