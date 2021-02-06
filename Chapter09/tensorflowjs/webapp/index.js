async function GetData(){

    $.get( "/data.json", function( data ) {
        $( "#data" ).text( data["dat"] );
           predict(data["dat"]) 
    });
}

async function predict(dat)
{
    const model =  await tf.loadLayersModel('/tfjs_model/model.json');
    console.log(model)
    dat = tf.tensor3d(dat, [1, 50, 25] )
    dat[0] = null
    console.log(dat)
    var pred = model.predict( dat)
    const values = pred.dataSync();
    let result = "Needs Maintenance"
    if(values[0] < .8)
        result = "Does not need Maintenance"
    
    $('#needed').html(result )
}