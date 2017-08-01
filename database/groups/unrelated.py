""" Use this file to declare unrelated groups of work """
from snowballing.approaches import GroupUnrelated
from .models import description

# Database Systems
with description("Cheney Dependency DB"):
    from ..work.y2007 import cheney2007b
    from ..work.y2011 import cheney2011a
    cheney_dependency_db = GroupUnrelated(cheney2007b, cheney2011a)

# Workflow Systems
with description("ProvMonitor"):
    from ..work.y2013 import neves2013a
    from ..work.y2014 import neves2014a
    provmonitor = GroupUnrelated(neves2013a, neves2014a)

with description("VisTrails"):
    from ..work.y2005 import bavoil2005a
    from ..work.y2006 import freire2006a
    from ..work.y2006 import callahan2006b
    from ..work.y2007 import scheidegger2007a
    from ..work.y2008 import scheidegger2008a
    vistrails = GroupUnrelated(
        bavoil2005a, freire2006a, callahan2006b, scheidegger2007a,
        scheidegger2008a,
    )

with description("Taverna"):
    from ..work.y2004 import oinn2004a
    from ..work.y2006 import oinn2006a
    from ..work.y2006 import hull2006a
    from ..work.y2008 import zhao2008a
    from ..work.y2008 import missier2008a
    from ..work.y2013 import wolstencroft2013a
    from ..work.y2014 import cohen2014a
    taverna = GroupUnrelated(
        oinn2004a, oinn2006a, hull2006a, zhao2008a, missier2008a, 
        wolstencroft2013a, cohen2014a,
    )

with description("Pegasus"):
    from ..work.y2004 import deelman2004b
    from ..work.y2007 import gil2007b
    from ..work.y2008 import kim2008a
    pegasus = GroupUnrelated(deelman2004b, gil2007b, kim2008a)

with description("Kepler"):
    from ..work.y2006 import ludascher2006a
    from ..work.y2006 import altintas2006a
    from ..work.y2006 import mcphillips2006a
    from ..work.y2007 import bowers2007a
    from ..work.y2008 import bowers2008a
    from ..work.y2008 import bowers2008b
    from ..work.y2009 import mouallem2009a
    from ..work.y2012 import bieda2012a
    from ..work.y2012 import dou2012a
    from ..work.y2012 import stropp2012a
    kepler = GroupUnrelated(
        ludascher2006a, altintas2006a, mcphillips2006a, bowers2007a, 
        bowers2008a, bowers2008b, mouallem2009a, bieda2012a, dou2012a,
        stropp2012a,
    )

with description("Chiron"):
    from ..work.y2013 import horta2013a
    chiron = GroupUnrelated(horta2013a)

with description("Karma"):
    from ..work.y2008 import simmhan2008a
    from ..work.y2008 import simmhan2008b
    from ..work.y2010 import simmhan2010a
    karma = GroupUnrelated(simmhan2008a, simmhan2008b, simmhan2010a)

with description("Swift"):
    from ..work.y2007 import zhao2007a
    swift = GroupUnrelated(zhao2007a)

with description("Tavaxy"):
    from ..work.y2012 import abouelhoda2012a
    tavaxy = GroupUnrelated(abouelhoda2012a)

with description("Galaxy"):
    from ..work.y2007 import taylor2007b
    from ..work.y2010 import goecks2010a
    galaxy = GroupUnrelated(taylor2007b, goecks2010a)

with description("Ediflow"):
    from ..work.y2011 import benzaken2011a
    ediflow = GroupUnrelated(benzaken2011a)

with description("Triana"):
    from ..work.y2007 import taylor2007a
    triana = GroupUnrelated(taylor2007a)

with description("Little JIL"):
    from ..work.y2011 import lerner2011a
    little_jil = GroupUnrelated(lerner2011a)

with description("SciCumulus"):
    from ..work.y2010 import oliveira2010a
    scicumulos = GroupUnrelated(oliveira2010a)

# Virtual Machines
with description("Paper Mâché"):
    from ..work.y2011 import brammer2011a
    paper_mache = GroupUnrelated(brammer2011a, _category="vm")
    
with description("SHARE"):
    from ..work.y2010 import gorp2010a
    from ..work.y2011 import gorp2011a
    share = GroupUnrelated(gorp2010a, gorp2011a, _category="vm")