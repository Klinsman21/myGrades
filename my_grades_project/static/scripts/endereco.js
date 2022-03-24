var map = L.map('map').setView({ lon: 0, lat: 0 }, 2)
let marker = L.marker([0, 0])
var lat = 0
var lon = 0
var zoom = 8

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        lat = 0
        lon = 0
        alert('Geolocalização não disponível para esse navegador')
    }
}


L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap contributors</a>'
}).addTo(map)


L.control.scale({ imperial: true, metric: true }).addTo(map)

map.on('click', function (e) {
    if (document.getElementById("pageType").value != "list") {
        marker.setLatLng(e.latlng)
        console.log(e.latlng)
        marker.addTo(map)
    }

});

function showPosition(position) {
    map.setView(new L.LatLng(position.coords.latitude, position.coords.longitude), 16)
    marker.setLatLng(L.latLng(position.coords.latitude, position.coords.longitude))
    marker.addTo(map)
}

function enviarParaMongo() {
    let matricula = document.getElementById("matricula").value
    let url = "http://localhost:3000/salvarLocalizacao"
    let xhr = new XMLHttpRequest()
    xhr.open("POST", url)
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    let data = `matricula=${matricula}&lat=${marker.getLatLng()["lat"]}&lng=${marker.getLatLng()["lng"]}`
    xhr.send(data)
}

function response() {
    data = this.responseText.replace('[', '').replace(']', '')
    data = JSON.parse(data)
    map.setView(new L.LatLng(data["lat"], data["lng"]), 16)
    marker.setLatLng(L.latLng(data["lat"], data["lng"]))
    marker.addTo(map)
}

function obterLatLng(matricula) {
    var oReq = new XMLHttpRequest()
    let url = `http://localhost:3000/getLatLng/${matricula}`
    oReq.onload = response
    oReq.open("GET", url)
    oReq.send()
}