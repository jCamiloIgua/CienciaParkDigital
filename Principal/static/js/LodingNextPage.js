//Inicio
function cargarPaginaInicio() {
    var containerCargando = document.querySelector(".container-cargando");
    containerCargando.style.display = "block";

    setTimeout(function () {
        containerCargando.style.display = "none";
        window.location.href = urInicio; // Redirecciona a la página de inicio
    }, 1100); // 1 segundos
}

//Iniciarsesion
function cargarPaginaIniSesion() {
    var containerCargando = document.querySelector(".container-cargando");
    containerCargando.style.display = "block";

    setTimeout(function () {
        containerCargando.style.display = "none";
        window.location.href = urIniSesion; // Redirecciona a la página de inicio
    }, 1100); // 1 segundos
}


function cargarPaginaRegistro() {
    var containerCargando = document.querySelector(".container-cargando");
    containerCargando.style.display = "block";

    setTimeout(function () {
        containerCargando.style.display = "none";
        window.location.href = urregistropro; // Redirecciona a la página de inicio
    }, 1100); // 1 segundos
}

function cargarPaginaRegistroEstudiante() {
    var containerCargando = document.querySelector(".container-cargando");
    containerCargando.style.display = "block";

    setTimeout(function () {
        containerCargando.style.display = "none";
        window.location.href = urregistroestu; // Redirecciona a la página de inicio
    }, 1100); // 1 segundos
}
