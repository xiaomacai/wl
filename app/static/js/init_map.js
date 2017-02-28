var map = new BMap.Map("allmap", {enableMapClick: false}); // 关闭底图可点动能
map.enableScrollWheelZoom(true);       // 鼠标滚动缩放
var point = new BMap.Point(117.051534, 36.660632);
map.centerAndZoom(point, 16);
