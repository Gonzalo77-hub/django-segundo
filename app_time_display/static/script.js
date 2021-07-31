function addZero(i){
    if (i < 10){
        i = "0" + i;
    }
    return i;
}

function mueveReloj(){ 
    momentoActual = new Date() 
    hora = addZero(momentoActual.getHours());
    minuto = addZero(momentoActual.getMinutes()); 
    segundo = addZero(momentoActual.getSeconds()); 

    horaImprimible = hora + " : " + minuto + " : " + segundo 

    document.form_reloj.reloj.value = horaImprimible 

    //La función se tendrá que llamar así misma para que sea dinámica, 
    //de esta forma:

    setTimeout(mueveReloj,1000)
}
