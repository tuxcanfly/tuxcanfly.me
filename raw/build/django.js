window.onload = function tryDraw() {
  var result;
  var dotFile = document.querySelector("#django_dot");

  var debugAlignmentRE = /[?&]alignment=([^&]+)/;
  var debugAlignmentMatch = window.location.search.match(debugAlignmentRE);
  var debugAlignment;
  if (debugAlignmentMatch) debugAlignment = debugAlignmentMatch[1];

  result = graphlibDot.parse(dotFile.textContent);
  if (result) {
    // Cleanup old graph
    var svg = d3.select("svg");

    var renderer = new dagreD3.Renderer();

    // Handle debugAlignment
    renderer.postLayout(function(graph) {
      if (debugAlignment) {
        // First find necessary delta...
        var minX = Math.min.apply(null, graph.nodes().map(function(u) {
          var value = graph.node(u);
          return value[debugAlignment] - value.width / 2;
        }));

        // Update node positions
        graph.eachNode(function(u, value) {
          value.x = value[debugAlignment] - minX;
        });

        // Update edge positions
        graph.eachEdge(function(e, u, v, value) {
          value.points.forEach(function(p) {
            p.x = p[debugAlignment] - minX;
          });
        });
      }
    });

    // Uncomment the following line to get straight edges
    //renderer.edgeInterpolate('linear');

    // Custom transition function
    function transition(selection) {
      return selection.transition().duration(500);
    }

    renderer.transition(transition);

    var layout = renderer.run(result, svg.select("g"));
    transition(d3.select("svg"))
      .attr("width", layout.graph().width + 40)
      .attr("height", layout.graph().height + 40)
    d3.select("svg")
      .call(d3.behavior.zoom().on("zoom", function() {
        var ev = d3.event;
        svg.select("g")
          .attr("transform", "translate(" + ev.translate + ") scale(" + ev.scale + ")");
      }));
  }
};
