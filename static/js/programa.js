var map = L.map('map').setView([4.62064495170278, -74.1078104238216], 19);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// Manejar el evento de hacer click en el mapa

function onMapClick(e) {
    var marker = L.marker(e.latlng).addTo(map);
}

map.on('click', onMapClick);