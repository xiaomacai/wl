var url = $SCRIPT_ROOT.substring(0,$SCRIPT_ROOT.indexOf('/map'));  // 请求根目录

var pointDisaster = new BMap.Point(117.071485, 36.666755);  // 受灾点坐标
var fireIcon = new BMap.Icon(src=url + '/static/img/fire.ico', new BMap.Size(110,67));
var marker1 = new BMap.Marker(pointDisaster, {icon:fireIcon});  // 创建受灾点标注
map.addOverlay(marker1);               // 将标注添加到地图中
marker1.setAnimation(BMAP_ANIMATION_BOUNCE); //跳动的动画


var pointRescue = new BMap.Point(117.037125, 36.659546);
var rescueIcon = new BMap.Icon(src=url + '/static/img/rescue.ico', new BMap.Size(150,60));

var marker2 = new BMap.Marker(pointRescue, {icon: rescueIcon})
map.addOverlay(marker2);
marker2.setAnimation(BMAP_ANIMATION_BOUNCE);