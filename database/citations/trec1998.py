# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y1984 import leblang1984a
from ..work.y1985 import leblang1985a
from ..work.y1988 import bershad1988a
from ..work.y1988 import howard1988a
from ..work.y1989 import bubenik1989a
from ..work.y1989 import mccarthy1989a
from ..work.y1990 import clemm1990a
from ..work.y1990 import stonebraker1990a
from ..work.y1990 import widom1990a
from ..work.y1991 import baker1991a
from ..work.y1991 import douglis1991a
from ..work.y1992 import cate1992a
from ..work.y1993 import danzig1993a
from ..work.y1993 import gupta1993a
from ..work.y1993 import jones1993a
from ..work.y1993 import levin1993a
from ..work.y1994 import braun1994a
from ..work.y1995 import gupta1995a
from ..work.y1996 import alvisi1996a
from ..work.y1996 import chankhunthod1996a
from ..work.y1996 import colby1996a
from ..work.y1996 import ghormley1996a
from ..work.y1996 import goldberg1996a
from ..work.y1996 import gwertzman1996a
from ..work.y1996 import kawaguchi1996a
from ..work.y1997 import duska1997a
from ..work.y1997 import gribble1997a
from ..work.y1997 import heydon1997a
from ..work.y1997 import iyenger1997a
from ..work.y1997 import zhang1997a
from ..work.y1998 import vahdat1998a
from ..work.y1998 import schechter1998a
from ..work.y1998 import vahdat1998b

DB(Citation(
    vahdat1998a, alvisi1996a, ref="[Alvisi & Marzullo 1996]",
    contexts=[
        "1Note that techniques from the fault tolerance community could potentially address this limitation [Alvisi & Marzullo 1996].",
        
    ],
))

DB(Citation(
    vahdat1998a,
    Site("Apache HTTP Server Project, 1995", "http://www.apache.org/"),
    ref="[Apa 1995]",
    contexts=[
        "The next benchmark is a compilation of the Apache HTTP server, version 1.2.4 [Apa 1995].",
        
    ],
))

DB(Citation(
    vahdat1998a, baker1991a, ref="[Baker et al. 1991]",
    contexts=[
        "Note that earlier ﬁle system tracing studies also inferred read and write operations to avoid the extra overhead of tracing the read/write system calls [Baker et al. 1991].",
        
    ],
))

DB(Citation(
    vahdat1998a, bershad1988a, ref="[Bershad & Pinkerton 1988]",
    contexts=[
        "Various tools such as Watchdogs [Bershad & Pinkerton 1988], Interposition Agents [Jones 1993], or SLIC [Ghormley et al. 1996] can be used to trace system call activity with little or no overhead.",
        
    ],
))

DB(Citation(
    vahdat1998a, braun1994a, ref="[Braun & Claffy 1994]",
    contexts=[
        "Similar studies of WWW trafﬁc yielded similar results [Braun & Claffy 1994, Duska et al. 1997, Gribble & Brewer 1997].",
        
    ],
))

DB(Citation(
    vahdat1998a, bubenik1989a, ref="[Bubenik & Zwaenepoel 1989]",
    contexts=[
        "Of course, earlier work in optimistic make [Bubenik & Zwaenepoel 1989] has demonstrated the value of creating output ﬁles in anticipation of user requests.",
        
    ],
))

DB(Citation(
    vahdat1998a, cate1992a, ref="[Cate 1992]",
    contexts=[
        "Gwertzman and Seltzer [Gwertzman & Seltzer 1996] recently proposed using the Alex protocol [Cate 1992] for maintaining cache consistency across the wide area.",
        
    ],
))

DB(Citation(
    vahdat1998a, chankhunthod1996a, ref="[Chankhunthod et al. 1996]",
    contexts=[
        "In response to the exponential growth of packets across the Internet, several researchers have proposed a number of caching schemes both to reduce the load on Internet backbones and to improve user response times [Gwertzman & Seltzer 1996, Chankhunthod et al. 1996, Zhang et al. 1997].",
        "Another approachis to allowproxycachesto cachedynamicobjects with a TTL-based invalidation scheme [Chankhunthod et al. 1996, Gwertzman & Seltzer 1996, Squ 1996].",
        "Harvest [Chankhunthod et al. 1996] and Squid [Squ 1996] are efforts into hierarchical web proxy caching.",
        
    ],
))

DB(Citation(
    vahdat1998a, clemm1990a, ref="[Clemm & Osterweil 1990]",
    contexts=[
        "DSEE [Leblang & Chase 1984, Leblang & McLean 1985], Odin [Clemm & Osterweil 1990] and Vesta [Levin & McJones 1993, Heydon et al. 1997] provide tools for modeling the behavior of programs, enabling the concise speciﬁcation of derivation rules, and distributing changes to developers.",
        
    ],
))

