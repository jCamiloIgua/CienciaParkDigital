function abrirRegistrar() {
    var ventana = document.getElementById("vent");
    ventana.style.display = "flex"; // Cambia a "flex" para centrar el contenido.
}

document.getElementById("vent").addEventListener("click", function (e) {
    if (e.target.id === "vent") {
        document.getElementById("vent").style.display = "none";
    }
});