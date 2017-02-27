// 通过获取nodes值在地图中显示点病标注出来
var ns = document.getElementsByName("nodes")[0].value;
var ns_array = ns.split('-');
ns_array.forEach(function (element) {
    lng_lat = element.split(',');
    add_lay(lng_lat[0], Number(lng_lat[1]), Number(lng_lat[2]));
});
