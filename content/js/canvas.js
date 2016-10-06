function getMousePos(canvas, evt) {
    var rect = canvas.getBoundingClientRect();
    return {
        x: evt.clientX - rect.left,
        y: evt.clientY - rect.top
    };
}

var canvas = document.getElementById('myCanvas');
var context = canvas.getContext('2d');
var r = 4

var dataCanvas =  document.createElement("canvas");
dataCanvas.width = 50;
dataCanvas.height = 50;
var dataCtx = dataCanvas.getContext('2d');

var clearButton = document.getElementById('bclear');
dataCtx.fillStyle = "white";
//dataCtx.fillRect(0,0, dataCanvas.width, dataCanvas.height);

clearButton.addEventListener('click', function(evt){
    context.clearRect(0,0, canvas.width, canvas.height);
    dataCtx.clearRect(0,0, dataCanvas.width, dataCanvas.height);
});

var procButton = document.getElementById('bproc');
google.charts.load("current", {packages:["corechart"]});
var chartDiv = document.getElementById('chart');


procButton.addEventListener('click', function(evt){
    dataCtx.drawImage(canvas, 0,0, canvas.width, canvas.height, 0,0,dataCanvas.width,dataCanvas.height);
    var data = dataCanvas.toDataURL('image/png');
    console.log(data) ;

    $.getJSON('http://hjkl-yjk21.rhcloud.com/classify', {
        //$.getJSON('http://localhost:7111/classify', {
        img: data
    }, function(data) {
        var dd = data.dist;
        //console.log(data.result);
        //console.log(data.dist);
        //console.log(typeof(data.dist));
        //console.log(dd instanceof Array);

        var idx = Array.apply(null, {length: 10}).map(Function.call, Number);
        if(! (dd instanceof Array)){
            dd = idx.map(function(){return 0.1;});
            //console.log(dd);
        }


        var a1 = [['Digit', 'log P (shifted)']];
        var minVal = (Math.min.apply(null, dd));

        var logP = idx.map(function(i){return [''+i, data.dist[i] - minVal];});

        a1 = a1.concat(logP);

        var bla = google.visualization.arrayToDataTable(a1);


        var options = {
            title: 'Output Distribution',
            width: 600,
            height:400,
            hAxis: {title: 'log-Probability'},
            vAxis: {title: 'Digit'}
        };
        var chart = new google.visualization.BarChart(chartDiv);

        chart.draw(bla, options);



    });

});

var md = false;

canvas.addEventListener('mousedown', function(evt){
    context.beginPath();
    md = true;
    var mousePos = getMousePos(canvas, evt);
    context.moveTo(mousePos.x, mousePos.y);
});

canvas.addEventListener('mouseup', function(evt){
    md = false;
    context.closePath();
});

canvas.addEventListener('mousemove', function(evt) {
    var mousePos = getMousePos(canvas, evt);
    if(md){
        context.lineTo(mousePos.x, mousePos.y);
        context.lineJoin = context.lineCap = 'round';
        context.shadowBlur = 0;
        context.shadowColor = 'rgb(0, 0, 0)';
        context.fillStyle = 'black';
        context.lineWidth = 13;
        context.stroke();
    }
}, false);

