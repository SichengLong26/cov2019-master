function get_time(){
    $.ajax({
        type: "post",
        url: "http://192.168.3.142:5000/time",
        success: function (data) {
            $("#tim").html(data)
        },
        error:function(){

        }
    });
}

function get_c1_data(){
    $.ajax({
        url: "http://192.168.3.142:5000/c1",
        type: "post",
        success: function (data) {
            $(".num h1").eq(0).html(data['confirm'])
            $(".num h1").eq(1).html(data['suspect'])
            $(".num h1").eq(2).html(data['heal'])
            $(".num h1").eq(3).html(data['dead'])
        },
        error:function(){

        }
    });
}


function get_center2(){
    $.ajax({
        url: "http://192.168.3.142:5000/c2",
        type: "post",
        success: function (datas) {
            ec_center_option.series[0].data = datas["data"]
            ec_center.setOption(ec_center_option)
        },
        error:function(){

        }
    });
}

function get_left1(){
    $.ajax({
        url: "http://192.168.3.142:5000/l1",
        type: "post",
        success: function (datas) {
            ec_left1_Option.xAxis[0].data=datas["day"]
            ec_left1_Option.series[0].data=datas["confirm"]
            ec_left1_Option.series[1].data=datas["suspect"]
            ec_left1_Option.series[2].data=datas["heal"]
            ec_left1_Option.series[3].data=datas["dead"]
            ec_left1.setOption(ec_left1_Option)
        },
        error:function(){

        }
    });
}


function get_left2() {
    $.ajax({
        url: "http://192.168.3.142:5000/l2",
        type: "post",
        success: function (datass) {
            ec_left2_option.xAxis.data=datass["city"];
            ec_left2_option.series[0].data=datass["confirm"];
            ec_left2.setOption(ec_left2_option);
        }
    })
}

function get_r1_data() {
    $.ajax({
        url: "http://192.168.3.142:5000/r1",
        type: "post",
        success: function (datas) {
            ec_right1_option.xAxis.data=datas["city"];
            ec_right1_option.series[0].data=datas["confirm"];
            ec_right1.setOption(ec_right1_option);
        }
    })
}

function get_r2_data() {
    $.ajax({
        url: "http://192.168.3.142:5000/r2",
        type: "post",
        success: function (data) {
            ec_right2_option.series[0].data=data.kws;
            ec_right2.setOption(ec_right2_option);
        }
    })
}

setInterval(get_time,1000)
setInterval(get_c1_data,1000)
setInterval(get_center2,1000)
setInterval(get_left1,1000)
setInterval(get_left2,1000)
setInterval(get_r1_data,1000)
setInterval(get_r2_data,1000)