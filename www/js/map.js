var map = L.map('map').setView([44.92863,1.72367], 13);

//L.tileLayer('https://{s}.tiles.mapbox.com/v3/{id}/{z}/{x}/{y}.png', {
L.tileLayer('http://tile.openstreetmap.org/{z}/{x}/{y}.png', {
	maxZoom: 18,
	attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
		'<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
		//'Imagery © <a href="http://mapbox.com">Mapbox</a>',
		'Imagery © <a href="http://openstreetmap.org">OpenSteetMap</a>',
	id: 'examples.map-i875mjb7'
}).addTo(map);


var popup = L.popup();

function onMapClick(e) {
	popup
		.setLatLng(e.latlng)
		.setContent("Tu as cliqué ici: " + e.latlng.lat.toString() + ', ' + e.latlng.lng.toString())
		.openOn(map);
}

map.on('click', onMapClick);
