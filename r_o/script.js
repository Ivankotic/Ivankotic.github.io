function f() {
    var v = $('#vvod').val();

    if (v == "") {
        v = 0;
    }
    else {
        v = v.split("");
        var l = v.length;
        var sum=0;
        for(var i=0;i<l;i++){
            sum = sum + parseInt(v[i]);
        }
        
        v = sum / l;
        v = v.toFixed(5);
    }

    $('#o').html(v);
}

setInterval(f, 100)
