$.getJSON($SCRIPT_ROOT + '/jquery/all_nodes', {}, function (data) {
    show_nodes(data.result);
});

function show_nodes(nodes_list) {
    var id, lng, lat;
    for (id in nodes_list) {
        lng = nodes_list[id]['longitude'];
        lat = nodes_list[id]['latitude'];
        add_lay(id, lng, lat);
    }
}
function add_lay(id, lng, lat) {
    // 在（lng,lat)的点标注
    point = new BMap.Point(Number(lng), Number(lat));
    var marker = new BMap.Marker(point);
    // marker.setLabel(new BMap.Label(id));    //添加标注标签为节点编号
    map.addOverlay(marker);
    // marker.addEventListener('click', attribute);    // 为marker添加事件，点击alert经纬度
}
