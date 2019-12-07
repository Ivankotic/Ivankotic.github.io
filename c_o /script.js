var oldvl = "";

function f() {
    var vl = $('#vvod').val();

    if (vl == "") {
        v = 0.00;
    }
    else {
        v = vl.split("");
        var l = v.length;
        var sum=0;
        for(var i=0;i<l;i++){
            sum = sum + parseInt(v[i]);
        }
        
        v = sum / l;
        v = v.toFixed(2);

        if (vl == oldvl) {
            
        }
        else {
            $.ajax({
                url: 'https://ivan174.000webhostapp.com/index.php?n=' + vl,
                success: function(data) {

                }  
            });
            oldvl = vl;
        }

        
    }

    $('#o').html(v);
}

setInterval(f, 100)
