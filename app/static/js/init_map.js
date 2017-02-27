var map = new BMap.Map("allmap", {enableMapClick: false}); // 关闭底图可点动能
map.enableScrollWheelZoom(true);       // 鼠标滚动缩放
var point = new BMap.Point(117.051534, 36.660632);
map.centerAndZoom(point, 16);


function add_lay(id, lng, lat) {
    // 在（lng,lat)的点标注
    point = new BMap.Point(Number(lng), Number(lat));
    marker = new BMap.Marker(point);
    marker.setLabel(new BMap.Label(id));    //添加标注标签为节点编号
    map.addOverlay(marker);
}


function setFormValue(lng, lat, name) {
    
    var a = document.getElementsByName("longitude")[0];
    var b = document.getElementsByName("latitude")[0];
    var c = document.getElementsByName("name")[0];

    a.value = lng;
    b.value = lat;
    c.value = name;
}