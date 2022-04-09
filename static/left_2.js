var ec_left2 = echarts.init(document.getElementById('l2'),"dark");
var ec_left2_option = {
	//标题样式
	title : {
	    text : "单日新增病例",
	    textStyle : {
	        color : 'white',
	    },
	    left : 'left'
	},
	  color: ['#3398DB'],
	    tooltip: {
	        trigger: 'axis',
	        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
	            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
	        }
	    },
    xAxis: {
        type: 'category',
        data: []
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [],
        type: 'bar',
		barMaxWidth:"50%"
    }]
};
ec_left2.setOption(ec_left2_option)