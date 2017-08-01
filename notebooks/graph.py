import os, sys

from textwrap import dedent
from pathlib import Path

from IPython.display import display

from snowballing.graph import Graph, getsvgcolors
from snowballing.operations import reload, load_work


class WebsiteGraph(Graph):
    
    def display(self, *args):
        """ Displays interactive graph and creates HTML page """
        if not super(WebsiteGraph, self).display(*args):
            return False
        
        background, color = {}, {}
        for key, value in self.toggle_widgets.items():
            background[key] = self.color_widgets[key].value
            color[key] = self.font_color_widgets[key].value

        legends = sorted(list(background.keys()))
        
        graph_name = self.graph_name + ".svg"
        html = dedent("""\
            <!DOCTYPE html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>PinS - Taxonomy</title>

                <!-- Bootstrap -->
                <link href="css/bootstrap.min.css" rel="stylesheet">
                <link href="css/style.css" rel="stylesheet">

                <!--[if lt IE 9]>
                  <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
                  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
                <![endif]-->
              <style type="text/CSS">
                .innercontainer {
                  display: inline-block;
                }

                ul.legend {
                  text-align: center;
                  list-style: none;
                  padding: 0;
                }

                ul.legend li {
                  display: inline-block;
                  padding: 10px 20px;
                  color: white;
                  margin: 10px;
                  border: 1px solid black;
                  vertical-align: middle;
                }

              </style>
            </head>

            <body>
        <nav class="navbar navbar-inverse navbar-fixed-top">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="index.html">PinS</a>
            </div>
            <div id="navbar" class="collapse navbar-collapse">
              <ul class="nav navbar-nav">
                <li><a href="index.html">Home</a></li>
                <li><a href="taxonomy.html">Taxonomy</a></li>
                <li><a href="approaches.html">Approaches</a></li>
                <li%s><a href="selected.html">Related Graph</a></li>
                <li%s><a href="graph.html">Full Graph</a></li>
              </ul>
              <ul class="nav navbar-nav navbar-right">
                <li><a href="https://github.com/dew-uff/pins"><span class="hidden-xs-down"> View on GitHub </span><svg version="1.1" width="16" height="16" viewBox="0 0 16 16" class="octicon octicon-mark-github" aria-hidden="true"><path id="githublogo" fill="rgb(157, 157, 157)" fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path></svg></a></li>
              </ul>
            </div><!--/.nav-collapse -->
          </div>
        </nav>
        <div class="container">
          <div class="starter-template">
              <div class="btn-toolbar" role="toolbar" aria-label="Toolbar">
                <div class="btn-group" role="group" aria-label="Download">
                  <a target="_blank" href="data/%s" download="%s" class="download btn btn-default">Download svg</a>
                </div>
              </div>
              <p> Tooltips provide extra information on each work. For unrelated work, the "due" attribute indicates why it is not related. </p>
              <div class="innercontainer">
                  <ul class="legend">
                    %s
                  </ul>
                  <div class="loadsvg"></div>
              </div>
          </div>
        </div> 
        <footer class="footer">
          <img height="50" alt="Universidade Federal Fluminense - Instituto da Computa&ccedil;&atilde;o"  title="Universidade Federal Fluminense - Instituto da Computa&ccedil;&atilde;o" src="images/ic.jpg">
          <img height="50" alt="New York University - Tandom School of Engineering" title="New York University - Tandom School of Engineering" src="images/nyu.png">
        </footer>
        <script src="js/jquery-3.1.0.min.js"></script>
        <script src="js/bootstrap.min.js"></script>
        <script src="js/svg-pan-zoom.min.js"></script>
        <script>
          $(".loadsvg").load("data/%s", function(){
                $("svg").addClass("refgraph");
                svgPanZoom('.refgraph', {'minZoom': 0.001});
                $(".hoverable polyline, .hoverable line").mouseenter(
                    function(e) {
                        //e.stopPropagation();
                        $(this).css("stroke", "blue");
                        $(this).css("stroke-width", "3px");
                    }).mouseleave(
                    function() {
                        $(this).css("stroke", "black");
                        $(this).css("stroke-width", "inherit");
                    });
                });
        </script>
        </body>
        </html>
        """) % (
            ' class="active"' if self.graph_name == "selected" else "",
            ' class="active"' if self.graph_name == "graph" else "",
            graph_name,
            graph_name,
            '\n'.join(
                ('    <li style="background-color:{};color:{}"><span>{}</span></li>'
                 .format(background[name], color[name], 
                         " ".join(name.split("_")).capitalize()))
                for name in legends
            ),
            graph_name,
        )
        html_name = str(Path("output") / (self.graph_name + ".html"))
        display(html_name)
        with open(html_name, "w") as html_file:
            html_file.write(html)
        
        return True


class GoalGraph(WebsiteGraph):
   
    def create_widgets(self):
        """ Creates custom categories """
        color_generator = getsvgcolors()
        
        work_list = load_work()
        goals = set()
        for work in work_list:
            if work.category not in ("snowball", "ok"):
                continue
            if not hasattr(work, "_meta"):
                continue
            goal = str(work._meta[0]["goal"])
            goals.add(goal)

        for goal in sorted(goals):
            color, textcolor = next(color_generator)
            self.create_category(
                goal, goal,
                True,
                color, textcolor,
            )
            
    def work_key(self, work):
        """ Returns work goal """
        if not hasattr(work, "_meta"):
            return None
        return str(work._meta[0]["goal"])
    
    def filter_work(self, work):
        """ Filters work """
        if work.category not in ("snowball", "ok"):
            return False
        return super(GoalGraph, self).filter_work(work)


class FullGraph(WebsiteGraph):
    
    def create_widgets(self):
        """ Creates custom categories """
        for class_ in self.visible_classes():
            self.create_category(
                class_[0], class_[1],
                True,
                class_[3], class_[4],
            )
