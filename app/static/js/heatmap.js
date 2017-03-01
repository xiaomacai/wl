var nodes;
var loads;
$(function () {
    $.getJSON($SCRIPT_ROOT + '/jquery/all_nodes', {}, function (data) {
        nodes = data.result;
    });
    $.getJSON($SCRIPT_ROOT + '/jquery/all_loads', {}, function (data) {
        loads = data.result;
    });
    show_heat_map(nodes, loads);

});

function show_heat_map(nodes, loads) {
    var points = [];

    loads.forEach(function (load) {
        var start_id = load[0];
        var end_id = load[1];
        var start_lng = nodes[start_id]['longitude'];
        var start_lat = nodes[start_id]['latitude'];
        var end_lng = nodes[end_id]['longitude'];
        var end_lat = nodes[end_id]['latitude'];
        var k = (start_lat - end_lat) / (start_lng - end_lng);
        var step = (start_lng - end_lng) / 10;
        var flow = load[4];

        for (var i = 0; i <= 10; i++) {
            var point = {"lng": end_lng + i * step, "lat": k * i * step + end_lat, "count": flow};
            points.push(point);
        }
    });

    heatmapOverlay = new BMapLib.HeatmapOverlay({"radius": 20});
    map.addOverlay(heatmapOverlay);
    heatmapOverlay.setDataSet({data: points, max: 100});
}