DB(Citation(
    vahdat1998a, colby1996a, ref="[Colby et al. 1996]",
    contexts=[
        "For example, research efforts into materialized views [Gupta et al. 1993, Gupta & Mumick 1995, Colby et al. 1996, Kawaguchi et al. 1996] in active databases [McCarthy & Dayal 1989, Stonebraker et al. 1990, Widom & Finkelstein 1990] has resulted in support for such views in many commercial database systems.",
        
    ],
))

DB(Citation(
    vahdat1998a, danzig1993a, ref="[Danzig et al. 1993]",
    contexts=[
        "One early study [Danzig et al. 1993] found that strategically-placed caches could reduce FTP ﬁle trafﬁc by as much as 50%.",
        
    ],
))

DB(Citation(
    vahdat1998a, douglis1991a, ref="[Douglis & Ousterhout 1991]",
    contexts=[
        "The performance results presented in Section 2.2 here are similar to overhead studies of process migration and remote execution in Sprite [Douglis & Ousterhout 1991].",
        
    ],
))

DB(Citation(
    vahdat1998a,
    DB(Email(1993, "Dozier, J.", "Personal Communication")),
    ref="[Dozier 1993]",
    contexts=[
        "It is believed that several journal articles have since been published still based on the incorrectdata [Dozier 1993].",
        
    ],
))

DB(Citation(
    vahdat1998a, duska1997a, ref="[Duska et al. 1997]",
    contexts=[
        "Similar studies of WWW trafﬁc yielded similar results [Braun & Claffy 1994, Duska et al. 1997, Gribble & Brewer 1997].",
        
    ],
))

DB(Citation(
    vahdat1998a, ghormley1996a, ref="[Ghormley et al. 1996]",
    contexts=[
        "Various tools such as Watchdogs [Bershad & Pinkerton 1988], Interposition Agents [Jones 1993], or SLIC [Ghormley et al. 1996] can be used to trace system call activity with little or no overhead.",
        
    ],
))

DB(Citation(
    vahdat1998a, goldberg1996a, ref="[Goldberg et al. 1996]",
    contexts=[
        "Since Unmake can provide process lineage information, it can trace ﬁle accesses back to the shell (and hence the user id) of the process that originally executed su. Such a tool can also be extended to monitor system calls, disallowing certain accesses based on the “effective”uid of the calling process [Goldberg et al. 1996]",
        
    ],
))

DB(Citation(
    vahdat1998a, gribble1997a, ref="[Gribble & Brewer 1997]",
    contexts=[
        "Similar studies of WWW trafﬁc yielded similar results [Braun & Claffy 1994, Duska et al. 1997, Gribble & Brewer 1997].",
        
    ],
))

DB(Citation(
    vahdat1998a, gupta1995a, ref="[Gupta & Mumick 1995]",
    contexts=[
        "For example, research efforts into materialized views [Gupta et al. 1993, Gupta & Mumick 1995, Colby et al. 1996, Kawaguchi et al. 1996] in active databases [McCarthy & Dayal 1989, Stonebraker et al. 1990, Widom & Finkelstein 1990] has resulted in support for such views in many commercial database systems.",
        
    ],
))

DB(Citation(
    vahdat1998a, gupta1993a, ref="[Gupta et al. 1993]",
    contexts=[
        "For example, research efforts into materialized views [Gupta et al. 1993, Gupta & Mumick 1995, Colby et al. 1996, Kawaguchi et al. 1996] in active databases [McCarthy & Dayal 1989, Stonebraker et al. 1990, Widom & Finkelstein 1990] has resulted in support for such views in many commercial database systems.",
        
    ],
))

DB(Citation(
    vahdat1998a, gwertzman1996a, ref="[Gwertzman & Seltzer 1996]",
    contexts=[
        "In response to the exponential growth of packets across the Internet, several researchers have proposed a number of caching schemes both to reduce the load on Internet backbones and to improve user response times [Gwertzman & Seltzer 1996, Chankhunthod et al. 1996, Zhang et al. 1997].",
        "Another approachis to allowproxycachesto cachedynamicobjects with a TTL-based invalidation scheme [Chankhunthod et al. 1996, Gwertzman & Seltzer 1996, Squ 1996].",
        "Gwertzman and Seltzer [Gwertzman & Seltzer 1996] recently proposed using the Alex protocol [Cate 1992] for maintaining cache consistency across the wide area.",
        
    ],
))

