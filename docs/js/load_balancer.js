let data = [{
        "lng": "121.4558",
        "lat": "31.0410",
        "name": "河西食堂",
        "count": Math.floor(Math.random() * 500)
    },
    {
        "lng": "121.4570",
        "lat": "31.0412",
        "name": "河西食堂",
        "count": Math.floor(Math.random() * 500)
    },
    {
        "lng": "121.4568",
        "lat": "31.0338",
        "name": "秋实阁",
        "count": Math.floor(Math.random() * 500)
    },
    {
        "lng": "121.4617",
        "lat": "31.0386",
        "name": "华闽食堂",
        "count": Math.floor(Math.random() * 500)
    },
    {
        "lng": "121.4650",
        "lat": "31.0405",
        "name": "秋林阁",
        "count": Math.floor(Math.random() * 500)
    }, {
        "lng": "121.4591",
        "lat": "31.0357",
        "name": "图书馆",
        "count": Math.floor(Math.random() * 1000)
    }];

let inmap = new inMap.Map({
    id: 'map',
    skin: "Blueness",
    center: [121.46, 31.037], // 地图中心点
    zoom: {
        value: 17,
        show: true
    }
});

let overlay = new inMap.DotOverlay({
    tooltip: {
        show: true,
        position: 'top',
        formatter: "{name}: {count}人"
    },
    style: {
        normal: {
            backgroundColor: "rgba(0, 0, 0, 1)",
            borderColor: "rgba(255, 255, 255, 1)",
            borderWidth: 1,
            size: 9
        },
        splitList: [{
            start: 0,
            end: 33,
            backgroundColor: "#FFFFFF"
        }, {
            start: 33,
            end: 67,
            backgroundColor: "#FFEEEE"
        }, {
            start: 67,
            end: 100,
            backgroundColor: "#FFDDDD"
        }, {
            start: 100,
            end: 133,
            backgroundColor: "#FFCCCC"
        }, {
            start: 133,
            end: 167,
            backgroundColor: "#FFBBBB"
        }, {
            start: 167,
            end: 200,
            backgroundColor: "#FFAAAA"
        }, {
            start: 200,
            end: 233,
            backgroundColor: "#FF9999"
        }, {
            start: 233,
            end: 267,
            backgroundColor: "#FF8888"
        }, {
            start: 267,
            end: 300,
            backgroundColor: "#FF7777"
        }, {
            start: 300,
            end: 333,
            backgroundColor: "#FF6666"
        }, {
            start: 333,
            end: 367,
            backgroundColor: "#FF5555"
        }, {
            start: 367,
            end: 400,
            backgroundColor: "#FF5555"
        }, {
            start: 400,
            end: 433,
            backgroundColor: "#FF4444"
        }, {
            start: 433,
            end: 467,
            backgroundColor: "#FF3333"
        }, {
            start: 467,
            end: 500,
            backgroundColor: "#FF2222"
        }, {
            start: 500,
            end: 533,
            backgroundColor: "#FF1111"
        }, {
            start: 533,
            backgroundColor: "#FF0000"
        }],
    },
    data: data
});

inmap.add(overlay);

(function(){
    for (let datum of data) {
        datum.count += Math.floor(Math.random() * 50) - 25;
        if (datum.count < 0)
            datum.count = 0;
    }
    overlay.setPoints(data);
    setTimeout(arguments.callee, 100);
})();
