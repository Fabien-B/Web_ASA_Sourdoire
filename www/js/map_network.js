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

addCompteur(44.93405,1.76915,2);
addCompteur(0,1.76915,2);
addCompteur(44.93405,1.86915,2);

function addCompteur(lat,lon,alt) {
	if(lat != 0 && lon != 0){
	L.marker([lat,lon]).addTo(map);
	}
}

var azer = jQuery.parseJSON("{'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'properties': {'altitude': None}, 'geometry': {'type': 'Point', 'coordinates': [None, None]}}, {'type': 'Feature', 'properties': {'altitude': 165}, 'geometry': {'type': 'Point', 'coordinates': [44.9796, 1.72813]}}, {'type': 'Feature', 'properties': {'altitude': 158}, 'geometry': {'type': 'Point', 'coordinates': [44.9789, 1.72392]}}, {'type': 'Feature', 'properties': {'altitude': 99}, 'geometry': {'type': 'Point', 'coordinates': [44.9855, 1.71438]}}, {'type': 'Feature', 'properties': {'altitude': 136}, 'geometry': {'type': 'Point', 'coordinates': [44.9812, 1.71462]}}, {'type': 'Feature', 'properties': {'altitude': 138}, 'geometry': {'type': 'Point', 'coordinates': [44.981, 1.71412]}}, {'type': 'Feature', 'properties': {'altitude': 145}, 'geometry': {'type': 'Point', 'coordinates': [44.9798, 1.71353]}}, {'type': 'Feature', 'properties': {'altitude': None}, 'geometry': {'type': 'Point', 'coordinates': [None, None]}}, {'type': 'Feature', 'properties': {'altitude': 163}, 'geometry': {'type': 'Point', 'coordinates': [44.9824, 1.72558]}}, {'type': 'Feature', 'properties': {'altitude': None}, 'geometry': {'type': 'Point', 'coordinates': [None, None]}}]}");
alert(azer);
L.geoJson(azer).addTo(map);
function get_network() {
	
   $.ajax({
		type:"get",
		url:'../page_reseau.py/get_json_compteurs',   // fonction python appelée
		data: {'id_ex':14}, // parametres passes a cette fonction
		success:function(reponse){  // recup dans reponse du return fait par la fonction corps_page_connecte
			alert(reponse);			
			return reponse;
		},
		error:function(){ alert("erreur lors de la recuperation des données");}
	});  
}