DB(Citation(
    vahdat1998a, heydon1997a, ref="[Heydon et al. 1997]",
    contexts=[
        "While not currently implemented, unmake combined with a source control system or, more generally, a ﬁle system capable of transparently producing older ﬁle versions [Heydon et al. 1997] can be used to rollback to earlier versions of output ﬁles",
        "DSEE [Leblang & Chase 1984, Leblang & McLean 1985], Odin [Clemm & Osterweil 1990] and Vesta [Levin & McJones 1993, Heydon et al. 1997] provide tools for modeling the behavior of programs, enabling the concise speciﬁcation of derivation rules, and distributing changes to developers.",
        
    ],
))

DB(Citation(
    vahdat1998a, howard1988a, ref="[Howard et al. 1988]",
    contexts=[
        "One approach to addressing this limitation is to use a wide-area ﬁle system such as AFS [Howard et al. 1988] or WebFS [Vahdat et al. 1998] to store and to cache dynamic web objects as normal ﬁles.",
        
    ],
))

DB(Citation(
    vahdat1998a, iyenger1997a, ref="[Iyenger & Challenger 1997]",
    contexts=[
        "While existing work allows for applications to be written that can cache their results [Iyenger & Challenger 1997], TREC automates this process by automatically caching program results and invalidates such results when the input to a CGI program changes (e.g., a new version of Navigator becomes available)",
        "Approximately 20% of the queries to IBM's Web server for the 1996 Olympic games resulted in the dynamic generation of HTML (e.g., to get current medal standings) [Iyenger & Challenger 1997].",
        "Iyenger and Challenger [Iyenger & Challenger 1997] have implemented a caching system and API as part of IBM's web server that allows for caching of dynamic data",
        
    ],
))

DB(Citation(
    vahdat1998a, jones1993a, ref="[Jones 1993]",
    contexts=[
        "Various tools such as Watchdogs [Bershad & Pinkerton 1988], Interposition Agents [Jones 1993], or SLIC [Ghormley et al. 1996] can be used to trace system call activity with little or no overhead.",
        
    ],
))

DB(Citation(
    vahdat1998a, kawaguchi1996a, ref="[Kawaguchi et al. 1996]",
    contexts=[
        "For example, research efforts into materialized views [Gupta et al. 1993, Gupta & Mumick 1995, Colby et al. 1996, Kawaguchi et al. 1996] in active databases [McCarthy & Dayal 1989, Stonebraker et al. 1990, Widom & Finkelstein 1990] has resulted in support for such views in many commercial database systems.",
        
    ],
))

DB(Citation(
    vahdat1998a, leblang1984a, ref="[Leblang & Chase 1984]",
    contexts=[
        "DSEE [Leblang & Chase 1984, Leblang & McLean 1985], Odin [Clemm & Osterweil 1990] and Vesta [Levin & McJones 1993, Heydon et al. 1997] provide tools for modeling the behavior of programs, enabling the concise speciﬁcation of derivation rules, and distributing changes to developers.",
        
    ],
))

DB(Citation(
    vahdat1998a, leblang1985a, ref="[Leblang & McLean 1985]",
    contexts=[
        "DSEE [Leblang & Chase 1984, Leblang & McLean 1985], Odin [Clemm & Osterweil 1990] and Vesta [Levin & McJones 1993, Heydon et al. 1997] provide tools for modeling the behavior of programs, enabling the concise speciﬁcation of derivation rules, and distributing changes to developers.",
        
    ],
))

DB(Citation(
    vahdat1998a, levin1993a, ref="[Levin & McJones 1993]",
    contexts=[
        "First, it frees users from manually specifying dependency information in a language that can be restrictive [Levin & McJones 1993].",
        "DSEE [Leblang & Chase 1984, Leblang & McLean 1985], Odin [Clemm & Osterweil 1990] and Vesta [Levin & McJones 1993, Heydon et al. 1997] provide tools for modeling the behavior of programs, enabling the concise speciﬁcation of derivation rules, and distributing changes to developers.",
        
    ],
))

DB(Citation(
    vahdat1998a, mccarthy1989a, ref="[McCarthy & Dayal 1989]",
    contexts=[
        "For example, research efforts into materialized views [Gupta et al. 1993, Gupta & Mumick 1995, Colby et al. 1996, Kawaguchi et al. 1996] in active databases [McCarthy & Dayal 1989, Stonebraker et al. 1990, Widom & Finkelstein 1990] has resulted in support for such views in many commercial database systems.",
        
    ],
))

