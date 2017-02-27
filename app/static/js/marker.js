var name;   //地名
var marker; // 标注
var lng;    // 经度
var lat;    // 维度


map.addEventListener("ondblclick", function (e) {
    lng = e.point.lng;
    lat = e.point.lat;

    var geoc = new BMap.Geocoder();
    geoc.getLocation(e.point, function (rs) {
        var addComp = rs.addressComponents;
        name = addComp.province + ',' + addComp.city + ',' + addComp.district + ',' +
            addComp.street + ',' + addComp.streetNumber;    // 地名
    });

    add_lay(lng, lat);  // 在双击点处添加标注
});


map.addEventListener("click", function (e) {

    var geoc = new BMap.Geocoder();
    geoc.getLocation(e.point, function (rs) {
        var addComp = rs.addressComponents;
        name = addComp.province + ',' + addComp.city + ',' + addComp.district + ',' +
            addComp.street + ',' + addComp.streetNumber;    // 地名
    });

    setFormValue(e.point.lng, e.point.lat, name);
});



