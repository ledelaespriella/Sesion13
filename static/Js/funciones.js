function guardarEst(){
    document.getElementById("formulario").action='/estudiante/save'
}

function consultarEst(){
    document.getElementById("formulario").action='/estudiante/get'
}

function listarEst(){
    document.getElementById("formulario").action='/estudiante/list'
}

function actualizarEst(){
    document.getElementById("formulario").action='/estudiante/update'
}

function eliminarrEst(){
    document.getElementById("formulario").action='/estudiante/delete'
}

function mostraContrasena(){
    var tipo = document.getElementById("password")
    if (tipo.type == "password"){
        tipo.type = "text"
    }else{
        tipo.type="password"
    }
}