DB(Citation(
    vahdat1998a,
    Site("ISAPIOverview", "http://www.microsft.com/msdn/sdk/platforms/doc/sdk/internet/src/isapimr%g.htm", authors="Microsoft Corporation"),
    ref="[Microsoft Corporation]",
    contexts=[
        ". Given the inherent inefﬁciency of spawning a new process for dynamically generated content, a number of systems, such as ISAPI [Microsoft Corporation ], NSAPI [Netscape ], and FastCGI [Open Market ], address this issue either by creating longlived “server” processes responsible for creating dynamic content or by linking dynamic content producers into the servers address space",
        
    ],
))

DB(Citation(
    vahdat1998a,
    Site("The Server-Application Function and Netscape Server API", "http://www.netscape.com/newsref/srd/server_api.html"),
    ref="[Netscape]",
    contexts=[
        ". Given the inherent inefﬁciency of spawning a new process for dynamically generated content, a number of systems, such as ISAPI [Microsoft Corporation ], NSAPI [Netscape ], and FastCGI [Open Market ], address this issue either by creating longlived “server” processes responsible for creating dynamic content or by linking dynamic content producers into the servers address space",
        
    ],
))

DB(Citation(
    vahdat1998a,
    Site("Fastcgi", "http://www.fastcgi.com"),
    ref="[Open Market]",
    contexts=[
        ". Given the inherent inefﬁciency of spawning a new process for dynamically generated content, a number of systems, such as ISAPI [Microsoft Corporation ], NSAPI [Netscape ], and FastCGI [Open Market ], address this issue either by creating longlived “server” processes responsible for creating dynamic content or by linking dynamic content producers into the servers address space",
        
    ],
))

DB(Citation(
    vahdat1998a,
    Site("VOV", "http://www.rtda.com/vov.html", authors="Runtime Design Automation"),
    ref="[RTDA]",
    contexts=[
       "VOV [RTDA ], a conﬁguration management toolkit, is similar to TREC, in that it observes program invocations to generate a trace of lineage information.",
         
    ],
))

DB(Citation(
    vahdat1998a, schechter1998a, ref="[Schechter et al. 1998]",
    contexts=[
        "Finally, one proposal advocates using HTTP proﬁles to predict accesses to dynamically generated data, allowing servers to pregenerate potentially expensive pages in anticipation of user requests [Schechter et al. 1998].",
        
    ],
))

DB(Citation(
    vahdat1998a,
    Site("Squid Internet Object Cache", "http://squid.nlanr.net/Squid/"),
    ref="[Squ 1996]",
    contexts=[
        "Another approachis to allowproxycachesto cachedynamicobjects with a TTL-based invalidation scheme [Chankhunthod et al. 1996, Gwertzman & Seltzer 1996, Squ 1996].",
        "Harvest [Chankhunthod et al. 1996] and Squid [Squ 1996] are efforts into hierarchical web proxy caching.",
        
    ],
    accessed="1996",
))

DB(Citation(
    vahdat1998a, stonebraker1990a, ref="[Stonebraker et al. 1990]",
    contexts=[
        "For example, research efforts into materialized views [Gupta et al. 1993, Gupta & Mumick 1995, Colby et al. 1996, Kawaguchi et al. 1996] in active databases [McCarthy & Dayal 1989, Stonebraker et al. 1990, Widom & Finkelstein 1990] has resulted in support for such views in many commercial database systems.",
        
    ],
))

DB(Citation(
    vahdat1998a, vahdat1998b, ref="[Vahdat et al. 1998]",
    contexts=[
        "One approach to addressing this limitation is to use a wide-area ﬁle system such as AFS [Howard et al. 1988] or WebFS [Vahdat et al. 1998] to store and to cache dynamic web objects as normal ﬁles.",
        
    ],
))

DB(Citation(
    vahdat1998a, widom1990a, ref="[Widom & Finkelstein 1990]",
    contexts=[
        "For example, research efforts into materialized views [Gupta et al. 1993, Gupta & Mumick 1995, Colby et al. 1996, Kawaguchi et al. 1996] in active databases [McCarthy & Dayal 1989, Stonebraker et al. 1990, Widom & Finkelstein 1990] has resulted in support for such views in many commercial database systems.",
        
    ],
))

DB(Citation(
    vahdat1998a, zhang1997a, ref="[Zhang et al. 1997]",
    contexts=[
        "In response to the exponential growth of packets across the Internet, several researchers have proposed a number of caching schemes both to reduce the load on Internet backbones and to improve user response times [Gwertzman & Seltzer 1996, Chankhunthod et al. 1996, Zhang et al. 1997].",
        
    ],
))
