var url = $SCRIPT_ROOT.substring(0, $SCRIPT_ROOT.indexOf('/map'));  // 请求根目录
var car_url = url + '/static/img/car.png';      // 汽车图片url

// 初始化地图
var map = new BMap.Map("allmap"); // 关闭底图可点动能
// map.enableScrollWheelZoom();       // 鼠标滚动缩放
var point = new BMap.Point(117.051534, 36.660632);
map.centerAndZoom(point, 16);

// 设置运动起点及终点
var myP1 = new BMap.Point(117.037125, 36.659546);    //起点
var myP2 = new BMap.Point(117.071485, 36.666755);    //终点

var myIcon = new BMap.Icon(src = car_url, new BMap.Size(62, 70), {    //小车图片
    //offset: new BMap.Size(0, -5),    //相当于CSS精灵
    imageOffset: new BMap.Size(0, 0)    //图片的偏移量。为了是图片底部中心对准坐标点。
});

var driving2 = new BMap.DrivingRoute(map, {renderOptions: {map: map, autoViewport: true}});    //驾车实例
driving2.search(myP1, myP2);    //显示一条公交线路

window.run = function () {
    var driving = new BMap.DrivingRoute(map);    //驾车实例
    driving.search(myP1, myP2);
    driving.setSearchCompleteCallback(function () {
        var pts = driving.getResults().getPlan(0).getRoute(0).getPath();    //通过驾车实例，获得一系列点的数组
        var paths = pts.length;    //获得有几个点

        var carMk = new BMap.Marker(pts[0], {icon: myIcon});
        map.addOverlay(carMk);
        i = 0;
        function resetMkPoint(i) {
            carMk.setPosition(pts[i]);
            if (i < paths) {
                setTimeout(function () {
                    i++;
                    resetMkPoint(i);
                }, 100);
            }
        }

        setTimeout(function () {
            resetMkPoint(5);
        }, 100)

    });
}

setTimeout(function () {
    run();
}, 5000);